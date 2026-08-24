---
title: "CanvasContext.addColorStop"
source_url: "https://open.dingtalk.com/document/development/jsapi-canvas-context-add-color-stop"
namespace: "development"
slug: "jsapi-canvas-context-add-color-stop"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 画布 > CanvasContext.addColorStop"
doc_id: "1MktoBUVKm"
updated_at: "2025-08-27 18:05:28"
---

> Source: https://open.dingtalk.com/document/development/jsapi-canvas-context-add-color-stop
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 画布 > CanvasContext.addColorStop
> Updated: 2025-08-27 18:05:28

# CanvasContext.addColorStop

调用CanvasContext.addColorStop，创建渐变点。

> - 小于最小 stop 的部分会按最小 stop 的 color 来渲染，大于最大 stop 的部分会按最大 stop 的 color 来渲染。
> - 需要使用 addColorStop()来指定渐变点，至少需要两个。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11579) |

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

- `stop`（number，必填）：表示渐变点在起点和终点中的位置，范围 0 ～ 1。
- `color`（string，必填）：渐变点颜色。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.CanvasContext.addColorStop({
  stop: 0,
  color: 'orange',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
