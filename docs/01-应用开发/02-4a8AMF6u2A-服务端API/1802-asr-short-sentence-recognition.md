---
title: "ASR 一句话语音识别"
source_url: "https://open.dingtalk.com/document/development/asr-short-sentence-recognition"
namespace: "development"
slug: "asr-short-sentence-recognition"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > AI > ASR 一句话语音识别"
doc_id: "YstbF7DMD7"
updated_at: "2026-01-22 20:17:44"
---

> Source: https://open.dingtalk.com/document/development/asr-short-sentence-recognition
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > AI > ASR 一句话语音识别
> Updated: 2026-01-22 20:17:44

# ASR 一句话语音识别

调用本接口，可根据音频的media\_id识别一段60秒内的语音。

> **[!IMPORTANT]**
>
> 本文档已于 2025年 11 月 13 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方企业应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/asr/voice/translate`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| media\_id | String | 是 | @lATOCLhLfc46kUl8zlUmRlM | 音频的mediaId，调用[上传媒体文件](0646-upload-media-files.md)接口获取media\_id参数值。  **[!IMPORTANT]**  目前只接受 ogg 或 amr 格式的音频。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。  如果返回44001，请检查 media\_id 对应的文件是否为音频格式，或请重新上传音频文件再次请求。 |
| result | String |  | 调用结果。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/asr/voice/translate?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "media_id":"@lATOCLhLfc46kUl8zlUmRlM"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/asr/voice/translate");
OapiAsrVoiceTranslateRequest req = new OapiAsrVoiceTranslateRequest();
req.setMediaId("@lATOCLhLfc46kUl8zlUmRlM");
OapiAsrVoiceTranslateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode":0,
    "errmsg":"success",
    "result":""
}
```

## 语音识别事件回调

**事件类型**

| **事件类型** | **说明** |
| --- | --- |
| voice\_translate\_short\_speech | 一句话识别结果。 |

**翻译回调**

| 参数 | **含义** |
| --- | --- |
| EventType | voice\_translate\_short\_speech |
| corpId | 企业的corpId。 |
| finish | 翻译结束。 |
| entityId | 翻译任务 id，为传入的 mediaId 或 url。 |
| content | 翻译结果。 |
| version | 推送结果的版本号（时间戳）。 |

**请求示例**

```
{
  "EventType": "voice_translate_short_speech",
  "corpId": "ding_corpid",
  "finish": false,
  "entityId": "@entity123",
  "content": "翻译测试",
  "version": 1599822649734
}
```

## 错误码

| **错误码** | **说明** | **排查方法** |
| --- | --- | --- |
| 44001 | 获取传入的 media\_id 对应的音频失败 | 请检查media\_id对应的文件是否为ogg或amr格式的音频文件，或请重新上传音频文件再次请求。 |
