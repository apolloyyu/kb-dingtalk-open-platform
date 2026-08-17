---
title: "设置Wi-Fi"
source_url: "https://open.dingtalk.com/document/development/set-wi-fi"
namespace: "development"
slug: "set-wi-fi"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 设置Wi-Fi"
doc_id: "YjXTwjZa74"
updated_at: "2025-09-17 21:00:31"
---

> Source: https://open.dingtalk.com/document/development/set-wi-fi
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 设置Wi-Fi
> Updated: 2025-09-17 21:00:31

# 设置Wi-Fi

调用 **setWifiList**，设置 Wi-Fi 中 AP 的相关信息。

## **功能描述**

在 [onGetWifiList](https://open.dingtalk.com/document/orgapp/listener-to-get-wi-fi-list-event) 回调触发后，利用接口设置入参中 wifiList 的 AP 相关信息。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 支持(钉钉版本≥7.0.10) | 不支持 |

## **示例代码**

```
dd.setWifiList([
  { SSID: 'xxxxxxxxxx', BSSID: 'xxxxxxxxx', password: 'xxxxxxxx' }
]);
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| wifiList | Array<Object> | 是 | 提供预设的 Wi-Fi 信息列表。 |
| SSID | String | 否 | 设备 SSID。 |
| BSSID | String | 否 | 设备 BSSID。 |
| password | String | 否 | 设备密码。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |
