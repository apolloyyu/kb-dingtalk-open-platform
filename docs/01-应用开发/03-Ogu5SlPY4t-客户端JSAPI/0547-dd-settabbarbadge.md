---
title: "添加tabBar文本"
source_url: "https://open.dingtalk.com/document/development/dd-settabbarbadge"
namespace: "development"
slug: "dd-settabbarbadge"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > TabBar > 添加tabBar文本"
doc_id: "lhNydtZLy4"
updated_at: "2025-09-17 20:59:08"
---

> Source: https://open.dingtalk.com/document/development/dd-settabbarbadge
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > TabBar > 添加tabBar文本
> Updated: 2025-09-17 20:59:08

# 添加tabBar文本

调用**dd.setTabBarBadge**为 tabBar 某一项的右上角添加文本。

## **示例代码**

```
dd.setTabBarBadge({
  index: 0,
  text: '新'
})
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| index | Number | 是 | tabBar 的哪一项，从左边算起。 |
| text | String | 是 | 显示的文本，超过 4 个字符则显示成 `...`。 |
| success | Function | 是 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数（调用成功、失败都会执行）。 |
