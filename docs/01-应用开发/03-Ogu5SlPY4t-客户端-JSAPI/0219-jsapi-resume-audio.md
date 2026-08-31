---
title: "resumeAudio"
source_url: "https://open.dingtalk.com/document/development/jsapi-resume-audio"
namespace: "development"
slug: "jsapi-resume-audio"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "多媒体 > 录音 > resumeAudio"
doc_id: "C44h4giYTM"
updated_at: "2025-08-27 18:06:39"
---

> Source: https://open.dingtalk.com/document/development/jsapi-resume-audio
> Path: 应用开发 / 客户端 JSAPI / 多媒体 > 录音 > resumeAudio
> Updated: 2025-08-27 18:06:39

# resumeAudio

调用resumeAudio，恢复暂停播放的语音。

> 恢复播放处于暂停状态的语音。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11682) |
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

- `localAudioId`（string，必填）：处于暂停状态的语音的本地标识。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.resumeAudio({
  localAudioId: 'localAudioId示例值',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
