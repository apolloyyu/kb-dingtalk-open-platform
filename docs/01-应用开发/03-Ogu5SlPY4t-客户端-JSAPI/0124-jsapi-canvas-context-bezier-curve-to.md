---
title: "CanvasContext.bezierCurveTo"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-bezier-curve-to"
namespace: "development"
slug: "jsapi-canvas-context-bezier-curve-to"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.bezierCurveTo"
doc_id: "MMdr8hQwbq"
updated_at: "2025-08-27 18:05:29"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-bezier-curve-to
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.bezierCurveTo
> Updated: 2025-08-27 18:05:29

# CanvasContext.bezierCurveTo

调用CanvasContext.bezierCurveTo，创建三次方贝塞尔曲线路径。曲线的起始点为路径中前一个点。

针对 moveTo(30, 30)bezierCurveTo(30, 150, 250, 150, 180, 20) 的三个关键坐标如下：

红色：起始点(20, 20)

蓝色：两个控制点(20, 150) (250, 150)

绿色：终止点(180, 20)

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10084) |

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

- `y`（number，必填）：结束点 y 坐标。
- `cp1x`（number，必填）：第一个贝塞尔控制点 x 坐标。
- `cp1y`（number，必填）：第一个贝塞尔控制点 y 坐标。
- `cp2x`（number，必填）：第二个贝塞尔控制点 x 坐标。
- `cp2y`（number，必填）：第二个贝塞尔控制点 y 坐标。
- `x`（number，必填）：结束点 x 坐标。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.bezierCurveTo(180, 20, 30, 150, 250, 150);
```

`success`返回对象示例：

```
{}
```
