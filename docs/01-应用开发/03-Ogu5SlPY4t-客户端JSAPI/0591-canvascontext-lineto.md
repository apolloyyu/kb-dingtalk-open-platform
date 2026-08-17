---
title: "增加一个新点(lineTo)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-lineto"
namespace: "development"
slug: "canvascontext-lineto"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 增加一个新点(lineTo)"
doc_id: "rHJ3GIZrGc"
updated_at: "2025-09-17 20:59:36"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-lineto
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 增加一个新点(lineTo)
> Updated: 2025-09-17 20:59:36

# 增加一个新点(lineTo)

调用**CanvasContext.lineTo lineTo**增加一个新点，然后创建一条从上次指定点到目标点的线。

> **[!IMPORTANT]**
>
> 用 `stroke()` 方法来画线条。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.moveTo(20, 20);
ctx.lineTo(150, 15);

ctx.moveTo(20, 55);
ctx.lineTo(120, 60);
ctx.stroke();
ctx.draw();
```

## **入参**

| **参数** | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 目标位置 x 坐标。 |
| y | Number | 目标位置 y 坐标 。 |
