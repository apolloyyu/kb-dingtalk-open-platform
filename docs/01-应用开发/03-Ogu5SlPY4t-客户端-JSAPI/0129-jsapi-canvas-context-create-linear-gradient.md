---
title: "CanvasContext.createLinearGradient"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-create-linear-gradient"
namespace: "development"
slug: "jsapi-canvas-context-create-linear-gradient"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.createLinearGradient"
doc_id: "Bgoxbbds3H"
updated_at: "2025-08-27 18:05:32"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-create-linear-gradient
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.createLinearGradient
> Updated: 2025-08-27 18:05:32

# CanvasContext.createLinearGradient

调用CanvasContext.createLinearGradient，创建一个线性的渐变色。

> 需要使用 `addColorStop()`  来指定渐变点，至少需要两个。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10089) |

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

- `x0`（number，必填）：起点 x 坐标。
- `x1`（number，必填）：起点 y 坐标。
- `y0`（number，必填）：终点 x 坐标。
- `y1`（number，必填）：终点 y 坐标。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.createLinearGradient(10, 10, 150, 10);
```

`success`返回对象示例：

```
{}
```
