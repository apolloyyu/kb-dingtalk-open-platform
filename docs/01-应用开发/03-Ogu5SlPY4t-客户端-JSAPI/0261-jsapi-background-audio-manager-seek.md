---
title: "BackgroundAudioManager.seek"
source_url: "https://open.dingtalk.com/document/development/jsapi-background-audio-manager-seek"
namespace: "development"
slug: "jsapi-background-audio-manager-seek"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 音频 > BackgroundAudioManager.seek"
doc_id: "wUwyd4azwp"
updated_at: "2025-08-27 18:07:03"
---

> Source: https://open.dingtalk.com/document/development/jsapi-background-audio-manager-seek
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 音频 > BackgroundAudioManager.seek
> Updated: 2025-08-27 18:07:03

# BackgroundAudioManager.seek

跳转到指定位置position，以秒为单位。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10226) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `position`（string，必填）：跳转到指定位置position，以秒为单位。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
const backgroundAudioManager = dd.getBackgroundAudioManager();

backgroundAudioManager.seek('20');
```
