---
title: "培训学习记录同步事件"
source_url: "https://open.dingtalk.com/document/development/training-learning-record-sync-events"
namespace: "development"
slug: "training-learning-record-sync-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 培训学习记录同步事件"
doc_id: "IUFPMFdLiF"
updated_at: "2025-08-28 19:47:04"
---

> Source: https://open.dingtalk.com/document/development/training-learning-record-sync-events
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 培训学习记录同步事件
> Updated: 2025-08-28 19:47:04

# 培训学习记录同步事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 培训学习记录同步事件 |
| 英文名称 | train\_course\_user\_info |

## 功能描述

培训学习记录同步事件数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
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
- `data.courseId`（string）：课程id。
- `data.learnContent`（array）：学习内容，具体字段见下文学习内容字段说明。
- `data.learnContent[].learnTime`（long）：学习时长，单位毫秒。
- `data.learnContent[].userId`（string）：员工userId。
- `data.learnContent[].uuid`（string）：记录的唯一标识，去重。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "train_course_user_info",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "courseId": "xxx",
    "learnContent": [
      {
        "learnTime": 100,
        "uuid": "xxxx",
        "userId": "xxxx"
      }
    ]
  }
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
- `biz_data.courseId`（string）：课程id。
- `biz_data.learnContent`（array）：学习内容，具体字段见下文学习内容字段说明。
- `biz_data.learnContent[].learnTime`（long）：学习时长，单位毫秒。
- `biz_data.learnContent[].userId`（string）：员工userId。
- `biz_data.learnContent[].uuid`（string）：记录的唯一标识，去重。

### **biz\_data数据示例(biz\_type=238)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 238,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "train_course_user_info",
    "courseId": "xxx",
    "learnContent": [
      {
        "learnTime": 100,
        "uuid": "xxxx",
        "userId": "xxxx"
      }
    ]
  }
}
```
