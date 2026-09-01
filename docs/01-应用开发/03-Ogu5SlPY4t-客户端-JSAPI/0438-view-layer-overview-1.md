---
title: "AXML 视图层"
source_url: "https://open.dingtalk.com/document/development/view-layer-overview-1"
namespace: "development"
slug: "view-layer-overview-1"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML 视图层"
doc_id: "vODEBKoVbZ"
updated_at: "2026-09-01 09:16:08"
---

> Source: https://open.dingtalk.com/document/development/view-layer-overview-1
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML 视图层
> Updated: 2026-09-01 09:16:08

# AXML 视图层

## **概述**

视图文件的后缀名是`axml`，定义了页面的标签结构。AXML是小程序框架设计的一套标签语言，用于描述小程序页面的结构。

AXML语法可分为五个部分：

- **数据绑定**
- **列表渲染**
- **条件渲染**
- **模板**
- **事件**

## **数据绑定**

### **简单绑定**

数据绑定使用 Mustache 语法（双大括号）将变量包起来，可以作用于各种场合。

- 作用于内容的例子：

  ```
  <view> {{ message }} </view>
  ```

  ```
  Page({
    data: {
      message: 'Hello dingtalk!'
    }
  })
  ```
- 作用于组件属性的例子（需要在双引号之内）：

  ```
  <view id="item-{{id}}"> </view>
  ```

  ```
  Page({
    data: {
      id: 0
    }
  })
  ```
- 作用于控制属性的例子（需要在双引号之内）：

  ```
  <view a:if="{{condition}}"> </view>
  ```

  ```
  Page({
    data: {
      condition: true
    }
  })
  ```
- 作用于关键字的例子（需要在双引号之内）：

  | 值 | 说明 |
  | --- | --- |
  | true | boolean 类型的 true，代表真值 |
  | false | boolean 类型的 false，代表假值 |

  ```
  <checkbox checked="{{false}}"> </checkbox>
  ```

  > **[!IMPORTANT]**
  >
  > 如果直接写`checked="false"`，计算结果是一个字符串，转成布尔值类型后代表true。

### **运算**

可以在 {{}} 内进行简单的运算，支持的有如下几种方式：

- 三元运算

  ```
  <view hidden="{{flag ? true : false}}"> Hidden </view>
  ```
- 算数运算

  ```
  <view> {{a + b}} + {{c}} + d </view>
  ```

  ```
  Page({
    data: {
      a: 1,
      b: 2,
      c: 3
    }
  })
  ```

  View 中的内容为`3 + 3 + d`。
- 逻辑判断

  ```
  <view a:if="{{length > 5}}"> </view>
  ```
- 字符串运算

  ```
  <view>{{"hello" + name}}</view>
  ```

  ```
  Page({
    data:{
      name: 'dingtalk'
    }
  })
  ```
- 数据路径运算

  ```
  <view>{{object.key}} {{array[0]}}</view>
  ```

  ```
  Page({
    data: {
      object: {
        key: 'Hello '
      },
      array: ['dingtalk']
    }
  })
  ```

### **组合**

也可以在 Mustache 内直接进行组合，构成新的数组或者对象。

- 数组

  ```
  <view a:for="{{[zero, 1, 2, 3, 4]}}"> {{item}} </view>
  ```

  ```
  Page({
    data: {
      zero: 0
    }
  })
  ```

  最终组合成数组[0, 1, 2, 3, 4]。
- 对象

  ```
  <template is="objectCombine" data="{{foo: a, bar: b}}"></template>
  ```

  ```
  Page({
    data: {
      a: 1,
      b: 2
    }
  })
  ```

  最终组合成的对象是 {foo: 1, bar: 2}。

  也可以用扩展运算符`...`来将一个对象展开。

  ```
  <template is="objectCombine" data="{{...obj1, ...obj2, e: 5}}"></template>
  ```

  ```
  Page({
    data: {
      obj1: {
        a: 1,
        b: 2
      },
      obj2: {
        c: 3,
        d: 4
      }
    }
  })
  ```

  最终组合成的对象是 {a: 1, b: 2, c: 3, d: 4, e: 5}。

  如果对象的 key 和 value 相同，也可以间接地表达。

  ```
  <template is="objectCombine" data="{{foo, bar}}"></template>
  ```

  ```
  Page({
    data: {
      foo: 'my-foo',
      bar: 'my-bar'
    }
  })
  ```

  最终组合成的对象是 {foo: 'my-foo', bar:'my-bar'}。

  ```
  <template is="objectCombine" data="{{...obj1, ...obj2, a, c: 6}}"></template>
  ```

  ```
  Page({
    data: {
      obj1: {
        a: 1,
        b: 2
      },
      obj2: {
        b: 3,
        c: 4
      },
      a: 5
    }
  })
  ```

  > **[!IMPORTANT]**
  >
  > 上面的方式可以随意组合，但是如有存在变量名相同的情况，后边的变量会覆盖前面变量。

  最终组合成的对象是 {a: 5, b: 3, c: 6}。

## **条件渲染**

### **a:if**

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

### **block a:if**

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

## **列表渲染**

### **a:for**

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

### **block a:for**

类似`block a:if`，可以将`a:for`用在`<block/>`标签上，以渲染一个包含多节点的结构块。

```
<block a:for="{{[1, 2, 3]}}">
  <view> {{index}}: </view>
  <view> {{item}} </view>
</block>
```

### **a:key**

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

### **key**

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

## **引用**

### **import**

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

### **include**

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

## **模板**

AXML提供模板（template），可以在模板中定义代码片段，在不同的地方调用。

> **[!NOTE]**
>
> 此处 template 区别于 slot，slot 可参考[自定义组件](0472-mini-app-development-process.md)。

### **定义模板**

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

### **使用模板**

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

### **模板作用域**

模板拥有自己的作用域，只能用`data`传入的数据，但可以通过 `onXX` 绑定页面的逻辑处理函数。

推荐用 template 方式来引入模板片段，因为 template 会指定自己的作用域，只使用`data`传入的数据，因此应用会对此进行优化。如果该 template 的 data 没有改变，该片段 UI 并不会重新渲染。

引入路径支持从 node\_modules 目录载入第三方模块，例如 page.axml:

```
<import src="./a.axml"/> <!-- 相对路径 -->
<import src="/a.axml"/> <!-- 项目绝对路径 -->
<import src="third-party/x.axml"/> <!-- 第三方 npm 包路径 -->
```

## **事件**

### **什么是事件**

- 事件是视图层到逻辑层的通讯方式。
- 事件可以将用户的行为反馈到逻辑层进行处理。
- 事件可以绑定在组件上，当达到触发条件，就会执行逻辑层中对应的事件函数。
- 事件对象可以携带额外信息，例如id, dataset, touches。

### **使用方式**

若要在组件中绑定一个事件处理函数，如 `onTap`，则需要在该页面的 .js 文件中的 `Page` 里定义`onTap` 对应的事件处理函数。

```
<view id="tapTest" data-hi="Dingtalk" onTap="tapName">
  <view id="tapTestInner" data-hi="DingtalkInner">
    Click me! 
  </view>
</view>
```

在相应的Page定义中写上相应的事件处理函数，参数是event。

```
Page({
  tapName(event) {
    console.log(event)
  }
})
```

控制台输出 event 信息如下所示:

```
{
  "type": "tap",
  "timeStamp": 1619083408000,
  "target": {
    "id": "tapTestInner",
    "dataset": {
      "hi": "Dingtalk"
    },
    "targetDataset": {
      "hi": "DingtalkInner"
    }
  },
  "currentTarget": {
    "id": "tapTest",
    "dataset": {
      "hi": "Dingtalk"
    }
  }
}
```

### **事件类型**

事件分为冒泡事件和非冒泡事件：

- **冒泡事件**

  当一个组件上的事件被触发后，该事件会向父节点传递。
- **非冒泡事件**

  当一个组件上的事件被触发后，该事件不会向父节点传递。

事件绑定的写法同组件的属性，以 key、value 的形式：

- key 以on或catch开头，然后跟上事件的类型，onTap, catchTap。
- value 是一个字符串，需要在对应的 Page 中定义同名的函数。不然当触发事件的时候会报错。

on 事件绑定不会阻止冒泡事件向上冒泡，catch 事件绑定可以阻止冒泡事件向上冒泡。

代码示例：

```
<view id="outter" onTap="handleTap1">
  view1
  <view id="middle" catchTap="handleTap2">
    view2
    <view id="inner" onTap="handleTap3">
      view3
    </view>
  </view>
</view>
```

以上代码中：

- 点击 view3 会先后触发 handleTap3 和 handleTap2。因为 tap 事件会冒泡到 view2，而view2 阻止了 tap 事件冒泡，不再向父节点传递。
- 点击 view2 会触发 handleTap2。
- 点击 view1 会触发 handleTap1。

冒泡事件列表如下，其他事件不冒泡。

| 类型 | 触发条件 |
| --- | --- |
| touchStart | 触摸动作开始 |
| touchMove | 触摸后移动 |
| touchEnd | 触摸动作结束 |
| touchCancel | 触摸动作被打断，如来电提醒，弹窗 |
| tap | 触摸后马上离开 |
| longTap | 触摸后，超过300ms再离开 |

### **事件对象**

#### **BaseEvent**

`BaseEvent`基础事件对象属性列表。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| type | String | 事件类型。 |
| timeStamp | Integer | 事件生成时的时间戳。 |
| target | Object | 触发事件的组件的属性值集合。 |

其中：

- type：代表事件的类型。
- timeStamp：页面打开到触发事件所经过的毫秒数。
- target：触发事件的源组件。

  | 属性 | 类型 | 说明 |
  | --- | --- | --- |
  | id | String | 事件源组件的id。 |
  | tagName | String | 当前组件的类型。 |
  | dataset | Object | 绑定事件的组件上由`data-`开头的自定义属性的集合。 |
  | targetDataset | Object | 实际触发事件的组件上由`data`-开头的自定义属性的集合。 |

  `dataset`在组件中可以定义数据，这些数据将会通过事件传递给逻辑层。

  书写方式： 以`data-`开头，多个单词由连字符-链接，不能有大写(大写会自动转成小写)，如`data-element-type`，最终会在`event.target.dataset`中会将连字符转成驼峰`elementType`。

  示例代码：

  ```
  <view data-alpha-beta="1" data-alphaBeta="2" onTap="bindViewTap"> DataSet Test </view>
  ```

  ```
  Page({
    bindViewTap:function(event){
      event.target.dataset.alphaBeta === 1 // - 会转为驼峰写法
      event.target.dataset.alphabeta === 2 // 大写会转为小写
    }
  })
  ```

#### **CustomEvent**

`CustomEvent`自定义事件对象属性列表（继承`BaseEvent`）。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| detail | Object | 额外的信息。 |

自定义事件所携带的数据，如表单组件的提交事件会携带用户的输入信息，媒体的错误事件会携带错误信息，详细的描述请参考组件定义中各个事件的定义。

#### **TouchEvent**

`TouchEvent`触摸事件对象属性列表（继承`BaseEvent`）。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| touches | Array | 当前停留在屏幕中的触摸点信息的数组。 |
| changedTouches | Array | 当前变化的触摸点信息的数组。 |

`touches`是一个数组，每个元素为一个`Touch`对象（`canvas`触摸事件中携带的`touches`是 `CanvasTouch`的数组），表示当前停留在屏幕上的触摸点。

`changedTouches`数据格式同`touches`。 表示有变化的触摸点，如从无变有（`touchstart`），位置变化（`touchmove`），从有变无（`touchend`、`touchcancel`）。

**Touch 对象**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| identifier | Number | 触摸点的标识符。 |
| pageX, pageY | Number | 距离文档左上角的距离，左上角为原点 ，横向为X轴，纵向为Y轴。 |
| clientX, clientY | Number | 距离页面可显示的区域（屏幕除去导航条）左上角距离，横向为X轴，纵向为Y轴。 |

**CanvasTouch 对象**

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| identifier | Number | 触摸点的标识符。 |
| x, y | Number | 距离 Canvas 左上角的距离，Canvas 的左上角为原点 ，横向为X轴，纵向为Y轴。 |
