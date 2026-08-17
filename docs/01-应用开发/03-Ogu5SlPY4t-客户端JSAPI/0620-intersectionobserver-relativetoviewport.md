---
title: "指定页面显示区域作为参照区域之一"
source_url: "https://open.dingtalk.com/document/development/intersectionobserver-relativetoviewport"
namespace: "development"
slug: "intersectionobserver-relativetoviewport"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 节点查询 > IntersectionObserver > 指定页面显示区域作为参照区域之一"
doc_id: "AHWG7nK5cM"
updated_at: "2025-09-17 20:59:54"
---

> Source: https://open.dingtalk.com/document/development/intersectionobserver-relativetoviewport
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 节点查询 > IntersectionObserver > 指定页面显示区域作为参照区域之一
> Updated: 2025-09-17 20:59:54

# 指定页面显示区域作为参照区域之一

调用IntersectionObserver.relativeToViewport指定页面显示区域作为参照区域之一。

## **入参说明**

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
