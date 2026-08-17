---
title: "画一条弧线(arc)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-arc"
namespace: "development"
slug: "canvascontext-arc"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 画一条弧线(arc)"
doc_id: "rnc8I6TwDl"
updated_at: "2025-09-17 20:59:37"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-arc
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 画一条弧线(arc)
> Updated: 2025-09-17 20:59:37

# 画一条弧线(arc)

使用CanvasContext.arc画一条弧线。

> **[!IMPORTANT]**
>
> - 创建一个圆可以用 `arc()` 方法指定其实弧度为0，终止弧度为 `2 * Math.PI`。
> - 用 `stroke()` 或者 `fill()` 方法来在 canvas 中画弧线。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.arc(200, 75, 50, 0, 2 * Math.PI);
ctx.setFillStyle('#CCCCCC');
ctx.fill();

ctx.beginPath();
ctx.moveTo(50, 65);
ctx.lineTo(170, 80);
ctx.moveTo(200, 35);
ctx.lineTo(200, 235);
ctx.setStrokeStyle('#AAAAAA');
ctx.stroke();

ctx.setFontSize(12);
ctx.setFillStyle('yellow');
ctx.fillText('0', 165, 78);
ctx.fillText('0.6*PI', 96, 148);
ctx.fillText('1*PI', 15, 57);
ctx.fillText('1.7*PI', 94, 20);

ctx.beginPath();
ctx.arc(200, 85, 2, 0, 2 * Math.PI);
ctx.setFillStyle('blue');
ctx.fill();

ctx.beginPath();
ctx.arc(200, 35, 2, 0, 2 * Math.PI);
ctx.setFillStyle('green');
ctx.fill();

ctx.beginPath();
ctx.arc(450, 60, 2, 0, 2 * Math.PI);
ctx.setFillStyle('red');
ctx.fill();

ctx.beginPath();
ctx.arc(150, 35, 50, 0, 1.8 * Math.PI);
ctx.setStrokeStyle('#666666');
ctx.stroke();

ctx.draw();
```

针对 `arc(150, 35, 50, 0, 1.8 * Math.PI)`的三个关键坐标如下：

- 绿色: 圆心 (15, 35)
- 红色: 起始弧度 (0)
- 蓝色: 终止弧度 (1.8 \* Math.PI)

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 圆 x 坐标。 |
| y | Number | 圆 y 坐标。 |
| r | Number | 圆 半径。 |
| sAngle | Number | 起始弧度，单位弧度（在3点钟方向）。 |
| eAngle | Numbers | 终止弧度。 |
| counterclockwise | Boolean | 可选，指定弧度的方向是逆时针还是顺时针。  **默认值**：false。 |
