---
title: "getBLEDeviceCharacteristics"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-ble-device-characteristics"
namespace: "development"
slug: "jsapi-get-ble-device-characteristics"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > getBLEDeviceCharacteristics"
doc_id: "PjXMe4BJtt"
updated_at: "2025-08-27 18:07:49"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-ble-device-characteristics
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > getBLEDeviceCharacteristics
> Updated: 2025-08-27 18:07:49

# getBLEDeviceCharacteristics

调用getBLEDeviceCharacteristics，获取蓝牙设备所有特征值。

> 建立连接后先执行`dd.getBLEDeviceServices`与`dd.getBLEDeviceCharacteristics`后再进行与蓝牙设备的数据交互。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10168) |

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

- `deviceId`（string，必填）：蓝牙设备 ID。  
    
  > \* Android 上为设备 MAC 地址。  
  > \* iOS 上为设备 UUID。
- `serviceId`（string，必填）：蓝牙特征值对应 service 的 UUID。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `characteristics`（array，必填）：设备特征值列。
- `characteristics[].properties`（object，必填）：该特征值支持的操作类型。
- `characteristics[].properties.read`（boolean，必填）：该特征值是否支持 read 操作。
- `characteristics[].properties.write`（boolean，必填）：该特征值是否支持 write 操作。
- `characteristics[].properties.notify`（boolean，必填）：该特征值是否支持 notify 操作。
- `characteristics[].properties.indicate`（boolean，必填）：该特征值是否支持 indicate 操作。
- `characteristics[].characteristicId`（string，必填）：蓝牙设备特征值的 uuid。
- `characteristics[].serviceId`（string，必填）：蓝牙设备特征值对应服务的 uuid。
- `characteristics[].value`（string，必填）：蓝牙设备特征值对应的16进制值。

## **示例****代码**

### 默认出入参

```
dd.getBLEDeviceCharacteristics({
  deviceId: '0D9C82AD-1CC0-414D-9526-119E08D28124',
  serviceId: '00001800-0000-1000-8000-00805f9b34fb',
  success: (res) => {
    const { characteristics } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "characteristics": [
    {
      "value": "0x26FF",
      "serviceId": "00001800-0000-1000-8000-00805f9b34fb",
      "properties": {
        "read": true,
        "write": true,
        "notify": true,
        "indicate": true
      },
      "characteristicId": "9fa480e0-4967-4542-9390-d343dc5d04ae"
    }
  ]
}
```
