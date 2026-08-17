---
title: "创建canvas"
source_url: "https://open.dingtalk.com/document/development/create-a-canvas"
namespace: "development"
slug: "create-a-canvas"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建canvas"
doc_id: "1LkqHUoLAW"
updated_at: "2025-09-17 20:59:23"
---

> Source: https://open.dingtalk.com/document/development/create-a-canvas
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建canvas
> Updated: 2025-09-17 20:59:23

# 创建canvas

调用**dd.createCanvasContext(canvasId)** 创建canvas绘图上下文。

> **[!IMPORTANT]**
>
> 该绘图上下文只作用于对应 `canvasId` 的 `<canvas/>。`

## **扫码体验**

![1595556154340-5 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1409903061/p172097.png)

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| canvasId | String | 定义在`<canvas/>`上的 id。 |

## **返回值**

返回值为[CanvasContext概览](https://open.dingtalk.com/document/orgapp/overview-of-canvascontext)。
