---
title: "CanvasContext.lineTo"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-line-to"
namespace: "development"
slug: "jsapi-canvas-context-line-to"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.lineTo"
doc_id: "oKRpuSFk79"
updated_at: "2025-08-27 18:05:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-line-to
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.lineTo
> Updated: 2025-08-27 18:05:36

# CanvasContext.lineTo

调用CanvasContext.lineTo，增加一个新点，然后创建一条从上次指定点到目标点的线。

> 用 stroke() 方法来画线条。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10096) |

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

### 出参

- `x`（number，必填）：目标位置 x 坐标。
- `y`（number，必填）：目标位置 y 坐标 。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.lineTo(120, 60);
```

`success`返回对象示例：

```
{}
```
