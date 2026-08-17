# DWS Agent Wiki（dingtalk-workspace-cli）

本 wiki 基于 dws CLI 源码仓库（commit f06ea4d9）实读生成，面向答疑 Agent，所有事实带源码路径引用。

## 篇目索引

- [架构总览](docs/architecture-overview.md) —— 程序入口、根命令构建、Schema 运行时装配与分层、统一结果信封。
- [命令树与 Schema/Shortcut 契约](docs/command-tree-and-schema.md) —— Shortcut/LeafSpec/corecmd.Spec 声明体系、评审输入与 dws schema 命令。
- [认证与凭证](docs/auth-and-credentials.md) —— OAuth/设备码登录、token 刷新、PAT 行为授权、keychain 加密存储与多 profile。
- [事件系统](docs/event-system.md) —— DingTalk Stream 长连接、本地 event bus、IPC 帧协议与 consume/listen-im 命令。
- [会话与消息](docs/chat-and-messaging.md) —— 群聊/消息/机器人两层命令组织、MCP 工具映射与 DING 消息。
- [富媒体与文件](docs/files-and-media.md) —— 云盘上传下载传输机制、媒体上传与 localio 安全 I/O。
- [审计与安全](docs/audit-and-security.md) —— 审计日志哈希链、凭据加密、提示注入扫描与确认门控。
- [配置与环境变量](docs/config-and-env.md) —— ~/.dws 配置目录、settings.json、环境变量清单、日志与 i18n。
- [常见报错与排查](docs/errors-and-troubleshooting.md) —— 错误类别与退出码、token 过期提示、debug/verbose 与日志排查。
- [构建发布与版本](docs/build-and-release.md) —— Makefile 目标、版本注入、dws upgrade 自升级与 Homebrew 发布。

---

生成时间 2026-08-17，source commit f06ea4d9，详见 MANIFEST.json。
