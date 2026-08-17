---
title: "设置为剪切路径(clip)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-clip"
namespace: "development"
slug: "canvascontext-clip"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置为剪切路径(clip)"
doc_id: "8mOQ9ehS0T"
updated_at: "2025-09-17 20:59:38"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-clip
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 设置为剪切路径(clip)
> Updated: 2025-09-17 20:59:38

# 设置为剪切路径(clip)

调用**CanvasContext.clip**将当前创建的路径设置为当前剪切路径。

## **示例****代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas')
dd.downloadFile({
  url: 'https://gw.dingding.com/zos/skylark-tools/public/files/dda114e320567e1d304790287d75a029.png',
  success: function(res) {
    ctx.save();
    ctx.beginPath();
    ctx.arc(50, 50, 25, 0, 2*Math.PI);
    ctx.clip();
    ctx.drawImage(res.tempFilePath, 25, 25);
    ctx.restore();
    ctx.draw();
  }
})
```
