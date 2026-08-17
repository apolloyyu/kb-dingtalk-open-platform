---
title: "设置填充色(setFillStyle)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setfillstyle"
namespace: "development"
slug: "canvascontext-setfillstyle"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置填充色(setFillStyle)"
doc_id: "0ZHmT64fWC"
updated_at: "2025-09-17 20:59:26"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setfillstyle
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置填充色(setFillStyle)
> Updated: 2025-09-17 20:59:26

# 设置填充色(setFillStyle)

调用**CanvasContext.setFillStyle**设置填充色。

> **[!NOTE]**
>
> 如果没有设置 `fillStyle`，则默认颜色为 `black`。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setFillStyle('blue');
ctx.fillRect(50, 50, 100, 175);
ctx.draw();
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| color | String | 颜色，如：blue，Hex格式：#000000。 |
