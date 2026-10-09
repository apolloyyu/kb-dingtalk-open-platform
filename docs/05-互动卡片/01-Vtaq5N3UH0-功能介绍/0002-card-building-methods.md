---
title: "构建方式"
source_url: "https://open.dingtalk.com/document/development/card-building-methods"
namespace: "development"
slug: "card-building-methods"
group: "互动卡片"
tab: "功能介绍"
breadcrumb: "构建方式"
doc_id: "YyJzgWT9Q7"
updated_at: "2026-10-09 18:10:26"
---

> Source: https://open.dingtalk.com/document/development/card-building-methods
> Path: 互动卡片 / 功能介绍 / 构建方式
> Updated: 2026-10-09 18:10:26

# 构建方式

## **链路选择指南**

互动卡片目前有两条链路，可共存于同一应用中。两者在结构来源、发送参数、更新方式和维护方式上存在差异（见下表），请在编码前完成选型。

| **对比项** | **卡片模板（含 AI 卡片模板）** | **JSON 构建（AI 卡片）** |
| --- | --- | --- |
| 结构来源 | 卡片平台搭建并发布的模板 | 消息中携带的组件树 |
| 发送参数 | `cardTemplateId` + `cardParamMap` | 组件树 + 数据模型，无需模板 ID |
| 修改结构 | 在平台修改模板并重新发布 | 修改生成 JSON 的代码即可，无需预先搭建和发布模板 |
| 更新内容 | 通过[卡片更新](../02-MhNX42mFB1-模板搭建卡片/0009-card-update.md)接口修改模板变量 | 使用 `updateDataModel` 按 JSON Pointer 路径更新数据；结构变化使用 `updateComponents` |
| 流转状态 | 仅 AI 卡片模板预设处理中、输入中、完成、失败四个状态，流式更新时传 `isFinalize`、`isError` | 与数据更新相互独立，由 `update-a2ui-card` 的 `flowStatus` 推进，取值详见[卡片状态](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0017-json-card-dws-send-and-update.md) |
| 投递方式 | 创建卡片实例后投放到会话或场域，详见[开放接口投放卡片实例](../02-MhNX42mFB1-模板搭建卡片/0006-open-interface-card-delivery-instance.md) | 调用 `send-a2ui-card` 一步完成，返回 `bizId` |
| 交互回调 | 通过事件回调返回业务侧 | 使用 `dws event consume` 监听当前登录用户收到的卡片操作事件；服务端 HTTP 回调尚未开放，标准 A2UI 响应暂不可用，详见[监听交互事件](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0016-json-card-listen-to-interaction-events.md) |
| 可视化配置 | 支持，运营人员可自行配置 | 不支持，结构由代码生成 |
| 适用场景 | 结构固定、样式统一、需要运营配置 | 结构在运行时确定，由业务代码或 Agent 生成 |

## 与 AI 卡片模板的区别

> **[!NOTE]**
>
> **AI 卡片**与**AI 卡片模板**名称相近，但属于两条不同的链路。前者的结构随消息下发；后者在卡片平台搭建，发布后获得模板 ID。JSON 构建中的"子项模板"是另一个概念，与卡片模板无关，详见[名词释义](0003-organization.md)。

| **对比项** | **AI 卡片（本文档）** | **AI 卡片模板** |
| --- | --- | --- |
| 结构定义位置 | 消息中的组件树 | 卡片平台搭建器 |
| 是否需要发布 | 无需预先搭建和发布模板 | 需要，发布后获得模板 ID |
| 状态切换方式 | 通过 `update-a2ui-card` 的 `flowStatus` 推进；业务数据使用 `updateDataModel` 单独更新 | 预设四个状态，流式更新时传 `isFinalize` / `isError` |
| 查看 | [JSON 构建卡片](../03-lHGhOeTVdR-JSON-构建卡片（AI）/0001-json-build-card.md) | [AI 卡片模板](../02-MhNX42mFB1-模板搭建卡片/0002-ai-card-template.md) |

> **[!NOTE]**
>
> 如果当前使用的 AI 卡片模板已满足需求，无需迁移。仅在模板无法表达所需结构时，才需要考虑切换链路。

## **模板链路迁移指南**

1. **移除 cardTemplateId**：发送参数中不再需要模板 ID，也不再需要 `cardParamMap`。
2. **将模板结构转换为组件树**：模板中的每个区块对应一个组件，具体映射关系请参考组件手册。
3. **将占位符替换为数据绑定**：原 `cardParamMap` 中的键改为数据模型中的路径。
4. **将状态切换改为 flowStatus**：不再传 `isFinalize` / `isError`，改用 `update-a2ui-card` 的 `flowStatus` 推进状态（例如完成时设为 `FINISH`，失败时设为 `ERROR`）；业务内容使用 `updateDataModel` 更新。
5. **先离线校验**，再真机验证：结构合法不代表渲染成功，两个步骤均需执行。
