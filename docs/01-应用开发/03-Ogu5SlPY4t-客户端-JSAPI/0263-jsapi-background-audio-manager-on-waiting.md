---
title: "BackgroundAudioManager.onWaiting"
source_url: "https://open.dingtalk.com/document/development/jsapi-background-audio-manager-on-waiting"
namespace: "development"
slug: "jsapi-background-audio-manager-on-waiting"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 音频 > BackgroundAudioManager.onWaiting"
doc_id: "GOfxTDJjpX"
updated_at: "2025-08-27 18:07:00"
---

> Source: https://open.dingtalk.com/document/development/jsapi-background-audio-manager-on-waiting
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 音频 > BackgroundAudioManager.onWaiting
> Updated: 2025-08-27 18:07:00

# BackgroundAudioManager.onWaiting

监听音频加载中事件。

> 当音频因为数据不足，需要停下来加载时会触发。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11489) |

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
dd.BackgroundAudioManager.onWaiting();
```

`success`返回对象示例：

```
{}
```
