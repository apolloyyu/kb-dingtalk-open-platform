---
title: "notifyBLECharacteristicValueChange"
source_url: "https://open.dingtalk.com/document/development/jsapi-notify-ble-haracteristic-value-change"
namespace: "development"
slug: "jsapi-notify-ble-haracteristic-value-change"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > notifyBLECharacteristicValueChange"
doc_id: "OD9YkGVbj9"
updated_at: "2025-08-27 18:07:50"
---

> Source: https://open.dingtalk.com/document/development/jsapi-notify-ble-haracteristic-value-change
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > notifyBLECharacteristicValueChange
> Updated: 2025-08-27 18:07:50

# notifyBLECharacteristicValueChange

调用notifyBLECharacteristicValueChange，启用低功耗蓝牙设备特征值变化时的notify功能。

> - 订阅操作成功后需要设备主动更新特征值的 value，才会触发onBLECharacteristicValueChange。
> - 订阅方式效率比较高，推荐使用订阅代替 read 方式。
> - 设备的特征值必须支持 notify/indicate 才可以成功调用，具体参照 haracteristic 的 properties 属性。
> - 必须先启用 notify 才能监听到设备 characteristicValueChange 事件。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10166) |

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

- `state`（boolean）：是否启用notify或indicate。
- `deviceId`（string，必填）：蓝牙设备 id，参考 device 对象。
- `serviceId`（string，必填）：蓝牙特征值对应 service 的 uuid。
- `characteristicId`（string，必填）：蓝牙特征值的 uuid。
- `descriptorId`（string）：notify 的 descriptor 的 uuid。  
    
  > 只有android 会用到，非必填，默认值00002902-0000-10008000-00805f9b34fb。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.notifyBLECharacteristicValueChange({
  state: true,
  deviceId: '0D9C82AD-1CC0-414D-9526-119E08D28124',
  serviceId: '00001800-0000-1000-8000-00805f9b34fb',
  descriptorId: '00002902-0000-10008000-00805f9b34fb',
  characteristicId: '9fa480e0-4967-4542-9390-d343dc5d04ae',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
