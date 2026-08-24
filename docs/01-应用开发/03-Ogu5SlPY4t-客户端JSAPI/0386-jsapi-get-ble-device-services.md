---
title: "getBLEDeviceServices"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-ble-device-services"
namespace: "development"
slug: "jsapi-get-ble-device-services"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > getBLEDeviceServices"
doc_id: "vx2ONp5fIU"
updated_at: "2025-08-27 18:07:48"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-ble-device-services
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > getBLEDeviceServices
> Updated: 2025-08-27 18:07:48

# getBLEDeviceServices

调用getBLEDeviceServices，获取蓝牙设备所有服务。

> 建立连接后先执行`getBLEDeviceServices`与`getBLEDeviceCharacteristics`后再进行与蓝牙设备的数据交互。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10167) |

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

- `deviceId`（string，必填）：蓝牙设备 id。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `services`（array，必填）
- `services[].isPrimary`（boolean，必填）：该服务是否为主服务。
- `services[].serviceId`（string，必填）：蓝牙设备服务的 uuid。

## **示例****代码**

### 默认出入参

```
dd.getBLEDeviceServices({
  deviceId: '0D9C82AD-1CC0-414D-9526-119E08D28124',
  success: (res) => {
    const { services } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "services": [
    { "isPrimary": true, "serviceId": "00001800-0000-1000-8000-00805f9b34fb" }
  ]
}
```
