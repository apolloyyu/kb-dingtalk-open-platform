---
title: "创建圆形的渐变色(createCircularGradient)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-createcirculargradient"
namespace: "development"
slug: "canvascontext-createcirculargradient"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建圆形的渐变色(createCircularGradient)"
doc_id: "F16TKeRa3o"
updated_at: "2025-09-17 20:59:28"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-createcirculargradient
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建圆形的渐变色(createCircularGradient)
> Updated: 2025-09-17 20:59:28

# 创建圆形的渐变色(createCircularGradient)

调用**CanvasContext.createCircularGradient**创建一个圆形的渐变色。

> **[!IMPORTANT]**
>
> - 起点在圆心，终点在圆环。
> - 需要使用 `addColorStop()` 来指定渐变点，至少需要两个。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

const grd = ctx.createCircularGradient(90, 60, 60);
grd.addColorStop(0, 'blue');
grd.addColorStop(1, 'red');

ctx.setFillStyle(grd);
ctx.fillRect(20, 20, 250, 180);
ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| x | Number | 圆心 x 坐标。 |
| y | Number | 圆心 y坐标。 |
| r | Number | 圆半径。 |
