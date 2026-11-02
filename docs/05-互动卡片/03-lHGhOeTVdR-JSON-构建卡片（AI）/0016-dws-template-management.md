---
title: "DWS 模板管理"
source_url: "https://open.dingtalk.com/document/development/dws-template-management"
namespace: "development"
slug: "dws-template-management"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "创建与校验 > DWS 模板管理"
doc_id: "LNsN635ROm"
updated_at: "2026-10-29 11:52:25"
---

> Source: https://open.dingtalk.com/document/development/dws-template-management
> Path: 互动卡片 / JSON 构建卡片（AI） / 创建与校验 > DWS 模板管理
> Updated: 2026-10-29 11:52:25

# DWS 模板管理

## 能力状态

| **项** | **状态** |
| --- | --- |
| 命令 | `dws aicard template create / get / update`。**尚未进入 DWS 公开版本**，需要包含最新 AICard 模块的 DWS 构建；先运行 `dws aicard template --help` 确认命令存在 |
| 服务 ID | 必须用 `--mcp-id` 或环境变量 `DWS_AICARD_TEMPLATE_MCP_ID` 显式指定，没有默认值。 |
| 作用范围 | 只管理模板资产：**不发送卡片、不激活业务绑定、不修改已发出的卡片**。 |

## 与场景模板的区别

[场景模板](0014-scene-template.md)是随 Skill 分发的本地 JSON 文件；本页的**云端模板**是保存在服务端、有模板 ID 和版本号的资产，适合由业务配置按 ID 和版本引用。常见做法是从场景模板改出自己的卡片，校验通过后再用 `create` 保存为云端模板。

## 创建模板

```
dws aicard template create --mcp-id 10764 --file card.a2ui.json --format json
```

- 文件必须是完整的 A2UI 消息数组，UTF-8 编码。
- 先在本地校验，通过后才调用服务，返回服务端分配的**模板 ID 和版本号**，请保存下来。

## 读取模板

```
dws aicard template get --mcp-id 10764 \
  --template-id <模板 ID> --version 1 --out template.a2ui.json --format json
```

| **参数** | **说明** |
| --- | --- |
| `--template-id` | 服务端返回的模板 ID；不支持按名称搜索。 |
| `--version` | 正整数版本号的字符串，如 `1`。 |
| `--out` | **新文件**路径；文件已存在时拒绝覆盖。 |

## 追加新版本

```
dws aicard template update --mcp-id 10764 \
  --template-id <模板 ID> --file revised.a2ui.json --format json
```

在同一个模板 ID 下追加一个版本，需要该模板的创建者权限。

## 通用说明

- 三个命令都需要登录的 Profile，并且只能访问当前组织的模板，跨组织访问会被拒绝。
- 加 `--dry-run` 只做本地校验，不调用服务、不写文件。
- 发送卡片仍然使用 [DWS 发送与更新](0019-json-card-dws-send-and-update.md)或 [机器人发送卡片](0020-robot-send-aicard.md)，与模板命令相互独立。
