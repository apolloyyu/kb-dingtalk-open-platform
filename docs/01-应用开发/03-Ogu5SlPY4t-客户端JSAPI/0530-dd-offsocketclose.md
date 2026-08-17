---
title: "取消监听WebSocket关闭事件"
source_url: "https://open.dingtalk.com/document/development/dd-offsocketclose"
namespace: "development"
slug: "dd-offsocketclose"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听WebSocket关闭事件"
doc_id: "8WZgQO9353"
updated_at: "2025-09-17 20:58:55"
---

> Source: https://open.dingtalk.com/document/development/dd-offsocketclose
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > WebSocket > 取消监听WebSocket关闭事件
> Updated: 2025-09-17 20:58:55

# 取消监听WebSocket关闭事件

调用**dd.offSocketClose**取消监听WebSocket关闭事件。

## **示例代码**

```
Page({
  onLoad() {
  dd.onSocketClose(this.callback);
  },
  onUnload() {
    dd.offSocketClose(this.callback);
    //    dd.offSocketClose();
  },
  callback(res) {
  dd.alert({content: '连接已关闭！'});
   },
})
```
