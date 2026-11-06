---
title: "视频会议成员状态变更"
source_url: "https://open.dingtalk.com/document/development/video-conference-member-status-change-stream"
namespace: "development"
slug: "video-conference-member-status-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 会议事件 > 视频会议成员状态变更"
doc_id: "wXQW67fs6R"
updated_at: "2025-10-16 14:32:17"
---

> Source: https://open.dingtalk.com/document/development/video-conference-member-status-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 会议事件 > 视频会议成员状态变更
> Updated: 2025-10-16 14:32:17

# 视频会议成员状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议成员状态变更 |
| 英文名称 | meeting\_member\_status\_change |

## 功能描述

当eventType为meeting\_member\_status\_change时，表示视频会议成员状态事件。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `openMemberModels`（array）：变更的成员信息列表。
- `openMemberModels[].deviceType`（string）：设备类型。
- `openMemberModels[].duration`（integer）：在会时长。
- `openMemberModels[].leaveTime`（long）：离开时间。
- `openMemberModels[].pstnJoin`（boolean）：是否为pstn入会。
- `openMemberModels[].conferenceId`（string）：会议id。
- `openMemberModels[].joinTime`（long）：入会时间。
- `openMemberModels[].userNick`（string）：用户昵称。
- `openMemberModels[].attendStatus`（integer）：成员状态。
- `openMemberModels[].host`（boolean）：是否为主持人。
- `openMemberModels[].coHost`（boolean）：是否为联席主持人。
- `openMemberModels[].userId`（string）：用户unionId（外部企业成员为空）。
- `statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `changeScene`（string）：成员状态变化细分类型：  
  \* user\_join：成员入会事件  
  \* user\_leave：成员离会事件  
  \* user\_invited：成员被邀请事件  
  \* user\_kicked：成员被踢事件

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "meeting_member_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openMemberModels": [
      {
        "deviceType": "Android",
        "duration": 100,
        "leaveTime": 1663143344000,
        "pstnJoin": false,
        "conferenceId": "6321*******9b6ed40",
        "joinTime": 1663143334000,
        "userNick": "会议参会者",
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
