---
title: "设置最大斜接长度(setMiterLimit)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setmiterlimit"
namespace: "development"
slug: "canvascontext-setmiterlimit"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置最大斜接长度(setMiterLimit)"
doc_id: "RVwwUrYznq"
updated_at: "2025-09-17 20:59:31"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setmiterlimit
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置最大斜接长度(setMiterLimit)
> Updated: 2025-09-17 20:59:31

# 设置最大斜接长度(setMiterLimit)

调用**CanvasContext.setMiterLimit**设置最大斜接长度，斜接长度指的是在两条线交汇处内角和外角之间的距离。

当 `setLineJoin()` 为 miter 时才有效。超过最大倾斜长度的，连接处将以 lineJoin 为 bevel 来显示。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.beginPath();
ctx.setLineWidth(15);
ctx.setLineJoin('miter');
ctx.setMiterLimit(1);
ctx.moveTo(10, 10);
ctx.lineTo(100, 50);
ctx.lineTo(10, 90);
ctx.stroke();

ctx.beginPath();
ctx.setLineWidth(15);
ctx.setLineJoin('miter');
ctx.setMiterLimit(2);
ctx.moveTo(50, 10);
ctx.lineTo(140, 50);
ctx.lineTo(50, 90);
ctx.stroke();

ctx.beginPath();
ctx.setLineWidth(15);
ctx.setLineJoin('miter');
ctx.setMiterLimit(3);
ctx.moveTo(90, 10);
ctx.lineTo(180, 50);
ctx.lineTo(90, 90);
ctx.stroke();

ctx.draw();
```

## **入参**

| 参数 | 类型 | **说明** |
| --- | --- | --- |
| miterLimit | Number | 最大斜接长度。 |
