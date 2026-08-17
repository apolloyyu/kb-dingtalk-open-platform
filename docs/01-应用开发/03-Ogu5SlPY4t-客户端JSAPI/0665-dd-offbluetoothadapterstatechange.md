---
title: "移除监听蓝牙状态变化事件"
source_url: "https://open.dingtalk.com/document/development/dd-offbluetoothadapterstatechange"
namespace: "development"
slug: "dd-offbluetoothadapterstatechange"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 移除监听蓝牙状态变化事件"
doc_id: "HXZ83EHSlF"
updated_at: "2025-09-17 21:00:25"
---

> Source: https://open.dingtalk.com/document/development/dd-offbluetoothadapterstatechange
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 移除监听蓝牙状态变化事件
> Updated: 2025-09-17 21:00:25

# 移除监听蓝牙状态变化事件

调用**dd.offBluetoothAdapterStateChange**移除本机蓝牙状态变化的事件的监听。

> **[!IMPORTANT]**
>
> 为防止多次注册事件监听导致一次事件多次回调，建议每次调用on方法监听事件之前，先调用off方法，关闭之前的事件监听。

## **示例代码**

```
dd.offBluetoothAdapterStateChange();
```
