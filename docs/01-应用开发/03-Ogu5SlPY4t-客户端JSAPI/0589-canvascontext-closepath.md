---
title: "关闭一个路径(closePath)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-closepath"
namespace: "development"
slug: "canvascontext-closepath"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 关闭一个路径(closePath)"
doc_id: "ArafHrecHj"
updated_at: "2025-09-17 20:59:35"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-closepath
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 关闭一个路径(closePath)
> Updated: 2025-09-17 20:59:35

# 关闭一个路径(closePath)

调用**CanvasContext.closePath**关闭一个路径。

> **[!IMPORTANT]**
>
> - 关闭路径会连接起点和终点。
> - 如果关闭路径后没有调用 `fill()` 或者 `stroke()` 并开启了新的路径，那之前的路径将不会被渲染。

## **示例代码**

**示例代码一**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.moveTo(20, 20);
ctx.lineTo(150, 20);
ctx.lineTo(150, 150);
ctx.closePath();
ctx.stroke();
ctx.draw();
```

**示例代码二**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.rect(20, 20, 150, 50);
ctx.closePath();

ctx.beginPath();
ctx.rect(20, 50, 150, 40);

ctx.setFillStyle('red');
ctx.fillRect(20, 80, 120, 30);

ctx.rect(20, 150, 150, 40);

ctx.setFillStyle('blue');
ctx.fill();
ctx.draw();
```
