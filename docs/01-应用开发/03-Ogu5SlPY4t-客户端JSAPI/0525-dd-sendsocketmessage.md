---
title: "发送数据"
source_url: "https://open.dingtalk.com/document/development/dd-sendsocketmessage"
namespace: "development"
slug: "dd-sendsocketmessage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 发送数据"
doc_id: "Wv2jaCWmuc"
updated_at: "2025-09-17 20:58:52"
---

> Source: https://open.dingtalk.com/document/development/dd-sendsocketmessage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 发送数据
> Updated: 2025-09-17 20:58:52

# 发送数据

调用**dd.sendSocketMessage**通过WebSocket连接发送数据。需要先使用dd.connectSocket发起连接，再使用dd.onSocketOpen回调之后再发送数据。

## **示例****代码**

```
dd.sendSocketMessage({
    data: this.data.toSendMessage, // 需要发送的内容
    success: (res) => {
        dd.alert({content: '数据发送！' + this.data.toSendMessage});
    },
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| data | String/ArrayBuffer | 是 | 需要发送的内容：普通的文本内容String或者经base64编码后的String。 |
| isBuffer | Boolean | 否 | 如果需要发送二进制数据，需要将入参数据经base64编码成String后赋值`data`，同时将此字段设置为true，否则如果是普通的文本内容String，不需要设置此字段。 |
| success | Function | 否 | 回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
