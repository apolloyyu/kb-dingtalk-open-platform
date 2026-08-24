---
title: "AI招聘找简历事件变更"
source_url: "https://open.dingtalk.com/document/development/events-hire-agent-sourcing-task-change"
namespace: "development"
slug: "events-hire-agent-sourcing-task-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > AI招聘找简历事件变更"
doc_id: "FuuZuv2LWd"
updated_at: "2026-08-18 09:33:45"
---

> Source: https://open.dingtalk.com/document/development/events-hire-agent-sourcing-task-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > AI招聘找简历事件变更
> Updated: 2026-08-18 09:33:45

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.syncAction`（string）：事件动作。任务事件：TASK\_STARTED、TASK\_FINISHED；候选人事件：CANDIDATE\_COLLECTED、CANDIDATE\_GREETED、CANDIDATE\_VIEWED。
- `data.scope`（string）：事件数据范围。task：任务事件；candidate：候选人事件。
- `data.taskId`（string）：Sourcing任务ID。
- `data.taskName`（string）：Sourcing任务名称。
- `data.sourceChannel`（string）：候选人来源渠道。
- `data.ownerUserId`（string）：任务创建人的钉钉用户ID。
- `data.corpId`（string）：企业ID。
- `data.candidateInfo`（object）：候选人事件信息。scope为candidate时必填。
- `data.candidateInfo.matchResult`（object）：候选人匹配结果。
- `data.candidateInfo.matchResult.failedHardCriteria`（array）：未满足的硬性条件。
- `data.candidateInfo.matchResult.pass`（boolean）：是否通过职位匹配。
- `data.candidateInfo.matchResult.summary`（string）：匹配结论。
- `data.candidateInfo.createAt`（long，必填）：候选人创建时间，毫秒时间戳。
- `data.candidateInfo.candidateName`（string，必填）：候选人名称。
- `data.candidateInfo.jobId`（string，必填）：候选人所属的职位ID。
- `data.candidateInfo.jobName`（string，必填）：候选人所属的职位名称。
- `data.candidateInfo.sex`（integer）：候选人性别。1男，2女
- `data.candidateInfo.age`（integer）：候选人年龄。
- `data.candidateInfo.phone`（string）：候选人手机号。
- `data.candidateInfo.email`（string）：候选人邮箱。
- `data.candidateInfo.location`（string）：候选人现居地。
- `data.candidateInfo.workYears`（integer）：候选人工作年限
- `data.candidateInfo.education`（string）：候选人最高学历。
- `data.candidateInfo.matchScore`（integer）：匹配分数，取值范围0至100。
- `data.candidateInfo.aiSummary`（string）：AI匹配总结。
- `data.candidateInfo.advantageDesc`（string）：匹配优势。
- `data.candidateInfo.disadvantageDesc`（string）：不匹配项。
- `data.candidateInfo.dialogueHistory`（string）：与候选人的沟通记录，Markdown格式。
- `data.candidateInfo.resumeFile`（object）：简历文件。
- `data.candidateInfo.resumeFile.fileName`（string，必填）：文件名。
- `data.candidateInfo.resumeFile.downloadUrl`（string，必填）：下载地址。
- `data.candidateInfo.resumeFile.expiresAt`（long，必填）：下载地址失效时间，毫秒时间戳。
- `data.taskInfo`（object）：任务事件信息。scope为task时必填。
- `data.taskInfo.endedAt`（long）：任务结束时间，毫秒时间戳。
- `data.taskInfo.jobs`（array，必填）：任务关联的来源职位列表。
- `data.taskInfo.jobs[].jobId`（string，必填）：职位ID。
- `data.taskInfo.jobs[].jobName`（string，必填）：职位名称。
- `data.taskInfo.startedAt`（long，必填）：任务开始时间，毫秒时间戳。
- `data.taskInfo.status`（string，必填）：任务状态。RUNNING、SUCCESS、FAILED。

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

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `syncAction`（string，必填）：事件动作。任务事件：TASK\_STARTED、TASK\_FINISHED；候选人事件：CANDIDATE\_COLLECTED、CANDIDATE\_GREETED、CANDIDATE\_VIEWED。
- `scope`（string，必填）：事件数据范围。task：任务事件；candidate：候选人事件。
- `taskId`（string，必填）：Sourcing任务ID。
- `taskName`（string，必填）：Sourcing任务名称。
- `sourceChannel`（string，必填）：候选人来源渠道。
- `ownerUserId`（string，必填）：任务创建人的钉钉用户ID。
- `corpId`（string，必填）：企业ID。
- `candidateInfo`（object）：候选人事件信息。scope为candidate时必填。
- `candidateInfo.matchResult`（object）：候选人匹配结果。
- `candidateInfo.matchResult.failedHardCriteria`（array）：未满足的硬性条件。
- `candidateInfo.matchResult.pass`（boolean）：是否通过职位匹配。
- `candidateInfo.matchResult.summary`（string）：匹配结论。
- `candidateInfo.createAt`（long，必填）：候选人创建时间，毫秒时间戳。
- `candidateInfo.candidateName`（string，必填）：候选人名称。
- `candidateInfo.jobId`（string，必填）：候选人所属的职位ID。
- `candidateInfo.jobName`（string，必填）：候选人所属的职位名称。
- `candidateInfo.sex`（integer）：候选人性别。1男，2女
- `candidateInfo.age`（integer）：候选人年龄。
- `candidateInfo.phone`（string）：候选人手机号。
- `candidateInfo.email`（string）：候选人邮箱。
- `candidateInfo.location`（string）：候选人现居地。
- `candidateInfo.workYears`（integer）：候选人工作年限
- `candidateInfo.education`（string）：候选人最高学历。
- `candidateInfo.matchScore`（integer）：匹配分数，取值范围0至100。
- `candidateInfo.aiSummary`（string）：AI匹配总结。
- `candidateInfo.advantageDesc`（string）：匹配优势。
- `candidateInfo.disadvantageDesc`（string）：不匹配项。
- `candidateInfo.dialogueHistory`（string）：与候选人的沟通记录，Markdown格式。
- `candidateInfo.resumeFile`（object）：简历文件。
- `candidateInfo.resumeFile.fileName`（string，必填）：文件名。
- `candidateInfo.resumeFile.downloadUrl`（string，必填）：下载地址。
- `candidateInfo.resumeFile.expiresAt`（long，必填）：下载地址失效时间，毫秒时间戳。
- `taskInfo`（object）：任务事件信息。scope为task时必填。
- `taskInfo.endedAt`（long）：任务结束时间，毫秒时间戳。
- `taskInfo.jobs`（array，必填）：任务关联的来源职位列表。
- `taskInfo.jobs[].jobId`（string，必填）：职位ID。
- `taskInfo.jobs[].jobName`（string，必填）：职位名称。
- `taskInfo.startedAt`（long，必填）：任务开始时间，毫秒时间戳。
- `taskInfo.status`（string，必填）：任务状态。RUNNING、SUCCESS、FAILED。

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

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.syncAction`（string）：事件动作。任务事件：TASK\_STARTED、TASK\_FINISHED；候选人事件：CANDIDATE\_COLLECTED、CANDIDATE\_GREETED、CANDIDATE\_VIEWED。
- `biz_data.scope`（string）：事件数据范围。task：任务事件；candidate：候选人事件。
- `biz_data.taskId`（string）：Sourcing任务ID。
- `biz_data.taskName`（string）：Sourcing任务名称。
- `biz_data.sourceChannel`（string）：候选人来源渠道。
- `biz_data.ownerUserId`（string）：任务创建人的钉钉用户ID。
- `biz_data.corpId`（string）：企业ID。
- `biz_data.candidateInfo`（object）：候选人事件信息。scope为candidate时必填。
- `biz_data.candidateInfo.matchResult`（object）：候选人匹配结果。
- `biz_data.candidateInfo.matchResult.failedHardCriteria`（array）：未满足的硬性条件。
- `biz_data.candidateInfo.matchResult.pass`（boolean）：是否通过职位匹配。
- `biz_data.candidateInfo.matchResult.summary`（string）：匹配结论。
- `biz_data.candidateInfo.createAt`（long，必填）：候选人创建时间，毫秒时间戳。
- `biz_data.candidateInfo.candidateName`（string，必填）：候选人名称。
- `biz_data.candidateInfo.jobId`（string，必填）：候选人所属的职位ID。
- `biz_data.candidateInfo.jobName`（string，必填）：候选人所属的职位名称。
- `biz_data.candidateInfo.sex`（integer）：候选人性别。1男，2女
- `biz_data.candidateInfo.age`（integer）：候选人年龄。
- `biz_data.candidateInfo.phone`（string）：候选人手机号。
- `biz_data.candidateInfo.email`（string）：候选人邮箱。
- `biz_data.candidateInfo.location`（string）：候选人现居地。
- `biz_data.candidateInfo.workYears`（integer）：候选人工作年限
- `biz_data.candidateInfo.education`（string）：候选人最高学历。
- `biz_data.candidateInfo.matchScore`（integer）：匹配分数，取值范围0至100。
- `biz_data.candidateInfo.aiSummary`（string）：AI匹配总结。
- `biz_data.candidateInfo.advantageDesc`（string）：匹配优势。
- `biz_data.candidateInfo.disadvantageDesc`（string）：不匹配项。
- `biz_data.candidateInfo.dialogueHistory`（string）：与候选人的沟通记录，Markdown格式。
- `biz_data.candidateInfo.resumeFile`（object）：简历文件。
- `biz_data.candidateInfo.resumeFile.fileName`（string，必填）：文件名。
- `biz_data.candidateInfo.resumeFile.downloadUrl`（string，必填）：下载地址。
- `biz_data.candidateInfo.resumeFile.expiresAt`（long，必填）：下载地址失效时间，毫秒时间戳。
- `biz_data.taskInfo`（object）：任务事件信息。scope为task时必填。
- `biz_data.taskInfo.endedAt`（long）：任务结束时间，毫秒时间戳。
- `biz_data.taskInfo.jobs`（array，必填）：任务关联的来源职位列表。
- `biz_data.taskInfo.jobs[].jobId`（string，必填）：职位ID。
- `biz_data.taskInfo.jobs[].jobName`（string，必填）：职位名称。
- `biz_data.taskInfo.startedAt`（long，必填）：任务开始时间，毫秒时间戳。
- `biz_data.taskInfo.status`（string，必填）：任务状态。RUNNING、SUCCESS、FAILED。

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
