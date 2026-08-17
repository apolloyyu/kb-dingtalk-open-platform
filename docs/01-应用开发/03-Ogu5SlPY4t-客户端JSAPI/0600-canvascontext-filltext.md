---
title: "绘制被填充的文本(fillText)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-filltext"
namespace: "development"
slug: "canvascontext-filltext"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 绘制被填充的文本(fillText)"
doc_id: "i0oRjsfCaD"
updated_at: "2025-09-17 20:59:41"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-filltext
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 绘制被填充的文本(fillText)
> Updated: 2025-09-17 20:59:41

# 绘制被填充的文本(fillText)

调用**CanvasContext.fillText**在画布上绘制被填充的文本。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.setFontSize(42);
ctx.fillText('Hello', 30, 30);
ctx.fillText('Dingtalk', 200, 200);

ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| text | String | 文本。 |
| x | Number | 绘制文本的左上角 x 坐标。 |
| y | Number | 绘制文本的左上角 y 坐标。 |
