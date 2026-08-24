---
title: "setKeepScreenOn"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-keep-screen-on"
namespace: "development"
slug: "jsapi-set-keep-screen-on"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 屏幕亮度 > setKeepScreenOn"
doc_id: "sFRYiX3Zf3"
updated_at: "2025-08-27 18:08:07"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-keep-screen-on
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 屏幕亮度 > setKeepScreenOn
> Updated: 2025-08-27 18:08:07

# setKeepScreenOn

调用setKeepScreenOn，设置屏幕常亮。

注意：H5容器关闭后自动失效。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 5.1.26 | 5.1.26 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11622) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11622) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `isKeep`（boolean，必填）：是否保持常亮，默认值false。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.setKeepScreenOn({
  isKeep: true,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
