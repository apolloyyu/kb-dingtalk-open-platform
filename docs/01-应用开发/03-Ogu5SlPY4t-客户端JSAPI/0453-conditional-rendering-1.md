---
title: "条件渲染"
source_url: "https://open.dingtalk.com/document/development/conditional-rendering-1"
namespace: "development"
slug: "conditional-rendering-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 条件渲染"
doc_id: "VprKTNShQ6"
updated_at: "2025-09-17 20:57:57"
---

> Source: https://open.dingtalk.com/document/development/conditional-rendering-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 条件渲染
> Updated: 2025-09-17 20:57:57

# 条件渲染

钉钉小程序支持a:if和block a:if条件渲染。

## **a:if**

在框架中，我们使用 `a:if="{{condition}}"` 来判断是否需要渲染该代码块。

```
<view a:if="{{condition}}"> True </view>
```

也可以使用`a:elif`和`a:else`来添加一个`else`块。

```
<view a:if="{{length > 5}}"> 1 </view>
<view a:elif="{{length > 2}}"> 2 </view>
<view a:else> 3 </view>
```

## **block a:if**

因为`a:if`是一个控制属性，需要将它添加到一个标签上。如果想一次性判断多个组件标签，可以使用一个 `<block/>` 标签将多个组件包装起来，并在它的上边使用`a:if`来控制属性。

```
<block a:if="{{true}}">
  <view> view1 </view>
  <view> view2 </view>
</block>
```

> **[!IMPORTANT]**
>
> `<block/>` 并不是一个组件，仅仅是一个包装元素，不会在页面中做任何渲染，只接受控制属性。
