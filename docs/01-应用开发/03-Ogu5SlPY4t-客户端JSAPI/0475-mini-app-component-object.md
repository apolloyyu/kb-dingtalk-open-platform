---
title: "组件对象"
source_url: "https://open.dingtalk.com/document/development/mini-app-component-object"
namespace: "development"
slug: "mini-app-component-object"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件对象"
doc_id: "oxlzDYkHN6"
updated_at: "2025-09-17 20:58:10"
---

> Source: https://open.dingtalk.com/document/development/mini-app-component-object
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件对象
> Updated: 2025-09-17 20:58:10

# 组件对象

## methods

我们当然不希望自定义组件只能渲染静态的数据，我们希望它可以响应用户点击事件，进而处理并触发组件重新渲染。

> **[!IMPORTANT]**
>
> 与Page不同，我们需要将事件处理函数定义在 methods 中。

首先修改组件的axml：

```
<!-- /components/counter/index.axml -->
<view>{{counter}}</view>
<button onTap="plusOne">+1</button>
```

在组件的js中处理事件：

```
// /components/counter/index.js
Component({
  data: { counter: 0 },
  methods: {
    plusOne(e) {
      console.log(e);
      this.setData({ counter: this.data.counter + 1 });
    },
  },
});
```

现在我们的页面就会多渲染一个按钮，每次点击它都会将页面的数字加1。

## props

我们希望自定义组件与外界不是隔离的。目前为止它是一个独立的模块，想让它与外界交流，那就需要让它可以接受外界的输入，然后做完处理之后，还可以通知外界说：我做完了。这些都可以通过 props 来实现。

> **[!NOTE]**
>
> - `class` 需要使用 `this.props.className` 来读取。
> - props 为外部传过来的属性，可指定默认属性，后面不可修改。
> - 自定义组件的 axml 中可以直接引用 props 属性。

示例代码：

```
// /components/counter/index.js
Component({
  data: { counter: 0 },
  props: {
    onCounterPlusOne: (data) => console.log(data),
    extra: 'default extra',
  },
  methods: {
    plusOne(e) {
      console.log(e);
      const counter = this.data.counter + 1;
      this.setData({ counter });
      this.props.onCounterPlusOne(counter);
    },
  },
});
```

以上代码使用 props 属性设置属性默认值，然后在事件处理函数中通过 this.props 可以取到这些属性。

```
<!-- /components/counter/index.axml -->
<view>{{counter}}</view>
<view>extra: {{extra}}</view>
<button onTap="plusOne">+1</button>
```

- 外部使用不传递 props。

  ```
  <!-- /pages/index/index.axml -->
  <my-component />
  ```

  页面输出：

  ```
  0
  extra: default extra
  +1
  ```

  此时并未传递参数，所以页面会显示组件js中 props 设定的默认值。
- 外部使用传递 props。

  ```
  // /pages/index/index.js
  Page({
    onCounterPlusOne(data) {
      console.log(data);
    }
  });
  ```

  ```
  // /pages/index/index.axml
  <my-component extra="external extra" onCounterPlusOne="onCounterPlusOne" />
  ```

  页面输出：

  ```
  0
  external extra
  +1
  ```

  此时传递了参数，所以页面会显示外部传递的 extra 值 external extra 。

  > **[!IMPORTANT]**
  >
  > 外部使用自定义组件时，如果传递的参数是函数，一定要以 on 为前缀，否则会将其处理为字符串。
