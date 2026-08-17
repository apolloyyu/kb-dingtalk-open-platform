---
title: "培训学习记录同步事件"
source_url: "https://open.dingtalk.com/document/development/training-learning-record-sync-events"
namespace: "development"
slug: "training-learning-record-sync-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 培训学习记录同步事件"
doc_id: "IUFPMFdLiF"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/training-learning-record-sync-events
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 培训学习记录同步事件
> Updated: 2022-01-19 19:29:22

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
