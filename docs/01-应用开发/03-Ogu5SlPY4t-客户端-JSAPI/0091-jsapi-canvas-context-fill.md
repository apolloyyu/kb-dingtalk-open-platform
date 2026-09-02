---
title: "CanvasContext.fill"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-fill"
namespace: "development"
slug: "jsapi-canvas-context-fill"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.fill"
doc_id: "h9ef5NXmf8"
updated_at: "2025-08-27 18:05:34"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-fill
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.fill
> Updated: 2025-08-27 18:05:34

# CanvasContext.fill

调用CanvasContext.fill，对当前路径中的内容进行填充。默认的填充色为黑色。

> 如果当前路径没有闭合，fill() 方法会将起点和终点进行连接，然后填充，详情见示例代码一。
> fill() 填充的的路径是从 beginPath() 开始计算，但是不会将 fillRect() 包含进去，详情见示例代码二。

示例代码一：

```
const ctx = dd.createCanvasContext('awesomeCanvas')
ctx.moveTo(20, 20)
ctx.lineTo(200, 20)
ctx.lineTo(200, 200)
ctx.fill()
ctx.draw( 
)
```

示例代码二：

```
const ctx = dd.createCanvasContext('awesomeCanvas');
ctx.rect(20, 20, 110, 40);
ctx.setFillStyle('blue');
ctx.fill();

ctx.beginPath();
ctx.rect(20, 30, 150, 40);
ctx.setFillStyle('yellow');
ctx.fillRect(20, 80, 150, 40);
ctx.rect(20, 150, 150, 40);
ctx.setFillStyle('red');
ctx.fill();
ctx.draw();
```

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.fill({});
```
