---
title: "开发自定义组件"
source_url: "https://open.dingtalk.com/document/development/mini-app-configure-components"
namespace: "development"
slug: "mini-app-configure-components"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件"
doc_id: "sgWHHkgaej"
updated_at: "2026-09-01 09:16:29"
---

> Source: https://open.dingtalk.com/document/development/mini-app-configure-components
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件
> Updated: 2026-09-01 09:16:29

# 开发自定义组件

## **组件配置**

开发者需要在.json文件中指明自定义组件的依赖。

```
{
  "component": true,
  "usingComponents": {
    "c1":"../x/index"
  }
}
```

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| component | Boolean | 是 | 指明是组件。 |
| usingComponents | Object | 否 | 指明依赖的组件所在的路径： 项目绝对路径以 / 开头，相对路径以 ./ 或者 ../ 开头，npm 路径不以 / 开头。 |

开发者需要在`.js`文件中调用Component定义组件。

```
Component({
  mixins:[{ didMount() {}, }],
  data: {y:2},
  props:{x:1},
  didUpdate(prevProps,prevData){},
  didUnmount(){},
  methods:{
    onMyClick(ev){
      dd.alert({});
      this.props.onXX({ ...ev, e2:1});
    },
  },
})
```

## **组件模板和样式**

### **axml**

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

### **slot**

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

### **acss**

和页面一样，自定义组件也可以定义自己的 acss 样式。acss 会自动被引入使用组件的页面，不需要页面手动引入。

## **data**

data 为组件的局部状态，和页面一样，可以通过this.setData更改，会触发组件的重新渲染；也可以通过this.$spliceData做数据的更改。

详情请参考[注册小程序页面](0433-getcurrentpages-methods-1.md#1c2bf0da22gb6)。

**示例代码**

```
// /components/counter/index.js
Component({
  data: { counter: 0 }
});
```

```
<!-- /components/counter/index.axml -->
<view>{{counter}}</view>
```

```
// /components/counter/index.json
{
  "component": true,
}
```

以上代码分别实现了自定义组件的三个要素：js、axml、json。然后我们在页面上就可以使用了。 首先需要在页面的 json 文件中声明依赖的组件，和组件的声明依赖方式相同。

```
// /pages/index/index.json
{
  "usingComponents": {
    "my-component": "/components/counter/index"
  }
}
```

然后在页面的 axml 中就可以使用了。

```
<!-- /pages/index/index.axml -->
<my-component />
```

页面输出：

```
0
```

## **mixins**

开发者有时候可能会实现多个自定义组件，而这些自定义组件可能会有些公共逻辑要处理，为此，小程序提供了mixins。

> **[!IMPORTANT]**
>
> - 每一个 mixin 只能包含 props、data、methods、didMount、didUpdate、didUnmount等属性。
> - 多个 mixin 中的属性 key 要确保不同，否则会报错。

```
// /mixins/lifecycle.js
export default {
  didMount(){},
  didUpdate(prevProps,prevData){},
  didUnmount(){},
};
```

```
// /pages/components/xx/index.js
import lifecycle from '../../mixins/lifecycle';

const initialState = {
  data: {
    y: 2
  },
};

const defaultProps = {
  props: {
    a: 3,
  },
};

const methods = {
  methods: {
    onTapHandler() {},
  },
}

Component({
  mixins: [
    lifecycle,
    initialState,
    defaultProps,
    methods
  ],
  data: {
    x: 1,
  },
});
```

## **组件对象**

### **methods**

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

### **props**

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

## **组件生命周期**

通过传递 props 属性实现了自定义组件与外部调用者的交流。但有时自定义组件依赖外部数据。

例如希望在自定义组件中向服务端发送请求获取数据。或者希望在确保组件已经渲染到页面上之后，再做某些操作。为此自定义组件提供了三个生命周期函数: didMount 、didUpdate 、didUnmount 。

### **didMount**

didMount为渲染后回调，此时页面已经渲染，通常在这里请求服务端数据比较合适。

```
Component({
  data: {},
  didMount() {
    let that = this;
    dd.httpRequest({
      url: 'http://httpbin.org/post',
      success: function(res) {
        that.setData({name: 'xiaoming'})                
      }
    });
  },
});
```

### **didUpdate**

didUpdate 为更新后回调，每次组件数据变更的时候都会调用。

> **[!IMPORTANT]**
>
> - 组件内部调用 this.setData 会触发 didUpdate
> - 外部调用者调用 this.setData 也会触发 didUpdate

```
Component({
  data: {},
  didUpdate(prevProps,prevData) {
    console.log(prevProps, this.props, prevData, this.data)
  },
});
```

### **didUnmount**

didUnmount 为删除后回调，每当组件示例从页面删除的时候会触发此回调。

```
Component({
  data: {},
  didUnmount() {
    console.log(this)
  },
});
```

## **其他组件实例属性**

除了 data、setData、props等属性外，组件实例上还有如下属性：

- `is`: 组件路径
- `$page`: 组件所属页面实例
- `$id`: 组件 id，在 axml 中也可直接渲染

  > **[!NOTE]**
  >
  > 在组件中可以使用 dd 调用 api。

```
// /components/xx/index.js
Component({
  didMount(){
    console.log(this.is);
    console.log(this.$page);
    console.log(this.$id);
  }
});
```

```
<!-- /components/xx/index.axml 组件id可直接在组件axml中渲染 -->
<view>{{$id}}</view>
```

```
// /pages/index/index.json
{
  "usingComponents": {
    "xx": "/components/xx/index"
  }
}
```

```
<!-- /pages/index/index.axml -->
<xx />
```

当组件在页面上渲染后，执行 didMount 回调，控制台输出大概是这样的：

```
/components/xx/index
{$viewId: 51, route: "pages/index/index"}
1
```
