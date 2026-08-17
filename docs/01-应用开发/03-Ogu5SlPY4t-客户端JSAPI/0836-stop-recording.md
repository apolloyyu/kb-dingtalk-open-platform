---
title: "停止录音"
source_url: "https://open.dingtalk.com/document/development/stop-recording"
namespace: "development"
slug: "stop-recording"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 停止录音"
doc_id: "VTXH8zjDcL"
updated_at: "2025-09-17 20:57:00"
---

> Source: https://open.dingtalk.com/document/development/stop-recording
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 停止录音
> Updated: 2025-09-17 20:57:00

# 停止录音

调用**device.audio.stopRecord**停止录音。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.stopRecord)在线调试该接口。

## 使用说明

停止语音录制，同时将录制的语音上传到服务端，返回音频资源的MediaID。返回的MediaID，可用于本地播放和音频下载。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.stopRecord({
    onSuccess : function(res){
        res.mediaId; // 返回音频的MediaID，可用于本地播放和音频下载
        res.duration; // 返回音频的时长，单位：秒
    },
    onFail : function (err) {
    }
});
```
