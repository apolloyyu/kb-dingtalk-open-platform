---
title: "创建IntersectionObserver对象实例"
source_url: "https://open.dingtalk.com/document/development/dd-createintersectionobserver"
namespace: "development"
slug: "dd-createintersectionobserver"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 节点查询 > 创建IntersectionObserver对象实例"
doc_id: "BHI34HkkNt"
updated_at: "2025-09-17 20:59:51"
---

> Source: https://open.dingtalk.com/document/development/dd-createintersectionobserver
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 节点查询 > 创建IntersectionObserver对象实例
> Updated: 2025-09-17 20:59:51

# 创建IntersectionObserver对象实例

调用**dd.createIntersectionObserver**创建并返回一个IntersectionObserver对象实例。需在page.onReady之后执行dd.createIntersectionObserver()。

## 使用限制

基础库 1.24.0 及以上版本，低版本需做兼容处理。

## 入参

入参为 Object 类型，属性如下：

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| thresholds | Number[] | 一个数值数组，包含所有阈值。  **默认值**：[0]。 |
| initialRatio | Number | 初始的相交比例，如果调用时检测到的相交比例与这个值不相等且达到阈值，则会触发一次监听器的回调函数。  **默认值**：0。 |
| selectAll | Boolean | 是否同时观测多个目标节点（而非一个），如果设为 true ，observe 的 targetSelector 将选中多个节点。  **默认值**：false。  **[!IMPORTANT]**  同时选中过多节点将影响渲染性能。 |

## **返回值**

[IntersectionObserver](https://open.dingtalk.com/document/orgapp/overview-of-intersectionobserver)
