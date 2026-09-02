---
title: "navigateBackPage"
source_url: "https://open.dingtalk.com/document/development/jsapi-navigate-back-page"
namespace: "development"
slug: "jsapi-navigate-back-page"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 跳转 > navigateBackPage"
doc_id: "G55cT5sgPU"
updated_at: "2025-08-27 18:06:27"
---

> Source: https://open.dingtalk.com/document/development/jsapi-navigate-back-page
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 跳转 > navigateBackPage
> Updated: 2025-08-27 18:06:27

# navigateBackPage

调用navigateBackPage，返回上一个应用。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.5.45 | 6.5.45 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11690) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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

- `extraData`（object）：返回上一个应用携带的参数，返回的目标H5微应用可在[页面resume事件的回调监听](https://open.dingtalk.com/document/orgapp/page-event-monitoring#title-3eu-h6b-5g0)中获取携带的参数。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.navigateBackPage({
  extraData: {},
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
