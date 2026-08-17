---
title: "事件对象"
source_url: "https://open.dingtalk.com/document/development/mini-app-event-object"
namespace: "development"
slug: "mini-app-event-object"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > 事件 > 事件对象"
doc_id: "El5kDCTp75"
updated_at: "2025-09-17 20:58:06"
---

> Source: https://open.dingtalk.com/document/development/mini-app-event-object
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > 事件 > 事件对象
> Updated: 2025-09-17 20:58:06

# 事件对象

当组件触发事件时，逻辑层绑定该事件的处理函数会收到一个事件对象。

## **BaseEvent**

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

## **CustomEvent**

`CustomEvent`自定义事件对象属性列表（继承`BaseEvent`）。

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| detail | Object | 额外的信息。 |

自定义事件所携带的数据，如表单组件的提交事件会携带用户的输入信息，媒体的错误事件会携带错误信息，详细的描述请参考组件定义中各个事件的定义。

## **TouchEvent**

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
