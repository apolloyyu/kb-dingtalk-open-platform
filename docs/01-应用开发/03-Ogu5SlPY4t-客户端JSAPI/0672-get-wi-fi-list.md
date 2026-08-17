---
title: "获取Wi-Fi列表"
source_url: "https://open.dingtalk.com/document/development/get-wi-fi-list"
namespace: "development"
slug: "get-wi-fi-list"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 获取Wi-Fi列表"
doc_id: "QtynrCwvnM"
updated_at: "2025-09-17 21:00:30"
---

> Source: https://open.dingtalk.com/document/development/get-wi-fi-list
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 获取Wi-Fi列表
> Updated: 2025-09-17 21:00:30

# 获取Wi-Fi列表

调用 **getWifiList**，获取 Wi-Fi 列表。

## **功能描述**

在 [onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event) 注册的回调中返回 wifiList 数据。iOS 将跳转到系统设置中的钉钉设置页，需要用户手动进入「无线局域网」设置页，Android 不会跳转。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥7.0.10) | 支持(钉钉版本≥7.0.10) | 不支持 |

> **[!NOTE]**
>
> - iOS 11.0 及 iOS 11.1 两个版本因系统问题，该方法失效。
> - 需在 [startWifi](https://open.dingtalk.com/document/orgapp/initialize-the-wi-fi-module) 中使用。

## **示例代码**

```
dd.getWifiList();
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |
