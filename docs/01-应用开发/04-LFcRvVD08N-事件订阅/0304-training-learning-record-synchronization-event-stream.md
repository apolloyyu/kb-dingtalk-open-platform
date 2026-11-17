---
title: "培训学习记录同步事件"
source_url: "https://open.dingtalk.com/document/development/training-learning-record-synchronization-event-stream"
namespace: "development"
slug: "training-learning-record-synchronization-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 智能人事事件 > 培训学习记录同步事件"
doc_id: "QPLuebNFRo"
updated_at: "2025-10-30 21:22:45"
---

> Source: https://open.dingtalk.com/document/development/training-learning-record-synchronization-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 智能人事事件 > 培训学习记录同步事件
> Updated: 2025-10-30 21:22:45

# 培训学习记录同步事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 培训学习记录同步事件 |
| 英文名称 | train\_course\_user\_info |
| 事件BizType | 238 |

## 功能描述

当biz\_type=238时，数据为培训学习记录同步相关数据。该数据为培训学习记录同步相关的数据变更时推送。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `courseId`（string）：课程id。
- `learnContent`（array）：学习内容，具体字段见下文学习内容字段说明。
- `learnContent[].userId`（string，必填）：员工userId。
- `learnContent[].learnTime`（long，必填）：学习时长，单位毫秒。
- `learnContent[].uuid`（string，必填）：记录的唯一标识，去重。

### **事件体数据示例如下:**

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
        "userId": "xxx",
        "uuid": "xxxx"
      }
    ]
  }
}
```
