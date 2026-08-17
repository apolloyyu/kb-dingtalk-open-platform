---
title: "创建三次方贝塞尔曲线路径(bezierCurveTo)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-beziercurveto"
namespace: "development"
slug: "canvascontext-beziercurveto"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建三次方贝塞尔曲线路径(bezierCurveTo)"
doc_id: "EubGLfRA6W"
updated_at: "2025-09-17 20:59:37"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-beziercurveto
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建三次方贝塞尔曲线路径(bezierCurveTo)
> Updated: 2025-09-17 20:59:37

# 创建三次方贝塞尔曲线路径(bezierCurveTo)

调用**CanvasContext****.bezierCurveTo**创建三次方贝塞尔曲线路径。曲线的起始点为路径中前一个点。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.beginPath();
ctx.arc(30, 30, 2, 0, 2 * Math.PI);
ctx.setFillStyle('red');
ctx.fill();

ctx.beginPath();
ctx.arc(250, 25, 2, 0, 2 * Math.PI);
ctx.setFillStyle('blue');
ctx.fill();

ctx.beginPath();
ctx.arc(20, 100, 2, 0, 2 * Math.PI);
ctx.arc(200, 100, 2, 0, 2 * Math.PI);
ctx.setFillStyle('green');
ctx.fill();

ctx.setFillStyle('yellow');
ctx.setFontSize(14);

ctx.beginPath();
ctx.moveTo(30, 30);
ctx.lineTo(30, 100);
ctx.lineTo(150, 75);

ctx.moveTo(250, 30);
ctx.lineTo(250, 80);
ctx.lineTo(70, 75);
ctx.setStrokeStyle('#EEEEEE');
ctx.stroke();

ctx.beginPath();
ctx.moveTo(30, 30);
ctx.bezierCurveTo(30, 150, 250, 150, 180, 20);
ctx.setStrokeStyle('black');
ctx.stroke();

ctx.draw();
```

针对 `moveTo(30, 30)``bezierCurveTo(30, 150, 250, 150, 180, 20)` 的三个关键坐标如下：

- 红色：起始点(20, 20)
- 蓝色：两个控制点(20, 150) (250, 150)
- 绿色：终止点(180, 20)

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| cp1x | Number | 第一个贝塞尔控制点 x 坐标。 |
| cp1y | Number | 第一个贝塞尔控制点 y 坐标。 |
| cp2x | Number | 第二个贝塞尔控制点 x 坐标。 |
| cp2y | Number | 第二个贝塞尔控制点 y 坐标。 |
| x | Number | 结束点 x 坐标。 |
| y | Number | 结束点 y 坐标。 |
