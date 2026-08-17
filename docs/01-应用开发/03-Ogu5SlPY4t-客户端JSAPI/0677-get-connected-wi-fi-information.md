---
title: "获取已连接Wi-Fi信息"
source_url: "https://open.dingtalk.com/document/development/get-connected-wi-fi-information"
namespace: "development"
slug: "get-connected-wi-fi-information"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 获取已连接Wi-Fi信息"
doc_id: "Xw7piCuEzH"
updated_at: "2025-09-17 21:00:33"
---

> Source: https://open.dingtalk.com/document/development/get-connected-wi-fi-information
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 获取已连接Wi-Fi信息
> Updated: 2025-09-17 21:00:33

# 获取已连接Wi-Fi信息

调用 **getConnectedWifi**，获取已连接 Wi-Fi 信息。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥7.0.10) | 支持(钉钉版本≥7.0.10) | 不支持 |

## **示例代码**

```
dd.getConnectedWifi({
  success: (res) => {
    const { wifi } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |

## **返回结果**

| **参数** | **类型** | **描述** |
| --- | --- | --- |
| wifi | Object | Wi-Fi 信息。 |
| SSID | String | 设备的 SSID。 |
| BSSID | String | 设备的 BSSID。 |
| secure | Boolean | 是否安全：   - **true**：安全 - **false**：不安全 |
| signalStrength | Number | Wi-Fi 信号强度，取值 0 ～ 100。  **[!NOTE]**  值越大强度越大。 |
