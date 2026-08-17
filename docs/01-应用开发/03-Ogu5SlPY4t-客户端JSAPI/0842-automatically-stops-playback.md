---
title: "监听播放自动停止"
source_url: "https://open.dingtalk.com/document/development/automatically-stops-playback"
namespace: "development"
slug: "automatically-stops-playback"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 监听播放自动停止"
doc_id: "WvvBFbqiey"
updated_at: "2025-09-17 20:57:04"
---

> Source: https://open.dingtalk.com/document/development/automatically-stops-playback
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 监听播放自动停止
> Updated: 2025-09-17 20:57:04

# 监听播放自动停止

调用**device.audio.onPlayEnd**监听播放自动停止。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.onPlayEnd)在线调试该接口。

## 使用说明

语音播放完毕时自动调用该方法设置的回调，并返回音频的的本地标识。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.onPlayEnd({
    onSuccess : function (res) {
        res.localAudioId;
    },
    onFail : function (err) {
    }
});
```
