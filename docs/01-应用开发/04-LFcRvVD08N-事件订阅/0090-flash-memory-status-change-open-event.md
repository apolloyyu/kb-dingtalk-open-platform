---
title: "闪记状态变更开放事件"
source_url: "https://open.dingtalk.com/document/development/flash-memory-status-change-open-event"
namespace: "development"
slug: "flash-memory-status-change-open-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 闪记状态变更开放事件"
doc_id: "iIGQzShy4d"
updated_at: "2025-12-08 14:19:30"
---

> Source: https://open.dingtalk.com/document/development/flash-memory-status-change-open-event
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 闪记状态变更开放事件
> Updated: 2025-12-08 14:19:30

# 闪记状态变更开放事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 闪记状态变更开放事件 |
| 英文名称 | flash\_minutes\_open\_event |

## 功能描述

音视频会议闪记的开放接口状态同步事件：

1. 当摘要已生成后，会发送状态同步事件，同步闪记状态为：摘要已生成
2. 当视频转码或合并完成后，发送状态同步事件，通知闪记状态为：视频已生成
   客户接收到该状态后可以通过开放接口获取相关闪记资源

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
- `data.openConfModel`（object）：会议模型。
- `data.openConfModel.conferenceId`（string，必填）：会议id，会议相关闪记必传
- `data.openConfModel.scheduleConferenceId`（string）：预约会议id，当会议为预约会议id时传递
- `data.bizType`（string）：闪记的业务类型：  
  - cloud\_record：云录制  
  - minutes：会中闪记
- `data.minutesEventType`（string）：当前闪记的状态信息：  
  - summary\_generated：摘要生成  
  - video\_generated：视频生成
- `data.minutesTaskId`（number）：闪记taskId，非必传字段，请依据conferenceId作为闪记状态依据。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "flash_minutes_open_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openConfModel": {
      "conferenceId": "66f100462fe0c1******aa90",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea"
    },
    "bizType": "cloud_record",
    "minutesEventType": "summary_generated",
    "minutesTaskId": "115****09"
  }
}
```

HTTP推送

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `openConfModel`（object，必填）：会议模型。
- `openConfModel.conferenceId`（string，必填）：会议id，会议相关闪记必传
- `openConfModel.scheduleConferenceId`（string）：预约会议id，当会议为预约会议id时传递
- `bizType`（string，必填）：闪记的业务类型：  
  - cloud\_record：云录制  
  - minutes：会中闪记
- `minutesEventType`（string，必填）：当前闪记的状态信息：  
  - summary\_generated：摘要生成  
  - video\_generated：视频生成
- `minutesTaskId`（number）：闪记taskId，非必传字段，请依据conferenceId作为闪记状态依据。

### **事件体示例**

```
{
  "EventType": "flash_minutes_open_event",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openConfModel": {
    "conferenceId": "66f100462fe0c1******aa90",
    "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea"
  },
  "bizType": "cloud_record",
  "minutesEventType": "summary_generated",
  "minutesTaskId": "115****09"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.openConfModel`（object）：会议模型。
- `biz_data.openConfModel.conferenceId`（string，必填）：会议id，会议相关闪记必传
- `biz_data.openConfModel.scheduleConferenceId`（string）：预约会议id，当会议为预约会议id时传递
- `biz_data.bizType`（string）：闪记的业务类型：  
  - cloud\_record：云录制  
  - minutes：会中闪记
- `biz_data.minutesEventType`（string）：当前闪记的状态信息：  
  - summary\_generated：摘要生成  
  - video\_generated：视频生成
- `biz_data.minutesTaskId`（number）：闪记taskId，非必传字段，请依据conferenceId作为闪记状态依据。

### **biz\_data数据示例(biz\_type=396)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 396,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "conferenceId": "66f100462fe0c1******aa90",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea"
    },
    "bizType": "cloud_record",
    "minutesEventType": "summary_generated",
    "syncAction": "flash_minutes_open_event",
    "minutesTaskId": "115****09"
  }
}
```
