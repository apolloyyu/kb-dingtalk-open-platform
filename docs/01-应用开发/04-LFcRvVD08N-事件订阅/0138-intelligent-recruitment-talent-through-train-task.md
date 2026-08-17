---
title: "智能招聘人才直通车任务"
source_url: "https://open.dingtalk.com/document/development/intelligent-recruitment-talent-through-train-task"
namespace: "development"
slug: "intelligent-recruitment-talent-through-train-task"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 智能招聘人才直通车任务"
doc_id: "N4QWJLSYjw"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/intelligent-recruitment-talent-through-train-task
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 智能招聘人才直通车任务
> Updated: 2022-01-19 19:29:22

# 智能招聘人才直通车任务

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能招聘人才直通车任务 |
| 英文名称 | ats\_talent\_auto\_chat\_task |

## 功能描述

创建人才直通车，仅招聘需求可申请。

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
  "eventType": "ats_talent_auto_chat_task",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "jobId": "jobxxxxx",
    "corpId": "dingxxxxxx",
    "configId": "configxxxx",
    "autoChatSettingVO": {
      "chatNum": 10,
      "chatWord": "你好xxxxx"
    },
    "talentSearchConditionsVO": {
      "maxSalary": 3000,
      "education": [
        1
      ],
      "maxAge": 20,
      "minAge": 30,
      "workingYear": [
        3
      ],
      "minSalary": 1000
    },
    "userId": "xxxx",
    "taskId": "taskxxxxx"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=163)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 163,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "jobId": "jobxxxxx",
    "corpId": "dingxxxxxx",
    "syncAction": "ats_talent_auto_chat_task",
    "configId": "configxxxx",
    "autoChatSettingVO": {
      "chatNum": 10,
      "chatWord": "你好xxxxx"
    },
    "talentSearchConditionsVO": {
      "maxSalary": 3000,
      "education": [
        1
      ],
      "maxAge": 20,
      "minAge": 30,
      "workingYear": [
        3
      ],
      "minSalary": 1000
    },
    "userId": "xxxx",
    "taskId": "taskxxxxx"
  }
}
```
