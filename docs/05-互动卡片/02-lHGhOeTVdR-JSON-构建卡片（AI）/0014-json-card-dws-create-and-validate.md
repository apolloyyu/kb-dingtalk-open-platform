---
title: "DWS 创建与校验"
source_url: "https://open.dingtalk.com/document/development/json-card-dws-create-and-validate"
namespace: "development"
slug: "json-card-dws-create-and-validate"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "创建与校验 > DWS 创建与校验"
doc_id: "uaoulNcjh0"
updated_at: "2026-09-30 09:14:04"
---

> Source: https://open.dingtalk.com/document/development/json-card-dws-create-and-validate
> Path: 互动卡片 / JSON 构建卡片（AI） / 创建与校验 > DWS 创建与校验
> Updated: 2026-09-30 09:14:04

# DWS 创建与校验

## 环境准备

DWS 内置 AI 卡片协议与校验器，查字段契约、离线校验和发给自己预览都用原生命令完成，**不需要 Python 环境**。先把配套 Skill 装进 Agent 目录：

```
dws skill setup --mode multi -s dingtalk-aicard
```

首次使用或遇到无法识别的命令时，确认二进制提供了 `explain`、`lint`、`preview` 三个子命令：

```
dws aicard --help
```

> **[!NOTE]**
>
> - 拷贝 Skill 文件不会给旧版二进制装上命令。
> - 命令缺失时先运行 `dws upgrade`。

## 创建卡片流程

卡片是一个按顺序执行的 JSON 消息数组，保存为 `card.a2ui.json`。按投递场景决定要发哪些消息：

| **场景** | **需要的消息** |
| --- | --- |
| 新建卡片 | createSurface → 根路径 updateDataModel → updateComponents；createSurface 显式声明 catalogId，纯静态卡片也要初始化数据。 |
| 客户端已创建空画布 | 只发 updateDataModel 与 updateComponents，不再创建画布。 |
| 更新已有卡片 | 沿用原 surfaceId，只发实际变化的部分，不要重放 createSurface 或无关的初始值。 |

组件树的根组件 `id` 为 `root`，同一张卡片的 `surfaceId` 保持不变。完整写法见 [最小示例：创建与更新](0001-json-build-card.md#739b42ba58lku)，更多场景见[使用示例](0013-json-card-usage-examples.md)。

## 查询字段契约

```
dws aicard explain <名称>

# 一次查多个，--compact 去掉批量结果里的重复结构
dws aicard explain Button copyText --compact
```

支持组件、函数、设计 Token 与公共类型，与 [组件](0003-json-card-component-overview.md)、[函数](0008-json-card-core-functions.md)、[公共类型](0010-json-card-common-types.md) 是同一份数据。

`explain` 与 `lint` 使用嵌入的协议离线工作，不需要 Python，也不需要登录 Profile。

> **[!NOTE]**
>
> - 查契约用 `dws aicard explain`，不是 `dws aicard lint --explain`。
> - 名称拼错时会返回候选建议。

## 离线校验命令

```
# 校验一个卡片文件
dws aicard lint --file card.a2ui.json

# 更严格的整卡预检
dws aicard lint --file card.a2ui.json --preflight new-card

# 只检查资源引用
dws aicard lint --file card.a2ui.json --preflight resources

# 自检：确认工具自带的协议包完好
dws aicard lint --self-check
```

| **参数** | **说明** |
| --- | --- |
| `--file` | 要校验的文件。  **[!NOTE]**  与 `--self-check` 二选一 |
| `--preflight` | new-card 或 resources，各有独立结论。 |
| `--emit` | 成功时在 `data.a2uiMessages` 返回可直接发送的 JSON 字符串数组，**不写文件**。  **[!NOTE]**  需配合 `--file`。 |
| `--fragment` | 按片段校验，与`--emit` 互斥。 |
| `--self-check` | 校验工具自带的协议包，不看业务文件。 |

读取结果时检查退出码、`ok` 与 `outcome`：成功内容在 `data`，失败在 `error`，结构诊断在 `error.details.diagnostics`。结构校验失败时退出码为 `3`。

> **[!NOTE]**
>
> JSON 结果只写到 stdout，DWS 的环境提示（如 Skill 迁移提醒）会写到 stderr，脚本解析时只读 stdout，**不要把两个流合并**。

## lint 与 **new-card** 校验范围对比

这是最容易误解的一处：**普通 lint 不检查引用闭合**。

| **检查项** | **普通 lint** | `--preflight new-card` |
| --- | --- | --- |
| JSON 语法 | ✓ | ✓ |
| 字段名、必填、类型、枚举 | ✓ | ✓ |
| 最终快照的根节点 | — | ✓ |
| 引用可达性 | — | ✓（不可达组件报警告） |
| 同一消息内重复 ID | — | ✓ |
| 静态环引用 | — | ✓ |

> **[!NOTE]**
>
> 以下内容任何离线校验都证明不了：绑定初始值、模板展开结果、函数运行结果、状态合并、设计效果，以及客户端版本是否支持某个组件。

## 预览卡片

写完先发给自己看一眼，不要直接发到业务会话：

```
# 只校验本地文件，不解析身份也不发送
dws aicard preview --file card.a2ui.json --dry-run

# 发到当前登录用户的单聊；--summary 是会话列表摘要，默认 "Card preview"
dws aicard preview --file card.a2ui.json --summary "卡片预览"
```

- 文件必须含 `createSurface` 与公共 `catalogId`。
- 命令不会修改源文件。
- 只能发给当前登录用户，不接受其他接收者。
- 发送使用 `PROCESSING` 状态，后续状态用 `dws chat message update-a2ui-card` 推进，详见[DWS 发送与更新](0017-json-card-dws-send-and-update.md)。

> **[!NOTE]**
>
> - 预览卡片上的按钮仍会触发真实业务动作。
> - 接口受理成功也不等于送达或渲染成功。

发到群聊或其他人的单聊，见 [DWS 发送与更新](0017-json-card-dws-send-and-update.md)。
