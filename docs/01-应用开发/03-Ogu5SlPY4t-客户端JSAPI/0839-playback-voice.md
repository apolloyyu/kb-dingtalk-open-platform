---
title: "播放语音"
source_url: "https://open.dingtalk.com/document/development/playback-voice"
namespace: "development"
slug: "playback-voice"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 播放语音"
doc_id: "WtolCY4aT4"
updated_at: "2025-09-17 20:57:02"
---

> Source: https://open.dingtalk.com/document/development/playback-voice
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 播放语音
> Updated: 2025-09-17 20:57:02

# 播放语音

调用**device.audio.play**播放语音。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.play)在线调试该接口。

## 使用说明

播放音频，在播放语音前可以使用`dd.device.audio.startRecord`开启录音，通过`dd.device.audio.stopRecord`、`dd.device.audio.onRecordEnd`获取录制的音频的MediaId或者通过`dd.device.audio.download`下载服务端音频资源获取localAudioId。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.play({
    localAudioId : "localAudioId",
 
    onSuccess : function () {
 
    },
 
    onFail : function (err) {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| localAudioId | String | 音频在设备本地的标识。 |
