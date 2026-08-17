---
title: "列表渲染"
source_url: "https://open.dingtalk.com/document/development/list-rendering-1"
namespace: "development"
slug: "list-rendering-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 列表渲染"
doc_id: "8CLwwj75SD"
updated_at: "2025-09-17 20:57:58"
---

> Source: https://open.dingtalk.com/document/development/list-rendering-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 列表渲染
> Updated: 2025-09-17 20:57:58

# 列表渲染

钉钉小程序支持a:for、block a:for、a:key和key方式的列表渲染。

## **a:for**

在组件上使用`a:for`属性可以绑定一个数组，然后就可以使用数组中各项的数据重复渲染该组件。

默认数组的当前项的下标变量名默认为`index`，数组当前项的变量名默认为`item`。

```
<view a:for="{{array}}">
  {{index}}: {{item.message}}
</view>
```

```
Page({
  data: {
    array: [{
      message: 'foo',
    }, {
      message: 'bar'
    }]
  }
})
```

使用`a:for-item`可以指定数组当前元素的变量名。

使用`a:for-index`可以指定数组当前下标的变量名。

```
<view a:for="{{array}}" a:for-index="idx" a:for-item="itemName">
  {{idx}}: {{itemName.message}}
</view>
```

`a:for`也可以嵌套，下边是一个九九乘法表。

```
<view a:for="{{[1, 2, 3, 4, 5, 6, 7, 8, 9]}}" a:for-item="i">
  <view a:for="{{[1, 2, 3, 4, 5, 6, 7, 8, 9]}}" a:for-item="j">
    <view a:if="{{i <= j}}">
      {{i}} * {{j}} = {{i * j}}
    </view>
  </view>
</view>
```

## **block a:for**

类似`block a:if`，可以将`a:for`用在`<block/>`标签上，以渲染一个包含多节点的结构块。

```
<block a:for="{{[1, 2, 3]}}">
  <view> {{index}}: </view>
  <view> {{item}} </view>
</block>
```

## **a:key**

如果列表中项目的位置会动态改变或者有新的项目添加到列表中，同时希望列表中的项目保持自己的特征和状态（比如 `<input/>` 中的输入内容，`<switch/>` 的选中状态），需要使用 a:key 来指定列表中项目的唯一的标识符。

`a:key`的值以两种形式来提供。

- 字符串，代表在`for`循环的`array`中`item`的某个属性。该属性的值需要是列表中唯一的字符串或数字，并且不能动态的改变。
- 保留关键字`*this`，代表在`for`循环中的`item`本身，表示需要`item`本身是唯一的字符串或者数字，比如当数据改变触发渲染层重新执行渲染的时候，会校正带有`key`的组件，框架会确保他们重新被排序，而不是重新创建，确保使组件保持自身的状态，并且提高列表渲染时的效率。

如果明确知道列表是静态，或者不用关注其顺序，则可以选择忽略。

```
<view class="container">
  <view a:for="{{list}}" a:key="*this">
    <view onTap="bringToFront" data-value="{{item}}">
    {{item}}: click to bring to front
    </view>
  </view>
</view>
```

```
Page({
  data:{
    list:['1', '2', '3', '4'],
  },
  bringToFront(e) {
    const { value } = e.target.dataset;
    const list = this.data.list.concat();
    const index = list.indexOf(value);
    if (index !== -1) {
      list.splice(index, 1);
      list.unshift(value);
      this.setData({ list });
    }
  }
});
```

## key

key 是比 a:key 更通用的写法，里面可以填充任意表达式和字符串。

```
<view class="container">
  <view a:for="{{list}}" key="{{item}}">
    <view onTap="bringToFront" data-value="{{item}}">
    {{item}}: click to bring to front
    </view>
  </view>
</view>
```

```
Page({
  data:{
    list:['1', '2', '3', '4'],
  },
  bringToFront(e) {
    const { value } = e.target.dataset;
    const list = this.data.list.concat();
    const index = list.indexOf(value);
    if (index !== -1) {
      list.splice(index, 1);
      list.unshift(value);
      this.setData({ list });
    }
  }
});
```

同时可以利用 key 来防止组件的复用，例如，如果允许用户输入不同类型的数据。

```
<input a:if="{{name}}" placeholder="Enter your username"/>
<input a:else placeholder="Enter your email address"/>
```

那么当你输入 name 然后切换到 email 时，当前输入值会保留，如果不想保留，可以加 key。

```
<input key="name" a:if="{{name}}" placeholder="Enter your username"/>
<input key="email" a:else placeholder="Enter your email address"/>
```
