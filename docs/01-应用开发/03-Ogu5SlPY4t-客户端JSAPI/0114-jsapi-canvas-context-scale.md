---
title: "CanvasContext.scale"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-scale"
namespace: "development"
slug: "jsapi-canvas-context-scale"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.scale"
doc_id: "XODLJfYwLf"
updated_at: "2025-08-27 18:05:41"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-scale
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.scale
> Updated: 2025-08-27 18:05:41

# CanvasContext.scale

在调用scale方法后，之后创建的路径其横纵坐标会被缩放。多次调用scale，倍数会相乘。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10104) |

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

- `scaleWidth`（number，必填）：横坐标缩放倍数 (1 = 100%，0.5 = 50%，2 = 200%)。 scaleHeight Number 纵坐标轴缩放倍数 (1 = 100%，0.5 = 50%，2 = 200%)。
- `scaleHeight`（number，必填）：纵坐标轴缩放倍数 (1 = 100%，0.5 = 50%，2 = 200%)。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.scale(3, 3);
```

`success`返回对象示例：

```
{}
```
