---
title: "监听WebSocket错误"
source_url: "https://open.dingtalk.com/document/development/dd-onsocketerror"
namespace: "development"
slug: "dd-onsocketerror"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听WebSocket错误"
doc_id: "vt4V7at9IB"
updated_at: "2025-09-17 20:58:51"
---

> Source: https://open.dingtalk.com/document/development/dd-onsocketerror
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听WebSocket错误
> Updated: 2025-09-17 20:58:51

# 监听WebSocket错误

调用**dd.onSocketError**监听WebSocket错误。

## 示例代码

```
dd.connectSocket({
  url: '开发者的服务器地址'
});

dd.onSocketOpen(function(res){
  console.log('WebSocket 连接已打开！');
});

dd.onSocketError(function(res){
  console.log('WebSocket 连接打开失败，请检查！');
});
```
