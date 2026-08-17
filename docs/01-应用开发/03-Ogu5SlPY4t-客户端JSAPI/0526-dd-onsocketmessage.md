---
title: "监听接收到的消息事件"
source_url: "https://open.dingtalk.com/document/development/dd-onsocketmessage"
namespace: "development"
slug: "dd-onsocketmessage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听接收到的消息事件"
doc_id: "YCxhUk0RF8"
updated_at: "2025-09-17 20:58:53"
---

> Source: https://open.dingtalk.com/document/development/dd-onsocketmessage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 监听接收到的消息事件
> Updated: 2025-09-17 20:58:53

# 监听接收到的消息事件

调用**dd.onSocketMessage**监听WebSocket接收到服务器的消息事件。

## **示例****代码**

```
dd.connectSocket({
  url: '服务器地址'
})

dd.onSocketMessage(function(res) {
  console.log('收到服务器内容：' + res.data)
})
```

## **回调返回值**

| **名称** | **类型** | **说明** |
| --- | --- | --- |
| data | String/ArrayBuffer | 服务器返回的消息。  普通的文本String或者经base64编码后的String。 |
| isBuffer | Boolean | - **true：****`data`**字段表示接收到的经过了base64编码后的String， - **false：**`data`字段表示接收到的普通String文本。 |
