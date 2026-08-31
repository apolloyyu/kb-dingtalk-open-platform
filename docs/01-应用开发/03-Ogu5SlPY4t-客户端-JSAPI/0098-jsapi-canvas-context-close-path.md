---
title: "CanvasContext.closePath"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-close-path"
namespace: "development"
slug: "jsapi-canvas-context-close-path"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.closePath"
doc_id: "NSgFaxzJsj"
updated_at: "2025-08-27 18:05:31"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-close-path
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.closePath
> Updated: 2025-08-27 18:05:31

# CanvasContext.closePath

调用CanvasContext.closePath，关闭一个路径。

> 关闭路径会连接起点和终点。
> 如果关闭路径后没有调用 fill() 或者 stroke() 并开启了新的路径，那之前的路径将不会被渲染。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10087) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.closePath();
```

`success`返回对象示例：

```
{}
```
