---
title: "语音转文字"
source_url: "https://open.dingtalk.com/document/development/voice-to-text"
namespace: "development"
slug: "voice-to-text"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 语音转文字"
doc_id: "dAPW1lE7hC"
updated_at: "2025-09-17 20:57:03"
---

> Source: https://open.dingtalk.com/document/development/voice-to-text
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 语音转文字
> Updated: 2025-09-17 20:57:03

# 语音转文字

调用**device.audio.translateVoice**语音转文字。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.translateVoice)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.translateVoice({
    mediaId : "@lATOCLhLfc46kUl8zlUmRlM",
    duration : 5.0,
    onSuccess : function (res) {
        res.mediaId; // 转换的语音的mediaId
        res.content; // 语音转换的文字内容
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| mediaId | String | 要转换的语音的mediaId。 |
| duration | Number | 语音的时长，单位：秒. |
