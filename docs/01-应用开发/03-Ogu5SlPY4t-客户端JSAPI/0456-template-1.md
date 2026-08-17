---
title: "模板"
source_url: "https://open.dingtalk.com/document/development/template-1"
namespace: "development"
slug: "template-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 模板"
doc_id: "MQUzUXZ3SR"
updated_at: "2025-09-17 20:57:59"
---

> Source: https://open.dingtalk.com/document/development/template-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 模板
> Updated: 2025-09-17 20:57:59

# 模板

AXML提供模板（template），可以在模板中定义代码片段，在不同的地方调用。

> **[!NOTE]**
>
> 此处 template 区别于 slot，slot 可参考[自定义组件](https://open.dingtalk.com/document/dingstart/mini-app-development-process)。

## 定义模板

使用`name`属性，作为模板的名字，然后在`<template/>`内定义代码片段。

```
<!--
  index: int
  msg: string
  time: string
-->
<template name="msgItem">
  <view>
    <text> {{index}}: {{msg}} </text>
    <text> Time: {{time}} </text>
  </view>
</template>
```

## 使用模板

使用`is`属性，声明需要使用的模板，然后将该模板所需要的`data`传入，例如：

```
<template is="msgItem" data="{{...item}}"/>
```

```
Page({
  data: {
    item: {
      index: 0,
      msg: 'this is a template',
      time: '2016-09-15'
    }
  }
})
```

`is`属性可以使用`Mustache`语法，来动态决定具体需要渲染哪个模板。

```
<template name="odd">
  <view> odd </view>
</template>
<template name="even">
  <view> even </view>
</template>

<block a:for="{{[1, 2, 3, 4, 5]}}">
    <template is="{{item % 2 == 0 ? 'even' : 'odd'}}"/>
</block>
```

## 模板作用域

模板拥有自己的作用域，只能用`data`传入的数据，但可以通过 `onXX` 绑定页面的逻辑处理函数。

推荐用 template 方式来引入模板片段，因为 template 会指定自己的作用域，只使用`data`传入的数据，因此应用会对此进行优化。如果该 template 的 data 没有改变，该片段 UI 并不会重新渲染。

引入路径支持从 node\_modules 目录载入第三方模块，例如 page.axml:

```
<import src="./a.axml"/> <!-- 相对路径 -->
<import src="/a.axml"/> <!-- 项目绝对路径 -->
<import src="third-party/x.axml"/> <!-- 第三方 npm 包路径 -->
```
