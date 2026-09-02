---
title: "BackgroundAudioManager.stop"
source_url: "https://open.dingtalk.com/document/development/jsapi-background-audio-manager-stop"
namespace: "development"
slug: "jsapi-background-audio-manager-stop"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 音频 > BackgroundAudioManager.stop"
doc_id: "Xi7F8RCe5O"
updated_at: "2025-08-27 18:07:02"
---

> Source: https://open.dingtalk.com/document/development/jsapi-background-audio-manager-stop
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 音频 > BackgroundAudioManager.stop
> Updated: 2025-08-27 18:07:02

# BackgroundAudioManager.stop

停止播放背景音乐

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10225) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 否 |
| 第三方企业应用 | 否 |
| 第三方个人应用 | 否 |

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

backgroundAudioManager.stop();
```
