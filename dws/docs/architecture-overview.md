---
title: 架构总览
source_refs: cmd/main.go, internal/app/root.go, internal/app/schema_source_register.go, internal/cli/schema_source_root.go, internal/cli/schema_runtime_registry.go, internal/cobracmd/tree.go, internal/executor/invocation.go, internal/apiclient/client.go, internal/output/envelope.go, internal/output/result.go, internal/output/emitter.go
---

# 架构总览

本文概述 `dws` CLI 的整体架构:程序入口、根命令工厂、Schema 运行时装配,以及声明、执行、输出各层的职责划分。

## 程序入口

入口在 `cmd/main.go` 的 `main()`。它通过 `app.ExecuteWithTelemetry` 执行,由 `clitrack` 包装埋点逻辑(`trackerConfig`、`trackRun`、`trackedExitError`)。设置环境变量 `DO_NOT_TRACK` 可以退出遥测。

## 根命令工厂

根命令工厂位于 `internal/app/root.go`:

- `ExecuteWithTelemetry`(约 L94)是最外层入口;
- `NewRootCommand`(约 L767)构建完整的 Cobra 命令树;
- `NewSchemaSourceRootCommand`(约 L783)构建 Schema 装配专用的声明树;
- 二者汇聚于 `newRootCommandWithMode`;
- 约 L930–958 挂载 `cli.NewSchemaCommand()`、`cli.NewMCPCommand()`,以及 auth/profile/skill/config/doctor 等 utility 命令。

`internal/cobracmd/tree.go` 只提供树工具:`MergeCommandTree`、`ChildByName`、`NewGroupCommand`。

## Schema 运行时装配

Schema 采用"声明即 Catalog"模式,没有 generate 产物:

1. `internal/app/schema_source_register.go` 中 `registerSchemaRuntimeDelivery()` 调用 `cli.RegisterSchemaSourceRoot(NewSchemaSourceRootCommand)`;
2. `internal/cli/schema_source_root.go` 中 `RegisterSchemaSourceRoot`(约 L88)以 atomic 存储 root factory;`deliverySchemaCatalog` 懒加载并缓存;没有 factory 时 fail-closed;来源常量为 `SchemaSourceRuntimeAssembled`;
3. `internal/cli/schema_runtime_registry.go` 中 `ResolveSchemaBuild`(约 L78)返回 `ResolvedSchemaBuild{effective, bound, registry, root}`,流程为 `resolveEffectiveCommandRegistry` → `resolveBoundCommandRegistry` → `resolveAssembleSchemaRegistry`。

## 分层职责

| 层 | 路径 | 职责 |
|---|---|---|
| Shortcut | `internal/shortcut` | 声明式 `Shortcut`;`adapter.go` 的 `FromShortcut` 转 `corecmd.Spec` |
| corecmd | `internal/corecmd` | `Spec` / `ContractDecl` / `FlagSpec` / `Constraint`;`New` 构建 Cobra 命令 |
| helpers | `internal/helpers` | 产品手写命令;leaf 框架在 `leaf.go` |
| executor | `internal/executor` | `invocation.go` 定义 `Invocation` / `Result` / `Runner` |
| apiclient | `internal/apiclient` | `client.go` 的 `APIClient.Do` |
| output | `internal/output` | 统一输出 |

## 统一结果信封

统一结果输出在 `internal/output`:

- `envelope.go` 定义 `Envelope{ok, outcome, data, meta, error, _notice}`,以及 `Meta`、`OperationInfo`、`Pagination`、`ErrorInfo`;提供 `NewSuccessEnvelope` / `NewFailureEnvelope`。
- `result.go` 定义 `CommandResult` 与 `Success` / `Pending` / `Partial` / `Failure`。业务命令返回 `CommandResult`,不手写外层 JSON。
- `emitter.go` 提供 `EmitResult` / `WriteEnvelope` / `Emitter`,配套 `formatter.go`、`filter.go`、`pretty.go`、`csv.go`、`ndjson.go`、`rollout.go`。
