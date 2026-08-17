---
title: "打开日期选择列表"
source_url: "https://open.dingtalk.com/document/development/dd-datepicker"
namespace: "development"
slug: "dd-datepicker"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 选择日期 > 打开日期选择列表"
doc_id: "40MyJ1iwa6"
updated_at: "2025-09-17 20:59:21"
---

> Source: https://open.dingtalk.com/document/development/dd-datepicker
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 选择日期 > 打开日期选择列表
> Updated: 2025-09-17 20:59:21

# 打开日期选择列表

调用**dd.datePicker**打开日期选择列表。

## 扫码体验

![1595556502783-2 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4675572061/p171202.png)

## **示例代码**

```
dd.datePicker({
  format: 'yyyy-MM-dd',
  currentDate: '2012-12-12',
  success: (res) => {
    dd.alert({
      content: res.date,
    });
  },
});
```

## **入参**

| **名称** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| format | String | 否 | 返回的日期格式。   - yyyy-MM-dd（默认） - HH:mm - yyyy-MM-dd HH:mm - yyyy-MM |
| currentDate | String | 否 | 初始选择的日期时间。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| date | String | 选择的日期。 |

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 11 | 用户取消操作。 |
