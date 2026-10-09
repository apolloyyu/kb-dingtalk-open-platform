---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/json-card-building-faq"
namespace: "development"
slug: "json-card-building-faq"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "其他参考 > 常见问题"
doc_id: "JA2iRnJzFy"
updated_at: "2026-09-30 09:13:59"
---

> Source: https://open.dingtalk.com/document/development/json-card-building-faq
> Path: 互动卡片 / JSON 构建卡片（AI） / 其他参考 > 常见问题
> Updated: 2026-09-30 09:13:59

# 常见问题

## 版本号

- **version 该填什么？**

  消息信封里的 `version` 固定为 `"v1.0"`。把它写成 `"V0.8"` 是最高频的错误，消息会被直接拒绝。`V0.8` 是组件与函数的能力版本（`aicardVersion`），`1.0` 是协议版本（`protocolVersion`），三者互不相同。

## 发送与更新

- **--content 为什么传对象不行？**

  它是**字符串数组**，每一项是 A2UI 消息对象**再做一次 JSON 序列化**后的字符串，不是直接嵌套的对象。用 `dws aicard lint --emit` 可以直接生成这个格式，不要手写转义。
- **发送时要不要传模板 ID？**

  不需要。JSON 构建的卡片结构全部由消息携带，不依赖卡片平台上的模板。需要模板 ID 的是[模板搭建](../02-MhNX42mFB1-模板搭建卡片/0001-card-template-building-and-publishing.md)的链路。
- **更新时能不能重发 createSurface？**

  不能。更新**只发** `updateComponents` **和** `updateDataModel` ，`createSurface` 属于创建阶段，一个卡片生命周期内只能出现一次。

## 组件

- **客户端动作为什么不生效？**

  先确认 `action.functionCall.catalogId` 显式写了 `urn:dingtalk:a2ui:host:v1`，Surface 或组件上的 catalogId 不能代替它。漏写或写错会被 lint 直接拒绝，所以 lint 通过后仍不生效，要排查的是运行时：当前会话的宿主授权与客户端版本支持，需真机确认。
- **只想改一个字段，要重发整棵组件树吗？**

  不要。用 `updateDataModel` 按 JSON Pointer 路径更新对应字段即可。重发整棵组件树会让客户端丢失用户已经输入的内容。路径必须以 `/` 开头。

## 校验

- **lint 通过了，为什么卡片还是显示不对？**

  离线校验只证明**结构合法**：字段名、必填、类型、枚举。它不能证明绑定初始值、模板展开结果、函数运行结果、设计效果，也不能证明目标客户端版本支持该组件。上线前必须真机验证。
- **普通 lint 和 --preflight new-card 有什么区别？**

  **普通 lint 不检查引用闭合**。`--preflight new-card` 额外检查最终快照的根节点、引用可达性、同一消息内的重复 ID 和静态环引用，不可达组件会产生警告。

## 概念

- **「AI 卡片模板」和这里讲的是一回事吗？**

  不是。[AI 卡片模板](../02-MhNX42mFB1-模板搭建卡片/0002-ai-card-template.md)是模板搭建链路里的一种模板类型，在卡片平台创建，内置处理中、输入中、完成、失败四个状态，靠 `isFinalize`、`isError` 切换。JSON 构建不需要模板。
- **文档里的「模板」到底指什么？**

  有三个不同含义：**卡片模板**指平台搭建、发布后有 ID 的那种；**子项模板**指 `Loop`、`Table` 里用一个组件按数据重复渲染的 `template` 字段；**场景模板**指[现成的卡片结构](0013-json-card-usage-examples.md)，复制即用。

## 迁移

- **已经在用模板卡，需要迁移吗？**

  不需要。两条链路可以在同一个应用里共存。只有当模板无法表达你要的结构时，才考虑换成 JSON 构建。
