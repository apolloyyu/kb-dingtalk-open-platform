---
title: "视频会议状态变更"
source_url: "https://open.dingtalk.com/document/development/event-meeting-status-change"
namespace: "development"
slug: "event-meeting-status-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议状态变更"
doc_id: "rLh7qAEEmW"
updated_at: "2025-08-27 16:11:17"
---

> Source: https://open.dingtalk.com/document/development/event-meeting-status-change
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议状态变更
> Updated: 2025-08-27 16:11:17

# 视频会议状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议状态变更 |
| 英文名称 | meeting\_status\_change |

## 功能描述

直播事件回调，表示视频会议状态变更事件推送的数据格式。

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
- `data.openConfModel`（object）：会议信息。
- `data.openConfModel.activeNum`（integer）：会中成员人数。
- `data.openConfModel.creatorNick`（string）：会议创建人昵称。
- `data.openConfModel.bizType`（string）：会议业务类型：  
  \* 0：普通视频会议  
  \* 1 ：公网投屏  
  \* 3 ：日程预约视频会议  
  \* rooms\_conf Rooms：视频会议
- `data.openConfModel.attendNum`（integer）：累积在会人数（包含已离会）。
- `data.openConfModel.confDuration`（integer）：会议持续时间。
- `data.openConfModel.conferenceId`（string）：会议id。
- `data.openConfModel.creatorId`（string）：创建者unionId。
- `data.openConfModel.startTime`（long）：会议开始时间。
- `data.openConfModel.invitedNum`（integer）：会议邀请人数。
- `data.openConfModel.title`（string）：会议标题。
- `data.openConfModel.scheduleConferenceId`（string）：计划会议id。
- `data.openConfModel.status`（integer）：会议状态。
- `data.openConfModel.calendarEventId`（string）：日程Id
- `data.openConfModel.bizScene`（string）：业务场景
- `data.statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `data.changeScene`（string）：会议状态变化细分类型：  
  \* conference\_created : 会议创建事件  
  \* conference\_closed : 会议关闭事件

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "meeting_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openConfModel": {
      "calendarEventId": "UUNoaGV5*****md3UT09",
      "bizType": "3",
      "creatorId": "2iPO*********wiEiE",
      "bizScene": "autoCall",
      "title": "开放会议",
      "activeNum": 10,
      "creatorNick": "开放会议创建者",
      "attendNum": 6,
      "confDuration": 1000,
      "conferenceId": "6321*******9b6ed40",
      "startTime": 1684215608570,
      "invitedNum": 10,
      "scheduleConferenceId": "f2fbaa7d-xxxx-45d6",
      "status": 1,
      "calendarEventId":"UUNoaGV5*****md3UT09",
      "bizScene":"autoCall"
    },
    "statusSeqNum": 1,
    "changeScene": "conference_created"
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
- `openConfModel`（object）：会议信息。
- `openConfModel.activeNum`（integer）：会中成员人数。
- `openConfModel.creatorNick`（string）：会议创建人昵称。
- `openConfModel.bizType`（string）：会议业务类型：  
  \* 0：普通视频会议  
  \* 1 ：公网投屏  
  \* 3 ：日程预约视频会议  
  \* rooms\_conf Rooms：视频会议
- `openConfModel.attendNum`（integer）：累积在会人数（包含已离会）。
- `openConfModel.confDuration`（integer）：会议持续时间。
- `openConfModel.conferenceId`（string）：会议id。
- `openConfModel.creatorId`（string）：创建者unionId。
- `openConfModel.startTime`（long）：会议开始时间。
- `openConfModel.invitedNum`（integer）：会议邀请人数。
- `openConfModel.title`（string）：会议标题。
- `openConfModel.scheduleConferenceId`（string）：计划会议id。
- `openConfModel.status`（integer）：会议状态。
- `openConfModel.calendarEventId`（string）：日程Id
- `openConfModel.bizScene`（string）：业务场景
- `statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `changeScene`（string）：会议状态变化细分类型：  
  \* conference\_created : 会议创建事件  
  \* conference\_closed : 会议关闭事件

### **事件体示例**

```
{
  "EventType": "meeting_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openConfModel": {
    "calendarEventId": "UUNoaGV5*****md3UT09",
    "bizType": "3",
    "creatorId": "2iPO*********wiEiE",
    "bizScene": "autoCall",
    "title": "开放会议",
    "activeNum": 10,
    "creatorNick": "开放会议创建者",
    "attendNum": 6,
    "confDuration": 1000,
    "conferenceId": "6321*******9b6ed40",
    "startTime": 1684215608570,
    "invitedNum": 10,
    "scheduleConferenceId": "f2fbaa7d-xxxx-45d6",
    "status": 1,
    "calendarEventId":"UUNoaGV5*****md3UT09",
    "bizScene":"autoCall"
  },
  "statusSeqNum": 1,
  "changeScene": "conference_created"
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
- `biz_data.openConfModel`（object）：会议信息。
- `biz_data.openConfModel.activeNum`（integer）：会中成员人数。
- `biz_data.openConfModel.creatorNick`（string）：会议创建人昵称。
- `biz_data.openConfModel.bizType`（string）：会议业务类型：  
  \* 0：普通视频会议  
  \* 1 ：公网投屏  
  \* 3 ：日程预约视频会议  
  \* rooms\_conf Rooms：视频会议
- `biz_data.openConfModel.attendNum`（integer）：累积在会人数（包含已离会）。
- `biz_data.openConfModel.confDuration`（integer）：会议持续时间。
- `biz_data.openConfModel.conferenceId`（string）：会议id。
- `biz_data.openConfModel.creatorId`（string）：创建者unionId。
- `biz_data.openConfModel.startTime`（long）：会议开始时间。
- `biz_data.openConfModel.invitedNum`（integer）：会议邀请人数。
- `biz_data.openConfModel.title`（string）：会议标题。
- `biz_data.openConfModel.scheduleConferenceId`（string）：计划会议id。
- `biz_data.openConfModel.status`（integer）：会议状态。
- `biz_data.openConfModel.calendarEventId`（string）：日程Id
- `biz_data.openConfModel.bizScene`（string）：业务场景
- `biz_data.statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `biz_data.changeScene`（string）：会议状态变化细分类型：  
  \* conference\_created : 会议创建事件  
  \* conference\_closed : 会议关闭事件

### **biz\_data数据示例(biz\_type=225)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 225,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "calendarEventId": "UUNoaGV5*****md3UT09",
      "bizType": "3",
      "creatorId": "2iPO*********wiEiE",
      "bizScene": "autoCall",
      "title": "开放会议",
      "activeNum": 10,
      "creatorNick": "开放会议创建者",
      "attendNum": 6,
      "confDuration": 1000,
      "conferenceId": "6321*******9b6ed40",
      "startTime": 1684215608570,
      "invitedNum": 10,
      "scheduleConferenceId": "f2fbaa7d-xxxx-45d6",
      "status": 1,
      "calendarEventId":"UUNoaGV5*****md3UT09",
      "bizScene":"autoCall"
    },
    "syncAction": "meeting_status_change",
    "statusSeqNum": 1,
    "changeScene": "conference_created"
  }
}
```
