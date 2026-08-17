---
title: "连接Wi-Fi"
source_url: "https://open.dingtalk.com/document/development/connection-wi-fi"
namespace: "development"
slug: "connection-wi-fi"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 连接Wi-Fi"
doc_id: "4R2dPlnqOY"
updated_at: "2025-09-17 21:00:30"
---

> Source: https://open.dingtalk.com/document/development/connection-wi-fi
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 连接Wi-Fi
> Updated: 2025-09-17 21:00:30

# 连接Wi-Fi

调用 **connectWifi**，连接 Wi-Fi。

## **功能描述**

若已知 Wi-Fi 信息，可以直接利用该接口连接。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥7.0.10) | 支持(钉钉版本≥7.0.10) | 不支持 |

> **[!NOTE]**
>
> 仅 Android 与 iOS 11 以上版本支持。

## **示例代码**

```
my.connectWifi({
  SSID: '',
  BSSID: '',
  success: function(res) {
    console.log(res)
  }
})
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| SSID | String | 是 | Wi-Fi 设备的 SSID。 |
| BSSID | String | 否 | Wi-Fi 设备的 BSSID。 |
| password | String | 否 | Wi-Fi 设备密码。 |
| isWEP | Boolean | 否 | Wi-Fi 是否为 WEP。  **[!NOTE]**  默认是 false。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |
