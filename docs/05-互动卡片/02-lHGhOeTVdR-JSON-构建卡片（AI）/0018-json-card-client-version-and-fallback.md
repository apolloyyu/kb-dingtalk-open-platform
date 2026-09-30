---
title: "客户端版本与降级"
source_url: "https://open.dingtalk.com/document/development/json-card-client-version-and-fallback"
namespace: "development"
slug: "json-card-client-version-and-fallback"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "其他参考 > 客户端版本与降级"
doc_id: "mU23CYJCf3"
updated_at: "2026-09-30 09:14:00"
---

> Source: https://open.dingtalk.com/document/development/json-card-client-version-and-fallback
> Path: 互动卡片 / JSON 构建卡片（AI） / 其他参考 > 客户端版本与降级
> Updated: 2026-09-30 09:14:00

# 客户端版本与降级

## 组件兼容性

- 各组件对应的客户端最低版本尚未在本站收录。
- 离线校验只能证明结构合法，不能证明目标客户端支持该组件。
- 上线前请在真机上验证目标版本的渲染结果。

## 降级策略

- 组件提供 `fallbackMarkdown` 字段，当渲染器无法渲染该组件时展示其中的 Markdown 内容。
- 建议对使用了较新组件的卡片补充`fallbackMarkdown` 字段。

## 验证流程

1. **离线校验**：确认结构合法。
2. **发给自己**：`dws aicard preview` 看真实渲染。
3. **覆盖目标版本**：在业务实际使用的客户端版本上复验。
