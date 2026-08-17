---
title: "隐藏加载提示"
source_url: "https://open.dingtalk.com/document/development/dd-hideloading"
namespace: "development"
slug: "dd-hideloading"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 隐藏加载提示"
doc_id: "MYD87GPPag"
updated_at: "2025-09-17 20:59:16"
---

> Source: https://open.dingtalk.com/document/development/dd-hideloading
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 隐藏加载提示
> Updated: 2025-09-17 20:59:16

# 隐藏加载提示

调用**dd.hideLoading**隐藏加载提示，可与dd.showLoading配合使用。

## **示例****代码**

```
dd.hideLoading();
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| page | Object | 否 | 具体指当前 page 实例，某些场景下，需要指明在哪个 page 执行 hideLoading。 |
