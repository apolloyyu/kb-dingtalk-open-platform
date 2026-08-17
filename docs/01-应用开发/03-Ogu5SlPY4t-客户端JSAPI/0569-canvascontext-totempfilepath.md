---
title: "把画布内容导出成图片(toTempFilePath)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-totempfilepath"
namespace: "development"
slug: "canvascontext-totempfilepath"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 把画布内容导出成图片(toTempFilePath)"
doc_id: "AHNDejOSWA"
updated_at: "2025-09-17 20:59:25"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-totempfilepath
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 把画布内容导出成图片(toTempFilePath)
> Updated: 2025-09-17 20:59:25

# 把画布内容导出成图片(toTempFilePath)

使用**CanvasContext.toTempFilePath**把当前画布的内容导出生成图片，并返回文件路径。

## **示例代码**

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.toTempFilePath({
  success() {},
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| x | Number | 否 | 画布 x 轴起点。  **默认值**： 0。 |
| y | Number | 否 | 画布 y 轴起点。  **默认值**： 0。 |
| width | Number | 否 | 画布宽度。  **默认值**：canvas 宽度 - x。 |
| height | Number | 否 | 画布高度。  **默认值**：canvas 高度 - y。 |
| destWidth | Number | 否 | 输出的图片宽度。  **默认值**：width。 |
| destHeight | Number | 否 | 输出的图片高度。  **默认值**：height。 |
| success | Function | 否 | 接口成功回调。 |
| fail | Function | 否 | 接口失败回调。 |
| complete | Function | 否 | 接口完成回调。 |
