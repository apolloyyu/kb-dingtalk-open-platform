---
title: "创建SelectorQuery节点查询对象"
source_url: "https://open.dingtalk.com/document/development/dd-createselectorquery"
namespace: "development"
slug: "dd-createselectorquery"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 节点查询 > 创建SelectorQuery节点查询对象"
doc_id: "gg11j5NpLI"
updated_at: "2025-09-17 20:59:55"
---

> Source: https://open.dingtalk.com/document/development/dd-createselectorquery
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 节点查询 > 创建SelectorQuery节点查询对象
> Updated: 2025-09-17 20:59:55

# 创建SelectorQuery节点查询对象

调用dd.createSelectorQuery创建一个节点查询对象SelectorQuery。

## 扫码体验

![1595557621441-22](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8965013061/p174248.png)

## 使用限制

基础库 `1.4.0` 或更高版本。

## **示例代码**

.axml示例代码：

```
<view className="all">节点 all1</view>

<view className="all">节点 all2</view>

<view id="one">节点 one</view>

<view id="scroll" style="height:200px;overflow: auto">
  <view style="height:400px">独立滚动区域</view>
</view>
```

.js示例代码：

```
Page({
  onReady() {
    dd.createSelectorQuery()
      .select('#non-exists').boundingClientRect()
      .select('#one').boundingClientRect()
      .selectAll('.all').boundingClientRect()
      .select('#scroll').scrollOffset()
      .selectViewport().boundingClientRect()
      .selectViewport().scrollOffset().exec((ret) => {
      console.log(JSON.stringify(ret, null, 2));
    });
  },
});
```

**ret结构**

```
[
  null,
  {
    "x": 1,
    "y": 2,
    "width": 1367,
    "height": 18,
    "top": 2,
    "right": 1368,
    "bottom": 20,
    "left": 1
  },
  [
    {
      "x": 1,
      "y": -34,
      "width": 1367,
      "height": 18,
      "top": -34,
      "right": 1368,
      "bottom": -16,
      "left": 1
    },
    {
      "x": 1,
      "y": -16,
      "width": 1367,
      "height": 18,
      "top": -16,
      "right": 1368,
      "bottom": 2,
      "left": 1
    }
  ],
  {
    "scrollTop": 0,
    "scrollLeft": 0
  },
  {
    "width": 1384,
    "height": 360
  },
  {
    "scrollTop": 35,
    "scrollLeft": 0
  }
]
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| params | object | 可以指定 page 属性，默认为当前页面。 |

## 返回值

[SelectorQuery](https://open.dingtalk.com/document/orgapp/selectorquery)
