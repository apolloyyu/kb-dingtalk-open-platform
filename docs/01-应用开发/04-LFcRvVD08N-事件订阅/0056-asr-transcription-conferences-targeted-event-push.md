---
title: "视频会议ASR转写结果开放事件定向推送"
source_url: "https://open.dingtalk.com/document/development/asr-transcription-conferences-targeted-event-push"
namespace: "development"
slug: "asr-transcription-conferences-targeted-event-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议ASR转写结果开放事件定向推送"
doc_id: "t9ed943x0h"
updated_at: "2025-12-08 14:17:21"
---

> Source: https://open.dingtalk.com/document/development/asr-transcription-conferences-targeted-event-push
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议ASR转写结果开放事件定向推送
> Updated: 2025-12-08 14:17:21

# 视频会议ASR转写结果开放事件定向推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议ASR转写结果开放事件定向推送 |
| 英文名称 | meeting\_asr\_result\_event\_directed |

## 功能描述

视频会议云录制、闪记ASR转写识别结果事件，指定App推送。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.openConfModel`（object）
- `data.openConfModel.conferenceId`（string，必填）：会议id。
- `data.openConfModel.scheduleConferenceId`（string，必填）：预约会议id。
- `data.payload`（object）：转写结果内容。
- `data.payload.result`（string，必填）：识别内容。
- `data.payload.speakerUnionId`（string，必填）：说话人unionId。
- `data.payload.words`（array，必填）：识别单词列表。
- `data.payload.words[].startTime`（long，必填）：开始时间，相对录制开始的时间。
- `data.payload.words[].text`（string，必填）：单词内容。
- `data.payload.words[].endTime`（long，必填）：结束时间，相对录制开始的时间。
- `data.payload.index`（string，必填）：句子id。
- `data.payload.time`（string，必填）：结束时间。
- `data.payload.beginTime`（string，必填）：开始时间。
- `data.header`（object）：转写结果头。
- `data.header.messageNo`（string，必填）：消息序列号。
- `data.header.name`（string，必填）：消息名。
- `data.header.messageId`（string，必填）：消息id。
- `data.timestamp`（long）：事件回调时间戳。
- `data.bizType`（string）：转写事件对应，业务类型。
- `data.recordId`（string）：转写事件对应业务id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "meeting_asr_result_event_directed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "recordId": "1232141245",
    "openConfModel": {
      "conferenceId": "67566af32fe07a026db9a940",
      "scheduleConferenceId": "5c7c9bb1-b256-4dc5-xxxx-xxxxxxxxxxxx"
    },
    "bizType": "minutes : 闪记 cloud_record : 云录制",
    "payload": {
      "result": "可以听到",
      "speakerUnionId": "lmvUrEjpboFrSMtgsiS9V3AiEiE",
      "words": [
        {
          "startTime": 32710,
          "text": "可",
          "endTime": 32770
        }
      ],
      "index": "1",
      "time": "33790",
      "beginTime": "33710"
    },
    "header": {
      "messageNo": "39",
      "name": "TranscriptionResultChanged",
      "messageId": "c76910d55f2649fdab594f572ef442e0"
    },
    "timestamp": 1733716797727
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `openConfModel`（object，必填）
- `openConfModel.conferenceId`（string，必填）：会议id。
- `openConfModel.scheduleConferenceId`（string，必填）：预约会议id。
- `payload`（object，必填）：转写结果内容。
- `payload.result`（string，必填）：识别内容。
- `payload.speakerUnionId`（string，必填）：说话人unionId。
- `payload.words`（array，必填）：识别单词列表。
- `payload.words[].startTime`（long，必填）：开始时间，相对录制开始的时间。
- `payload.words[].text`（string，必填）：单词内容。
- `payload.words[].endTime`（long，必填）：结束时间，相对录制开始的时间。
- `payload.index`（string，必填）：句子id。
- `payload.time`（string，必填）：结束时间。
- `payload.beginTime`（string，必填）：开始时间。
- `header`（object，必填）：转写结果头。
- `header.messageNo`（string，必填）：消息序列号。
- `header.name`（string，必填）：消息名。
- `header.messageId`（string，必填）：消息id。
- `timestamp`（long，必填）：事件回调时间戳。
- `bizType`（string，必填）：转写事件对应，业务类型。
- `recordId`（string，必填）：转写事件对应业务id。

### **事件体示例**

```
{
  "EventType": "meeting_asr_result_event_directed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "recordId": "1232141245",
  "openConfModel": {
    "conferenceId": "67566af32fe07a026db9a940",
    "scheduleConferenceId": "5c7c9bb1-b256-4dc5-xxxx-xxxxxxxxxxxx"
  },
  "bizType": "minutes : 闪记 cloud_record : 云录制",
  "payload": {
    "result": "可以听到",
    "speakerUnionId": "lmvUrEjpboFrSMtgsiS9V3AiEiE",
    "words": [
      {
        "startTime": 32710,
        "text": "可",
        "endTime": 32770
      }
    ],
    "index": "1",
    "time": "33790",
    "beginTime": "33710"
  },
  "header": {
    "messageNo": "39",
    "name": "TranscriptionResultChanged",
    "messageId": "c76910d55f2649fdab594f572ef442e0"
  },
  "timestamp": 1733716797727
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.openConfModel`（object）
- `biz_data.openConfModel.conferenceId`（string，必填）：会议id。
- `biz_data.openConfModel.scheduleConferenceId`（string，必填）：预约会议id。
- `biz_data.payload`（object）：转写结果内容。
- `biz_data.payload.result`（string，必填）：识别内容。
- `biz_data.payload.speakerUnionId`（string，必填）：说话人unionId。
- `biz_data.payload.words`（array，必填）：识别单词列表。
- `biz_data.payload.words[].startTime`（long，必填）：开始时间，相对录制开始的时间。
- `biz_data.payload.words[].text`（string，必填）：单词内容。
- `biz_data.payload.words[].endTime`（long，必填）：结束时间，相对录制开始的时间。
- `biz_data.payload.index`（string，必填）：句子id。
- `biz_data.payload.time`（string，必填）：结束时间。
- `biz_data.payload.beginTime`（string，必填）：开始时间。
- `biz_data.header`（object）：转写结果头。
- `biz_data.header.messageNo`（string，必填）：消息序列号。
- `biz_data.header.name`（string，必填）：消息名。
- `biz_data.header.messageId`（string，必填）：消息id。
- `biz_data.timestamp`（long）：事件回调时间戳。
- `biz_data.bizType`（string）：转写事件对应，业务类型。
- `biz_data.recordId`（string）：转写事件对应业务id。

### **biz\_data数据示例(biz\_type=412)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 412,
  "biz_data": {
    "recordId": "1232141245",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "conferenceId": "67566af32fe07a026db9a940",
      "scheduleConferenceId": "5c7c9bb1-b256-4dc5-xxxx-xxxxxxxxxxxx"
    },
    "bizType": "minutes : 闪记 cloud_record : 云录制",
    "syncAction": "meeting_asr_result_event_directed",
    "payload": {
      "result": "可以听到",
      "speakerUnionId": "lmvUrEjpboFrSMtgsiS9V3AiEiE",
      "words": [
        {
          "startTime": 32710,
          "text": "可",
          "endTime": 32770
        }
      ],
      "index": "1",
      "time": "33790",
      "beginTime": "33710"
    },
    "header": {
      "messageNo": "39",
      "name": "TranscriptionResultChanged",
      "messageId": "c76910d55f2649fdab594f572ef442e0"
    },
    "timestamp": 1733716797727
  }
}
```
