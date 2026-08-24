---
title: "CanvasContext.setTextAlign"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-set-text-align"
namespace: "development"
slug: "jsapi-canvas-context-set-text-align"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.setTextAlign"
doc_id: "aDP1rif3Mw"
updated_at: "2025-08-27 18:05:46"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-set-text-align
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.setTextAlign
> Updated: 2025-08-27 18:05:46

# CanvasContext.setTextAlign

调用CanvasContext.setTextAlign， Canvas 2D API 描述绘制文本时，文本的对齐方式。

> 该对齐是基于CanvasRenderingContext2D.fillText 方法的x的值。如果 textAlign="center"，那么该文本将画在 x-50%\*width。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10114) |

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

- `textAlign`（string，必填）：枚举：  
     
  \* left：左  
  \* right：右  
  \* center：中间  
  \* start：开头  
  \* end：结尾

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const canvasContext = dd.createCanvasContext();
canvasContext.canvasId = 'awesomeCanvas';
canvasContext.setTextAlign({
  textAlign: 'left',
});
```
