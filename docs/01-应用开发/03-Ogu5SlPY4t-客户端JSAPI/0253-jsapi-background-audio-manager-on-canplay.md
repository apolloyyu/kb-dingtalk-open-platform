---
title: "BackgroundAudioManager.onCanplay"
source_url: "https://open.dingtalk.com/document/development/jsapi-background-audio-manager-on-canplay"
namespace: "development"
slug: "jsapi-background-audio-manager-on-canplay"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "多媒体 > 音频 > BackgroundAudioManager.onCanplay"
doc_id: "h5KP2UQORL"
updated_at: "2025-08-27 18:06:58"
---

> Source: https://open.dingtalk.com/document/development/jsapi-background-audio-manager-on-canplay
> Path: 应用开发 / 客户端JSAPI / 多媒体 > 音频 > BackgroundAudioManager.onCanplay
> Updated: 2025-08-27 18:06:58

# BackgroundAudioManager.onCanplay

监听背景音频进入可以播放事件。

> 不保证后面可以流畅播放。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11488) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

（object）

## **示例****代码**

### 默认出入参

```
dd.BackgroundAudioManager.onCanplay();
```

`success`返回对象示例：

```
{}
```
