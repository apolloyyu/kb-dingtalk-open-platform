---
title: "BackgroundAudioManager.play"
source_url: "https://open.dingtalk.com/document/development/jsapi-background-audio-manager-play"
namespace: "development"
slug: "jsapi-background-audio-manager-play"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 音频 > BackgroundAudioManager.play"
doc_id: "KIFYvO117g"
updated_at: "2025-08-27 18:07:01"
---

> Source: https://open.dingtalk.com/document/development/jsapi-background-audio-manager-play
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 音频 > BackgroundAudioManager.play
> Updated: 2025-08-27 18:07:01

# BackgroundAudioManager.play

播放背景音乐

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10223) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const backgroundAudioManager = dd.getBackgroundAudioManager();
backgroundAudioManager.src = 'http://music.xxxx/url?id=317151.mp3';
backgroundAudioManager.title = 'abc';
backgroundAudioManager.coverImgUrl =
  'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg';
backgroundAudioManager.play();
```
