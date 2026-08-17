---
title: "设置字体大小(setFontSize)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-setfontsize"
namespace: "development"
slug: "canvascontext-setfontsize"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置字体大小(setFontSize)"
doc_id: "daALcEXfGo"
updated_at: "2025-09-17 20:59:41"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-setfontsize
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置字体大小(setFontSize)
> Updated: 2025-09-17 20:59:41

# 设置字体大小(setFontSize)

调用**CanvasContext.setFontSize**设置字体大小。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas')；

ctx.setFontSize(14)；
ctx.fillText('14', 20, 20)；；；
ctx.setFontSize(22)
ctx.fillText('22', 40, 40)
ctx.setFontSize(30)；
ctx.fillText('30', 60, 60)；
ctx.setFontSize(38)；
ctx.fillText('38', 90, 90)；

ctx.draw()；
```

## **入参**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| fontSize | Number | 字号。 |
