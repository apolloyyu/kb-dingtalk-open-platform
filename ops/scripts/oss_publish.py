#!/usr/bin/env python3
"""知识库国内下载源：把 GitHub 上的分支打成与 GitHub 下载包同结构的 tar.gz，发布到阿里云 OSS。

钉仔沙箱冷启动要从 GitHub 下载知识库包，工作日约 15% 要多等 1~2 分钟、约 6% 等不到(2026-10-30 线上日志)。
答疑 skill 的 scripts/fetch_*.sh 先读这里发布的清单：3 秒内拿不到、2 小时没确认或校验不符，就退回 GitHub。

由 mirror_sync.sh 每轮(executor kb.mirror，约 10 分钟)在 GitLab→GitHub 同步之后调用；也可手动：
    python3 ops/scripts/oss_publish.py [--repo DIR] [--dry-run]

对象(公网可读)：<桶>/dingzai-kb/<名>.tar.gz 与 <名>.json，<名> = GitHub 包的顶层目录名(<仓>-<分支>)。
清单 {name, format, commit, sha256, size, built_at, checked_at[, excluded_binaries]}：先传包、再传清单。内容没变时每 REFRESH_S 只重写
checked_at；只有清单里的 commit 等于本仓记录的 GitHub 分支头时才刷新，所以「清单新鲜」= 包就是 GitHub 当前版本，
上传坏了清单只会变旧，下载端 2 小时后自动走 GitHub。
密钥：环境变量 DZ_KB_OSS_AK_ID / DZ_KB_OSS_AK_SECRET，或 ~/.config/dingzai-kb/oss.env(600，KEY=VALUE 两行)。
子账号只有 dingzai-kb/ 前缀的 PutObject 权限。没有密钥 = 未启用，静默跳过。
输出：stdout 一行，以 "OSS " 开头；rc 0=正常/跳过，1=有包发布失败(mirror_sync 不因此改变自己的退出码)。
明细追加到 <git 目录>/oss-publish.log，不含密钥。
"""
import argparse
import base64
import datetime
import fcntl
import gzip
import hashlib
import hmac
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BUCKET = os.environ.get("KB_OSS_BUCKET", "icms-document")
REGION = os.environ.get("KB_OSS_REGION", "cn-beijing")
PREFIX = os.environ.get("KB_OSS_PREFIX", "dingzai-kb")
HOST = f"{BUCKET}.oss-{REGION}.aliyuncs.com"
ENV_FILE = os.environ.get("KB_OSS_ENV_FILE", "~/.config/dingzai-kb/oss.env")
REFRESH_S = 1800          # 内容没变时多久重写一次清单(下载端认 2 小时内确认过的清单)
DEADLINE_S = 100          # 本轮总时长上限(executor 给整个 mirror_sync.sh 180s)，超时的包下一轮再发
BRANCHES = ("main", "staging")
FORMAT = 1                # 打包规则版本：改了打包方式就加一，旧清单视为过期、按新规则重发
CHECK_FILE = {"dingtalk-workspace-cli": "CHANGELOG.md"}  # 下载脚本判断包完整用的文件，其余仓是 AGENTS.md
# 上游源码包去掉 ≥256KB 的二进制(含 NUL)：2026-10-28 起源码仓带了约 86MB 平台库/payload，整包 55MB，
# 助理只读源码与文档，用不上。知识库仓不做这一步(索引文件一个都不能少)。
BIG_BINARY = 256 * 1024
# 钉仔 dws skill 二级按需拉取的开源源码，随 kb-dws-wiki 一起发布。取本机 dws_regen 每天 pull 的源码副本(即当天
# 知识库构建所用版本)，不每轮去 GitHub 拉：源码仓 55MB，ECS 拉 GitHub 也会 90s 拉不完(2026-11-02 实测)。副本不在则不发布。
UPSTREAM = {"kb-dws-wiki": [("dingtalk-workspace-cli-main", os.environ.get(
    "KB_OSS_DWS_SOURCE", "~/ding-open-copilot/local-assistant/workdir/kb/dws-source"))]}


def sign_v4(method, key, headers, ak, sk, now, bucket=BUCKET, region=REGION, query=""):
    """OSS V4 请求头签名，算法与官方 SDK alibabacloud_oss_v2.signer.v4 一致(用其单测向量校验)。
    就地补 x-oss-date / x-oss-content-sha256 / Authorization；query 为已编码的查询串。"""
    ts = now.astimezone(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    day = ts[:8]
    headers["x-oss-date"] = ts
    headers.setdefault("x-oss-content-sha256", "UNSIGNED-PAYLOAD")
    scope = f"{day}/{region}/oss/aliyun_v4_request"
    uri = urllib.parse.quote(f"/{bucket}/{key}", safe="/")
    pairs = sorted(p.partition("=")[::2] for p in query.split("&")) if query else []
    canon_query = "&".join(k + ("=" + v if v else "") for k, v in pairs)
    signed = sorted((k.lower(), v) for k, v in headers.items()
                    if k.lower().startswith("x-oss-") or k.lower() in ("content-type", "content-md5"))
    canon = "\n".join([method, uri, canon_query, "".join(f"{k}:{v}\n" for k, v in signed), "",
                       headers["x-oss-content-sha256"]])
    to_sign = "\n".join(["OSS4-HMAC-SHA256", ts, scope, hashlib.sha256(canon.encode()).hexdigest()])
    k = ("aliyun_v4" + sk).encode()
    for part in (day, region, "oss", "aliyun_v4_request"):
        k = hmac.new(k, part.encode(), hashlib.sha256).digest()
    sig = hmac.new(k, to_sign.encode(), hashlib.sha256).hexdigest()
    headers["Authorization"] = f"OSS4-HMAC-SHA256 Credential={ak}/{scope},Signature={sig}"
    return headers


def load_creds():
    ak, sk = os.environ.get("DZ_KB_OSS_AK_ID", ""), os.environ.get("DZ_KB_OSS_AK_SECRET", "")
    path = os.path.expanduser(ENV_FILE)
    if not (ak and sk) and os.path.isfile(path):
        vals = {}
        with open(path, encoding="utf-8") as f:
            for line in f:
                k, _, v = line.strip().removeprefix("export ").partition("=")
                vals[k.strip()] = v.strip().strip("'\"")
        ak, sk = vals.get("DZ_KB_OSS_AK_ID", ""), vals.get("DZ_KB_OSS_AK_SECRET", "")
    return (ak, sk) if ak and sk else None


class Oss:
    """最小 OSS 客户端：签名 PUT + 公网 GET。错误只带 HTTP 码与 OSS 错误码，不带请求头/签名串。"""

    def __init__(self, creds, dry_run=False):
        self.creds, self.dry_run = creds, dry_run

    def url(self, key):
        return f"https://{HOST}/{urllib.parse.quote(key)}"

    def get_json(self, key):
        """公网读清单；不存在返回 None，其它错误抛出。"""
        req = urllib.request.Request(self.url(key), headers={"Cache-Control": "no-cache"})
        try:
            with urllib.request.urlopen(req, timeout=5) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            raise RuntimeError(f"GET HTTP {e.code}") from None

    def put(self, key, body, ctype, timeout=60):
        if self.dry_run:
            return
        last = None
        for attempt in (1, 2):
            h = {"Content-Type": ctype, "Content-MD5": base64.b64encode(hashlib.md5(body).digest()).decode(),
                 "Cache-Control": "no-cache"}
            sign_v4("PUT", key, h, *self.creds, now=datetime.datetime.now(datetime.timezone.utc))
            req = urllib.request.Request(self.url(key), data=body, method="PUT", headers=h)
            try:
                with urllib.request.urlopen(req, timeout=timeout):
                    return
            except urllib.error.HTTPError as e:
                m = re.search(rb"<Code>([^<]{1,60})</Code>", e.read() or b"")
                last = f"PUT HTTP {e.code} {m.group(1).decode() if m else ''}".strip()
                if e.code < 500:
                    break  # 4xx(权限/签名/时钟)重试也一样
            except (urllib.error.URLError, OSError) as e:
                last = f"PUT {type(e).__name__}: {str(getattr(e, 'reason', e))[:80]}"
            time.sleep(2 * attempt)
        raise RuntimeError(last)


def git(args, *cmd, **kw):
    return subprocess.run(["git", *args, *cmd], capture_output=True, text=True, timeout=kw.get("timeout", 60))


def big_binaries(git_args, commit):
    """[(路径, 字节)]：≥BIG_BINARY 且前 8000 字节含 NUL 的文件(git 判二进制的同一规则)。"""
    out = []
    for ent in git(git_args, "ls-tree", "-r", "-l", "-z", commit).stdout.split("\0"):
        meta, _, path = ent.partition("\t")
        f = meta.split()
        if len(f) == 4 and f[1] == "blob" and f[3].isdigit() and int(f[3]) >= BIG_BINARY:
            head = subprocess.run(["git", *git_args, "cat-file", "blob", f[2]], capture_output=True, timeout=60).stdout
            if b"\0" in head[:8000]:
                out.append((path, int(f[3])))
    return out


def build_tgz(git_args, commit, name, exclude=()):
    """git archive → gzip(mtime=0)：顶层目录 <name>/，与 GitHub /archive/refs/heads/<分支>.tar.gz 解开后同结构
    (exclude 里的路径除外)。"""
    spec = ["--", ".", *(":(exclude,literal)" + p for p in exclude)] if exclude else []
    buf = io.BytesIO()
    with subprocess.Popen(["git", *git_args, "archive", "--format=tar", f"--prefix={name}/", commit, *spec],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL) as p, \
            gzip.GzipFile(fileobj=buf, mode="wb", mtime=0, compresslevel=6) as gz:
        shutil.copyfileobj(p.stdout, gz, 1 << 20)
    if p.returncode:
        raise RuntimeError(f"git archive rc={p.returncode}")
    return buf.getvalue()


def targets(repo_dir, repo):
    """[(包名, git 参数, ref, 去二进制)]：本仓 GitHub 远端(origin)的 main/staging，加上该仓随附的上游源码。"""
    out = [(f"{repo}-{b}", ["-C", repo_dir], f"refs/remotes/origin/{b}", False) for b in BRANCHES]
    for name, src in UPSTREAM.get(repo, []):
        src = os.path.expanduser(src)
        if os.path.isdir(src):
            out.append((name, ["-C", src], "HEAD", True))
    return out


def resolve(git_args, ref):
    """ref 当前提交，不存在返回 None。"""
    r = git(git_args, "rev-parse", "-q", "--verify", ref + "^{commit}")
    return r.stdout.strip() if r.returncode == 0 else None


def publish_one(oss, name, git_args, ref, now, log, strip=False):
    """返回动作：absent / fresh / refreshed / uploaded:<短哈希>；失败抛 RuntimeError。"""
    commit = resolve(git_args, ref)
    if not commit:
        return "absent"
    mkey, tkey = f"{PREFIX}/{name}.json", f"{PREFIX}/{name}.tar.gz"
    try:
        m = oss.get_json(mkey)
    except (RuntimeError, urllib.error.URLError, OSError, ValueError) as e:
        log(f"{name}: read manifest failed ({str(e)[:80]}), republish")
        m = None
    if m and m.get("commit") == commit and m.get("sha256") and m.get("format") == FORMAT:
        if now - float(m.get("checked_at") or 0) < REFRESH_S:
            return "fresh"
        oss.put(mkey, json.dumps({**m, "checked_at": int(now)}).encode(), "application/json", timeout=15)
        return "refreshed"
    chk = CHECK_FILE.get(name.rsplit("-", 1)[0], "AGENTS.md")
    if git(git_args, "cat-file", "-e", f"{commit}:{chk}").returncode:
        raise RuntimeError(f"{commit[:7]} 缺 {chk}，下载端会判包不完整，不发布")
    dropped = big_binaries(git_args, commit) if strip else []
    body = build_tgz(git_args, commit, name, [p for p, _ in dropped])
    if len(body) < 100_000:
        raise RuntimeError(f"package too small ({len(body)}B)")
    digest = hashlib.sha256(body).hexdigest()
    oss.put(tkey, body, "application/gzip")
    oss.put(mkey, json.dumps({"name": name, "format": FORMAT, "commit": commit, "sha256": digest, "size": len(body),
                              "built_at": int(now), "checked_at": int(now),
                              **({"excluded_binaries": [p for p, _ in dropped]} if dropped else {})}).encode(),
            "application/json", timeout=15)
    log(f"{name}: uploaded {commit[:10]} {len(body)}B sha256={digest[:12]}"
        + (f" (去掉二进制 {len(dropped)} 个 {sum(n for _, n in dropped)}B)" if dropped else ""))
    return f"uploaded:{commit[:7]}"


def repo_name(repo_dir):
    url = git(["-C", repo_dir], "remote", "get-url", "origin").stdout.strip()
    base = url.rstrip("/").rsplit("/", 1)[-1].rsplit(":", 1)[-1]
    return base[:-4] if base.endswith(".git") else (base or os.path.basename(os.path.abspath(repo_dir)))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
    ap.add_argument("--dry-run", action="store_true", help="只打包算校验，不上传")
    a = ap.parse_args(argv)
    if os.environ.get("KB_OSS_DISABLE") == "1":
        print("OSS skip(disabled)")
        return 0
    creds = load_creds()
    if not creds and not a.dry_run:
        print("OSS skip(no-credentials)")
        return 0
    gdir = os.path.abspath(os.path.join(a.repo, git(["-C", a.repo], "rev-parse", "--git-common-dir").stdout.strip()))
    lock = open(os.path.join(gdir, "oss-publish.lock"), "w")
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        print("OSS skip(busy)")
        return 0
    logf = os.path.join(gdir, "oss-publish.log")

    def log(msg):
        if a.dry_run:
            print("[dry-run] " + msg, file=sys.stderr)
            return
        with open(logf, "a", encoding="utf-8") as f:
            f.write(time.strftime("%F %T ") + msg + "\n")

    repo, start = repo_name(a.repo), time.time()
    oss, done, bad = Oss(creds, a.dry_run), [], []
    for name, git_args, ref, strip in targets(a.repo, repo):
        if time.time() - start > DEADLINE_S:
            done.append(f"{name}=deferred")
            continue
        try:
            act = publish_one(oss, name, git_args, ref, time.time(), log, strip)
            if act != "absent":
                done.append(f"{name}={act}")
        except (RuntimeError, subprocess.SubprocessError, OSError) as e:
            bad.append(f"{name}: {str(e)[:120]}")
            log(f"{name}: FAIL {str(e)[:200]}")
    if os.path.exists(logf) and os.path.getsize(logf) > 512_000:  # 只留最近一段
        with open(logf, encoding="utf-8") as f:
            tail = f.readlines()[-2000:]
        with open(logf, "w", encoding="utf-8") as f:
            f.writelines(tail)
    if bad:
        print("OSS ALERT " + "; ".join(bad) + (" | " + " ".join(done) if done else ""))
        return 1
    print("OSS ok " + (" ".join(done) or "nothing"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
