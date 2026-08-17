---
title: "停止监听已获取Wi-Fi列表数据事件"
source_url: "https://open.dingtalk.com/document/development/stop-listening-to-the-obtained-wi-fi-list-data-event"
namespace: "development"
slug: "stop-listening-to-the-obtained-wi-fi-list-data-event"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 停止监听已获取Wi-Fi列表数据事件"
doc_id: "NDdkAp3ULB"
updated_at: "2025-09-17 21:00:35"
---

> Source: https://open.dingtalk.com/document/development/stop-listening-to-the-obtained-wi-fi-list-data-event
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 停止监听已获取Wi-Fi列表数据事件
> Updated: 2025-09-17 21:00:35

# 停止监听已获取Wi-Fi列表数据事件

调用 **offGetWifiList**，停止监听已获取 Wi-Fi 列表数据事件。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥7.0.10) | 支持(钉钉版本≥7.0.10) | 不支持 |

## **示例代码**

```
dd.offGetWifiList();
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |
