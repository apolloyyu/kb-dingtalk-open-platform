---
title: "统一跳转协议"
source_url: "https://open.dingtalk.com/document/development/unified-jump-protocol"
namespace: "development"
slug: "unified-jump-protocol"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "常见问题 > 统一跳转协议"
doc_id: "pAS2GXnOwB"
updated_at: "2026-07-22 16:25:13"
---

> Source: https://open.dingtalk.com/document/development/unified-jump-protocol
> Path: 应用开发 / 客户端JSAPI / 常见问题 > 统一跳转协议
> Updated: 2026-07-22 16:25:13

# 统一跳转协议

本文介绍了统一跳转协议的常见问题。

- **链接如何在PC端侧边栏或在工作台中打开？**

  答：链接在PC端侧边栏和在工作台中打开方式如下。

  - **在PC端侧边栏打开**：加上`pc_slide=true`后缀，如`dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.dingtalk.com&pc_slide=true`。此外，在H5微应用中，也可以通过[打开侧边面板](0873-open-side-panel.md)来实现。
  - **在工作台中打开**：加上`%26ddtab%3Dtrue`后缀，如`dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fwww.dingtalk.com%26ddtab%3Dtrue`。
  > **[!IMPORTANT]**
  >
  > 中间的"https%3A%2F%2Fwww.dingtalk.com"是目标地址*"*https://www.dingtalk.com*"*经urlencode后的值。
- **如何在PC端与移动端打开不同的URL？**

  答：模板参考 `dingtalk://dingtalkclient/action/open_platform_link?pcLink=XXX&mobileLink=XXX`

  例如：`dingtalk://dingtalkclient/action/open_platform_link?pcLink=https%3A%2F%2Fwww.taobao.com&mobileLink=https%3A%2F%2Fm.dingtalk.com`

  可实现在移动端内打开钉钉官网，在PC端打开淘宝官网。

  > **[!IMPORTANT]**
  >
  > 目标URL需要进行urlencode转换。
- **如何打开钉钉待办页面？**

  答：可以用dingtalk协议唤起（需所在环境支持dingtalk协议）：

  ```
  dingtalk://dingtalkclient/action/switchtab?index=1&type=task
  ```
