---
title: "取消监听WebSocket错误"
source_url: "https://open.dingtalk.com/document/development/dd-offsocketerror"
namespace: "development"
slug: "dd-offsocketerror"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听WebSocket错误"
doc_id: "awDejUfgL4"
updated_at: "2025-09-17 20:58:52"
---

> Source: https://open.dingtalk.com/document/development/dd-offsocketerror
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听WebSocket错误
> Updated: 2025-09-17 20:58:52

# 取消监听WebSocket错误

调用dd.offSocketError取消监听WebSocket错误。

## **示例代码**

```
Page({
  onLoad() {
    this.callback = this.callback.bind(this);
    dd.onSocketError(this.callback);
  },
  onUnload() {
    dd.offSocketError(this.callback);
  },
  callback(res) {
  },
})
```
