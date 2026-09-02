---
title: "stopRecord"
source_url: "https://open.dingtalk.com/document/development/jsapi-stop-record"
namespace: "development"
slug: "jsapi-stop-record"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 录音 > stopRecord"
doc_id: "06gn7YtdFE"
updated_at: "2025-08-27 18:06:39"
---

> Source: https://open.dingtalk.com/document/development/jsapi-stop-record
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 录音 > stopRecord
> Updated: 2025-08-27 18:06:39

# stopRecord

调用stopRecord，停止录音。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11701) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.stopRecord({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
