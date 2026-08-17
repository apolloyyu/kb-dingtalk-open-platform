---
title: "保存当前绘图上下文(save)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-save"
namespace: "development"
slug: "canvascontext-save"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 保存当前绘图上下文(save)"
doc_id: "viUxVx4cIo"
updated_at: "2025-09-17 20:59:42"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-save
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 保存当前绘图上下文(save)
> Updated: 2025-09-17 20:59:42

# 保存当前绘图上下文(save)

调用**CanvasContext.save**保存当前的绘图上下文。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas')

// save the default fill style
ctx.save();
ctx.setFillStyle('red');
ctx.fillRect(10, 10, 150, 100);

// restore to the previous saved state
ctx.restore();
ctx.fillRect(50, 50, 150, 100);

ctx.draw();
```
