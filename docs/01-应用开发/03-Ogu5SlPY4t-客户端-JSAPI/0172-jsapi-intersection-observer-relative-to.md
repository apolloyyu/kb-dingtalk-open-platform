---
title: "IntersectionObserver.relativeTo"
source_url: "https://open.dingtalk.com/document/development/jsapi-intersection-observer-relative-to"
namespace: "development"
slug: "jsapi-intersection-observer-relative-to"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > IntersectionObserver.relativeTo"
doc_id: "cYxFdhijvX"
updated_at: "2025-08-27 18:06:15"
---

> Source: https://open.dingtalk.com/document/development/jsapi-intersection-observer-relative-to
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 节点查询 > IntersectionObserver.relativeTo
> Updated: 2025-08-27 18:06:15

# IntersectionObserver.relativeTo

调用IntersectionObserver.relativeTo，使用选择器指定一个节点，作为参照区域之一。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10038) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `selector`（string，必填）：选择器。
- `margins`（object）：用来扩展（或收缩）参照节点布局区域的边界。
- `margins.left`（number）：节点布局区域的左边界。
- `margins.right`（number）：节点布局区域的右边界。
- `margins.top`（number）：节点布局区域的上边界。
- `margins.bottom`（number）：节点布局区域的下边界。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const intersectionObserver = dd.IntersectionObserver();

intersectionObserver.relativeTo({ top, left, right, bottom }, 'xxId');
```
