---
title: "将像素数据绘制到画布(putImageData)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-putimagedata"
namespace: "development"
slug: "canvascontext-putimagedata"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 将像素数据绘制到画布(putImageData)"
doc_id: "JHQztB1L7L"
updated_at: "2025-09-17 20:59:44"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-putimagedata
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 将像素数据绘制到画布(putImageData)
> Updated: 2025-09-17 20:59:44

# 将像素数据绘制到画布(putImageData)

调用CanvasContext.putImageData将像素数据绘制到画布。

> **[!IMPORTANT]**
>
> 使用 dd.canIUse('createCanvasContext.putImageData') 进行可用性判断。

## **示例****代码**

```
const data = new Uint8ClampedArray([255, 0, 0, 1])
const ctx = dd.createCanvasContext('canvas')

ctx.putImageData({
    x: 0,
    y: 0,
    width: 1,
    height: 1,
    data: data,
    success(res) {}
})
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8ClampedArray | 是 | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba。 |
| x | Number | 是 | 源图像数据在目标画布中的位置偏移量（x 轴方向的偏移量）。 |
| y | Number | 是 | 源图像数据在目标画布中的位置偏移量（y 轴方向的偏移量）。 |
| width | Number | 是 | 源图像数据矩形区域的宽度 。 |
| height | Number | 是 | 源图像数据矩形区域的高度。 |
| success | Function | 否 | 成功回调。 |
| fail | Function | 否 | 失败回调。 |
| complete | Function | 否 | 完成回调。 |
