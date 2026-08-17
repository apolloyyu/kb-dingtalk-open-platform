---
title: "事件概述"
source_url: "https://open.dingtalk.com/document/development/mini-app-event-overview"
namespace: "development"
slug: "mini-app-event-overview"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > 事件 > 事件概述"
doc_id: "0dHK2YNiRU"
updated_at: "2025-09-17 20:58:05"
---

> Source: https://open.dingtalk.com/document/development/mini-app-event-overview
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > 事件 > 事件概述
> Updated: 2025-09-17 20:58:05

# 事件概述

## 什么是事件？

- 事件是视图层到逻辑层的通讯方式。
- 事件可以将用户的行为反馈到逻辑层进行处理。
- 事件可以绑定在组件上，当达到触发条件，就会执行逻辑层中对应的事件函数。
- 事件对象可以携带额外信息，例如id, dataset, touches。

## 使用方式

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

## 事件类型

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
