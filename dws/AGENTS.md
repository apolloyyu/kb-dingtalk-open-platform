# dws 域 — 检索协议

本目录是 dws CLI(DingTalk Workspace CLI,开源命令行工具)的整理版知识层,
由模型实读源码生成;生成时的源码 commit 见 `meta/MANIFEST.json` 的 `source_commit`,
每篇 frontmatter 的 `source_refs` 列出该篇事实来源的源码文件路径。

用法:
1. 先查 `index.md` 选主题篇目,读正文;
2. **本层是加速层,不是权威层**:参数/flag 以 `dws <cmd> --help` 实测为准,
   行为细节求证下钻源码仓库(github.com/DingTalk-Real-AI/dingtalk-workspace-cli);
3. 时效判断:对照 `meta/MANIFEST.json` 的 source_commit 与上游 CHANGELOG;
4. 本层由流水线整目录再生成维护,不做手工增量修改;发现事实错误,
   走上游仓库 issue 或触发重新生成,不要改本目录文件。
