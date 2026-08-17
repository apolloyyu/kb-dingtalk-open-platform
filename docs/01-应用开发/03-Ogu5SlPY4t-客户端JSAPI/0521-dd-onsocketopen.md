---
title: "监听WebSocket连接打开事件"
source_url: "https://open.dingtalk.com/document/development/dd-onsocketopen"
namespace: "development"
slug: "dd-onsocketopen"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听WebSocket连接打开事件"
doc_id: "fzvb4DGfs9"
updated_at: "2025-09-17 20:58:50"
---

> Source: https://open.dingtalk.com/document/development/dd-onsocketopen
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听WebSocket连接打开事件
> Updated: 2025-09-17 20:58:50

# 监听WebSocket连接打开事件

调用**dd.onSocketOpen**监听WebSocket连接打开事件。

## **示例****代码**

```
dd.connectSocket({
  url: 'test.php',
});

dd.onSocketOpen(function(res) {
  console.log('WebSocket 连接已打开！');
});
```
