---
title: "隐藏弱提示"
source_url: "https://open.dingtalk.com/document/development/dd-hidetoast"
namespace: "development"
slug: "dd-hidetoast"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 隐藏弱提示"
doc_id: "t4leZVyDJn"
updated_at: "2025-09-17 20:59:14"
---

> Source: https://open.dingtalk.com/document/development/dd-hidetoast
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 隐藏弱提示
> Updated: 2025-09-17 20:59:14

# 隐藏弱提示

调用**dd.hideToast**隐藏弱提示。

## 扫码体验

![1595556977173-3 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7724572061/p172094.png)

## 代码示例

```
 hideToast() {
    dd.hideToast()
  }
```

## 入参

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
