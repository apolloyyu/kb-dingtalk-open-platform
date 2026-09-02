---
title: "translateVoice"
source_url: "https://open.dingtalk.com/document/development/jsapi-translate-voice"
namespace: "development"
slug: "jsapi-translate-voice"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 录音 > translateVoice"
doc_id: "f4ExxGk8ci"
updated_at: "2025-08-27 18:06:41"
---

> Source: https://open.dingtalk.com/document/development/jsapi-translate-voice
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 录音 > translateVoice
> Updated: 2025-08-27 18:06:41

# translateVoice

调用translateVoice。语音转文字。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11640) |
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

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `mediaId`（string，必填）：要转换的语音的mediaId。
- `duration`（number，必填）：语音的时长，单位：秒。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `mediaId`（string，必填）：转换的语音的mediaId。
- `content`（string，必填）：语音转换的文字内容。

## **示例****代码**

### 默认出入参

```
dd.translateVoice({
  mediaId: '@lATOCLhLfc46kUl8zlUmRlM',
  duration: 5,
  success: (res) => {
    const { content, mediaId } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "content": "content示例值", "mediaId": "@lATOCLhLfc46kUl8zlUmRlM" }
```
