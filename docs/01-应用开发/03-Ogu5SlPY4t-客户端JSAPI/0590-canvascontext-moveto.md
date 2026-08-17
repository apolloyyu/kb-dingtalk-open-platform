---
title: "移动路径(moveTo)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-moveto"
namespace: "development"
slug: "canvascontext-moveto"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 移动路径(moveTo)"
doc_id: "oMOwtQdz1F"
updated_at: "2025-09-17 20:59:36"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-moveto
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 移动路径(moveTo)
> Updated: 2025-09-17 20:59:36

# 移动路径(moveTo)

调用**CanvasContext.moveTo**将路径移动到画布中的指定点，不创建线条。

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
