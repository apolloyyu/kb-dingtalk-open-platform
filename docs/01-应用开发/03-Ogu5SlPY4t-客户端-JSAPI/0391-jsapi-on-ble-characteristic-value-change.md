---
title: "onBLECharacteristicValueChange"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-ble-characteristic-value-change"
namespace: "development"
slug: "jsapi-on-ble-characteristic-value-change"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > onBLECharacteristicValueChange"
doc_id: "Rj7kpY4YAe"
updated_at: "2025-08-27 18:07:51"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-ble-characteristic-value-change
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > onBLECharacteristicValueChange
> Updated: 2025-08-27 18:07:51

# onBLECharacteristicValueChange

调用onBLECharacteristicValueChange，监听低功耗蓝牙设备的特征值变化的事件。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10169) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `deviceId`（string，必填）：蓝牙设备 id，参考 device 对象。
- `serviceId`（string，必填）：蓝牙特征值对应 service 的 uuid。
- `characteristicId`（string，必填）：蓝牙特征值的 uuid。
- `value`（string，必填）：特征值最新的16进制值。

## **示例****代码**

### 默认出入参

```
dd.onBLECharacteristicValueChange((res) => {
  const { value, deviceId, serviceId, characteristicId } = res;
});
```

返回对象示例：

```
{
  "value": "0x26FF",
  "deviceId": "0D9C82AD-1CC0-414D-9526-119E08D28124",
  "serviceId": "00001800-0000-1000-8000-00805f9b34fb",
  "characteristicId": "9fa480e0-4967-4542-9390-d343dc5d04ae"
}
```
