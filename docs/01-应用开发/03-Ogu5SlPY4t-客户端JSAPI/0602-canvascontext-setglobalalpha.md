---
title: "设置全局画笔透明度(setGlobalAlpha)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setglobalalpha"
namespace: "development"
slug: "canvascontext-setglobalalpha"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置全局画笔透明度(setGlobalAlpha)"
doc_id: "dVMBhJDmA8"
updated_at: "2025-09-17 20:59:42"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setglobalalpha
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置全局画笔透明度(setGlobalAlpha)
> Updated: 2025-09-17 20:59:42

# **设置全局画笔透明度(setGlobalAlpha)**

调用**CanvasContext.setGlobalAlpha**设置全局画笔透明度。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.setFillStyle('yellow');
ctx.fillRect(10, 10, 150, 100);
ctx.setGlobalAlpha(0.2);
ctx.setFillStyle('blue');
ctx.fillRect(50, 50, 150, 100);
ctx.setFillStyle('red');
ctx.fillRect(100, 100, 150, 100);

ctx.draw();
```

## **入参**

| 参数 | 类型 | 范围 | 说明 |
| --- | --- | --- | --- |
| alpha | Number | 0~1 | 透明度。  **0**：完全透明  **1**：不透明 |
