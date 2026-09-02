---
title: "getConnectedBluetoothDevices"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-connected-bluetooth-devices"
namespace: "development"
slug: "jsapi-get-connected-bluetooth-devices"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > getConnectedBluetoothDevices"
doc_id: "t8dq1uqBi5"
updated_at: "2025-08-27 18:07:56"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-connected-bluetooth-devices
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > getConnectedBluetoothDevices
> Updated: 2025-08-27 18:07:56

# getConnectedBluetoothDevices

调用getConnectedBluetoothDevices，获取处于已连接状态的设备。

> - 如果传递的services为空，则返回所有的已经连接的设备。
> - Android上获取到的deviceId为设备MAC地址，iOS上则为设备uuid。因此deviceId不能硬编码到代码中，需要区分处理。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10179) |

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

- `services`（array，必填）：蓝牙设备主 service 的 uuid 列表。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `devices`（array，必填）
- `devices[].RSSI`（number，必填）：设备信号强度。
- `devices[].name`（string，必填）：蓝牙设备名称，某些设备可能没有。
- `devices[].deviceName`（string，必填）：值与 name 一致。兼容旧版本。
- `devices[].localName`（string，必填）：广播设备名称。
- `devices[].deviceId`（string，必填）：设备 Id。
- `devices[].advertisData`（string，必填）：设备的广播内容。
- `devices[].manufacturerData`（string，必填）：设备的manufacturerData。

## **示例****代码**

### 默认出入参

```
dd.getConnectedBluetoothDevices({
  services: ['00001800-0000-1000-8000-00805f9b34fb'],
  success: (res) => {
    const { devices } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "devices": [
    {
      "RSSI": 100,
      "name": "我的耳机",
      "deviceId": "0D9C82AD-1CC0-414D-9526-119E08D28124",
      "localName": "名称",
      "deviceName": "我的耳机",
      "advertisData": "0x26FF",
      "manufacturerData": "0x1800"
    }
  ]
}
```
