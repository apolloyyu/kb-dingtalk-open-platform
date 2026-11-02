#!/usr/bin/env python3
"""oss_publish.py 离线测试(不连 OSS)：签名对官方 SDK 单测向量、发布顺序与清单刷新规则、打包结构、密钥读取。
用法: python3 ops/scripts/test_oss_publish.py"""
import datetime
import gzip
import io
import json
import os
import subprocess
import sys
import tarfile
import tempfile
import unittest
from urllib.parse import quote, urlencode

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import oss_publish as op  # noqa: E402


GITC = ("-c", "core.hooksPath=/dev/null", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false")


def sh(cwd, *cmd):
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def make_repo(root, files):
    os.makedirs(root)
    sh(root, "git", "init", "-q", "-b", "main")
    for k, v in files.items():
        os.makedirs(os.path.dirname(os.path.join(root, k)) or root, exist_ok=True)
        with open(os.path.join(root, k), "wb") as f:
            f.write(v)
    sh(root, "git", "add", "-A")
    sh(root, "git", *GITC, "commit", "-q", "-m", "c")
    return sh(root, "git", "rev-parse", "HEAD")


class FakeOss:
    def __init__(self, fail_tgz=False):
        self.store, self.puts, self.fail_tgz = {}, [], fail_tgz

    def get_json(self, key):  # 与 Oss.get_json 一致：非对象内容当空清单
        if key not in self.store:
            return None
        m = json.loads(self.store[key])
        return m if isinstance(m, dict) else {}

    def put(self, key, body, ctype, timeout=60):
        if self.fail_tgz and key.endswith(".tar.gz"):
            raise RuntimeError("PUT HTTP 403 AccessDenied")
        self.puts.append(key)
        self.store[key] = body


class SignTest(unittest.TestCase):
    """向量取自 aliyun/alibabacloud-oss-python-sdk-v2 tests/unit/signer/test_v4.py。"""

    def _sign(self, ts, extra=None):
        h = {"x-oss-head1": "value", "abc": "value", "ZAbc": "value", "XYZ": "value",
             "content-type": "text/plain", "x-oss-content-sha256": "UNSIGNED-PAYLOAD", **(extra or {})}
        q = urlencode({"param1": "value1", "+param1": "value3", "|param1": "value4",
                       "+param2": "", "|param2": "", "param2": ""}, quote_via=quote)
        now = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc)
        return op.sign_v4("PUT", "1234+-/123/1.txt", h, "ak", "sk", now, bucket="bucket", region="cn-hangzhou",
                          query=q)["Authorization"]

    def test_sdk_vector(self):
        self.assertEqual(self._sign(1702743657), "OSS4-HMAC-SHA256 Credential=ak/20231216/cn-hangzhou/oss/"
                         "aliyun_v4_request,Signature=e21d18daa82167720f9b1047ae7e7f1ce7cb77a31e8203a7d5f4624fa0284afe")

    def test_sdk_vector_with_token_header(self):
        self.assertEqual(self._sign(1702784856, {"x-oss-security-token": "token"}),
                         "OSS4-HMAC-SHA256 Credential=ak/20231217/cn-hangzhou/oss/aliyun_v4_request,"
                         "Signature=b94a3f999cf85bcdc00d332fbd3734ba03e48382c36fa4d5af5df817395bd9ea")


class PublishTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = os.path.join(self.tmp.name, "kb-x")
        self.c1 = make_repo(self.repo, {"AGENTS.md": b"# kb\n", "docs/blob.bin": os.urandom(150_000)})
        sh(self.repo, "git", "update-ref", "refs/remotes/origin/main", self.c1)
        self.args, self.logs = ["-C", self.repo], []

    def tearDown(self):
        self.tmp.cleanup()

    def pub(self, oss, now, ref="refs/remotes/origin/main", name="kb-x-main"):
        return op.publish_one(oss, name, self.args, ref, now, self.logs.append)

    def test_upload_then_fresh_then_refresh(self):
        oss = FakeOss()
        self.assertEqual(self.pub(oss, 1000.0), "uploaded:" + self.c1[:7])
        # 先传包、再传清单：下载端读到新清单时包一定已在
        self.assertEqual(oss.puts, ["dingzai-kb/kb-x-main.tar.gz", "dingzai-kb/kb-x-main.json"])
        m = json.loads(oss.store["dingzai-kb/kb-x-main.json"])
        body = oss.store["dingzai-kb/kb-x-main.tar.gz"]
        self.assertEqual((m["commit"], m["size"], m["checked_at"]), (self.c1, len(body), 1000))
        import hashlib
        self.assertEqual(m["sha256"], hashlib.sha256(body).hexdigest())
        with tarfile.open(fileobj=io.BytesIO(body)) as t:
            names = t.getnames()
        self.assertIn("kb-x-main/AGENTS.md", names)  # 与 GitHub 包同结构：顶层目录 = 包名
        self.assertTrue(all(n == "kb-x-main" or n.startswith("kb-x-main/") for n in names))
        self.assertEqual(gzip.decompress(body)[:0], b"")
        self.assertEqual(self.pub(oss, 1000.0 + op.REFRESH_S - 1), "fresh")
        self.assertEqual(len(oss.puts), 2)
        self.assertEqual(self.pub(oss, 1000.0 + op.REFRESH_S + 1), "refreshed")
        self.assertEqual(oss.puts[-1], "dingzai-kb/kb-x-main.json")
        m2 = json.loads(oss.store["dingzai-kb/kb-x-main.json"])
        self.assertEqual((m2["sha256"], m2["built_at"], m2["checked_at"]), (m["sha256"], 1000, 1000 + op.REFRESH_S + 1))

    def test_garbled_manifest_is_republished(self):
        for junk in (b"[1]", b'{"commit": "x", "checked_at": "soon"}'):
            oss = FakeOss()
            oss.store["dingzai-kb/kb-x-main.json"] = junk
            self.assertEqual(self.pub(oss, 1.0), "uploaded:" + self.c1[:7])
        oss = FakeOss()
        self.pub(oss, 1.0)
        m = json.loads(oss.store["dingzai-kb/kb-x-main.json"])
        oss.store["dingzai-kb/kb-x-main.json"] = json.dumps({**m, "checked_at": "soon"}).encode()
        self.assertEqual(self.pub(oss, 2.0), "refreshed")  # 同一提交只重写清单，不重传包

    def test_same_commit_builds_identical_package(self):
        a, b = FakeOss(), FakeOss()
        self.pub(a, 1.0)
        self.pub(b, 99.0)
        self.assertEqual(a.store["dingzai-kb/kb-x-main.tar.gz"], b.store["dingzai-kb/kb-x-main.tar.gz"])

    def test_new_commit_reuploads(self):
        oss = FakeOss()
        self.pub(oss, 1.0)
        with open(os.path.join(self.repo, "AGENTS.md"), "a") as f:
            f.write("more\n")
        sh(self.repo, "git", *GITC, "commit", "-qam", "c2")
        c2 = sh(self.repo, "git", "rev-parse", "HEAD")
        sh(self.repo, "git", "update-ref", "refs/remotes/origin/main", c2)
        self.assertEqual(self.pub(oss, 2.0), "uploaded:" + c2[:7])
        self.assertEqual(json.loads(oss.store["dingzai-kb/kb-x-main.json"])["commit"], c2)

    def test_failed_package_upload_keeps_old_manifest_aging(self):
        oss = FakeOss()
        self.pub(oss, 1.0)
        old = oss.store["dingzai-kb/kb-x-main.json"]
        with open(os.path.join(self.repo, "AGENTS.md"), "a") as f:
            f.write("more\n")
        sh(self.repo, "git", *GITC, "commit", "-qam", "c2")
        sh(self.repo, "git", "update-ref", "refs/remotes/origin/main", "HEAD")
        oss.fail_tgz = True
        with self.assertRaises(RuntimeError):
            self.pub(oss, 1.0 + 2 * op.REFRESH_S)
        # 清单没被刷新：旧 commit、旧 checked_at，下载端过 2 小时自然退回 GitHub
        self.assertEqual(oss.store["dingzai-kb/kb-x-main.json"], old)

    def test_absent_branch_and_incomplete_package(self):
        oss = FakeOss()
        self.assertEqual(self.pub(oss, 1.0, ref="refs/remotes/origin/staging", name="kb-x-staging"), "absent")
        sh(self.repo, "git", "rm", "-q", "AGENTS.md")
        sh(self.repo, "git", *GITC, "commit", "-qm", "rm")
        sh(self.repo, "git", "update-ref", "refs/remotes/origin/main", "HEAD")
        with self.assertRaises(RuntimeError):
            self.pub(oss, 1.0)
        self.assertEqual(oss.puts, [])

    def test_upstream_source_from_local_clone(self):
        up = os.path.join(self.tmp.name, "up")
        import base64
        c = make_repo(up, {"CHANGELOG.md": b"# c\n", "blob.bin": os.urandom(150_000),
                           "lib/big.a": b"\0" + os.urandom(300_000),
                           "big.go": base64.b64encode(os.urandom(240_000))})  # 大文本照留
        old = op.UPSTREAM
        op.UPSTREAM = {"kb-x": [("dingtalk-workspace-cli-main", up)]}
        try:
            t = op.targets(self.repo, "kb-x")
            op.UPSTREAM = {"kb-x": [("dingtalk-workspace-cli-main", up + "-missing")]}
            self.assertEqual(len(op.targets(self.repo, "kb-x")), 2)  # 源码副本不在：不发布，不报错
        finally:
            op.UPSTREAM = old
        self.assertEqual([x[0] for x in t], ["kb-x-main", "kb-x-staging", "dingtalk-workspace-cli-main"])
        self.assertEqual([x[3] for x in t], [False, False, True])  # 只有上游源码去二进制
        name, args, ref, strip = t[2]
        oss = FakeOss()
        self.assertEqual(op.publish_one(oss, name, args, ref, 1.0, self.logs.append, strip), "uploaded:" + c[:7])
        with tarfile.open(fileobj=io.BytesIO(oss.store["dingzai-kb/dingtalk-workspace-cli-main.tar.gz"])) as tf:
            names = tf.getnames()
        for keep in ("CHANGELOG.md", "blob.bin", "big.go"):  # 小二进制、大文本都保留
            self.assertIn("dingtalk-workspace-cli-main/" + keep, names)
        self.assertNotIn("dingtalk-workspace-cli-main/lib/big.a", names)
        self.assertEqual(json.loads(oss.store["dingzai-kb/dingtalk-workspace-cli-main.json"])["excluded_binaries"],
                         ["lib/big.a"])
        self.assertEqual(op.publish_one(oss, name, args, ref, 2.0, self.logs.append, strip), "fresh")


class CredsTest(unittest.TestCase):
    def test_env_file_and_missing(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "oss.env")
            with open(p, "w") as f:
                f.write("DZ_KB_OSS_AK_ID=LTAIexample\nexport DZ_KB_OSS_AK_SECRET='s3cr3t'\n")
            old, env = op.ENV_FILE, {k: os.environ.pop(k) for k in ("DZ_KB_OSS_AK_ID", "DZ_KB_OSS_AK_SECRET")
                                     if k in os.environ}
            try:
                op.ENV_FILE = p
                self.assertEqual(op.load_creds(), ("LTAIexample", "s3cr3t"))
                op.ENV_FILE = os.path.join(d, "missing.env")
                self.assertIsNone(op.load_creds())
            finally:
                op.ENV_FILE = old
                os.environ.update(env)


if __name__ == "__main__":
    unittest.main(verbosity=1)
