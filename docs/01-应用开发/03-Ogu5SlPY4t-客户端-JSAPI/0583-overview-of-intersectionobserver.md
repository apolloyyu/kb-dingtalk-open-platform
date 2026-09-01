---
title: "IntersectionObserver 对象"
source_url: "https://open.dingtalk.com/document/development/overview-of-intersectionobserver"
namespace: "development"
slug: "overview-of-intersectionobserver"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 节点查询 > IntersectionObserver > IntersectionObserver 对照"
doc_id: "DwxKuTZ7So"
updated_at: "2026-09-01 09:16:45"
---

> Source: https://open.dingtalk.com/document/development/overview-of-intersectionobserver
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 节点查询 > IntersectionObserver > IntersectionObserver 对照
> Updated: 2026-09-01 09:16:45

# IntersectionObserver 对象

## **概览**

IntersectionObserver 对象，用于推断某些节点是否可以被用户看见、有多大比例被用户看见。

| **方法** | **描述** |
| --- | --- |
| **IntersectionObserver.disconnect** | 停止监听。 |
| **IntersectionObserver.observe** | 指定目标节点，并开始监听相交状态变化情况。 |
| **IntersectionObserver.relativeTo** | 使用选择器指定一个节点，作为参照区域之一。 |
| **IntersectionObserver.relativeToViewport** | 指定页面显示区域作为参照区域之一。 |

## **停止监听**

调用**IntersectionObserver.disconnect**停止监听。

> **[!NOTE]**
>
> 回调函数将不再触发。

## **监听相交状态变化**

调用**IntersectionObserver.observe**指定目标节点并开始监听相交状态变化情况。

### **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| targetSelector | String | 选择器。 |
| callback | Function | 监听相交状态变化的回调函数。 |

### **callback 参数**

- **Object res 属性**

  | **属性** | **类型** | **描述** |
  | --- | --- | --- |
  | intersectionRatio | Number | 相交比例。 |
  | intersectionRect | Object | 相交区域的边界。 |
  | boundingClientRect | Object | 目标边界。 |
  | relativeRect | Object | 参照区域的边界。 |
  | time | Number | 相交检测时的时间戳。 |
- **res.intersectionRect 属性**

  | **属性** | **类型** | **描述** |
  | --- | --- | --- |
  | left | Number | 左边界。 |
  | right | Number | 右边界。 |
  | top | Number | 上边界。 |
  | bottom | Number | 下边界。 |
- **res.boundingClientRect 属性**

  | **属性** | **类型** | **描述** |
  | --- | --- | --- |
  | left | Number | 左边界。 |
  | right | Number | 右边界。 |
  | top | Number | 上边界。 |
  | bottom | Number | 下边界。 |
- **res.relativeRect 属性**

  | **属性** | **类型** | **描述** |
  | --- | --- | --- |
  | left | Number | 左边界。 |
  | right | Number | 右边界。 |
  | top | Number | 上边界。 |
  | bottom | Number | 下边界。 |

## **设置参照区域**

### **指定节点**

调用**IntersectionObserver.relativeTo**使用选择器指定一个节点，作为参照区域之一。

#### **入参说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| selector | String | 选择器。 |
| margins | Object | 用来扩展（或收缩）参照节点布局区域的边界。 |

**margins** 属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| left | Number | 否 | 节点布局区域的左边界。 |
| right | Number | 否 | 节点布局区域的右边界。 |
| top | Number | 否 | 节点布局区域的上边界。 |
| bottom | Number | 否 | 节点布局区域的下边界。 |

### **指定页面显示区域**

调用**IntersectionObserver.relativeToViewport**指定页面显示区域作为参照区域之一。

#### **入参说明**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| margins | Object | 用来扩展（或收缩）参照节点布局区域的边界。 |

**margins** 属性如下：

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| left | Number | 否 | 节点布局区域的左边界。 |
| right | Number | 否 | 节点布局区域的右边界。 |
| top | Number | 否 | 节点布局区域的上边界。 |
| bottom | Number | 否 | 节点布局区域的下边界。 |
