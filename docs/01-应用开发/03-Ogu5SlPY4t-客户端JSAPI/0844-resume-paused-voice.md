---
title: "恢复暂停播放的语音"
source_url: "https://open.dingtalk.com/document/development/resume-paused-voice"
namespace: "development"
slug: "resume-paused-voice"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 恢复暂停播放的语音"
doc_id: "oHqyb5ICbW"
updated_at: "2025-09-17 20:57:05"
---

> Source: https://open.dingtalk.com/document/development/resume-paused-voice
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 恢复暂停播放的语音
> Updated: 2025-09-17 20:57:05

# 恢复暂停播放的语音

调用**device.audio.resume**恢复暂停播放的语音。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.resume)在线调试该接口。

## 使用说明

恢复播放处于暂停状态的语音。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.resume({
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
| localAudioId | String | 处于暂停状态的语音的本地标识。 |
