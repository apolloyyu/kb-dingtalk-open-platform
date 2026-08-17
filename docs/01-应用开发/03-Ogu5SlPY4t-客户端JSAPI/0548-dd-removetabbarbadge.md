---
title: "移除tabBar文本"
source_url: "https://open.dingtalk.com/document/development/dd-removetabbarbadge"
namespace: "development"
slug: "dd-removetabbarbadge"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > TabBar > 移除tabBar文本"
doc_id: "IYtqRZI8r4"
updated_at: "2025-09-17 20:59:09"
---

> Source: https://open.dingtalk.com/document/development/dd-removetabbarbadge
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > TabBar > 移除tabBar文本
> Updated: 2025-09-17 20:59:09

# 移除tabBar文本

调用**dd.removeTabBarBadge**移除 tabBar 某一项右上角的文本。

## **示****例代****码**

```
dd.removeTabBarBadge({
  index: 0
})
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| index | Number | 是 | tabBar 的哪一项，从左边算起。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数（调用成功、失败都会执行）。 |
