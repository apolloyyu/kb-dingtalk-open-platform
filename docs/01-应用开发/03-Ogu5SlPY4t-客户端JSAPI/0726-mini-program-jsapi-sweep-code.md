---
title: "扫码"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-sweep-code"
namespace: "development"
slug: "mini-program-jsapi-sweep-code"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 扫码"
doc_id: "RjvrkkJ6B8"
updated_at: "2025-09-17 21:01:07"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-sweep-code
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 扫码
> Updated: 2025-09-17 21:01:07

# 扫码

调用dd.scan使用扫一扫功能。

## 扫码体验

![1595553928470-2 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7009783061/p172677.png)

## **示例****代码**

```
dd.scan({
  type: 'qr',
  success: (res) => {
    dd.alert({ title: res.code });
  },
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| type | String | 否 | 扫码样式。   - **qr**：二维码扫码框 - **bar**：条形码扫码框   **默认值**：qr。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| code | String | 扫码所得数据。 |
| qrCode | String | 扫描二维码时返回二维码数据。 |
| barCode | String | 扫描条形码时返回条形码数据。 |

## **错误码**

| **error** | **描述** |
| --- | --- |
| 10 | 用户取消。 |
| 11 | 操作失败。 |
