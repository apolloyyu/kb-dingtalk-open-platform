---
title: "开启监听蓝牙状态变化事件"
source_url: "https://open.dingtalk.com/document/development/dd-onbluetoothadapterstatechange"
namespace: "development"
slug: "dd-onbluetoothadapterstatechange"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 开启监听蓝牙状态变化事件"
doc_id: "Cxp5x3Xrfe"
updated_at: "2025-09-17 21:00:25"
---

> Source: https://open.dingtalk.com/document/development/dd-onbluetoothadapterstatechange
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 开启监听蓝牙状态变化事件
> Updated: 2025-09-17 21:00:25

# 开启监听蓝牙状态变化事件

调用**dd.onBluetoothAdapterStateChange(callback)** 监听本机蓝牙状态变化的事件。

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 事件回调函数。 |

**callback 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| available | Boolean | 蓝牙模块是否可用。 |
| discovering | Boolean | 蓝牙模块是否处于搜索状态。 |
