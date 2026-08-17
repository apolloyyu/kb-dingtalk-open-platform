---
title: 配置与环境变量
source_refs: pkg/config/constants.go, internal/plugin/loader.go, pkg/configmeta/registry.go, internal/transport/client.go, internal/apiclient/client.go, internal/logging/logger.go, internal/app/root.go, internal/i18n/i18n.go, internal/app/event_command.go, internal/upgrade/github.go
---

# 配置与环境变量

本篇覆盖配置目录、settings.json、环境变量清单、代理、日志与 i18n。

## 配置目录

默认 `~/.dws`（`pkg/config/constants.go` 的 `DefaultConfigDir()`），优先级 `DWS_CONFIG_DIR` > `~/.dws`。未使用 XDG 规范。

## settings.json

`~/.dws/settings.json` 存储插件配置（pluginConfigs），由 `internal/plugin/loader.go` 的 `settingsPath()` / `loadSettings()` 读取，并经 `InjectPluginConfigEnv()` 注入环境变量。

另有覆盖文件：`~/.dws/mcp_url`、`~/.dws/terminal_url` 可覆盖 MCP / 开放平台地址（`GetMCPBaseURL` / `GetTerminalBaseURL`，pkg/config/constants.go）。

## 环境变量注册表

`pkg/configmeta/registry.go` 提供 `Register()` / `ConfigItem`，变量分 `core` / `auth` / `network` / `security` / `audit` / `runtime` / `debug` / `external` 八类，供 `dws config list` 展示。

## 主要环境变量清单

| 变量 | 用途 |
|---|---|
| `DWS_CONFIG_DIR` | 配置目录覆盖 |
| `DWS_LANG` | i18n 语言 |
| `DWS_CLIENT_ID` / `DWS_CLIENT_SECRET` | 客户端凭据 |
| `DWS_KEYCHAIN_DIR` / `DWS_DISABLE_KEYCHAIN` | keychain 存储控制 |
| `DINGTALK_DWS_AGENTCODE` | Agent 标识 |
| `DWS_CHANNEL` | 渠道标识 |
| `DWS_SKILL_SOURCE` / `DWS_SKILL_API_HOST` | Skill 来源 |
| `DWS_STREAM_TICKET_MODE` / `DWS_STREAM_SOURCE_ID` / `DWS_STREAM_URL` | Stream 长连接（event_command.go） |
| `DWS_UPGRADE_URL` / `DWS_UPGRADE_REPOSITORY` | 自升级源（upgrade/github.go） |
| `GITHUB_TOKEN` / `GH_TOKEN` | GitHub API 凭据 |
| `DO_NOT_TRACK` | 关闭遥测 |
| `DWS_ALLOW_HTTP_ENDPOINTS` | 允许 HTTP（非 HTTPS）端点 |
| `DWS_AUDIT_DIR` / `DWS_AUDIT_FORWARD_URL` / `DWS_AUDIT_FORWARD_TOKEN` / `DWS_AUDIT_REDACT` | 审计目录/转发/脱敏 |

## 代理

使用 `http.ProxyFromEnvironment`，支持标准 `HTTP_PROXY` / `HTTPS_PROXY` / `NO_PROXY`（`internal/transport/client.go`、`internal/apiclient/client.go`）。

## 日志

`internal/logging/logger.go`：JSON 行写入 `~/.dws/logs/dws.log`，单文件上限 5MB，保留 2 个备份（`rotatingWriter`）；入口为 `Setup()` / `FileLogger`。另有 `redact.go`（脱敏）与 `multi_handler.go`。

级别映射由 `configureLogLevel()`（internal/app/root.go）控制：`--debug` → Debug、`--verbose` → Info、默认 Warn；文件日志恒为 Debug 级。

## i18n

`internal/i18n/i18n.go`：语言选取顺序 `DWS_LANG` → 回退 `LANG` → 默认 `en`；文案通过 `go:embed` 内嵌 `locales/en.json`、`locales/zh.json`；API 为 `T()` / `Tf()` / `Init()`。
