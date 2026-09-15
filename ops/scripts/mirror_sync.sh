#!/usr/bin/env bash
# 知识库双远端快进同步：GitLab(写入口) <-> GitHub(助理沙箱读取的镜像)。
# 只做 --ff-only：任一方向不能快进即告警退出，绝不强推。由应用 executor 的 kb.mirror 调度
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
