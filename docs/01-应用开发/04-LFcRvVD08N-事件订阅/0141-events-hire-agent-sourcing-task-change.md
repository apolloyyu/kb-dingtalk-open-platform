---
title: "AI招聘找简历事件变更"
source_url: "https://open.dingtalk.com/document/development/events-hire-agent-sourcing-task-change"
namespace: "development"
slug: "events-hire-agent-sourcing-task-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > AI招聘找简历事件变更"
doc_id: "FuuZuv2LWd"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-hire-agent-sourcing-task-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > AI招聘找简历事件变更
> Updated: 2022-01-19 19:29:22

# AI招聘找简历事件变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | AI招聘找简历事件变更 |
| 英文名称 | hire\_agent\_sourcing\_task\_change |

## 功能描述

AI招聘找简历任务任务变更的相关数据推送。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "hire_agent_sourcing_task_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "dingxxx",
    "syncAction": "CANDIDATE_COLLECTED",
    "candidateInfo": {
      "jobName": "Java高级工程师",
      "workYears": 7,
      "education": "硕士",
      "sex": 1,
      "matchResult": {
        "summary": "工作年限和学历未满足职位硬性要求",
        "failedHardCriteria": [
          "要求5年及以上Java开发经验，候选人为3年"
        ],
        "pass": true
      },
      "resumeFile": {
        "fileName": "张三-简历.pdf",
        "downloadUrl": "https://example.com/resume/signed-path",
        "expiresAt": 1786579200000
      },
      "dialogueHistory": "HR：你好，我们正在招聘Java高级工程师。\\n候选人：你好，可以进一步沟通。",
      "disadvantageDesc": "无电商行业经验",
      "createAt": 1786579200000,
      "jobId": "job123",
      "matchScore": 86,
      "candidateName": "张三",
      "phone": "13800000000",
      "aiSummary": "Java后端经验符合职位要求",
      "location": "杭州",
      "advantageDesc": "7年Java后端开发经验\\n具备大型分布式系统经验",
      "age": 24,
      "email": "zhangsan@example.com"
    },
    "sourceChannel": "BOSS",
    "scope": "candidate",
    "ownerUserId": "dinguserid",
    "taskName": "找简历",
    "taskInfo": {
      "endedAt": 1786579200000,
      "jobs": [
        {
          "jobName": "Java高级工程师",
          "jobId": "job123"
        }
      ],
      "startedAt": 1786492800000,
      "status": "SUCCESS"
    },
    "taskId": "task123"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "hire_agent_sourcing_task_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpId": "dingxxx",
  "syncAction": "CANDIDATE_COLLECTED",
  "candidateInfo": {
    "jobName": "Java高级工程师",
    "workYears": 7,
    "education": "硕士",
    "sex": 1,
    "matchResult": {
      "summary": "工作年限和学历未满足职位硬性要求",
      "failedHardCriteria": [
        "要求5年及以上Java开发经验，候选人为3年"
      ],
      "pass": true
    },
    "resumeFile": {
      "fileName": "张三-简历.pdf",
      "downloadUrl": "https://example.com/resume/signed-path",
      "expiresAt": 1786579200000
    },
    "dialogueHistory": "HR：你好，我们正在招聘Java高级工程师。\\n候选人：你好，可以进一步沟通。",
    "disadvantageDesc": "无电商行业经验",
    "createAt": 1786579200000,
    "jobId": "job123",
    "matchScore": 86,
    "candidateName": "张三",
    "phone": "13800000000",
    "aiSummary": "Java后端经验符合职位要求",
    "location": "杭州",
    "advantageDesc": "7年Java后端开发经验\\n具备大型分布式系统经验",
    "age": 24,
    "email": "zhangsan@example.com"
  },
  "sourceChannel": "BOSS",
  "scope": "candidate",
  "ownerUserId": "dinguserid",
  "taskName": "找简历",
  "taskInfo": {
    "endedAt": 1786579200000,
    "jobs": [
      {
        "jobName": "Java高级工程师",
        "jobId": "job123"
      }
    ],
    "startedAt": 1786492800000,
    "status": "SUCCESS"
  },
  "taskId": "task123"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=504)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 504,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "dingxxx",
    "syncAction": "CANDIDATE_COLLECTED",
    "candidateInfo": {
      "jobName": "Java高级工程师",
      "workYears": 7,
      "education": "硕士",
      "sex": 1,
      "matchResult": {
        "summary": "工作年限和学历未满足职位硬性要求",
        "failedHardCriteria": [
          "要求5年及以上Java开发经验，候选人为3年"
        ],
        "pass": true
      },
      "resumeFile": {
        "fileName": "张三-简历.pdf",
        "downloadUrl": "https://example.com/resume/signed-path",
        "expiresAt": 1786579200000
      },
      "dialogueHistory": "HR：你好，我们正在招聘Java高级工程师。\\n候选人：你好，可以进一步沟通。",
      "disadvantageDesc": "无电商行业经验",
      "createAt": 1786579200000,
      "jobId": "job123",
      "matchScore": 86,
      "candidateName": "张三",
      "phone": "13800000000",
      "aiSummary": "Java后端经验符合职位要求",
      "location": "杭州",
      "advantageDesc": "7年Java后端开发经验\\n具备大型分布式系统经验",
      "age": 24,
      "email": "zhangsan@example.com"
    },
    "sourceChannel": "BOSS",
    "scope": "candidate",
    "ownerUserId": "dinguserid",
    "taskName": "找简历",
    "taskInfo": {
      "endedAt": 1786579200000,
      "jobs": [
        {
          "jobName": "Java高级工程师",
          "jobId": "job123"
        }
      ],
      "startedAt": 1786492800000,
      "status": "SUCCESS"
    },
    "taskId": "task123"
  }
}
```
