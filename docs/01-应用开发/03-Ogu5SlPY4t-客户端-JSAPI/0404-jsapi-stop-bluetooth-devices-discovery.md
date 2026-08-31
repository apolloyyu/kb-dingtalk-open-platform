---
title: "stopBluetoothDevicesDiscovery"
source_url: "https://open.dingtalk.com/document/development/jsapi-stop-bluetooth-devices-discovery"
namespace: "development"
slug: "jsapi-stop-bluetooth-devices-discovery"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > stopBluetoothDevicesDiscovery"
doc_id: "CkhOPo8DsB"
updated_at: "2025-08-27 18:08:00"
---

> Source: https://open.dingtalk.com/document/development/jsapi-stop-bluetooth-devices-discovery
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > stopBluetoothDevicesDiscovery
> Updated: 2025-08-27 18:08:00

# stopBluetoothDevicesDiscovery

调用dd.stopBluetoothDevicesDiscovery停止搜寻附近的蓝牙外围设备。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10177) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 否 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.stopBluetoothDevicesDiscovery({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
