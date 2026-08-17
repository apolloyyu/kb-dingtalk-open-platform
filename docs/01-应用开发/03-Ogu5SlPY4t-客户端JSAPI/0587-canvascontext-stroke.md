---
title: "画出当前路径的边框(stroke)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-stroke"
namespace: "development"
slug: "canvascontext-stroke"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 画出当前路径的边框(stroke)"
doc_id: "zFhkJF0xXc"
updated_at: "2025-09-17 20:59:34"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-stroke
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 画出当前路径的边框(stroke)
> Updated: 2025-09-17 20:59:34

# **画出当前路径的边框(stroke)**

调用**CanvasContext****.stroke**画出当前路径的边框。默认 black。

> **[!IMPORTANT]**
>
> `stroke()` 描绘的的路径是从 `beginPath()` 开始计算，但是不会将 `strokeRect()` 包含进去，详情见**示例代码二**。

## **示例代码**

**示例代码一**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.moveTo(20, 20);
ctx.lineTo(150, 10);
ctx.lineTo(150, 150);
ctx.stroke();
ctx.draw();
```

**示例代码二**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.rect(10, 10, 100, 30);
ctx.setStrokeStyle('blue');
ctx.stroke();

ctx.beginPath();
ctx.rect(20, 50, 150, 50);

ctx.setStrokeStyle('yellow');
ctx.strokeRect(15, 75, 200, 35);

ctx.rect(20, 200, 150, 30);

ctx.setStrokeStyle('red');
ctx.stroke();
ctx.draw();
```
