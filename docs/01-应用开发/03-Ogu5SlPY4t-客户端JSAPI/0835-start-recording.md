---
title: "开始录音"
source_url: "https://open.dingtalk.com/document/development/start-recording"
namespace: "development"
slug: "start-recording"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 开始录音"
doc_id: "MzLCoRzgFA"
updated_at: "2025-09-17 20:57:00"
---

> Source: https://open.dingtalk.com/document/development/start-recording
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 开始录音
> Updated: 2025-09-17 20:57:00

# 开始录音

调用**device.audio.startRecord**开始录音。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.startRecord)在线调试该接口。

## 使用说明

启动语音录制。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.startRecord({
    onSuccess : function () {//支持最长为300秒（包括）的音频录制，默认60秒(包括)。
    },
    onFail : function (err) {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| maxDuration | Number | 可选参数，录音最大时长，单位：秒，必须为整数，范围[1,300]。 |
