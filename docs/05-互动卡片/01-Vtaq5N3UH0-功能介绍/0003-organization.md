---
title: "名词释义"
source_url: "https://open.dingtalk.com/document/development/organization"
namespace: "development"
slug: "organization"
group: "互动卡片"
tab: "功能介绍"
breadcrumb: "名词释义"
doc_id: "MIbt8OCVUe"
updated_at: "2026-10-09 14:34:35"
---

> Source: https://open.dingtalk.com/document/development/organization
> Path: 互动卡片 / 功能介绍 / 名词释义
> Updated: 2026-10-09 14:34:35

# 名词释义

## 使用说明

本表供按需查阅，无需通读，前半部分为两种构建方式共用的**通用术语**，后半部分仅适用于 **JSON 构建**。

文档、SDK 与模型提示词**统一使用本表词汇**，字段级契约详见各组件与消息文档。

## 通用术语

### 「模板」两种含义

"模板"一词在不同语境下指代两个概念，接入时请先确认具体所指：

| **名称** | **含义** | **使用场景** |
| --- | --- | --- |
| 卡片模板 | 在卡片平台搭建并发布后获得 ID，决定整张卡片的结构。 | 模板搭建链路，`cardTemplateId`。 |
| 子项模板 | 以单个组件为模子，按数据列表重复渲染出多个实例。 | JSON 构建，`Loop` / `Table` / `GridLayout` 的 `template` 字段。 |

### 「AI 卡片」两种含义

| **名称** | **含义** |
| --- | --- |
| AI 卡片模板 | **模板搭建**链路中的一种模板类型，内置处理中、输入中、完成、失败四个状态，通过流式更新接口传 `isFinalize`、`isError` 切换。 |
| 钉钉 AI 卡片 V0.8 | 本文档 **JSON 构建**链路的对外产品名称，结构随消息下发，无需模板；状态使用 `flowStatus` 表示，内容使用 `updateDataModel` 更新。 |

### 投递相关术语

| **术语** | **含义** |
| --- | --- |
| `bizId` | 卡片业务 ID，发送时返回，更新时用于定位卡片。 |
| `flowStatus` | 卡片的流转状态，共 9 个取值，详见 [DWS 发送与更新](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0017-json-card-dws-send-and-update.md)。 |
| 宿主函数 | 即宿主动作，详见下方**协议术语**。 |

## JSON 构建术语

### 协议术语

| **Term** | **术语** | **定义** |
| --- | --- | --- |
| `A2UI` | A2UI 协议 | Agent to UI，开放的声明式 UI 协议：Agent 以 JSON 消息描述界面，由 Renderer 渲染为原生 UI，钉钉 AI 卡片基于其 v1.0 扩展。 |
| `Agent` | Agent | 生成 A2UI 消息的一方，通常为开发者的服务端程序或 AI 应用。 |
| `Renderer` | 渲染器 | 接收 A2UI 消息并将其绘制为原生 UI 的一方，在 AI 卡片中即钉钉客户端。 |
| `Component` | 组件 | 卡片 UI 的基本构成单元，可嵌套形成组件树，如 Text、Button、Column。 |
| `Surface` | 画布 | 承载组件树的渲染容器，按交付边界由宿主或 `createSurface` 创建；更新时复用原 `surfaceId`。 |
| `Data Model` | 数据模型 | 与组件树分离存储的数据树，由 `updateDataModel` 消息维护。 |
| `Data Binding` | 数据绑定 | 组件字段对数据模型路径的引用，写作 `{"path": "/…"}`。使字段取值随数据更新而变化，无需重发组件树。 |
| `Action` | 动作 | 组件的交互处理器，可向 Agent 派发事件，或调用渲染端本地函数。 |
| `Message` | 消息 | A2UI 的通信单元，当前公开四种：`createSurface`、`updateComponents`、`updateDataModel`、`deleteSurface`。 |
| `Catalog` | 组件目录 | 声明可用组件与函数集合及其字段约束的契约；其 `catalogId` 为运行时标识，不是下载地址。协议包按文件分片仅为便于按需阅读，分片不是独立的运行时 Catalog。 |
| `Host Action` | 宿主动作 | 由钉钉宿主执行的函数，如确认弹窗、复制、图片预览等，写在 `action.functionCall` 中，必须显式声明宿主 catalogId `urn:dingtalk:a2ui:host:v1`。 |

### 创作术语

| **Term** | **术语** | **定义** |
| --- | --- | --- |
| `Style` | 样式 | 组件的视觉属性取值，如颜色、字号、圆角、背景等。 |
| `Style Guide` | 样式指南 | 各场景下组件样式选用的建议文档，允许偏离。 |
| `Pattern` | 意图模式 | 针对一类使用意图推荐的组件组合，允许偏离。 |
| `Data` | 数据 | 单次发送时填入卡片结构的业务值，区别于协议层的 Data Model。 |
| `Render` | 渲染 | Renderer 将消息绘制为客户端界面的过程。 |
| `Validation` | 校验 | Schema 校验仅检查公开 JSON Schema；结构 lint 在其上叠加同版本的槽位与函数约束。普通 lint 不检查引用闭合、绑定初值、状态合并或渲染效果，两者均不模拟运行时。 |
| `Verification` | 验证 | 包含三个独立环节：送达指在同一目标会话中回读到消息；渲染指在指定客户端版本上观察到预期结果；交互指操作后观察到回调或状态变化。接口受理成功不等于其中任何一项。 |

### 三个版本字段

| **字段** | **取值** | **含义** |
| --- | --- | --- |
| `version` | `"v1.0"` | 消息包络版本，每条消息必填。 |
| `protocolVersion` | `"1.0"` | A2UI 协议版本，投递接口透传。 |
| `aicardVersion` | `"V0.8"` | 组件与函数的能力集版本。 |
