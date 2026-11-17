---
title: "vibrate"
source_url: "https://open.dingtalk.com/document/development/jsapi-vibrate"
namespace: "development"
slug: "jsapi-vibrate"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 振动 > vibrate"
doc_id: "MiOhqgQZNt"
updated_at: "2025-08-27 18:07:44"
---

> Source: https://open.dingtalk.com/document/development/jsapi-vibrate
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 振动 > vibrate
> Updated: 2025-08-27 18:07:44

# vibrate

调用vibrate使用振动功能。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10150) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10150) |

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
dd.vibrate({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
