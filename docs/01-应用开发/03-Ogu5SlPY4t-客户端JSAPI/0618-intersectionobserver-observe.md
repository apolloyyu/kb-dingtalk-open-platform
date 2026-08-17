---
title: "监听相交状态变化"
source_url: "https://open.dingtalk.com/document/development/intersectionobserver-observe"
namespace: "development"
slug: "intersectionobserver-observe"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 节点查询 > IntersectionObserver > 监听相交状态变化"
doc_id: "h2jjjw6cbf"
updated_at: "2025-09-17 20:59:53"
---

> Source: https://open.dingtalk.com/document/development/intersectionobserver-observe
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 节点查询 > IntersectionObserver > 监听相交状态变化
> Updated: 2025-09-17 20:59:53

# 监听相交状态变化

调用**IntersectionObserver.observe**指定目标节点并开始监听相交状态变化情况。

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| targetSelector | String | 选择器。 |
| callback | Function | 监听相交状态变化的回调函数。 |

## **callback 参数**

**Object res 属性**

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| intersectionRatio | Number | 相交比例。 |
| intersectionRect | Object | 相交区域的边界。 |
| boundingClientRect | Object | 目标边界。 |
| relativeRect | Object | 参照区域的边界。 |
| time | Number | 相交检测时的时间戳。 |

**res.intersectionRect 属性**

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| left | Number | 左边界。 |
| right | Number | 右边界。 |
| top | Number | 上边界。 |
| bottom | Number | 下边界。 |

**res.boundingClientRect 属性**

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| left | Number | 左边界。 |
| right | Number | 右边界。 |
| top | Number | 上边界。 |
| bottom | Number | 下边界。 |

**res.relativeRect 属性**

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| left | Number | 左边界。 |
| right | Number | 右边界。 |
| top | Number | 上边界。 |
| bottom | Number | 下边界。 |
