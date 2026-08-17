---
title: "创建渐变点(addColorStop)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-addcolorstop"
namespace: "development"
slug: "canvascontext-addcolorstop"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建渐变点(addColorStop)"
doc_id: "ZG6bu1auwb"
updated_at: "2025-09-17 20:59:29"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-addcolorstop
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 创建渐变点(addColorStop)
> Updated: 2025-09-17 20:59:29

# 创建渐变点(addColorStop)

使用**CanvasContext.addColorStop**创建一个颜色的渐变点。

> **[!IMPORTANT]**
>
> - 小于最小 stop 的部分会按最小 stop 的 color 来渲染，大于最大 stop 的部分会按最大 stop 的 color 来渲染。
> - 需要使用 `addColorStop()`来指定渐变点，至少需要两个。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

const grd = ctx.createLinearGradient(40, 20, 230, 40);
grd.addColorStop(0.36, 'orange');
grd.addColorStop(0.56, 'cyan');
grd.addColorStop(0.63, 'yellow');
grd.addColorStop(0.76, 'blue');
grd.addColorStop(0.54, 'green');
grd.addColorStop(1, 'purple');
grd.addColorStop(0.4, 'red');

ctx.setFillStyle(grd);
ctx.fillRect(20, 20, 250, 180);
ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| stop | Number | 表示渐变点在起点和终点中的位置，范围 0 ～ 1。 |
| color | String | 渐变点颜色。 |
