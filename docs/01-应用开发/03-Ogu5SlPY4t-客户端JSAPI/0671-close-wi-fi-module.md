---
title: "关闭Wi-Fi模块"
source_url: "https://open.dingtalk.com/document/development/close-wi-fi-module"
namespace: "development"
slug: "close-wi-fi-module"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 关闭Wi-Fi模块"
doc_id: "midZ33vyqr"
updated_at: "2025-09-17 21:00:29"
---

> Source: https://open.dingtalk.com/document/development/close-wi-fi-module
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 关闭Wi-Fi模块
> Updated: 2025-09-17 21:00:29

# 关闭Wi-Fi模块

调用 **stopWifi**，关闭 Wi-Fi 模块。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥7.0.10) | 支持(钉钉版本≥7.0.10) | 不支持 |

## **示例代码**

```
dd.stopWifi({
  success: function(res) {
    console.log(res)
  }
})
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |
