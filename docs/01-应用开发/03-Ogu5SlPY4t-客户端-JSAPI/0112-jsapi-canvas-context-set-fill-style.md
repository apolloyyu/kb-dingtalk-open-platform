---
title: "CanvasContext.setFillStyle"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-set-fill-style"
namespace: "development"
slug: "jsapi-canvas-context-set-fill-style"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.setFillStyle"
doc_id: "VAs6ORZmA2"
updated_at: "2025-08-27 18:05:43"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-set-fill-style
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.setFillStyle
> Updated: 2025-08-27 18:05:43

# CanvasContext.setFillStyle

调用CanvasContext.setFillStyle设置填充色。

> 如果没有设置 fillStyle，则默认颜色为 black。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10105) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### color

- `color`（string）：颜色，如：blue，Hex，格式：#000000。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.setFillStyle({
  color: '#000000',
});
```
