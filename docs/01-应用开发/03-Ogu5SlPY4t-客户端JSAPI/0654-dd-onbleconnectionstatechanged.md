---
title: "监听蓝牙连接状态事件"
source_url: "https://open.dingtalk.com/document/development/dd-onbleconnectionstatechanged"
namespace: "development"
slug: "dd-onbleconnectionstatechanged"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 监听蓝牙连接状态事件"
doc_id: "FGDlZBv9Eg"
updated_at: "2025-09-17 21:00:18"
---

> Source: https://open.dingtalk.com/document/development/dd-onbleconnectionstatechanged
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 监听蓝牙连接状态事件
> Updated: 2025-09-17 21:00:18

# 监听蓝牙连接状态事件

调用**dd.onBLEConnectionStateChanged(callback)** 监听低功耗蓝牙连接的错误事件，包括设备丢失，连接异常断开等。

> **[!IMPORTANT]**
>
> 为防止多次注册事件监听导致一次事件多次回调，建议每次调用on方法监听事件之前，先调用off方法，关闭之前的事件监听。

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 事件回调函数。 |

**callback 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| deviceId | String | 蓝牙设备 id，参考 device 对象。 |
| connected | Boolean | 连接目前的状态。 |
