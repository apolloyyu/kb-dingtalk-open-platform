---
title: "将描述画到画布中(draw)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-draw"
namespace: "development"
slug: "canvascontext-draw"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 将描述画到画布中(draw)"
doc_id: "fI1FT7DI22"
updated_at: "2025-09-17 20:59:43"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-draw
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 将描述画到画布中(draw)
> Updated: 2025-09-17 20:59:43

# 将描述画到画布中(draw)

调用**CanvasContext.draw**将之前在绘图上下文中的描述（路径、变形、样式）画到 canvas 中。

> **[!IMPORTANT]**
>
> 绘图上下文需要由 `dd.createCanvasContext(canvasId)` 来创建。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.setFillStyle('blue');
ctx.fillRect(20, 20, 180, 80);
ctx.draw();
ctx.fillRect(60, 60, 250, 120);
ctx.draw(true);
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| reserve | Boolean | 本次绘制是否接着上一次绘制，默认为false。   - 参数为 false 时，则在本次调用 drawCanvas绘制之前 native 层应先清空画布再继续绘制。 - 参数为true 时，则保留当前画布上的内容，本次调用drawCanvas绘制的内容覆盖在上面。 |
