---
title: 审计与安全
source_refs: internal/audit/event.go, internal/audit/collect.go, internal/audit/rotate.go, internal/audit/chain.go, internal/audit/forward.go, internal/audit/redact.go, internal/app/audit_runtime.go, internal/security/crypto.go, internal/security/storage.go, internal/security/fingerprint.go, internal/safety/content_scan.go, internal/app/runner.go, internal/corecmd/corecmd.go, internal/app/flags.go, internal/helpers/helpers.go
---

# 审计与安全

本篇覆盖审计日志链路、本地凭据加密、内容安全扫描，以及命令确认门控（`--yes`）。

## 审计事件与触发

审计记录结构见 `internal/audit/event.go` 的 `Event`，字段包括：时间、`execution_id`、`agent_id`、`Actor{user/corp}`、product、command、endpoint（经 `RedactURL` 脱敏）、`params_summary`（脱敏后截断 1024）、result、错误分类、耗时、CLI 版本、os/arch，以及 `prev_hash` / `hash`。

触发点为 `internal/app/audit_runtime.go` 的 `emitAudit`（约 L113）。

## 审计存储与链路

| 模块 | 职责 |
|---|---|
| `collect.go` `BuildSink` | 默认目录 `<configDir>/audit`，`DWS_AUDIT_DIR` 可覆盖，保留 90 天 |
| `rotate.go` `DateRotatingWriter` | 按日滚动写 `audit-YYYYMMDD.jsonl`（JSONL 格式，flock 跨进程锁） |
| `chain.go` `Chain.SealFromFile` | sha256 哈希链（prev_hash/hash）防篡改 |
| `forward.go` `HTTPForwarder` | 远端转发，`DWS_AUDIT_FORWARD_URL` / `DWS_AUDIT_FORWARD_TOKEN` / `DWS_AUDIT_REDACT` |
| `redact.go` `RedactEvent` | 脱敏级别 `none` / `hashed` / `minimal` |

## 本地凭据保护（internal/security）

注意：`internal/security` 是本地凭据保护模块，不是敏感词过滤：

- `crypto.go`：`DeriveKey` / `Encrypt`，PBKDF2-SHA256 迭代 600k 轮派生密钥，AES-256-GCM 加密；
- `storage.go`：`SecureTokenStorage`，token 加密存储在 `.data` 文件；
- `fingerprint.go`：`selectMAC` 选取网卡 MAC 作机器指纹，`virtualMACPrefixes` 避开虚拟网卡前缀。

## 内容安全：提示注入扫描

`internal/safety/content_scan.go` 的 `ContentScanner.ScanPayload` 用正则检测提示注入，包括 `ignore_previous_instructions`、`reveal_system_prompt`、`policy_bypass` 及其中文变体，输出 `Finding` / `Report`。

由 `internal/app/runner.go` 的 `scanContent`（约 L963）在运行时响应上执行；enforce 模式命中即拦截。

## 确认门控与 --yes

- 叶子通过 `DeclareLeafMetadata` / `Spec` 声明 `contract.SafetySpec.Confirmation = "user_required"`。
- 运行时 `internal/corecmd/corecmd.go` 的 `ConfirmSafety`（约 L1193）在 RunE 包装内执行（约 L417–485）；`helpers/leaf.go` 亦调用该门控。
- `confirmationBypass`（corecmd.go 约 L1276）判断是否可绕过：检查 `yes` / `dry-run` / `user-say-yes`，取值范围跨本命令 flagset、继承 flagset 与 root persistent flagset。
- 全局 `--yes` 注册于 `internal/app/flags.go` 约 L55，语义为 "AI Agent 模式"。
- 非交互场景遇到 EOF 不视为拒绝，而是返回结构化错误 `confirmation_required`（提示加 `--yes`）。
- Sheet 破坏性操作另有 `protectSheetMutationCommand`（helpers/sheet_batch.go 约 L380），只要求 `--yes` 门。
- 遗留助手 `helpers/helpers.go` 的 `confirmDelete` / `confirmDangerousAction`（约 L735 / L761）仍在使用。

**规则**：当 `confirmation=user_required` 时，Agent 在添加 `--yes` 之前必须先获得用户确认。
