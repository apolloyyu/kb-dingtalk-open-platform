---
title: "AI招聘消息通知事件"
source_url: "https://open.dingtalk.com/document/development/events-hire-agent-notification"
namespace: "development"
slug: "events-hire-agent-notification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > AI招聘消息通知事件"
doc_id: "OoN932IbOO"
updated_at: "2026-09-02 10:05:18"
---

> Source: https://open.dingtalk.com/document/development/events-hire-agent-notification
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > AI招聘消息通知事件
> Updated: 2026-09-02 10:05:18

# AI招聘消息通知事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI招聘消息通知事件 |
| 英文名称 | hire\_agent\_notification |

## 功能描述

AI招聘的人才库激活中，消息通知开放事件。

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
- `data.action`（string）：通知动作。RESUME\_UPLOAD\_NOTICE，表示简历上传通知。
- `data.data`（object）：通知业务数据。action 为 OUTREACH\_RESUME\_UPLOAD\_NOTICE 时使用以下数据结构。
- `data.data.candidate`（object，必填）：候选人信息。
- `data.data.candidate.candidateId`（string，必填）：招聘 Agent 中的候选人 ID。
- `data.data.candidate.sourceCandidateId`（string，必填）：客户候选人系统中的候选人 ID。
- `data.data.candidate.candidateName`（string，必填）：候选人姓名。
- `data.data.candidate.phoneNumber`（string，必填）：候选人手机号。
- `data.data.candidate.email`（string，必填）：候选人邮箱。
- `data.data.job`（object，必填）：职位信息。
- `data.data.job.jobId`（string，必填）：职位 ID。
- `data.data.job.jobName`（string，必填）：职位名称。
- `data.data.job.jobDescription`（string，必填）：职位详情。
- `data.data.resumeUploadShortUrl`（string，必填）：候选人上传简历的完整短链接。
- `data.data.freshnessLevel`（string，必填）：简历新鲜度。FRESH：新鲜；STALE：过时。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "hire_agent_notification",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "data": {
      "candidate": {
        "phoneNumber": "13800000000",
        "candidateName": "张三",
        "sourceCandidateId": "sourceCandidate123",
        "candidateId": "candidate123",
        "email": "zhangsan@example.com"
      },
      "resumeUploadShortUrl": "https://dturl.co/xxxxx",
      "freshnessLevel": "FRESH",
      "job": {
        "jobName": "Java高级工程师",
        "jobId": "job123",
        "jobDescription": "负责招聘 Agent 相关系统的设计与开发。"
      }
    },
    "action": "RESUME_UPLOAD_NOTICE"
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
- `action`（string，必填）：通知动作。RESUME\_UPLOAD\_NOTICE，表示简历上传通知。
- `data`（object，必填）：通知业务数据。action 为 OUTREACH\_RESUME\_UPLOAD\_NOTICE 时使用以下数据结构。
- `data.candidate`（object，必填）：候选人信息。
- `data.candidate.candidateId`（string，必填）：招聘 Agent 中的候选人 ID。
- `data.candidate.sourceCandidateId`（string，必填）：客户候选人系统中的候选人 ID。
- `data.candidate.candidateName`（string，必填）：候选人姓名。
- `data.candidate.phoneNumber`（string，必填）：候选人手机号。
- `data.candidate.email`（string，必填）：候选人邮箱。
- `data.job`（object，必填）：职位信息。
- `data.job.jobId`（string，必填）：职位 ID。
- `data.job.jobName`（string，必填）：职位名称。
- `data.job.jobDescription`（string，必填）：职位详情。
- `data.resumeUploadShortUrl`（string，必填）：候选人上传简历的完整短链接。
- `data.freshnessLevel`（string，必填）：简历新鲜度。FRESH：新鲜；STALE：过时。

### **事件体示例**

```
{
  "EventType": "hire_agent_notification",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "data": {
    "candidate": {
      "phoneNumber": "13800000000",
      "candidateName": "张三",
      "sourceCandidateId": "sourceCandidate123",
      "candidateId": "candidate123",
      "email": "zhangsan@example.com"
    },
    "resumeUploadShortUrl": "https://dturl.co/xxxxx",
    "freshnessLevel": "FRESH",
    "job": {
      "jobName": "Java高级工程师",
      "jobId": "job123",
      "jobDescription": "负责招聘 Agent 相关系统的设计与开发。"
    }
  },
  "action": "RESUME_UPLOAD_NOTICE"
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
- `biz_data.action`（string）：通知动作。RESUME\_UPLOAD\_NOTICE，表示简历上传通知。
- `biz_data.data`（object）：通知业务数据。action 为 OUTREACH\_RESUME\_UPLOAD\_NOTICE 时使用以下数据结构。
- `biz_data.data.candidate`（object，必填）：候选人信息。
- `biz_data.data.candidate.candidateId`（string，必填）：招聘 Agent 中的候选人 ID。
- `biz_data.data.candidate.sourceCandidateId`（string，必填）：客户候选人系统中的候选人 ID。
- `biz_data.data.candidate.candidateName`（string，必填）：候选人姓名。
- `biz_data.data.candidate.phoneNumber`（string，必填）：候选人手机号。
- `biz_data.data.candidate.email`（string，必填）：候选人邮箱。
- `biz_data.data.job`（object，必填）：职位信息。
- `biz_data.data.job.jobId`（string，必填）：职位 ID。
- `biz_data.data.job.jobName`（string，必填）：职位名称。
- `biz_data.data.job.jobDescription`（string，必填）：职位详情。
- `biz_data.data.resumeUploadShortUrl`（string，必填）：候选人上传简历的完整短链接。
- `biz_data.data.freshnessLevel`（string，必填）：简历新鲜度。FRESH：新鲜；STALE：过时。

### **biz\_data数据示例(biz\_type=512)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 512,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "data": {
      "candidate": {
        "phoneNumber": "13800000000",
        "candidateName": "张三",
        "sourceCandidateId": "sourceCandidate123",
        "candidateId": "candidate123",
        "email": "zhangsan@example.com"
      },
      "resumeUploadShortUrl": "https://dturl.co/xxxxx",
      "freshnessLevel": "FRESH",
      "job": {
        "jobName": "Java高级工程师",
        "jobId": "job123",
        "jobDescription": "负责招聘 Agent 相关系统的设计与开发。"
      }
    },
    "syncAction": "hire_agent_notification",
    "action": "RESUME_UPLOAD_NOTICE"
  }
}
```
