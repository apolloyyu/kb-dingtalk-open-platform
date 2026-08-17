---
title: 常见报错与排查
source_refs: internal/errors/errors.go, internal/errors/exitcodes.go, internal/errors/pat.go, internal/helpers/errors.go, internal/helpers/helpers.go, internal/app/flags.go, internal/app/root.go
---

# 常见报错与排查

本篇覆盖错误体系、退出码、PAT 错误、helpers 层 CLIError、token 过期提示与排查流程。

## 错误体系（internal/errors/errors.go）

- `Category`：`api` / `auth` / `validation` / `discovery` / `internal` / `partial_failure`。
- `Error` 结构：`Message` / `Operation` / `Retryable` / `Hint` / `Actions` / `RPCCode` / `ServerDiag` 等。
- 构造器：`NewAPI` / `NewAuth` / `NewValidation` / `NewDiscovery` / `NewInternal`。
- 输出：`PrintJSON` / `PrintHumanAt`；详级 `Verbosity` 三级：Normal / Verbose / Debug。

## 退出码表（internal/errors/exitcodes.go `exitCodeByCategory`）

| 退出码 | 类别 |
|---|---|
| 1 | api |
| 2 | auth |
| 3 | validation |
| 4 | PAT（`ExitCodePermission`） |
| 5 | internal |
| 6 | discovery |
| 7 | partial（`ExitCodePartial`） |

## PAT 错误

`internal/errors/pat.go` 的 `PATError`：退出码 4；`RawStderr()` 原样透传 JSON（用于 host-owned agent 模式）。

## helpers 层 CLIError

`internal/helpers/errors.go` 定义 `CLIError`（`Code` / `Message` / `Suggestion`），常见错误码：`AUTH_TOKEN_EXPIRED`、`AUTH_NOT_CONFIGURED`、`NETWORK_TIMEOUT`、`NETWORK_UNREACHABLE`、`MCP_SERVER_ERROR` 等。`WrapError` 按网络故障模式分类（DNS / TLS / 拒连 / 超时）。

## token 过期提示

- 匹配 `"token验证失败"` / `USER_TOKEN_ILLEGAL` → 提示 "Token 已过期或验证失败"；
- `apiKeyExpired` → 提示 "API Key 已过期"；
- 建议文案 `authExpiredSuggestion()` = "Re-authenticate: dws auth login"（internal/helpers/helpers.go）；
- 网关码 `DWS_SERVICE_UNAUTHORIZED` / `TOKEN_VERIFIED_FAILED`（`dwsGatewayErrors`）；
- `TOKEN_VERIFIED_FAILED` / `CLI_ORG_NOT_AUTHORIZED` 提示 "该组织尚未开启 CLI 数据访问权限"（internal/errors/errors.go `serverGuidance`）。

## debug / verbose

全局持久 flag `--debug`、`--verbose`（`-v`）注册于 `internal/app/flags.go` 的 `GlobalFlags`；`internal/app/root.go` 的 `resolveVerbosity()` 将其映射到错误输出详级。多处错误提示会建议 "Use --verbose for detailed logs"。日志文件 `~/.dws/logs/dws.log` 恒为 Debug 级，排查时先看日志。

## 排查建议流程

1. 看退出码定类别（对照上表）；
2. 加 `--verbose` 重跑命令；
3. 查 `~/.dws/logs/dws.log`；
4. 认证问题跑 `dws auth status` 看诊断 reason；
5. 仍无法定位时跑 `dws doctor`。
