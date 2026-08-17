---
title: "引用"
source_url: "https://open.dingtalk.com/document/development/reference-2"
namespace: "development"
slug: "reference-2"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 引用"
doc_id: "HIV8Q7InOL"
updated_at: "2025-09-17 20:57:59"
---

> Source: https://open.dingtalk.com/document/development/reference-2
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 引用
> Updated: 2025-09-17 20:57:59

# 引用

AXML提供两种文件引用方式import和include。

## **import**

`import`可以加载已经定义好的`template`。

例如，在`item.axml`中定义了一个叫`item`的`template`。

```
<!-- item.axml -->
<template name="item">
  <text>{{text}}</text>
</template>
```

在`index.axml`中引用`item.axml`，就可以使用`item`模板。

```
<import src="./item.axml"/>
<template is="item" data="{{text: 'forbar'}}"/>
```

`import`有作用域的概念，只会`import`目标文件中定义的`template`。比如，C import B，B import A，在`C`中可以使用`B`定义的`template`，在`B`中可以使用`A`定义的`template`，但是`C`不能使用`A`中定义的`template`。

```
<!-- A.axml -->
<template name="A">
  <text> A template </text>
</template>
```

```
<!-- B.axml -->
<import src="./a.axml"/>
<template name="B">
  <text> B template </text>
</template>
```

```
<!-- C.axml -->
<import src="./b.axml"/>
<template is="A"/>  <!-- Error! Can not use tempalte when not import A. -->
<template is="B"/>
```

注意：template 的子节点只能是一个而不是多个。

允许示例代码：

```
<template name="x">
  <view />
</template>
```

不允许示例代码：

```
<template name="x">
  <view />
  <view />
</template>
```

## include

`include`可以将目标文件除了`<template/>`的整个代码引入，相当于是拷贝到`include`位置。

```
<!-- index.axml -->
<include src="./header.axml"/>
<view> body </view>
<include src="./footer.axml"/>
```

```
<!-- header.axml -->
<view> header </view>
```

```
<!-- footer.axml -->
<view> footer </view>
```
