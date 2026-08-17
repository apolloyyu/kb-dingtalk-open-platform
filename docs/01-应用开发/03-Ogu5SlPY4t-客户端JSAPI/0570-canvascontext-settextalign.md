---
title: "文本对齐方式(setTextAlign)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-settextalign"
namespace: "development"
slug: "canvascontext-settextalign"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 文本对齐方式(setTextAlign)"
doc_id: "6TTbyjMXbM"
updated_at: "2025-09-17 20:59:25"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-settextalign
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 文本对齐方式(setTextAlign)
> Updated: 2025-09-17 20:59:25

# 文本对齐方式(setTextAlign)

**CanvasContext.setTextAlign**是 Canvas 2D API 描述绘制文本时，文本的对齐方式。

> **[!IMPORTANT]**
>
> 该对齐是基于CanvasRenderingContext2D.fillText 方法的x的值。如果 textAlign="center"，那么该文本将画在 x-50%\*width。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setTextAlign("left");
ctx.fillText("Hello world", 0, 100);
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| textAlign | String | 枚举 "left" "right" "center" "start" "end"。 |
