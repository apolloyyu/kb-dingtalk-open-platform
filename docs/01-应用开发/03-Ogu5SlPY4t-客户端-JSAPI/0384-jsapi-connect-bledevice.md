---
title: "connectBLEDevice"
source_url: "https://open.dingtalk.com/document/development/jsapi-connect-bledevice"
namespace: "development"
slug: "jsapi-connect-bledevice"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > connectBLEDevice"
doc_id: "F2qjaywfEd"
updated_at: "2025-08-27 18:07:47"
---

> Source: https://open.dingtalk.com/document/development/jsapi-connect-bledevice
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > connectBLEDevice
> Updated: 2025-08-27 18:07:47

# connectBLEDevice

调用connectBLEDevice，连接低功耗蓝牙设备。

> - 若小程序在之前已有搜索过某个蓝牙设备，可直接传入之前搜索获取的 deviceId 直接尝试连接该设备，无需进行搜索操作。
> - 若指定的蓝牙设备已经连接，重复连接直接返回成功。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10161) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `deviceId`（string，必填）：蓝牙设备ID，可通过[获取所有已发现的蓝牙设备](https://open.dingtalk.com/document/orgapp/dd-getbluetoothdevices)或[监听发现新设备事件](https://open.dingtalk.com/document/orgapp/dd-onbluetoothdevicefound)接口中获取。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.connectBLEDevice({
  deviceId: '0D9C82AD-1CC0-414D-9526-119E08D28124',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
