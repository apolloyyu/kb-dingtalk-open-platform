---
title: "填充内容(fill)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-fill"
namespace: "development"
slug: "canvascontext-fill"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 填充内容(fill)"
doc_id: "uFy9mxzOwH"
updated_at: "2025-09-17 20:59:34"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-fill
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 填充内容(fill)
> Updated: 2025-09-17 20:59:34

# 填充内容(fill)

调用**CanvasContext.fill**对当前路径中的内容进行填充。默认的填充色为黑色。

> **[!IMPORTANT]**
>
> - 如果当前路径没有闭合，`fill()` 方法会将起点和终点进行连接，然后填充，详情见**示例代码一**。
> - `fill()` 填充的的路径是从 `beginPath()` 开始计算，但是不会将 `fillRect()` 包含进去，详情见**示例代码二**。

## **示例代码**

**示例代码一**

```
const ctx = dd.createCanvasContext('awesomeCanvas')
ctx.moveTo(20, 20)
ctx.lineTo(200, 20)
ctx.lineTo(200, 200)
ctx.fill()
ctx.draw( 
)
```

**示例代码二**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.rect(20, 20, 110, 40);
ctx.setFillStyle('blue');
ctx.fill();

ctx.beginPath();
ctx.rect(20, 30, 150, 40);

ctx.setFillStyle('yellow');
ctx.fillRect(20, 80, 150, 40);

ctx.rect(20, 150, 150, 40);

ctx.setFillStyle('red');
ctx.fill();
ctx.draw();
```
