---
title: "缩放(scale)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-scale"
namespace: "development"
slug: "canvascontext-scale"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 缩放(scale)"
doc_id: "wHQxjHbk3a"
updated_at: "2025-09-17 20:59:39"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-scale
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 缩放(scale)
> Updated: 2025-09-17 20:59:39

# 缩放(scale)

在调用scale方法后，之后创建的路径其横纵坐标会被缩放。多次调用scale，倍数会相乘。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.strokeRect(15, 15, 30, 25);
ctx.scale(3, 3);
ctx.strokeRect(15, 15, 30, 25);
ctx.scale(3, 3);
ctx.strokeRect(15, 15, 30, 25);

ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| scaleWidth | Number | 横坐标缩放倍数 (1 = 100%，0.5 = 50%，2 = 200%)。 |
| scaleHeight | Number | 纵坐标轴缩放倍数 (1 = 100%，0.5 = 50%，2 = 200%)。 |
