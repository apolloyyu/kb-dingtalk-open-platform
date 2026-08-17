---
title: "取消监听接收消息事件"
source_url: "https://open.dingtalk.com/document/development/dd-offsocketmessage"
namespace: "development"
slug: "dd-offsocketmessage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听接收消息事件"
doc_id: "kxJgWEwCc1"
updated_at: "2025-09-17 20:58:53"
---

> Source: https://open.dingtalk.com/document/development/dd-offsocketmessage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听接收消息事件
> Updated: 2025-09-17 20:58:53

# 取消监听接收消息事件

调用**dd.offSocketMessage**取消监听WebSocket接收到服务器的消息事件。

## 示例代码

```
dd.connectSocket({
  url: '服务器地址'
})

dd.onSocketMessage(function(res) {
  console.log('收到服务器内容：' + res.data)
})

dd.offSocketMessage();
```
