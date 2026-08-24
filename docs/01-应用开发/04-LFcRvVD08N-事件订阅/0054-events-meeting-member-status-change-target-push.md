---
title: "视频会议成员状态变更App定向推送"
source_url: "https://open.dingtalk.com/document/development/events-meeting-member-status-change-target-push"
namespace: "development"
slug: "events-meeting-member-status-change-target-push"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "音视频 > 视频/音频会议 > 视频会议成员状态变更App定向推送"
doc_id: "9EfDKBKAOS"
updated_at: "2025-08-27 16:11:19"
---

> Source: https://open.dingtalk.com/document/development/events-meeting-member-status-change-target-push
> Path: 应用开发 / 事件订阅 / 音视频 > 视频/音频会议 > 视频会议成员状态变更App定向推送
> Updated: 2025-08-27 16:11:19

# 视频会议成员状态变更App定向推送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议成员状态变更App定向推送 |
| 英文名称 | meeting\_member\_status\_change\_target\_push |

## 功能描述

视频会议成员状态变更定向推送，目前支持定向推送通过开放接口创建的会议成员事件，定向推送给调用方所属的应用。

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
- `data.openMemberModels`（array）：变更的成员信息列表。
- `data.openMemberModels[].duration`（integer，必填）：在会时长。
- `data.openMemberModels[].leaveTime`（long，必填）：离开时间。
- `data.openMemberModels[].deviceType`（string，必填）：设备类型。
- `data.openMemberModels[].pstnJoin`（boolean，必填）：是否为pstn入会：  
  \* true：是  
  \* false：否
- `data.openMemberModels[].joinTime`（long，必填）：入会时间。
- `data.openMemberModels[].attendStatus`（integer，必填）：成员状态。
- `data.openMemberModels[].host`（boolean，必填）：是否为主持人：  
  \* true：是  
  \* false：否
- `data.openMemberModels[].coHost`（boolean，必填）：是否为联席主持人：  
    
  \* true：是  
  \* false：否
- `data.openMemberModels[].conferenceId`（string，必填）：会议id。
- `data.openMemberModels[].userNick`（string，必填）：用户昵称。
- `data.openMemberModels[].userId`（string，必填）：用户unionId（外部企业成员为空）。
- `data.statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `data.changeScene`（string）：成员状态变化细分类型：   
  - user\_join：成员入会事件  
  - user\_leave：成员离会事件  
  - user\_invited：成员被邀请事件  
  - user\_kicked：成员被踢事件

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "meeting_member_status_change_target_push",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openMemberModels": [
      {
        "duration": 1000,
        "leaveTime": 1663143344000,
        "deviceType": "Android",
        "pstnJoin": false,
        "joinTime": 1663143334000,
        "userNick": "会议参会者",
        "conferenceId": "6321*******9b6ed40",
        "attendStatus": 3,
        "host": false,
        "coHost": true,
        "userId": "2iPO*********wiEiE"
      }
    ],
    "statusSeqNum": 2,
    "changeScene": "user_join"
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
- `openMemberModels`（array，必填）：变更的成员信息列表。
- `openMemberModels[].duration`（integer，必填）：在会时长。
- `openMemberModels[].leaveTime`（long，必填）：离开时间。
- `openMemberModels[].deviceType`（string，必填）：设备类型。
- `openMemberModels[].pstnJoin`（boolean，必填）：是否为pstn入会：  
  \* true：是  
  \* false：否
- `openMemberModels[].joinTime`（long，必填）：入会时间。
- `openMemberModels[].attendStatus`（integer，必填）：成员状态。
- `openMemberModels[].host`（boolean，必填）：是否为主持人：  
  \* true：是  
  \* false：否
- `openMemberModels[].coHost`（boolean，必填）：是否为联席主持人：  
    
  \* true：是  
  \* false：否
- `openMemberModels[].conferenceId`（string，必填）：会议id。
- `openMemberModels[].userNick`（string，必填）：用户昵称。
- `openMemberModels[].userId`（string，必填）：用户unionId（外部企业成员为空）。
- `statusSeqNum`（integer，必填）：会议、成员信息总体序列号, 用于区分消息顺序。
- `changeScene`（string，必填）：成员状态变化细分类型：   
  - user\_join：成员入会事件  
  - user\_leave：成员离会事件  
  - user\_invited：成员被邀请事件  
  - user\_kicked：成员被踢事件

### **事件体示例**

```
{
  "EventType": "meeting_member_status_change_target_push",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "openMemberModels": [
    {
      "duration": 1000,
      "leaveTime": 1663143344000,
      "deviceType": "Android",
      "pstnJoin": false,
      "joinTime": 1663143334000,
      "userNick": "会议参会者",
      "conferenceId": "6321*******9b6ed40",
      "attendStatus": 3,
      "host": false,
      "coHost": true,
      "userId": "2iPO*********wiEiE"
    }
  ],
  "statusSeqNum": 2,
  "changeScene": "user_join"
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
- `biz_data.openMemberModels`（array）：变更的成员信息列表。
- `biz_data.openMemberModels[].duration`（integer，必填）：在会时长。
- `biz_data.openMemberModels[].leaveTime`（long，必填）：离开时间。
- `biz_data.openMemberModels[].deviceType`（string，必填）：设备类型。
- `biz_data.openMemberModels[].pstnJoin`（boolean，必填）：是否为pstn入会：  
  \* true：是  
  \* false：否
- `biz_data.openMemberModels[].joinTime`（long，必填）：入会时间。
- `biz_data.openMemberModels[].attendStatus`（integer，必填）：成员状态。
- `biz_data.openMemberModels[].host`（boolean，必填）：是否为主持人：  
  \* true：是  
  \* false：否
- `biz_data.openMemberModels[].coHost`（boolean，必填）：是否为联席主持人：  
    
  \* true：是  
  \* false：否
- `biz_data.openMemberModels[].conferenceId`（string，必填）：会议id。
- `biz_data.openMemberModels[].userNick`（string，必填）：用户昵称。
- `biz_data.openMemberModels[].userId`（string，必填）：用户unionId（外部企业成员为空）。
- `biz_data.statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `biz_data.changeScene`（string）：成员状态变化细分类型：   
  - user\_join：成员入会事件  
  - user\_leave：成员离会事件  
  - user\_invited：成员被邀请事件  
  - user\_kicked：成员被踢事件

### **biz\_data数据示例(biz\_type=349)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 349,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "meeting_member_status_change_target_push",
    "openMemberModels": [
      {
        "duration": 1000,
        "leaveTime": 1663143344000,
        "deviceType": "Android",
        "pstnJoin": false,
        "joinTime": 1663143334000,
        "userNick": "会议参会者",
        "conferenceId": "6321*******9b6ed40",
        "attendStatus": 3,
        "host": false,
        "coHost": true,
        "userId": "2iPO*********wiEiE"
      }
    ],
    "statusSeqNum": 2,
    "changeScene": "user_join"
  }
}
```
