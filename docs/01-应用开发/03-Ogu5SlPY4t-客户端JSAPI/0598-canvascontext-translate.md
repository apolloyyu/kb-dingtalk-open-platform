---
title: "变换原点坐标(translate)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-translate"
namespace: "development"
slug: "canvascontext-translate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 变换原点坐标(translate)"
doc_id: "QTJ75vnPNM"
updated_at: "2025-09-17 20:59:40"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-translate
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 变换原点坐标(translate)
> Updated: 2025-09-17 20:59:40

# 变换原点坐标(translate)

调用CanvasContext.translate对当前坐标系的原点(0, 0)进行变换，默认的坐标系原点为页面左上角。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.strokeRect(20, 20, 250, 80);
ctx.translate(30, 30);
ctx.strokeRect(20, 20, 250, 80);
ctx.translate(30, 30);
ctx.strokeRect(20, 20, 250, 80);

ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 水平坐标平移量。 |
| y | Number | 竖直坐标平移量。 |
