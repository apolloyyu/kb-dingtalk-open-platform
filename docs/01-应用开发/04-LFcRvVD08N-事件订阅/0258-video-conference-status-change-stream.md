---
title: "视频会议状态变更"
source_url: "https://open.dingtalk.com/document/development/video-conference-status-change-stream"
namespace: "development"
slug: "video-conference-status-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 会议事件 > 视频会议状态变更"
doc_id: "CL4eP5DuTg"
updated_at: "2025-10-16 14:32:17"
---

> Source: https://open.dingtalk.com/document/development/video-conference-status-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 会议事件 > 视频会议状态变更
> Updated: 2025-10-16 14:32:17

# 视频会议状态变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 视频会议状态变更 |
| 英文名称 | meeting\_status\_change |

## 功能描述

当eventType为meeting\_status\_change，表示视频会议状态变更事件。

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
- `openConfModel.startTime`（integer）：会议开始时间。
- `openConfModel.invitedNum`（integer）：会议邀请人数。
- `openConfModel.title`（string）：会议标题。
- `openConfModel.scheduleConferenceId`（string）：计划会议id。
- `openConfModel.status`（integer）：会议状态。
- `statusSeqNum`（integer）：会议、成员信息总体序列号, 用于区分消息顺序。
- `changeScene`（string）：会议状态变化细分类型：  
  \* conference\_created : 会议创建事件  
  \* conference\_closed : 会议关闭事件

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "meeting_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "openConfModel": {
      "activeNum": 10,
      "creatorNick": "开放会议创建者",
      "bizType": "3",
      "attendNum": 6,
      "confDuration": 1000,
      "conferenceId": "6321*******9b6ed40",
      "creatorId": "2iPO*********wiEiE",
      "startTime": 1684215608570,
      "invitedNum": 10,
      "title": "开放会议",
      "scheduleConferenceId": "f2fbaa7d-xxxx-45d6",
      "status": 1
    },
    "statusSeqNum": 1,
    "changeScene": "conference_created"
  }
}
```
