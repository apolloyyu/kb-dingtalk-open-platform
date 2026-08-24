---
title: "setScreenBrightness"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-screen-brightness"
namespace: "development"
slug: "jsapi-set-screen-brightness"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 屏幕亮度 > setScreenBrightness"
doc_id: "RD2oIM7XrM"
updated_at: "2025-10-21 16:38:39"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-screen-brightness
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 屏幕亮度 > setScreenBrightness
> Updated: 2025-10-21 16:38:39

# setScreenBrightness

调用setScreenBrightness，设置屏幕亮度。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11624) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11624) |

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

- `brightness`（number，必填）：屏幕亮度，取值范围0-1.0。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
dd.setScreenBrightness({
  brightness: 0.5,
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{}
```
