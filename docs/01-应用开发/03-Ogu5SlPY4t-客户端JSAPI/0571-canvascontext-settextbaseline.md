---
title: "文本基线（setTextBaseline）"
source_url: "https://open.dingtalk.com/document/development/canvascontext-settextbaseline"
namespace: "development"
slug: "canvascontext-settextbaseline"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 文本基线（setTextBaseline）"
doc_id: "QKwhUreLLH"
updated_at: "2025-09-17 20:59:26"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-settextbaseline
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 文本基线（setTextBaseline）
> Updated: 2025-09-17 20:59:26

# 文本基线（setTextBaseline）

**textBaseline**是 Canvas 2D API 描述绘制文本时，当前文本基线的属性。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.setTextBaseline("top");
ctx.fillText("Hello world", 0, 100);
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| textBaseline | String | 枚举 "top" "hanging" "middle""alphabetic" "ideographic" "bottom"。 |
