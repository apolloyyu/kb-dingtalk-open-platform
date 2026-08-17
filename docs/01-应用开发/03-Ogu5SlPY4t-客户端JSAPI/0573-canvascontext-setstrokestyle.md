---
title: "设置边框颜色(setStrokeStyle)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setstrokestyle"
namespace: "development"
slug: "canvascontext-setstrokestyle"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置边框颜色(setStrokeStyle)"
doc_id: "fNxgjZC8Za"
updated_at: "2025-09-17 20:59:27"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setstrokestyle
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置边框颜色(setStrokeStyle)
> Updated: 2025-09-17 20:59:27

# 设置边框颜色(setStrokeStyle)

调用**CanvasContext.setStrokeStyle**设置边框颜色。

> **[!NOTE]**
>
> 如果没有设置 `strokeStyle`，则默认颜色为 `black`。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setStrokeStyle('blue');
ctx.strokeRect(50, 50, 100, 175);
ctx.draw();
```

## **入参说明**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| color | String | 颜色，如：blue，Hex格式：#000000。 |
