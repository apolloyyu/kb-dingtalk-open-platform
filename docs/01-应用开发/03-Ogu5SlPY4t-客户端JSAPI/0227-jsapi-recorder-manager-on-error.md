---
title: "RecorderManager.onerror"
source_url: "https://open.dingtalk.com/document/development/jsapi-recorder-manager-on-error"
namespace: "development"
slug: "jsapi-recorder-manager-on-error"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 录音 > RecorderManager.onerror"
doc_id: "c89mdmnjvE"
updated_at: "2025-08-27 18:06:43"
---

> Source: https://open.dingtalk.com/document/development/jsapi-recorder-manager-on-error
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 录音 > RecorderManager.onerror
> Updated: 2025-08-27 18:06:43

# RecorderManager.onerror

录音管理监听错误。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10238) |

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

### 入参

- `error`（number，必填）：错误码。
- `errMsg`（string，必填）：错误信息。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
const recorderManager = dd.getRecorderManager();

recorderManager.onerror = (err) => {
  dd.alert({ content: 'onerror' });
};
```

`success`返回对象示例：

```
{ "error": 3, "errMsg": "编码器创建失败" }
```
