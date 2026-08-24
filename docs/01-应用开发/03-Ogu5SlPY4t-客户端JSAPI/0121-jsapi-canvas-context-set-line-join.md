---
title: "CanvasContext.setLineJoin"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-set-line-join"
namespace: "development"
slug: "jsapi-canvas-context-set-line-join"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.setLineJoin"
doc_id: "skTmLbPNyl"
updated_at: "2025-08-27 18:05:45"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-set-line-join
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.setLineJoin
> Updated: 2025-08-27 18:05:45

# CanvasContext.setLineJoin

调用CanvasContext.setLineJoin，设置线条的交点样式。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10109) |

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

- `lineJoin`（string，必填）：线条的结束交点样式，范围 'round'、'bevel'、'miter'。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.setLineJoin({
  lineJoin: 'bevel',
});
```
