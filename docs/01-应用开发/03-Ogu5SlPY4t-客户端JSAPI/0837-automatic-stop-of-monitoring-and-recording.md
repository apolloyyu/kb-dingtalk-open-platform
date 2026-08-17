---
title: "监听录音自动停止"
source_url: "https://open.dingtalk.com/document/development/automatic-stop-of-monitoring-and-recording"
namespace: "development"
slug: "automatic-stop-of-monitoring-and-recording"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 监听录音自动停止"
doc_id: "OxcR4wnkpP"
updated_at: "2025-09-17 20:57:01"
---

> Source: https://open.dingtalk.com/document/development/automatic-stop-of-monitoring-and-recording
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 监听录音自动停止
> Updated: 2025-09-17 20:57:01

# 监听录音自动停止

调用**device.audio.onRecordEnd**监听录音自动停止。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.onRecordEnd)在线调试该接口。

## 使用说明

当语音录制时间超过60秒时，钉钉会自动停止语音录制，同时将录制的语音上传到服务端，返回音频资源的MediaID。推荐在调用 `dd.device.audio.startRecord` 前设置监听录音自动停止的回调。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.onRecordEnd({
    onSuccess : function(res) {
        res.mediaId; // 停止播放音频MediaID
        res.duration; // 返回音频的时长，单位：秒
    },
    onFail : function (err) {
 
    }
});
```
