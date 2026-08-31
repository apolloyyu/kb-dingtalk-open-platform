---
title: "CanvasContext.arc"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-arc"
namespace: "development"
slug: "jsapi-canvas-context-arc"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.arc"
doc_id: "WCxTBuLfCI"
updated_at: "2025-08-27 18:05:28"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-arc
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.arc
> Updated: 2025-08-27 18:05:28

# CanvasContext.arc

调用CanvasContext.arc，画一条弧线。

> 创建一个圆可以用 arc() 方法指定其实弧度为0，终止弧度为 2 \* Math.PI。
> 用 stroke() 或者 fill() 方法来在 canvas 中画弧线。

针对 arc(150, 35, 50, 0, 1.8 \* Math.PI)的三个关键坐标如下：

绿色: 圆心 (15, 35)

红色: 起始弧度 (0)

蓝色: 终止弧度 (1.8 \* Math.PI)

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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

- `r`（number，必填）：圆 半径。
- `x`（number，必填）：圆 x 坐标。
- `y`（number，必填）：圆 y 坐标。
- `eAngle`（number，必填）：终止弧度。
- `sAngle`（number，必填）：起始弧度，单位弧度（在3点钟方向）。
- `counterclockwise`（boolean，必填）：指定弧度的方向是逆时针还是顺时针。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.arc(50, 150, 35, 1.8 * Math.PI, 0, false);
```

`success`返回对象示例：

```
{}
```
