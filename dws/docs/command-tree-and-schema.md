---
title: 命令树与 Schema/Shortcut 契约
source_refs: internal/shortcut/types.go, internal/shortcut/register.go, internal/helpers/leaf.go, internal/corecmd/corecmd.go, internal/corecmd/contract_decl.go, internal/corecmd/contract/types.go, internal/corecmd/contract/final.go, internal/cli/param_concepts.json, internal/cli/param_concepts.go, internal/cli/schema_command_exclusions.go, internal/cli/schema_parameter_mapping_ledger.go, internal/cli/schema_identity_collect.go, internal/cli/command_meta.go, internal/cli/canonical.go, internal/cli/schema_catalog.go
---

# 命令树与 Schema/Shortcut 契约

Cobra 命令树由 `app.NewRootCommand` 构建;`cobracmd/tree.go` 仅提供树合并/查找工具。本文介绍 Shortcut、corecmd 契约、评审输入与 `dws schema` 命令。

## Shortcut 声明层

`internal/shortcut/types.go` 定义 `Shortcut` 结构(约 L147),字段包括 `Service`、`Command`、`Flags`、`Constraints`、`Risk`、`Safety`、`Contract`(`corecmd.ContractDecl`)、`Disposition`、`Validate`、`Execute` 等。`register.go` 提供 `Register` / `Commands` / `build`。

注意:`LeafSpec` 不在 shortcut 包,而在 `internal/helpers/leaf.go`(约 L136,`NewLeafCommand` 约 L193;别名 `LeafFlag`=`corecmd.FlagSpec`、`LeafContract`=`corecmd.ContractDecl`)。

## corecmd 契约层

- `internal/corecmd/corecmd.go`:`Spec`(约 L236,含 `Safety`、`Contract`、`Invoke` / `Orchestrate` / `ResultInvoke`)、`FlagSpec`、`Constraint`、`Ctx`、`New`(约 L373)。
- `contract_decl.go`:`ContractDecl`(约 L39)与 `validateContractDecl`。
- `contract/` 子包:`types.go`(`ToolIdentitySpec`、`ResultSpec`、`SafetySpec` 约 L324、`InterfaceSpec`、`SelectionSpec`、`ParamDecl`)、`final.go`(`ContractFinalPayload`)、`product.go`、`provenance.go`。

## 评审输入(internal/cli)

以下文件仅作为装配输入,**不是** Catalog 声明权威:

| 输入 | 路径 | 职责 |
|---|---|---|
| 参数概念 | `param_concepts.json` | `morphological_rules` + `concepts`,经 `param_concepts.go` go:embed 加载为 `Concept`、`ParamMorphRule`;argv 同义词/概念词典 |
| 排除 | `schema_command_exclusions.go` | `reviewedRuntimeSchemaExclusionGroups`,精确排除(如 schema 自身),必须有非空原因 |
| 映射台账 | `schema_parameter_mapping_ledger.go` | `reviewedSchemaParameterMappingExclusions`、`reviewedSchemaParameterBindingRemovals`;只管理 mapping_exclusions / removals |
| 身份收集 | `schema_identity_collect.go` | `CollectIdentitySpecs`、`BuildEffectiveFromSpecs`、`IdentityCollectionReport`;从 live Cobra 叶子的 `ContractFinal.Identity` 收集命令身份 |
| 统一消费入口 | `command_meta.go` | `CommandMeta`、`ResolveMeta`、`installDeliveryCommandMeta` |

## 三层别名(不可混淆)

| 层 | 含义 |
|---|---|
| `FlagSpec.Aliases` | Cobra flag 同义词 |
| `ContractFinal.Identity` aliases | 评审过的 CLI 路径别名 |
| `param_concepts.json` | argv 概念词典,中央预解析归一化 |

## dws schema 命令

`internal/cli/canonical.go` 的 `NewSchemaCommand`(约 L68),`Use` 为 `schema [path]`,flags 包括 `--all` / `--compact` / `--cli-path`(L115–117);`list` 等价于无参(L85)。载荷由 `internal/cli/schema_catalog.go` 的 `deliverySchemaAllPayload` / `deliverySchemaOverviewPayload` / `queryDeliverySchemaPayload` 提供;默认 JSON 输出。

- `schema --all` 是稳定全量导出契约;
- 日常发现走 overview → compact product/group → compact leaf。

## 双向完备性

- 每个 `SchemaRegistry` 工具必须能解析到可执行的 Cobra 命令;
- 每个公开可运行的叶子要么进入 Schema,要么在 `schema_command_exclusions.go` 中有精确评审排除;
- 禁止前缀/通配排除。
