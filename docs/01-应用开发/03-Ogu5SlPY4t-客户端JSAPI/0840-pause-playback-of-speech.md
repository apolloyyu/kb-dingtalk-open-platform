---
title: "暂停播放语音"
source_url: "https://open.dingtalk.com/document/development/pause-playback-of-speech"
namespace: "development"
slug: "pause-playback-of-speech"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 暂停播放语音"
doc_id: "f7XvnlJBqX"
updated_at: "2025-09-17 20:57:03"
---

> Source: https://open.dingtalk.com/document/development/pause-playback-of-speech
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 暂停播放语音
> Updated: 2025-09-17 20:57:03

# 暂停播放语音

调用**device.audio.pause**暂停播放语音。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.pause)在线调试该接口。

## 使用说明

暂停正在播放的语音。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.pause({
    localAudioId : "localAudioId",
    onSuccess : function() {
    },
    onFail : function(err) {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| localAudioId | String | 正在播放的音频的本地标识。 |
