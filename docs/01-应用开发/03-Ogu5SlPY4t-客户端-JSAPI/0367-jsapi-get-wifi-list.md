---
title: "getWifiList"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-wifi-list"
namespace: "development"
slug: "jsapi-get-wifi-list"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > Wi-Fi > getWifiList"
doc_id: "wsCiACSlAZ"
updated_at: "2025-08-27 18:07:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-wifi-list
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > Wi-Fi > getWifiList
> Updated: 2025-08-27 18:07:36

# getWifiList

获取 Wi-Fi 列表。

在 [onGetWifiList](https://open.dingtalk.com/document/orgapp/jsapi-onGetWifiList) 注册的回调中返回 wifiList 数据。iOS 将跳转到系统设置中的钉钉设置页，需要用户手动进入「无线局域网」设置页，Android 不会跳转。

> - iOS 11.0 及 iOS 11.1 两个版本因系统问题，该方法失效。
> - 需在 [startWifi](https://open.dingtalk.com/document/orgapp/jsapi-startWifi) 中使用。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11472) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.getWifiList({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
