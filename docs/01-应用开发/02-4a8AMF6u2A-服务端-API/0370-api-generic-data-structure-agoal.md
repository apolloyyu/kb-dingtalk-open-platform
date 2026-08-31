---
title: "通用数据结构"
source_url: "https://open.dingtalk.com/document/development/api-generic-data-structure-agoal"
namespace: "development"
slug: "api-generic-data-structure-agoal"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Agoal > 通用数据结构"
doc_id: "sox5fILkNn"
updated_at: "2026-08-12 09:16:17"
---

> Source: https://open.dingtalk.com/document/development/api-generic-data-structure-agoal
> Path: 应用开发 / 服务端 API / Agoal > 通用数据结构
> Updated: 2026-08-12 09:16:17

# 通用数据结构

## Entity

实体

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| metas | Array of [Meta](#d550bdace7bhy) |  | 字段列表 |
| type | String | DIMENSION | 类型 |
| linkSourceId | String | 67dbb24f7aac3f62d8b98fb5 | 关联资源ID |
| data | Map | {"title": "123"} | 数据 |
| linkSourceType | String | EXTERNAL\_PERF\_TASK | 关联资源类型 |
| children | Array of 子节点 |  | 子节点 |
| metas | Array of [Meta](#d550bdace7bhy) |  | 字段列表 |
| type | String | DIMENSION | 类型 |
| linkSourceId | String | 67dbb24f7aac3f62d8b98fb5 | 关联资源ID |
| data | Map | {"title": "123"} | 数据 |
| linkSourceType | String | EXTERNAL\_PERF\_TASK | 关联资源类型 |
| id | String | 123 | 唯一标识 |
| isDeleted | String | y/n | 是否删除 |
| id | String | 123 | 唯一标识 |
| isDeleted | String | y/n | 是否删除 |

## Meta

元数据

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| active | Boolean | true | 是否启用 |
| type | String | string | 类型 |
| scheme | Map | {"width": 200} | 渲染约束 |
| category | String | common | 分类 |
| required | Boolean | true | 是否必填 |
| alias | String | 编码 | 别名 |
| title | String | 名称 | 标题 |
| forceActive | Boolean | true | 强制启动 |
| code | String | title | 标识 |
| forceRequired | Boolean | true | 强制必填 |

## OpenAgoalAlignDTO

Agoal 对齐

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| objectiveId | String | 662e006fe4b0f579bbcxxxxx | 对齐的目标 id |
| objectType | String | objective | 被对齐的对象类型 objective/keyResult |
| objectId | String | 662e006fe4b0f579bbcxxxxx | 被对齐的对象 id: 目标 id/KR id |
| alignType | String | COOPERATION | 对齐关系类型；SUPPORT-承接，COOPERATION-协同 |

## OpenAgoalFieldMetaDTO

字段元数据

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| fieldId | String | 662e006fe4b0f579bbcxxxxx | 字段ID |
| code | String | foo | 字段元数据标识 |
| title | String | 字段名 | 字段元数据名称 |
| alias | String | 字段别名 | 字段元数据别名 |
| note | String | 字段备注 | 字段备注 |
| source | String | OPEN | 字段数据来源 |
| active | Boolean | true | 是否启用 |
| type | String | string | 字段类型 |
| entityType | String | OBJECTIVE | 实体类型 |

## OpenAgoalKeyActionDTO

Agoal关键行动DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| keyActionId | String | 6444f5e9a4261c6e699dxxxx | 关键行动id |
| title | String | 测试 | 关键行动标题 |
| url | String | https://agoal.dingtalk.com | 关键行动url |

## OpenAgoalKeyResultDTO

Agoal关键进展DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| keyResultId | String | 6444f5e9a4261c6e699dxxxx | 关键结果id |
| title | String | 测试KR | 关键结果title |
| titleMentions | Array of [TitleMention](#78992f8d51sog) |  | 关键结果at人信息 |
| type | Integer | 1 | 关键结果类型 |
| status | Integer | 1 | 关键结果状态 |
| progress | Integer | 10 | 关键结果进度 |
| weight | double | 30 | 关键结果权重 |
| keyActions | Array of [OpenAgoalKeyActionDTO](#02c4fa12c4x1d) |  | 关联的关键行动 |

## OpenAgoalLatestProgressDTO

Agoal最新进展DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| progressId | String | 6444f5e9a4261c6e699dxxxx | Agoal最新进展id |
| created | Long | 1716952481672 | Agoal最新进展创建时间 |
| creator | [OpenAgoalUserDTO](#52e896dc1dt47) |  | Agoal最新进展创建人 |
| htmldescription | String | <article class=\"4ever-article\"><p style=\"text-align:left;text-indent:0;margin-left:0;margin-top:0;margin-bottom:0\"><span>xxx</span></p></article> | Agoal最新进展文本内容 |

## OpenAgoalObjectiveDTO

Agoal目标DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| objectiveId | String | 6444f5e9a4261c6e699dxxxx | 目标id |
| title | String | 测试目标 | 目标title |
| executor | [OpenAgoalUserDTO](#52e896dc1dt47) |  | 目标执行人 |
| teams | Array of [OpenAgoalTeamDTO](#1f99935508oqw) |  | 目标归属团队 |
| period | [OpenObjectiveRulePeriodDTO](#f4125dbbf8v4m) |  | 目标周期 |
| progress | Integer | 0 | 目标进度 |
| status | Integer | 1 | 目标状态 |
| keyResults | Array of [OpenAgoalKeyResultDTO](#1d71397cb2yt7) |  | 目标关联关键结果 |
| weight | double | 30 | 目标权重 |
| objectiveRule | [OpenOrgObjectiveRuleDTO](#655aea60bee0u) |  | 目标所属规则 |
| keyActions | Array of [OpenAgoalKeyActionDTO](#02c4fa12c4x1d) |  | 关联的关键行动 |
| latestProgress | [OpenAgoalLatestProgressDTO](#47ac1fd6f22nb) |  | 最新进展 |
| relatedUsers | Array of [OpenAgoalUserDTO](#52e896dc1dt47) |  | 关联方 |
| upAlignObjectIds | Array of String | 68c8fd9de4b0bexxx47f45a4 | 对齐的目标id |
| downAlignObjectIds | Array of String | 68c8xd9de4b0bex47f45a4 | 对齐的目标id |
| approveStatus | String | approved | 审批状态  待审批：preApprove  审批中：approving  审批通过：approved  审批不通过：notApproved |
| created | Long | 1723690100689 | 创建时间 |
| updated | Long | 1723690100689 | 更新时间 |

## OpenAgoalObjectiveDimensionDTO

目标维度

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| dimensionId | String | 662e006fe4b0f579bbcxxxxx | 目标维度 id |
| fieldConfig | Array of [OpenAgoalFieldMetaDTO](#823f1ed9a170z) |  | 维度字段配置 |
| fieldValueMap | Map | name:xxx | 维度字段值 |
| children | Array of children |  | 子维度 |
| dimensionId | String | 662e006fe4b0f57ccbcxxxxx | 目标维度 id |
| title | String | 这是子维度标题 | 维度标题 |
| weight | double | 100 | 权重 |
| title | String | 这是维度标题 | 维度标题 |
| weight | double | 100 | 权重 |

## OpenAgoalOrgObjectiveDTO

Agoal目标DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| objectiveId | String | 6444f5e9a4261c6e699dxxxx | 目标id |
| title | String | 测试目标 | 目标title |
| status | String | formalEffective | 状态 |
| executor | [OpenAgoalUserDTO](#52e896dc1dt47) |  | 目标执行人 |
| team | [OpenAgoalTeamDTO](#1f99935508oqw) |  | 归属团队 |
| period | [OpenObjectiveRulePeriodDTO](#f4125dbbf8v4m) |  | 目标周期 |
| upAlignObjects | Array of [OpenAgoalAlignDTO](#231aa711de0vv) |  | 上对齐数据 |
| downAlignObjects | Array of [OpenAgoalAlignDTO](#231aa711de0vv) |  | 下对齐数据 |
| fieldConfig | Array of [OpenAgoalFieldMetaDTO](#823f1ed9a170z) |  | 目标字段配置 |
| fieldValueMap | Map | name：xxx | 目标字段值 |
| dimension | [OpenAgoalObjectiveDimensionDTO](#2af9dc3a9atxt) |  | 目标所属维度（顶层维度） |

## OpenAgoalOrgObjectiveListDTO

组织目标列表

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| totalCount | Long | 100 | 组织目标总数 |
| objectiveList | Array of [OpenAgoalOrgObjectiveDTO](#e1b3fd71d1eqw) |  | 组织目标列表 |

## OpenAgoalPeriodDTO

Agoal 周期

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| periodId | String | 6444f5e9a4261c6e699dxxxx | 周期id |
| name | String | 2024年度 | 周期名称 |
| startDate | Long | 1711900800000 | 开始时间 |
| endDate | Long | 1743436799000 | 结束时间 |
| periodType | String | season | 周期类型 |

## OpenAgoalProgressDTO

目标进展

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| progressId | String | 66bd6c7455c22xxxx | 进展 id |
| htmlContent | String | <article class=\"4ever-article\"><p style=\"text-align:left;text-indent:0;margin-left:0;margin-top:0;margin-bottom:0\"><span data-type=\"text\">这是一条测试进展</span></p><p style=\"text-align:left;text-indent:0;margin-left:0;margin-top:0;margin-bottom:0\"><span data-type=\"text\"></span></p></article> | 进展内容 |
| created | Long | 1723690100689 | 创建时间 |
| updated | Long | 1723690100689 | 更新时间 |
| creator | [OpenAgoalUserDTO](#52e896dc1dt47) |  | 创建者用户信息 |
| modifier | [OpenAgoalUserDTO](#52e896dc1dt47) |  | 更新者用户信息 |
| progress | Integer | 100 | 进度百分比 |
| keyResults | Array of [OpenAgoalKeyResultDTO](#1d71397cb2yt7) |  | 关联的KR信息 |

## OpenAgoalTeamDTO

Agoal部门DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| teamId | String | 6444f5e9a4261c6e699dxxxx | Agoal部门id |
| deptId | String | 8535683xx | 部门deptId |
| name | String | 测试部门 | 部门名称 |

## OpenAgoalUserDTO

Agoal用户DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| userId | String | 6444f5e9a4261c6e699dxxxx | Agoal用户id |
| dingUserId | String | 211042291978xxxx | 用户dingUserId |
| name | String | 测试 | 用户名称 |

## OpenObjectiveRuleDTO

Agoal目标规则DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| objectiveRuleId | String | 6444f5e9a4261c6e699dxxxx | 目标规则id |
| objectiveRuleName | String | 规则 | 目标规则名称 |
| objectiveCategory | String | OKR / PBC | 目标类型 |
| probationRule | Boolean | true | 是否是试用期规则 |
| periods | Array of [OpenObjectiveRulePeriodDTO](#f4125dbbf8v4m) |  | 周期对象集合 |
| popRuleView | Array of [OpenObjectiveRuleScopeDTO](#7cffcbf8823zh) |  | 应用范围 |
| excludePopRuleView | Array of [OpenObjectiveRuleScopeDTO](#7cffcbf8823zh) |  | 排除应用范围 |
| status | String | ONLINE | 状态   - **已启用**：ONLINE - **已禁用**：OFFLINE - **未启用**：DRAFT |

## OpenObjectiveRulePeriodDTO

Agoal目标规则周期DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| periodId | String | 6444f5e9a4261c6e699dxxxx | 周期id |
| name | String | 2024年度 | 周期名称 |
| startDate | Long | 1711900800000 | 开始时间 |
| endDate | Long | 1743436799000 | 结束时间 |
| periodType | String | season | 周期类型 |

## OpenObjectiveRuleScopeDTO

Agoal目标规则应用范围DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| scopeType | String | USER | 应用范围类型   - **个人**：USER - **部门**：DEPARTMENT - **组织**：ORGANIZATION |
| scopeId | String | 82347xxx2382 | 应用范围id   - **个人**：openId - **部门**：deptId - **组织**：dingtalkCorpId |

## OpenOrgObjectiveRuleDTO

目标规则对象DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| objectiveRuleId | String | 6444f5e9a4261c6e699dxxxx | 目标规则id |
| objectiveRuleName | String | 测试规则 | 规则名称 |
| objectiveCategory | String | OKR / PBC | 规则类型 |

## OpenOrgPerfDocDTO

Agoal考核文档DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| docId | String | 68ff24096990383xxx7e71d8 | 文档Id |
| score | String | 100 | 得分 |
| executor | [OpenAgoalUserDTO](#52e896dc1dt47) |  | 负责人 |
| team | [OpenAgoalTeamDTO](#1f99935508oqw) |  | 部门 |
| state | String | PENDING | 状态   - **待完善考核表**：ASSESSMENT\_TOBECOMPLETED - **待启动**：PENDING - **进行中**：IN\_PROGRESS - **已终止**：FINISHED - **已归档**：ARCHIVED |

## OpenOrgPerfPlanDTO

Agoal考核计划DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| planId | String | 68ff23f2699038xxx87e71cf | 考核计划Id |
| title | String | 考核计划 | 名称 |
| status | String | PENDING | 状态   - **待启动**：PENDING - **进行中**：IN\_PROGRESS - **已归档**：ARCHIVED |

## OpenScoreCardDimensionDTO

指标id结构

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| scoreCardId | String | 67492b72f3532a0f0751exxx | 计分卡id |
| dimensionList | Array of dimensionList |  | 维度列表 |
| dimensionId | String | 67493024b9e95c2fb523a30xx | 维度id |
| indicatorList | Array |  | 原始指标信息[有引用指标库的指标] |
| indicatorId | String | 67493024b9e95c2fb523a3xx | 指标id |
| originId | String | 6824587ab942892303512e31 | 原始指标id |
| originCode | String | code\_6824587ab942892303512e31 | 原始指标code |
| indicatorIdList | Array of String | 67493024b9e95c2fb523a3xx | 指标id |

## OpenUserAdminDTO

OpenUserAdminDTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| dingCorpId | String | dingxxxxe3d8c283bb4aa39a90f97fcb1e09 | 钉钉corpId |
| dingUserId | String | 211042291978xxxx | 员工staffId |

## OpenUserSubAdminDTO

用户子管理员DTO

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| dingCorpId | String | dingxxxxe3d8c283bb4aa39a90f97fcb1e09 | 钉钉corpId |
| dingUserId | String | 211042291978xxxx | 员工staffId |
| deptIds | Array of String | 123 | 部门ID |
| permissionGroupCodes | Array of String | 123 | 权限分组编码 |

## PerfTask

考核任务

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| status | String | ONGOING | 状态枚举 |
| isDeleted | String | y/n | 是否删除 |
| title | String | xxx考核任务 | 名称 |
| userId | String | 23223423 | 负责人钉钉user id |
| id | String | 328497234 | 唯一标识 |
| cycleName | String | 2026年/2026年第一季度 | 周期名称 |

## TitleMention

Agoal关键进展at对象

| 参数名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| user | [OpenAgoalUserDTO](#52e896dc1dt47) |  | 用户对象 |
| offset | Integer | 0 | 起始 |
| length | Integer | 10 | 长度 |
