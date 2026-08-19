---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/dingbadge-faq"
namespace: "development"
slug: "dingbadge-faq"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 常见问题"
doc_id: "OiSFvYiBo0"
updated_at: "2026-07-21 09:26:05"
---

> Source: https://open.dingtalk.com/document/development/dingbadge-faq
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 常见问题
> Updated: 2026-07-21 09:26:05

# 常见问题

本文介绍了钉工牌常见问题。

- **如何识别二维码是钉工牌的码？**

  答：钉钉电子码目前均为dingbadge为内容前缀，可以通过该前缀识别是否为钉工牌的码。
- **如何知道用户当前的码是否具备支付能力？**

  答：解码钉工牌电子码接口会返回码类型，如果是支付码那么该码同时也是支付宝扣款码值，可以调用支付宝的收单接口扣款。
- **钉工牌的码的过期策略是怎么样的？**

  答：1分钟自动刷新，2分钟内解码有效。
