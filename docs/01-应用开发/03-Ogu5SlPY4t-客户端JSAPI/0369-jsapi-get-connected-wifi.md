---
title: "getConnectedWifi"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-connected-wifi"
namespace: "development"
slug: "jsapi-get-connected-wifi"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > Wi-Fi > getConnectedWifi"
doc_id: "Rpb0q5lyeF"
updated_at: "2025-08-27 18:07:37"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-connected-wifi
> Path: 应用开发 / 客户端JSAPI / 设备能力 > Wi-Fi > getConnectedWifi
> Updated: 2025-08-27 18:07:37

# getConnectedWifi

获取已连接 Wi-Fi 信息。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11476) |

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

### 入参

- `wifi`（object，必填）：Wi-Fi 信息。
- `wifi.SSID`（string，必填）：设备的 SSID。
- `wifi.BSSID`（string，必填）：设备的 BSSID。
- `wifi.secure`（string，必填）：是否安全：   
    
  \* true：安全   
  \* false：不安全
- `wifi.signalStrength`（string，必填）：Wi-Fi 信号强度，取值 0 ～ 100。  
    
  > 值越大强度越大。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.getConnectedWifi({
  success: (res) => {
    const { wifi } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "wifi": {
    "SSID": `SSID示例值`,
    "BSSID": `BSSID示例值`,
    "secure": `secure示例值`,
    "signalStrength": `signalStrength示例值`
  }
}
```
