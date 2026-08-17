---
title: "关闭WebSocket连接"
source_url: "https://open.dingtalk.com/document/development/dd-closesocket"
namespace: "development"
slug: "dd-closesocket"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 关闭WebSocket连接"
doc_id: "RL7pKp0pea"
updated_at: "2025-09-17 20:58:54"
---

> Source: https://open.dingtalk.com/document/development/dd-closesocket
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 关闭WebSocket连接
> Updated: 2025-09-17 20:58:54

# 关闭WebSocket连接

调用**dd.closeSocket**关闭WebSocket连接。

## **示例****代码**

```
dd.onSocketOpen(function() {
  dd.closeSocket()
})

dd.onSocketClose(function(res) {
  console.log('WebSocket 已关闭！')
})
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| success | Function | 否 | 回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
