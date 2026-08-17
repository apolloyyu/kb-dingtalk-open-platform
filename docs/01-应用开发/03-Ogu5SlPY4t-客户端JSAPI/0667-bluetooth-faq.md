---
title: "移除发现新设备事件"
source_url: "https://open.dingtalk.com/document/development/bluetooth-faq"
namespace: "development"
slug: "bluetooth-faq"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 移除发现新设备事件"
doc_id: "ijSZDsHw1a"
updated_at: "2025-09-17 21:00:26"
---

> Source: https://open.dingtalk.com/document/development/bluetooth-faq
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 移除发现新设备事件
> Updated: 2025-09-17 21:00:26

# 移除发现新设备事件

调用**dd.offBluetoothDeviceFound**移除寻找到新的蓝牙设备事件的监听。

> **[!IMPORTANT]**
>
> 为防止多次注册事件监听导致一次事件多次回调，建议每次调用on方法监听事件之前，先调用off方法，关闭之前的事件监听。

## **示例代码**

```
dd.offBluetoothDeviceFound();
```
