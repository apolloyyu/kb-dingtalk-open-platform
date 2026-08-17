---
title: "获取已连接设备"
source_url: "https://open.dingtalk.com/document/development/dd-getconnectedbluetoothdevices"
namespace: "development"
slug: "dd-getconnectedbluetoothdevices"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取已连接设备"
doc_id: "6SSD7MZDvC"
updated_at: "2025-09-17 21:00:24"
---

> Source: https://open.dingtalk.com/document/development/dd-getconnectedbluetoothdevices
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取已连接设备
> Updated: 2025-09-17 21:00:24

# 获取已连接设备

调用**dd.getConnectedBluetoothDevices**获取处于已连接状态的设备。

> **[!IMPORTANT]**
>
> - 如果传递的services为空，则返回所有的已经连接的设备。
> - Android上获取到的deviceId为设备MAC地址，iOS上则为设备uuid。因此deviceId不能硬编码到代码中，需要区分处理。

## **示例代码**

```
dd.getConnectedBluetoothDevices({
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
| services | Array | 否 | 蓝牙设备主 service 的 uuid 列表。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| devices | Array | 已连接的设备列表。 |

**device对象**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| name | String | 蓝牙设备名称，某些设备可能没有。 |
| deviceName(兼容旧版本) | String | 值与 name 一致。 |
| localName | String | 广播设备名称。 |
| deviceId | String | 设备 Id。 |
| RSSI | Number | 设备信号强度。 |
| advertisData | Hex String | 设备的广播内容。 |
| manufacturerData | Hex String | 设备的manufacturerData。 |
