---
title: "取消监听WebSocket连接打开事件"
source_url: "https://open.dingtalk.com/document/development/dd-offsocketopen"
namespace: "development"
slug: "dd-offsocketopen"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听WebSocket连接打开事件"
doc_id: "50lRJvC2AC"
updated_at: "2025-09-17 20:58:51"
---

> Source: https://open.dingtalk.com/document/development/dd-offsocketopen
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听WebSocket连接打开事件
> Updated: 2025-09-17 20:58:51

# 取消监听WebSocket连接打开事件

调用**dd.offSocketOpen**取消监听WebSocket连接打开事件。

## **示例****代码**

```
Page({
  onLoad() {
    this.callback = this.callback.bind(this);
    dd.onSocketOpen(this.callback);
  },
  onUnload() {
    dd.offSocketOpen(this.callback);
  },
  callback(res) {
  },
})
```
