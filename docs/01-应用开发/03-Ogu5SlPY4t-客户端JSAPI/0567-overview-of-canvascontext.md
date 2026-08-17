---
title: "CanvasContext概览"
source_url: "https://open.dingtalk.com/document/development/overview-of-canvascontext"
namespace: "development"
slug: "overview-of-canvascontext"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 画布 > CanvasContext概览"
doc_id: "Ub1CqPCwKM"
updated_at: "2025-09-17 20:59:24"
---

> Source: https://open.dingtalk.com/document/development/overview-of-canvascontext
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 画布 > CanvasContext概览
> Updated: 2025-09-17 20:59:24

# CanvasContext概览

| **方法** | **说明** |
| --- | --- |
| CanvasContext.toTempFilePath | 把当前画布的内容导出生成图片，并返回文件路径。 |
| CanvasContext.setTextAlign | Canvas 2D API 描述绘制文本时，文本的对齐方式的属性。 |
| CanvasContext.setTextBaseline | Canvas 2D API 描述绘制文本时，当前文本基线的属性。 |
| CanvasContext.setFillStyle | 设置填充色。 |
| CanvasContext.setStrokeStyle | 设置边框颜色。 |
| CanvasContext.setShadow | 设置阴影样式。 |
| CanvasContext.createLinearGradient | 创建一个线性的渐变色。 |
| CanvasContext.createCircularGradient | 创建一个圆形的渐变色。起点在圆心，终点在圆环。 |
| CanvasContext.addColorStop | 创建一个圆形的渐变色。 |
| CanvasContext.setLineWidth | 设置线条的宽度。 |
| CanvasContext.setLineCap | 设置线条的端点样式。 |
| CanvasContext.setLineJoin | 设置线条的交点样式。 |
| CanvasContext.setMiterLimit | 设置最大斜接长度。 |
| CanvasContext.rect | 创建二次贝塞尔曲线路径。 |
| CanvasContext.fillRect | 填充矩形。 |
| CanvasContext.strokeRect | 画一个矩形（非填充）。 |
| CanvasContext.clearRect | 清除画布上在该矩形区域内的内容。 |
| CanvasContext.fill | 对当前路径中的内容进行填充。 |
| CanvasContext.stroke | 画出当前路径的边框。默认 black。 |
| CanvasContext.beginPath | 开始创建一个路径，需要调用 fill 或者 stroke 才会使用路径进行填充或描边。 |
| CanvasContext.closePath | 关闭一个路径。 |
| CanvasContext.moveTo | 把路径移动到画布中的指定点，不创建线条。 |
| CanvasContext.lineTo | 增加一个新点，然后创建一条从上次指定点到目标点的线。 |
| CanvasContext.arc | 画一条弧线。 |
| CanvasContext.bezierCurveTo | 创建三次方贝塞尔曲线路径。 |
| CanvasContext.clip | 将当前创建的路径设置为当前剪切路径。 |
| CanvasContext.quadraticCurveTo | 创建二次贝塞尔曲线路径。 |
| CanvasContext.scale | 在调用scale方法后，之后创建的路径其横纵坐标会被缩放。多次调用scale，倍数会相乘。 |
| CanvasContext.rotate | 以原点为中心，原点可以用 translate 方法修改。顺时针旋转当前坐标轴。多次调用rotate，旋转的角度会叠加。 |
| CanvasContext.translate | 对当前坐标系的原点(0, 0)进行变换，默认的坐标系原点为页面左上角。 |
| CanvasContext.setFontSize | 设置字体大小。 |
| CanvasContext.fillText | 在画布上绘制被填充的文本。 |
| CanvasContext.drawImage | 绘制图像，图像保持原始尺寸。 |
| CanvasContext.setGlobalAlpha | 设置全局画笔透明度。 |
| CanvasContext.save | 保存当前的绘图上下文。 |
| CanvasContext.restore | 恢复之前保存的绘图上下文。 |
| CanvasContext.draw | 将之前在绘图上下文中的描述（路径、变形、样式）画到 canvas 中。 |
| CanvasContext.getImageData | 获取 canvas 区域隐含的像素数据。 |
| CanvasContext.putImageData | 将像素数据绘制到画布。 |
