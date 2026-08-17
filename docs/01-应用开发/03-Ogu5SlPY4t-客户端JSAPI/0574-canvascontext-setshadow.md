---
title: "设置阴影样式(setShadow)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setshadow"
namespace: "development"
slug: "canvascontext-setshadow"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置阴影样式(setShadow)"
doc_id: "tmZCIlHlRI"
updated_at: "2025-09-17 20:59:27"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setshadow
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置阴影样式(setShadow)
> Updated: 2025-09-17 20:59:27

# 设置阴影样式(setShadow)

调用**CanvasContext.setShadow**设置阴影样式。

> **[!NOTE]**
>
> 如果没有设置，`offsetX` 的默认值为 0， `offsetY` 的默认值为 0， `blur` 的默认值为 0，`color` 的默认值为 `black`。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setStrokeStyle('blue');
ctx.strokeRect(50, 50, 100, 175);
ctx.draw();
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| offsetX | Number | 阴影相对于形状水平方向的偏移。 |
| offsetY | Number | 阴影相对于形状竖直方向的偏移。 |
| blur | Number | 阴影的模糊级别，值越大越模糊，范围 0~100。 |
| color | String | 阴影颜色。 |
