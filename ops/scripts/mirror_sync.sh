#!/usr/bin/env bash
# 知识库双远端同步：GitLab(写入口) <-> GitHub(助理沙箱读取的镜像)。
# main：快进或无冲突自动合并，冲突告警退出，绝不强推。staging(测试助理)：GitHub 侧强制跟随 GitLab，见下文。由应用 executor 的 kb.mirror 调度
# (ECS/Aone 容器均适用)，也可手动执行。用法: mirror_sync.sh [仓库目录]，缺省为脚本所在仓。
# gitlab 远端缺失时按 KB_GITLAB_NS(默认 git@code.alibaba-inc.com:dingtalk-openplatform-ai)自动补齐，
# 全新克隆(容器重建)无需手工配置。
set -u
REPO="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$REPO" || { echo "ERR no repo $REPO"; exit 2; }
# 与每日流水线(kb_pipeline.sh / dws_regen.py)互斥:它们 apply 阶段工作区有大量未提交改动,
# 此时同步会 merge 失败或搅乱工作区(2026-09-05~09 实录)。流水线持有 .git/kb-pipeline.lock,
# 这里 flock -n 探测到锁就让路;输出以 OK 开头,executor 不会当异常记日志。
exec 9>"$REPO/.git/kb-pipeline.lock"
flock -n 9 || { echo "OK skip(pipeline-running)"; exit 0; }
GH=origin; GL=gitlab
# ---- staging 分支(测试助理拉取):GitLab→GitHub 搬运 + 每次把 main 追平进 staging ----
# 只动 refs 和临时 worktree,不切换本仓工作区(流水线用的是 main 工作区)。缺分支=未启用,静默跳过。
# main 同步的所有 exit 路径与输出不变(结果行永远是 stdout 最后一行);staging 结果只走 stderr,
# 以 "STAGING " 开头;main 正常而 staging 告警时 rc=4(与 main 的 rc=3 分叉告警区分)。
SB=${KB_STAGING_BRANCH:-staging}
# 冲突时可自动取 GitHub main 版本的生成层路径;bin/notes/ops/scripts/cards/graph/AGENTS.md 等人工文件冲突一律告警
AUTO_MAIN=${KB_STAGING_AUTO_RE:-'^(docs/|index/|meta/|ops/changes/|MANIFEST\.json$)'}
_wt_merge(){ # $1=base $2=要合入的 ref(GitHub main) $3=说明;生成层冲突取 GitHub main 的版本;成功则推 GitHub staging
  local wt; wt=$(mktemp -d) || return 4
  git worktree add -q --detach "$wt" "$1" 2>/dev/null || { rm -rf "$wt"; echo "ALERT worktree failed"; return 4; }
  if ! ( cd "$wt" && git merge -q --no-ff "$2" -m "merge: $3 to #85045988" >/dev/null 2>&1 ); then
    local bad; bad=$(cd "$wt" && git -c core.quotepath=off diff --name-only -z --diff-filter=U | tr '\0' '\n' | grep -Ev "$AUTO_MAIN")
    if [ -n "$bad" ]; then
      ( cd "$wt" && git merge --abort 2>/dev/null ); git worktree remove --force "$wt"
      echo "ALERT merge conflict ($3): $(echo "$bad" | head -5 | tr '\n' ' ')"; return 4
    fi
    # 生成层一律以 GitHub main 为准(无论哪一侧是 theirs);main 里已删除的文件就删除
    ( cd "$wt" && git -c core.quotepath=off diff --name-only -z --diff-filter=U | while IFS= read -r -d '' f; do
        if git cat-file -e "$GH/main:$f" 2>/dev/null; then git checkout "$GH/main" -- "$f"; else git rm -q -- "$f"; fi
      done && git add -A && git commit -q --no-edit ) \
      || { git worktree remove --force "$wt"; echo "ALERT auto-resolve failed ($3)"; return 4; }
  fi
  local head; head=$(cd "$wt" && git rev-parse HEAD)
  git worktree remove --force "$wt"
  git push -q --force "$GH" "$head:refs/heads/$SB" || { echo "ALERT push rejected"; return 4; }
  echo "OK $3 -> ${head:0:7}"
}
sync_staging(){
  # GitHub staging = GitLab staging + GitHub main。GitLab staging 是唯一真相(ops.py 每次 stage 按
  # "main + 当前提案" 重建,reject 时重置回 main);GitHub staging 上只允许镜像产生的 merge,所以可以强制移动。
  if ! git fetch -q "$GL" "$SB" 2>/dev/null; then
    # GitLab 上删了 staging 而 GitHub 还在:测试助理会停在旧版本,提醒
    git ls-remote --exit-code --heads "$GH" "$SB" >/dev/null 2>&1 && { echo "ALERT gitlab staging gone, github staging stale"; return 4; }
    echo "OK absent"; return 0
  fi
  local gl gh base extra; gl=$(git rev-parse "$GL/$SB")
  if git fetch -q "$GH" "$SB" 2>/dev/null; then gh=$(git rev-parse "$GH/$SB"); else gh=""; fi
  base=$gl
  if [ -n "$gh" ] && git merge-base --is-ancestor "$gl" "$gh"; then
    # gh 里除了 gl 和 main 之外不能有别的非 merge 提交(否则是已被撤下的旧提案,要丢弃)
    extra=$(git rev-list --no-merges -n1 "$gh" "^$gl" "^$GH/main")
    [ -z "$extra" ] && base=$gh
  fi
  if git merge-base --is-ancestor "$GH/main" "$base"; then
    [ "$base" = "$gh" ] && { echo "OK in-sync ${gh:0:7}"; return 0; }
    git push -q --force "$GH" "$base:refs/heads/$SB" || { echo "ALERT push rejected"; return 4; }
    echo "OK gitlab $SB ${base:0:7} -> github"; return 0
  fi
  _wt_merge "$base" "$GH/main" "main $(git rev-parse --short "$GH/main") 追平进 $SB"
}
_on_exit(){
  local rc=$?
  [ "${KB_STAGING_DISABLE:-0}" = 1 ] && exit $rc
  local out src; out=$(sync_staging 2>&1); src=$?
  # 无事发生(absent/in-sync)不打印,避免每 10 分钟刷日志
  case "$out" in *"OK absent"|*"OK in-sync"*) [ $src -eq 0 ] && exit $rc;; esac
  echo "STAGING $(echo "$out" | tail -1)" >&2
  [ $rc -eq 0 ] && [ $src -ne 0 ] && exit 4
  exit $rc
}
trap _on_exit EXIT
if ! git remote get-url "$GL" >/dev/null 2>&1; then
  git remote add "$GL" "${KB_GITLAB_NS:-git@code.alibaba-inc.com:dingtalk-openplatform-ai}/$(basename "$REPO").git" \
    && echo "INFO added remote $GL" || { echo "ERR cannot add remote $GL"; exit 2; }
fi
git fetch -q "$GH" main && git fetch -q "$GL" main || { echo "ERR fetch failed"; exit 1; }
gh=$(git rev-parse "$GH/main"); gl=$(git rev-parse "$GL/main")
if [ "$gh" = "$gl" ]; then echo "OK in-sync ${gh:0:7}"; git merge -q --ff-only "$GH/main" 2>/dev/null; exit 0; fi
# 设计:GitLab 是人的写入口,GitHub 是完整历史(人 + ECS 每日 ingest/构建)。ECS 只做 GitLab→GitHub
# 单向搬运,**不往 GitLab 推**(无写权限,且 ECS 提交邮箱过不了推送规则)。
# 因此"GitHub 领先"是正常态:人在下次推 GitLab 前先 fetch origin 并合并,GitLab 便重新领先。
if git merge-base --is-ancestor "$gl" "$gh"; then          # GitHub 领先(ECS 日常提交)→ 正常,不动
  git merge -q --ff-only "$GH/main" 2>/dev/null; echo "OK github-ahead ${gl:0:7}..${gh:0:7}"; exit 0
elif git merge-base --is-ancestor "$gh" "$gl"; then        # GitLab 领先(人工提交)→ 推到 GitHub
  git push -q "$GH" "$gl:refs/heads/main" && echo "OK gitlab->github ${gh:0:7}..${gl:0:7}"
else
  # 分叉(人推 GitLab 前没并 GitHub):按设计 GitHub 是完整历史,直接在本机合并后推 GitHub,
  # 无需人工;GitLab 落后属正常态。只有真正的合并冲突才告警。
  # 前提:工作区干净(流水线持锁时本脚本已让路;其它脏文件视为异常,不动)
  if [ -n "$(git status --porcelain)" ]; then echo "ALERT dirty worktree, skip auto-merge"; exit 3; fi
  git checkout -q -B main "$gh" 2>/dev/null
  if git merge -q --no-ff "$gl" -m "merge: 自动并入 GitLab 侧人工提交 ${gl:0:7}(镜像分叉自动收敛) to #85045988"; then
    git push -q "$GH" HEAD:refs/heads/main && echo "OK auto-merged gitlab=${gl:0:7} into github=${gh:0:7} -> $(git rev-parse --short HEAD)"; exit 0
  else
    git merge --abort 2>/dev/null; git checkout -q -B main "$gh"
    echo "ALERT merge conflict github=${gh:0:7} gitlab=${gl:0:7} —— 人工改动与 ECS 生成物撞了同一文件,需人工解决"; exit 3
  fi
fi
rc=$?
if [ $rc -ne 0 ]; then
  # 推送被拒(典型:ECS 对 GitLab 只读,rc=128 "access rights")也按分叉级别告警,
  # 否则只刷日志无人知晓,日积月累必分叉(2026-09-05~11 实录)
  echo "ALERT push rejected rc=$rc github=${gh:0:7} gitlab=${gl:0:7} —— 检查该机器对目标远端的写权限"; exit 3
fi
git merge -q --ff-only "$GL/main" 2>/dev/null; exit 0
