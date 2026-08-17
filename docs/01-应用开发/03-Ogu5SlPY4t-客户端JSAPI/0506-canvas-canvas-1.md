---
title: "canvas 画布"
source_url: "https://open.dingtalk.com/document/development/canvas-canvas-1"
namespace: "development"
slug: "canvas-canvas-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 画布 > canvas 画布"
doc_id: "GQIkz1VVtw"
updated_at: "2025-09-17 20:58:34"
---

> Source: https://open.dingtalk.com/document/development/canvas-canvas-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 画布 > canvas 画布
> Updated: 2025-09-17 20:58:34

# canvas 画布

本文介绍画布组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **说明** |
| --- | --- | --- |
| id | String | 组件唯一标识符。  同一页面中的 `id` 不可重复。如果需要在高 dpr 下取得更细腻的显示，需要先将 `canvas` 用属性设置放大，用样式缩写，例如：   ``` <!-- getSystemInfoSync().pixelRatio === 2 --> <canvas width="200" height="200" style="width:100px;height:100px;"/> ``` |
| style | String | - |
| class | String | - |
| width | String | **默认值：**300px。 |
| height | String | **默认值：**225px。 |
| disable-scroll | Boolean | 禁止屏幕滚动以及下拉刷新。  **默认值**：false。 |
| onTap | EventHandle | 点击。 |
| onTouchStart | EventHandle | 触摸动作开始。 |
| onTouchMove | EventHandle | 触摸后移动。 |
| onTouchEnd | EventHandle | 触摸动作结束。 |
| onTouchCancel | EventHandle | 触摸动作被打断，如来电提醒，弹窗。 |
| onLongTap | EventHandle | 长按 500ms 之后触发，触发了长按事件后进行移动将不会触发屏幕的滚动。 |

## 示例代码

.axml示例代码：

```
<canvas
  id="canvas"
  class="canvas"
  onTouchStart="log"
  onTouchMove="log"
  onTouchEnd="log"
/>
```

.js示例代码：

```
Page({
  onReady() {
    this.point = {
      x: Math.random() * 295,
      y: Math.random() * 295,
      dx: Math.random() * 5,
      dy: Math.random() * 5,
      r: Math.round(Math.random() * 255 | 0),
      g: Math.round(Math.random() * 255 | 0),
          b: Math.round(Math.random() * 255 | 0),
    };

    this.interval = setInterval(() => {this.draw() }, 17);
  },

  draw() {
    var ctx = dd.createCanvasContext('canvas');
    ctx.setFillStyle('#FFF');
    ctx.fillRect(0, 0, 305, 305);

    ctx.beginPath();
    ctx.arc(this.point.x, this.point.y, 10, 0, 2 * Math.PI);
    ctx.setFillStyle("rgb(" + this.point.r + ", " + this.point.g + ", " + this.point.b + ")");
    ctx.fill();
    ctx.draw();

    this.point.x += this.point.dx;
    this.point.y += this.point.dy;
    if (this.point.x <= 5 || this.point.x >= 295) {
      this.point.dx = -this.point.dx;
      this.point.r = Math.round(Math.random() * 255 | 0);
      this.point.g = Math.round(Math.random() * 255 | 0);
      this.point.b = Math.round(Math.random() * 255 | 0);
    }

    if (this.point.y <= 5 || this.point.y >= 295) {
      this.point.dy = -this.point.dy;
      this.point.r = Math.round(Math.random() * 255 | 0);
      this.point.g = Math.round(Math.random() * 255 | 0);
      this.point.b = Math.round(Math.random() * 255 | 0);
    }
  },
  drawBall() {

  },
  log(e) {
    if (e.touches && e.touches[0]) {
      console.log(e.type, e.touches[0].x, e.touches[0].y);
    } else {
      console.log(e.type);
    }
  },
  onUnload() {
    clearInterval(this.interval)
  }
})
```
