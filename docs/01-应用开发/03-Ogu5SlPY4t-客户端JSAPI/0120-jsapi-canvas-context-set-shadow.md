---
title: "CanvasContext.setShadow"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-set-shadow"
namespace: "development"
slug: "jsapi-canvas-context-set-shadow"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.setShadow"
doc_id: "NmOUPodi2k"
updated_at: "2025-08-27 18:05:44"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-set-shadow
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.setShadow
> Updated: 2025-08-27 18:05:44

# CanvasContext.setShadow

调用CanvasContext.setShadow，设置阴影样式。

> 如果没有设置，offsetX 的默认值为 0， offsetY 的默认值为 0， blur 的默认值为 0，color 的默认值为 black。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10112) |

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

### 入参

- `offsetX`（number）：阴影相对于形状水平方向的偏移。
- `offsetY`（number）：阴影相对于形状竖直方向的偏移。
- `blur`（number）：阴影的模糊级别，值越大越模糊，范围 0~100。
- `color`（string）：阴影颜色。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.setShadow({
  blur: 0,
  color: '#ffffff',
  offsetX: 0,
  offsetY: 0,
});
```
