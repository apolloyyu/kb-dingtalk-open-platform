---
title: "视频会议状态变更App定向推送"
source_url: "https://open.dingtalk.com/document/development/events-meeting-status-change-target-push"
namespace: "development"
slug: "events-meeting-status-change-target-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议状态变更App定向推送"
doc_id: "mjW9UKjyM1"
updated_at: "2025-08-27 16:11:19"
---

> Source: https://open.dingtalk.com/document/development/events-meeting-status-change-target-push
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议状态变更App定向推送
> Updated: 2025-08-27 16:11:19

# 视频会议状态变更App定向推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议状态变更App定向推送 |
| 英文名称 | meeting\_status\_change\_target\_push |

## 功能描述

视频会议状态变更定向推送，目前支持定向推送通过开放接口创建的会议事件，定向推送给调用方所属的应用。

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
- `data.statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序
- `data.changeScene`（string）：会议状态变化细分类型：   
   - conference\_created : 会议创建事件。  
  - conference\_closed : 会议关闭事件。
- `data.openConfModel`（object）：会议信息。
- `data.openConfModel.bizType`（integer）：会议业务类型。
- `data.openConfModel.activeNum`（integer）：当前在会人数。
- `data.openConfModel.attendNum`（integer）：累积入会人数。
- `data.openConfModel.confDuration`（long）：会议时长，单位毫秒。
- `data.openConfModel.conferenceId`（string，必填）：会议id。
- `data.openConfModel.startTime`（long，必填）：会议开始时间戳，单位毫秒。
- `data.openConfModel.endTime`（long）：会议结束时间戳，单位毫秒。
- `data.openConfModel.invitedNum`（long）：邀请人数。
- `data.openConfModel.status`（integer，必填）：会议状态。   
  - 0：初始化。   
  - 1：会议结束。   
  - 2：会议开始。
- `data.openConfModel.title`（string，必填）：会议标题。
- `data.openConfModel.roomCode`（string）：会议码。
- `data.openConfModel.externalLinkUrl`（string）：会议的入会链接。
- `data.openConfModel.creatorId`（string，必填）：会议创建人的unionId。
- `data.openConfModel.creatorNick`（string，必填）：会议创建人的昵称。
- `data.openConfModel.scheduleConferenceId`（string）：预约会议id，为预约会议时有该字段。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "meeting_status_change_target_push",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openConfModel": {
      "bizType": 0,
      "creatorId": "2iPOLxxxxx",
      "roomCode": "4272xxxxx",
      "title": "开放会议",
      "activeNum": 10,
      "creatorNick": "小钉",
      "attendNum": 15,
      "confDuration": 1000000,
      "conferenceId": "6321*******9b6ed40",
      "startTime": 1663293270000,
      "endTime": 1663294270000,
      "invitedNum": 20,
      "externalLinkUrl": "https://meeting.dingtalk.com/app?roomCode\u003d42726xxx\u0026token\u003d1_7ac9xxx",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea",
      "status": 1
    },
    "statusSeqNum": 1,
    "changeScene": "conference_created"
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
- `statusSeqNum`（integer，必填）：会议、成员信息总体序列号, 用于区分消息顺序
- `changeScene`（string，必填）：会议状态变化细分类型：   
   - conference\_created : 会议创建事件。  
  - conference\_closed : 会议关闭事件。
- `openConfModel`（object，必填）：会议信息。
- `openConfModel.bizType`（integer）：会议业务类型。
- `openConfModel.activeNum`（integer）：当前在会人数。
- `openConfModel.attendNum`（integer）：累积入会人数。
- `openConfModel.confDuration`（long）：会议时长，单位毫秒。
- `openConfModel.conferenceId`（string，必填）：会议id。
- `openConfModel.startTime`（long，必填）：会议开始时间戳，单位毫秒。
- `openConfModel.endTime`（long）：会议结束时间戳，单位毫秒。
- `openConfModel.invitedNum`（long）：邀请人数。
- `openConfModel.status`（integer，必填）：会议状态。   
  - 0：初始化。   
  - 1：会议结束。   
  - 2：会议开始。
- `openConfModel.title`（string，必填）：会议标题。
- `openConfModel.roomCode`（string）：会议码。
- `openConfModel.externalLinkUrl`（string）：会议的入会链接。
- `openConfModel.creatorId`（string，必填）：会议创建人的unionId。
- `openConfModel.creatorNick`（string，必填）：会议创建人的昵称。
- `openConfModel.scheduleConferenceId`（string）：预约会议id，为预约会议时有该字段。

### **事件体示例**

```
{
  "EventType": "meeting_status_change_target_push",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openConfModel": {
    "bizType": 0,
    "creatorId": "2iPOLxxxxx",
    "roomCode": "4272xxxxx",
    "title": "开放会议",
    "activeNum": 10,
    "creatorNick": "小钉",
    "attendNum": 15,
    "confDuration": 1000000,
    "conferenceId": "6321*******9b6ed40",
    "startTime": 1663293270000,
    "endTime": 1663294270000,
    "invitedNum": 20,
    "externalLinkUrl": "https://meeting.dingtalk.com/app?roomCode\u003d42726xxx\u0026token\u003d1_7ac9xxx",
    "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea",
    "status": 1
  },
  "statusSeqNum": 1,
  "changeScene": "conference_created"
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
- `biz_data.statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序
- `biz_data.changeScene`（string）：会议状态变化细分类型：   
   - conference\_created : 会议创建事件。  
  - conference\_closed : 会议关闭事件。
- `biz_data.openConfModel`（object）：会议信息。
- `biz_data.openConfModel.bizType`（integer）：会议业务类型。
- `biz_data.openConfModel.activeNum`（integer）：当前在会人数。
- `biz_data.openConfModel.attendNum`（integer）：累积入会人数。
- `biz_data.openConfModel.confDuration`（long）：会议时长，单位毫秒。
- `biz_data.openConfModel.conferenceId`（string，必填）：会议id。
- `biz_data.openConfModel.startTime`（long，必填）：会议开始时间戳，单位毫秒。
- `biz_data.openConfModel.endTime`（long）：会议结束时间戳，单位毫秒。
- `biz_data.openConfModel.invitedNum`（long）：邀请人数。
- `biz_data.openConfModel.status`（integer，必填）：会议状态。   
  - 0：初始化。   
  - 1：会议结束。   
  - 2：会议开始。
- `biz_data.openConfModel.title`（string，必填）：会议标题。
- `biz_data.openConfModel.roomCode`（string）：会议码。
- `biz_data.openConfModel.externalLinkUrl`（string）：会议的入会链接。
- `biz_data.openConfModel.creatorId`（string，必填）：会议创建人的unionId。
- `biz_data.openConfModel.creatorNick`（string，必填）：会议创建人的昵称。
- `biz_data.openConfModel.scheduleConferenceId`（string）：预约会议id，为预约会议时有该字段。

### **biz\_data数据示例(biz\_type=348)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 348,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "openConfModel": {
      "bizType": 0,
      "creatorId": "2iPOLxxxxx",
      "roomCode": "4272xxxxx",
      "title": "开放会议",
      "activeNum": 10,
      "creatorNick": "小钉",
      "attendNum": 15,
      "confDuration": 1000000,
      "conferenceId": "6321*******9b6ed40",
      "startTime": 1663293270000,
      "endTime": 1663294270000,
      "invitedNum": 20,
      "externalLinkUrl": "https://meeting.dingtalk.com/app?roomCode\u003d42726xxx\u0026token\u003d1_7ac9xxx",
      "scheduleConferenceId": "5ba0a5ce-xxxx-4a4f-bc68-xxxx81980eea",
      "status": 1
    },
    "syncAction": "meeting_status_change_target_push",
    "statusSeqNum": 1,
    "changeScene": "conference_created"
  }
}
```
