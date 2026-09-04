#!/usr/bin/env bash
# 知识库双远端快进同步：GitLab(写入口) <-> GitHub(助理沙箱读取的镜像)。
# 只做 --ff-only：任一方向不能快进即告警退出，绝不强推。由应用 executor 的 kb.mirror 调度
# (ECS/Aone 容器均适用)，也可手动执行。用法: mirror_sync.sh [仓库目录]，缺省为脚本所在仓。
# gitlab 远端缺失时按 KB_GITLAB_NS(默认 git@code.alibaba-inc.com:dingtalk-openplatform-ai)自动补齐，
# 全新克隆(容器重建)无需手工配置。
set -u
REPO="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$REPO" || { echo "ERR no repo $REPO"; exit 2; }
GH=origin; GL=gitlab
if ! git remote get-url "$GL" >/dev/null 2>&1; then
  git remote add "$GL" "${KB_GITLAB_NS:-git@code.alibaba-inc.com:dingtalk-openplatform-ai}/$(basename "$REPO").git" \
    && echo "INFO added remote $GL" || { echo "ERR cannot add remote $GL"; exit 2; }
fi
git fetch -q "$GH" main && git fetch -q "$GL" main || { echo "ERR fetch failed"; exit 1; }
gh=$(git rev-parse "$GH/main"); gl=$(git rev-parse "$GL/main")
if [ "$gh" = "$gl" ]; then echo "OK in-sync ${gh:0:7}"; git merge -q --ff-only "$GH/main" 2>/dev/null; exit 0; fi
if git merge-base --is-ancestor "$gl" "$gh"; then          # GitHub 领先(流水线提交) → 补到 GitLab
  git push -q "$GL" "$gh:refs/heads/main" && echo "OK github->gitlab ${gl:0:7}..${gh:0:7}"
elif git merge-base --is-ancestor "$gh" "$gl"; then        # GitLab 领先(人工提交) → 推到 GitHub
  git push -q "$GH" "$gl:refs/heads/main" && echo "OK gitlab->github ${gh:0:7}..${gl:0:7}"
else
  echo "ALERT diverged github=${gh:0:7} gitlab=${gl:0:7} —— 两边各有独立提交,需人工 rebase,本脚本不强推"; exit 3
fi
rc=$?; [ $rc -eq 0 ] && git merge -q --ff-only "$GL/main" 2>/dev/null; exit $rc
