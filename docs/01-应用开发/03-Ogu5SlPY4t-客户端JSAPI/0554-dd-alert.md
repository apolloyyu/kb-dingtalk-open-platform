---
title: "显示警告框"
source_url: "https://open.dingtalk.com/document/development/dd-alert"
namespace: "development"
slug: "dd-alert"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示警告框"
doc_id: "O8UXdsJzMd"
updated_at: "2025-09-17 20:59:13"
---

> Source: https://open.dingtalk.com/document/development/dd-alert
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示警告框
> Updated: 2025-09-17 20:59:13

# 显示警告框

调用**dd.alert**显示警告框，可以设置警告框的标题、内容、按钮文字等。

## 扫码体验

![1595556951230-2 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3568903061/p172089.png)

## **示例****代码**

```
dd.alert({
  title: '亲',
  content: '您本月的账单已出',
  buttonText: '我知道了',
  success: () => {
    dd.alert({
      title: '用户点击了「我知道了」',
    });
  },
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| title | String | 是 | alert框的标题。 |
| content | String | 是 | alert框的内容。 |
| buttonText | String | 否 | 按钮文字。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
