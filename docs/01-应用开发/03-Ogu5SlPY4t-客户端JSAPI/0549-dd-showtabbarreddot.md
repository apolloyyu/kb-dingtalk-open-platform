---
title: "显示tabBar红点"
source_url: "https://open.dingtalk.com/document/development/dd-showtabbarreddot"
namespace: "development"
slug: "dd-showtabbarreddot"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > TabBar > 显示tabBar红点"
doc_id: "YszYUsDdpl"
updated_at: "2025-09-17 20:59:09"
---

> Source: https://open.dingtalk.com/document/development/dd-showtabbarreddot
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > TabBar > 显示tabBar红点
> Updated: 2025-09-17 20:59:09

# 显示tabBar红点

调用**dd.showTabBarRedDot**显示tabBar某一项的右上角的红点。

## **示例代码**

```
dd.showTabBarRedDot({
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
