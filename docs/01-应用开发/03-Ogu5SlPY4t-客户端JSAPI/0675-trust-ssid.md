---
title: "信任SSID"
source_url: "https://open.dingtalk.com/document/development/trust-ssid"
namespace: "development"
slug: "trust-ssid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 信任SSID"
doc_id: "O0igOfk1ij"
updated_at: "2025-09-17 21:00:32"
---

> Source: https://open.dingtalk.com/document/development/trust-ssid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > Wi-Fi > 信任SSID
> Updated: 2025-09-17 21:00:32

# 信任SSID

调用 **registerSSID**，信任该 SSID。

## **功能描述**

信任该 SSID，对于需要 Portal 认证的 Wi-Fi，不会弹出 Portal 认证页面。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 支持(钉钉版本≥7.0.10) | 不支持 |

## **示例代码**

```
dd.registerSSID({
  SSID: 'SSID示例值',
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

## **入参说明**

| **参数** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| SSID | String | 是 | 设备 SSID。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Funciton | 否 | 调用结束的回调。  **[!NOTE]**  调用成功、失败都会执行。 |
