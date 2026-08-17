---
title: "获取canvas区域隐含的像素数据(getImageData)"
source_url: "https://open.dingtalk.com/document/development/canvascontext-getimagedata"
namespace: "development"
slug: "canvascontext-getimagedata"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > 获取canvas区域隐含的像素数据(getImageData)"
doc_id: "5iYBzRpGcF"
updated_at: "2025-09-17 20:59:44"
---

> Source: https://open.dingtalk.com/document/development/canvascontext-getimagedata
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > 获取canvas区域隐含的像素数据(getImageData)
> Updated: 2025-09-17 20:59:44

# 获取canvas区域隐含的像素数据(getImageData)

调用**CanvasContext.getImageData**获取canvas区域隐含的像素数据。

> **[!IMPORTANT]**
>
> 使用 dd.canIUse('createCanvasContext.getImageData') 进行可用性判断。

## **示例****代码**

```
const ctx = dd.createCanvasContext('canvas')

ctx.getImageData({
  x: 0,
  y: 0,
  width: 100,
  height: 100,
  success(res) {
    console.log(res.width) // 100
    console.log(res.height) // 100
    console.log(res.data instanceof Uint8ClampedArray) // true
    console.log(res.data.length) // 100 * 100 * 4
  }
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| x | Number | 是 | 将要被提取的图像数据矩形区域的左上角横坐标。 |
| y | Number | 是 | 将要被提取的图像数据矩形区域的左上角纵坐标。 |
| width | Number | 是 | 将要被提取的图像数据矩形区域的宽度。 |
| height | Number | 是 | 将要被提取的图像数据矩形区域的高度。 |
| success | Function | 否 | 成功回调。 |
| fail | Function | 否 | 失败回调。 |
| complete | Function | 否 | 完成回调。 |

**success 回调**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| width | Number | 图像数据矩形的宽度。 |
| height | Number | 图像数据矩形的高度。 |
| data | Uunt8ClampedArray | 图像像素点数据，一维数组，每四项表示一个像素点的 rgba。 |
