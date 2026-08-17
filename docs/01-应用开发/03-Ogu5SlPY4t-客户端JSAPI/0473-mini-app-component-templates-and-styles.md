---
title: "组件模板和样式"
source_url: "https://open.dingtalk.com/document/development/mini-app-component-templates-and-styles"
namespace: "development"
slug: "mini-app-component-templates-and-styles"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件模板和样式"
doc_id: "0jEzWj4e17"
updated_at: "2025-09-17 20:58:08"
---

> Source: https://open.dingtalk.com/document/development/mini-app-component-templates-and-styles
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件模板和样式
> Updated: 2025-09-17 20:58:08

# 组件模板和样式

与页面类似，自定义组件可以有自己的 axml 模板和 acss 样式。

## axml

自定义组件必定会有 axml，否则无法进行渲染。

```
<!-- /components/xx/index.axml -->
<view onTap="onMyClick" id="c-{{$id}}"/>
```

```
Component({
  methods: {
    onMyClick(e) {
      console.log(this.is, this.$id);
    },
  },
});
```

> **[!IMPORTANT]**
>
> 与页面不同，用户自定义事件需要放到 methods 里面。

## slot

通过在组件 js 中支持 props，自定义组件可以和外部调用者互相沟通，接受外部调用者传来的数据，同时可以调用外部调用者传来的函数，通知外部调用者组件内部的变化。

但是这样还不够，我们的自定义组件还不够灵活，我们要的不仅仅是数据的处理与通知，还希望自定义组件的 axml 结构可以使用外部调用者传来的 axml 组装。也就是说，外部调用者可以传递 axml 给自定义组件，自定义组件使用其组装出最终的组件 axml 结构。

为此，小程序提供了`slot`。

**default slot**

可以将 slot 理解为`槽位`，`default slot`就是默认槽位，如果调用者在组件标签`<xx>`之间不传递 axml，则最终会将默认槽位渲染出来。而如果调用者在组件标签`<xx>`之间传递有 axml，则使用其替代`默认槽位`，进而组装出最终的 axml 以供渲染。

示例代码：

```
<!-- /components/xx/index.axml -->
<view>
  <slot>
    <view>default slot & default value</view>
  </slot>
  <view>other</view>
</view>
```

- 调用者不传递axml：

  ```
  <!-- /pages/index/index.axml -->
  <xx />
  ```

  页面输出：

  ```
  default slot & default value
  other
  ```
- 调用者传递axml

  ```
  <!-- /pages/index/index.axml -->
  <xx>
    <view>xx</view>
    <view>yy</view>
  </xx>
  ```

  页面输出：

  ```
  xx
  yy
  other
  ```

**named slot**

仅仅有`default slot`显然是不够灵活的，因为它只能传递一份 axml，而如果我们的组件比较复杂的话，我们通常希望可以在不同的位置渲染不同的 axml，这就需要可以传递多个 axml。这就需要`named slot`了。

`named slot`就是`命名槽位`，外部调用者可以在自定义组件标签的子标签中指定要将哪一部分的 axml 放入到自定义组件的哪个`命名槽位`中。而自定义组件标签的子标签中的没有指定`命名槽位`的部分则会放入到`默认槽位`上。如果仅仅传递了`命名槽位`，则会渲染出`默认槽位`。

示例代码：

```
<!-- /components/xx/index.axml -->
<view>
  <slot>
    <view>default slot & default value</view>
  </slot>
  <slot name="header"/>
  <view>body</view>
  <slot name="footer"/>
</view>
```

- 只传递命名槽位：

  ```
  <!-- /pages/index/index.axml -->
  <xx>
    <view slot="header">header</view>
    <view slot="footer">footer</view>
  </xx>
  ```

  页面输出：

  ```
  default slot & default value
  header
  body
  footer
  ```
- 传递命名slot与默认slot

  ```
  <!-- /pages/index/index.axml -->
  <xx>
    <view>this is to default slot</view>
    <view slot="header">header</view>
    <view slot="footer">footer</view>
  </xx>
  ```

  页面输出：

  ```
  this is to default slot
  header
  body
  footer
  ```

**slot scope**

到此我们的自定义组件已经比较灵活了，但是还不够灵活。通过使用named slot，自定义组件的 axml 要么使用自定义组件自己的 axml，要么使用外部调用者（比如页面）的axml。

使用自定义组件自己的 axml，可以访问到组件内部的数据，同时通过props属性，可以访问到外部调用者的数据。

示例代码：

```
// /components/xx/index.js
Component({
  data: {
    x: 1,
  },
  props: {
    y: '',
  },
});
```

```
<!-- /components/xx/index.axml -->
<view>component data: {{x}}</view>
<view>page data: {{y}}</view>
```

```
// /pages/index/index.js
Page({
  data: { y: 2 },
});
```

```
<!-- /pages/index/index.axml -->
<xx y="{{y}}" />
```

页面输出：

```
component data: 1
page data: 2
```

而自定义组件通过`slot`使用外部调用者（比如页面）的axml时，却只能访问到外部调用者的数据。

```
<!-- /components/xx/index.axml -->
<view>
  <slot>
    <view>default slot & default value</view>
  </slot>
  <view>body</view>
</view>
```

```
// /pages/index/index.js
Page({
  data: { y: 2 },
});
```

```
<!-- /pages/index/index.axml -->
<xx>
  <view>page data: {{y}}</view>
</xx>
```

页面输出：

```
page data: 2
body
```

通过使用slot scope让外部调用者传递的 axml 可以访问到组件内部的数据。

示例代码：

```
// /components/xx/index.js
Component({
  data: {
    x: 1,
  },
});
```

```
<!-- /components/xx/index.axml -->
<view>
  <slot x="{{x}}">
    <view>default slot & default value</view>
  </slot>
  <view>body</view>
</view>
```

```
// /pages/index/index.js
Page({
  data: { y: 2 },
});
```

```
<!-- /pages/index/index.axml -->
<xx>
  <view slot-scope="props">
    <view>component data: {{props.x}}</view>
    <view>page data: {{y}}</view>
  </view>
</xx>
```

页面输出：

```
component data: 1
page data: 2
body
```

在外部调用者使用组件自定义标签的时候，使用slot-scope属性，slot-scope 的值将被用作一个临时变量名，此变量接收从自定义组件 axml 传递过来的 prop 对象。

## acss

和页面一样，自定义组件也可以定义自己的 acss 样式。acss 会自动被引入使用组件的页面，不需要页面手动引入。
