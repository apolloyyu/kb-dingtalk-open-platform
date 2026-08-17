---
title: "创建路径(beginPath)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-beginpath"
namespace: "development"
slug: "canvascontext-beginpath"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建路径(beginPath)"
doc_id: "oZde6fpDmf"
updated_at: "2025-09-17 20:59:35"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-beginpath
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建路径(beginPath)
> Updated: 2025-09-17 20:59:35

# 创建路径(beginPath)

调用**CanvasContex****t.beginPath**开始创建一个路径，需要调用 fill 或者 stroke 才会使用路径进行填充或描边。

> **[!IMPORTANT]**
>
> - 在最开始的时候相当于调用了一次 `beginPath()`。
> - 同一个路径内的多次`setFillStyle()`、`setStrokeStyle()`、`setLineWidth()`等设置，以最后一次设置为准。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.rect(20, 20, 150, 50);
ctx.setFillStyle('blue');
ctx.fill();

ctx.beginPath();
ctx.rect(20, 50, 150, 40);

ctx.setFillStyle('yellow');
ctx.fillRect(20, 170, 150, 40);

ctx.rect(10, 100, 100, 30);

ctx.setFillStyle('red');
ctx.fill();
ctx.draw();
```
