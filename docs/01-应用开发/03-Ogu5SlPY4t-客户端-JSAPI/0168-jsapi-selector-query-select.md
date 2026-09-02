---
title: "SelectorQuery.select"
source_url: "https://open.dingtalk.com/document/development/jsapi-selector-query-select"
namespace: "development"
slug: "jsapi-selector-query-select"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > SelectorQuery.select"
doc_id: "KzxkzxL7WP"
updated_at: "2025-08-27 18:06:17"
---

> Source: https://open.dingtalk.com/document/development/jsapi-selector-query-select
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 节点查询 > SelectorQuery.select
> Updated: 2025-08-27 18:06:17

# SelectorQuery.select

调用SelectorQuery.select，选择当前第一个匹配选择器的节点，选择器支持 id 选择器以及 class 选择器。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10044) |

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

- `selector`（string，必填）：选择当前第一个匹配选择器的节点，选择器支持 id 选择器以及 class 选择器。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const selectorQuery = dd.createSelectorQuery();

selectorQuery.select('.all');
```
