---
title: "playAudio"
source_url: "https://open.dingtalk.com/document/development/jsapi-play-audio"
namespace: "development"
slug: "jsapi-play-audio"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 录音 > playAudio"
doc_id: "sXwYpznzvc"
updated_at: "2025-08-27 18:06:38"
---

> Source: https://open.dingtalk.com/document/development/jsapi-play-audio
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 录音 > playAudio
> Updated: 2025-08-27 18:06:38

# playAudio

调用playAudio，播放语音。

播放音频，在播放语音前可以使用`startRecord`开启录音，通过`stopRecord`、`onRecordEnd`获取录制的音频的`MediaId`或者通过`downloadAudio`下载服务端音频资源获取`localAudioId`。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11920) |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `localAudioId`（string，必填）：音频在设备本地的标识。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认Demo标题

```
dd.playAudio({
  localAudioId: 'localAudioId示例值',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
