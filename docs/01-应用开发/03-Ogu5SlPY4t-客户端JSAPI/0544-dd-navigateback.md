---
title: "返回上一级或多级页面"
source_url: "https://open.dingtalk.com/document/development/dd-navigateback"
namespace: "development"
slug: "dd-navigateback"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 导航栏 > 返回上一级或多级页面"
doc_id: "rzibOSL8ry"
updated_at: "2025-09-17 20:59:06"
---

> Source: https://open.dingtalk.com/document/development/dd-navigateback
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 导航栏 > 返回上一级或多级页面
> Updated: 2025-09-17 20:59:06

# 返回上一级或多级页面

调用**dd.navigateBack**关闭当前页面，返回上一级或多级页面。可通过 getCurrentPages 获取当前的页面栈信息，决定需要返回几层。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4354199951/p163552.png)

## 示例代码

```
// 注意：调用 navigateTo 跳转时，调用该方法的页面会被加入堆栈，
// 而 redirectTo 方法则不会。见下方示例代码

// 此处是one页面
dd.navigateTo({
  url: 'two?pageId=10000'
})

// 此处是two页面
dd.navigateTo({
  url: 'one?pageId=99999'
})

// 在three页面内 navigateBack，将返回one页面
dd.navigateBack({
  delta: 2
})
```

> **[!NOTE]**
>
> dd.navigateTo 和 dd.redirectTo 不允许跳转到 tabbar 页面；如果需要跳转到 tabbar 页面，请使用 dd.switchTab。

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| delta | Number | 返回的页面数，如果 delta 大于现有打开的页面数，则返回到当前页面栈最顶部的页。  **默认值**：1。 |
