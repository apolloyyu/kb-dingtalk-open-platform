---
title: "顺时针旋转(rotate)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-rotate"
namespace: "development"
slug: "canvascontext-rotate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 顺时针旋转(rotate)"
doc_id: "z58qtTongu"
updated_at: "2025-09-17 20:59:39"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-rotate
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 顺时针旋转(rotate)
> Updated: 2025-09-17 20:59:39

# 顺时针旋转(rotate)

以原点为中心（原点可以用translate方法修改），顺时针旋转当前坐标轴。多次调用rotate，旋转的角度会叠加。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.strokeRect(200, 20, 180, 150);
ctx.rotate(30 * Math.PI / 180);
ctx.strokeRect(200, 20, 180, 150);
ctx.rotate(30 * Math.PI / 180);
ctx.strokeRect(200, 20, 180, 150);

ctx.draw();
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| rotate | Number | 旋转角度，以弧度计(degrees \* Math.PI/180；degrees 范围为0~360)。 |
