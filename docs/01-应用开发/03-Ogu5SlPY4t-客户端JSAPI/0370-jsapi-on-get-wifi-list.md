---
title: "onGetWifiList"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-get-wifi-list"
namespace: "development"
slug: "jsapi-on-get-wifi-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > Wi-Fi > onGetWifiList"
doc_id: "E0Ekuzyvta"
updated_at: "2025-08-27 18:07:37"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-get-wifi-list
> Path: 应用开发 / 客户端JSAPI / 设备能力 > Wi-Fi > onGetWifiList
> Updated: 2025-08-27 18:07:37

# onGetWifiList

监听获取到 Wi-Fi 列表事件。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11480) |

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

- `wifiList`（array，必填）：Wi-Fi 列表数据。
- `wifiList[].SSID`（string，必填）：设备的 SSID。
- `wifiList[].secure`（boolean，必填）：Wi-Fi 是否安全：  
    
  \* true：安全  
    
  \* false：不安全
- `wifiList[].signalStrength`（number，必填）：Wi-Fi 信号强度，取值 0 ～ 100。  
    
  > 值越大强度越大。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.onGetWifiList({
  success: (res) => {
    const { wifiList } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "wifiList": [{ "SSID": `SSID示例值`, "secure": true, "signalStrength": 27 }] }
```
