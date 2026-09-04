#!/usr/bin/env bash
# 知识库双远端快进同步：GitLab(写入口) <-> GitHub(助理沙箱读取的镜像)。
# 只做 --ff-only：任一方向不能快进即告警退出，绝不强推。由 ECS cron 每 10 分钟调用，
# 也可手动执行。用法: mirror_sync.sh [仓库目录]，缺省为脚本所在仓。
set -u
REPO="${1:-$(cd "$(dirname "$0")/../.." && pwd)}"
cd "$REPO" || { echo "ERR no repo $REPO"; exit 2; }
GH=origin; GL=gitlab
git remote get-url "$GL" >/dev/null 2>&1 || { echo "ERR remote $GL 未配置(git remote add gitlab <ssh url>)"; exit 2; }
git fetch -q "$GH" main && git fetch -q "$GL" main || { echo "ERR fetch failed"; exit 1; }
gh=$(git rev-parse "$GH/main"); gl=$(git rev-parse "$GL/main")
if [ "$gh" = "$gl" ]; then echo "OK in-sync $gh"; git merge -q --ff-only "$GH/main" 2>/dev/null; exit 0; fi
if git merge-base --is-ancestor "$gl" "$gh"; then          # GitHub 领先(流水线提交) → 补到 GitLab
  git push -q "$GL" "$gh:refs/heads/main" && echo "OK github->gitlab $gl..$gh"
elif git merge-base --is-ancestor "$gh" "$gl"; then        # GitLab 领先(人工提交) → 推到 GitHub
  git push -q "$GH" "$gl:refs/heads/main" && echo "OK gitlab->github $gh..$gl"
else
  echo "ALERT diverged github=$gh gitlab=$gl —— 两边各有独立提交,需人工 rebase,本脚本不强推"; exit 3
fi
rc=$?; [ $rc -eq 0 ] && git merge -q --ff-only "$GL/main" 2>/dev/null; exit $rc
