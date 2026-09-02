---
title: "createIntersectionObserver"
source_url: "https://open.dingtalk.com/document/development/jsapi-create-intersection-observer"
namespace: "development"
slug: "jsapi-create-intersection-observer"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > createIntersectionObserver"
doc_id: "FiKu8nUf08"
updated_at: "2025-08-27 18:06:13"
---

> Source: https://open.dingtalk.com/document/development/jsapi-create-intersection-observer
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 节点查询 > createIntersectionObserver
> Updated: 2025-08-27 18:06:13

# createIntersectionObserver

调用createIntersectionObserver，创建并返回一个IntersectionObserver对象实例。

> 需在page.onReady之后执行dd.createIntersectionObserver()。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10035) |

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

- `selectAll`（boolean，必填）：是否同时观测多个目标节点（而非一个），如果设为 true ，observe 的 targetSelector 将选中多个节点。  
    
  \*\*默认值：\*\* false。  
    
    
  > 同时选中过多节点将影响渲染性能。
- `thresholds`（array，必填）：一个数值数组，包含所有阈值。  
    
  默认值：[0]。
- `initialRatio`（number，必填）：初始的相交比例，如果调用时检测到的相交比例与这个值不相等且达到阈值，则会触发一次监听器的回调函数。  
    
  \*\*默认值：\*\* 0。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.createIntersectionObserver(true, [0], 0);
```
