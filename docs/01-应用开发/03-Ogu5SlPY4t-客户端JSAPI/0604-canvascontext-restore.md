---
title: "恢复绘图上下文(restore)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-restore"
namespace: "development"
slug: "canvascontext-restore"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 恢复绘图上下文(restore)"
doc_id: "uPvzUHjIrU"
updated_at: "2025-09-17 20:59:43"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-restore
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 恢复绘图上下文(restore)
> Updated: 2025-09-17 20:59:43

# 恢复绘图上下文(restore)

调用**CanvasContext.restore**恢复之前保存的绘图上下文。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');

ctx.save();
ctx.setFillStyle('red');
ctx.fillRect(20, 20, 250, 80);

ctx.restore();
ctx.fillRect(60, 60, 155, 130);

ctx.draw();
```
