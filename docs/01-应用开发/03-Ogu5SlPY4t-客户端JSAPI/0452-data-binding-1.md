---
title: "数据绑定"
source_url: "https://open.dingtalk.com/document/development/data-binding-1"
namespace: "development"
slug: "data-binding-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 数据绑定"
doc_id: "E6QRU96D99"
updated_at: "2025-09-17 20:57:57"
---

> Source: https://open.dingtalk.com/document/development/data-binding-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > AXML视图层 > 数据绑定
> Updated: 2025-09-17 20:57:57

# 数据绑定

AXML中的动态数据均来自对应 Page 的data。

## 简单绑定

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

## 运算

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

## 组合

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

  > **[!IMPORTANT]**
  >
  > 上面的方式可以随意组合，但是如有存在变量名相同的情况，后边的变量会覆盖前面变量。

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

  最终组合成的对象是 {a: 5, b: 3, c: 6}。
