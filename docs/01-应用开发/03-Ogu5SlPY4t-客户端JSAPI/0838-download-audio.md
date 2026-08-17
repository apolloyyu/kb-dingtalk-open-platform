---
title: "下载音频"
source_url: "https://open.dingtalk.com/document/development/download-audio"
namespace: "development"
slug: "download-audio"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 下载音频"
doc_id: "McmWDbOLEs"
updated_at: "2025-09-17 20:57:02"
---

> Source: https://open.dingtalk.com/document/development/download-audio
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 音频 > 下载音频
> Updated: 2025-09-17 20:57:02

# 下载音频

调用**device.audio.download**下载音频。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=device.audio.download)在线调试该接口。

## 使用说明

使用 `dd.device.audio.stopRecord` 或者 `dd.device.audio.onRecordEnd` 获取的MediaId下载音频资源。下载完成后返回音频在本地的MediaId。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.device.audio.download({
    mediaId : "@lATOCLhLfc46kUl8zlUmRlM",
    onSuccess : function(res) {
        res.localAudioId;
    },
    onFail : function (err) {
    }
});
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| mediaId | String | 音频在服务端的标识。 |
