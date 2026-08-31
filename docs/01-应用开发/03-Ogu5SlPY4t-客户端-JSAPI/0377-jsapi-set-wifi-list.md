---
title: "setWifiList"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-wifi-list"
namespace: "development"
slug: "jsapi-set-wifi-list"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > Wi-Fi > setWifiList"
doc_id: "5ari1RSeQg"
updated_at: "2025-08-27 18:07:41"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-wifi-list
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > Wi-Fi > setWifiList
> Updated: 2025-08-27 18:07:41

# setWifiList

Wi-Fi 设置。

在 [onGetWifiList](https://open.dingtalk.com/document/orgapp/jsapi-onGetWifiList) 回调触发后，利用接口设置入参中 wifiList 的 AP 相关信息。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.10 | 7.0.10 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11473) |

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

- `wifiList`（array，必填）：提供预设的 Wi-Fi 信息列表。
- `wifiList[].SSID`（string）：设备 SSID。
- `wifiList[].BSSID`（string）：设备 BSSID。
- `wifiList[].password`（string）：设备密码。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

（object）

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.setWifiList([
  { SSID: 'xxxxxxxxxx', BSSID: 'xxxxxxxxx', password: 'xxxxxxxx' },
]);
```

`success`返回对象示例：

```
{}
```
