---
title: "navigateBackMiniProgram"
source_url: "https://open.dingtalk.com/document/development/jsapi-navigate-back-mini-program"
namespace: "development"
slug: "jsapi-navigate-back-mini-program"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 跳转 > navigateBackMiniProgram"
doc_id: "4St0ac8Bbk"
updated_at: "2025-08-27 18:06:28"
---

> Source: https://open.dingtalk.com/document/development/jsapi-navigate-back-mini-program
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 跳转 > navigateBackMiniProgram
> Updated: 2025-08-27 18:06:28

# navigateBackMiniProgram

调用navigateBackMiniProgram，返回到上一个钉钉小程序。

> 只有使用跳转到另一个钉钉小程序方法（navigateToMiniProgram）跳转的目标小程序，才可以调用本接口返回上一个小程序。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10191) |

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

- `extraData`（object，必填）：需要传递给目标小程序的数据，目标小程序可在App.onLaunch()或App.onShow()方法中获取到这份数据。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.navigateBackMiniProgram({
  extraData: { data1: 'test' },
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
