---
title: "查找设备并连接"
source_url: "https://open.dingtalk.com/document/development/dd-connectbledevice"
namespace: "development"
slug: "dd-connectbledevice"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 查找设备并连接"
doc_id: "4QLymify0F"
updated_at: "2025-09-17 21:00:14"
---

> Source: https://open.dingtalk.com/document/development/dd-connectbledevice
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 查找设备并连接
> Updated: 2025-09-17 21:00:14

# 查找设备并连接

调用**dd.connectBLEDevice**连接低功耗蓝牙设备。

> **[!NOTE]**
>
> - 若小程序在之前已有搜索过某个蓝牙设备，可直接传入之前搜索获取的 deviceId 直接尝试连接该设备，无需进行搜索操作。
> - 若指定的蓝牙设备已经连接，重复连接直接返回成功。

## **示例代码**

```
dd.connectBLEDevice({
  // 这里的 deviceId 可通过 getBluetoothDevices 或 onBluetoothDeviceFound 接口中获取
  deviceId: deviceId,
  success: (res) => {
    console.log(res)
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | String | 是 | 蓝牙设备ID，可通过[获取所有已发现的蓝牙设备](https://open.dingtalk.com/document/orgapp/dd-getbluetoothdevices)或[监听发现新设备事件](https://open.dingtalk.com/document/orgapp/dd-onbluetoothdevicefound)接口中获取。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
