---
title: "视频会议成员状态变更"
source_url: "https://open.dingtalk.com/document/development/video-conference-member-status-change-stream"
namespace: "development"
slug: "video-conference-member-status-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 会议事件 > 视频会议成员状态变更"
doc_id: "wXQW67fs6R"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/video-conference-member-status-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 会议事件 > 视频会议成员状态变更
> Updated: 2022-01-19 19:29:22

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

### data部分(事件业务信息)

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
