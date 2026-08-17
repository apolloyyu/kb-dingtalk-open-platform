---
title: "创建线性的渐变色(createLinearGradient)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-createlineargradient"
namespace: "development"
slug: "canvascontext-createlineargradient"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建线性的渐变色(createLinearGradient)"
doc_id: "C4hmHf1CKM"
updated_at: "2025-09-17 20:59:28"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-createlineargradient
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建线性的渐变色(createLinearGradient)
> Updated: 2025-09-17 20:59:28

# 创建线性的渐变色(createLinearGradient)

调用**CanvasContext.createLinearGradient**创建一个线性的渐变色。

> **[!IMPORTANT]**
>
> 需要使用 `addColorStop()` 来指定渐变点，至少需要两个。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

const grd = ctx.createLinearGradient(10, 10, 150, 10);
grd.addColorStop(0, 'yellow');
grd.addColorStop(1, 'blue');

ctx.setFillStyle(grd);
ctx.fillRect(20, 20, 250, 180);
ctx.draw();
```

## 入参

| **参数** | 类型 | 说明 |
| --- | --- | --- |
| x0 | Number | 起点 x 坐标。 |
| x1 | Number | 起点 y 坐标。 |
| y0 | Number | 终点 x 坐标。 |
| y1 | Number | 终点 y 坐标。 |
