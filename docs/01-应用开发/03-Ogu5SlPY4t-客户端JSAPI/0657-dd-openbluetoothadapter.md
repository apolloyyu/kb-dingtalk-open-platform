---
title: "初始化蓝牙接口"
source_url: "https://open.dingtalk.com/document/development/dd-openbluetoothadapter"
namespace: "development"
slug: "dd-openbluetoothadapter"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 初始化蓝牙接口"
doc_id: "HsfxyNZK15"
updated_at: "2025-09-17 21:00:20"
---

> Source: https://open.dingtalk.com/document/development/dd-openbluetoothadapter
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 初始化蓝牙接口
> Updated: 2025-09-17 21:00:20

# 初始化蓝牙接口

调用**dd.openBluetoothAdapter**初始化小程序蓝牙模块，生效周期为调用**dd.openBluetoothAdapter** 至调用**dd.closeBluetoothAdapter，**或小程序被销毁为止。

在小程序蓝牙适配器模块生效期间，开发者可以正常调用蓝牙模块API，并会收到蓝牙模块相关的on事件回调。

小程序蓝牙模块初始化完成后，可以通过调用`dd.onBluetoothAdapterStateChange`监听手机蓝牙状态的改变。

> **[!IMPORTANT]**
>
> - 在调用`dd.openBluetoothAdapter`API之前，调用小程序其它蓝牙模块相关API，API会返回错误，参见下方错误码。
> - 在用户蓝牙未开启或者手机不支持蓝牙功能的情况下，调用`dd.openBluetoothAdapter`会返回错误，参见下方错误码。

## **示例代码**

```
dd.openBluetoothAdapter({
  success: (res) => {
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| autoClose | Boolean | 否 | 不传的话默认是true，表示是否在离开当前页面时自动断开蓝牙(仅对android有效)。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| isSupportBLE | Boolean | 是否支持 BLE。 |

## **错误码**

| **错误码** | **描述** | 解决方案 |
| --- | --- | --- |
| 12 | 蓝牙未打开。 | 请尝试打开蓝牙。 |
| 13 | 与系统服务的链接暂时丢失。 | 请尝试重新连接。 |
| 14 | 未授权使用蓝牙功能。 | 请授权使用蓝牙功能。 |
| 15 | 未知错误。 | - |
| 10000 | 未初始化蓝牙适配器 |  |
