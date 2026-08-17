---
title: "获取所有已发现的蓝牙设备"
source_url: "https://open.dingtalk.com/document/development/dd-getbluetoothdevices"
namespace: "development"
slug: "dd-getbluetoothdevices"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取所有已发现的蓝牙设备"
doc_id: "thxYKEBsoY"
updated_at: "2025-09-17 21:00:23"
---

> Source: https://open.dingtalk.com/document/development/dd-getbluetoothdevices
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取所有已发现的蓝牙设备
> Updated: 2025-09-17 21:00:23

# 获取所有已发现的蓝牙设备

调用**dd.getBluetoothDevices**获取所有已发现的蓝牙设备，包括已经和本机处于连接状态的设备。

> **[!IMPORTANT]**
>
> - 模拟器可能无法获取advertisData及RSSI，请使用真机调试。
> - 开发者工具和Android上获取到的deviceId为设备MAC地址，iOS上则为设备uuid。因此deviceId 不能硬编码到代码中，需要分平台处理，iOS可根据设备属性（ localName、advertisData、manufacturerData等属性）进行动态匹配。

## **示例代码**

```
dd.getBluetoothDevices({
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

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| devices | Array | 已发现的设备列表。 |

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
