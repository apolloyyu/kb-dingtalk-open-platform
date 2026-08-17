---
title: "停止播放音频"
source_url: "https://open.dingtalk.com/document/development/stop-audio-playback"
namespace: "development"
slug: "stop-audio-playback"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 停止播放音频"
doc_id: "djroXndWvI"
updated_at: "2025-09-17 20:57:05"
---

> Source: https://open.dingtalk.com/document/development/stop-audio-playback
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 停止播放音频
> Updated: 2025-09-17 20:57:05

# 停止播放音频

调用**device.audio.stop**停止播放音频。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.stop)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.stop({
    localAudioId : "localAudioId",
    onSuccess : function (res) {
    },
    onFail : function () {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| localAudioId | String | 处于播放或者暂停状态的语音的本地标识。 |
