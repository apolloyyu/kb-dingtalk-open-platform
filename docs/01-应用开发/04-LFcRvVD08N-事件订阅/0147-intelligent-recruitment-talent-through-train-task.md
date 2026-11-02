---
title: "智能招聘人才直通车任务"
source_url: "https://open.dingtalk.com/document/development/intelligent-recruitment-talent-through-train-task"
namespace: "development"
slug: "intelligent-recruitment-talent-through-train-task"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 智能招聘人才直通车任务"
doc_id: "N4QWJLSYjw"
updated_at: "2025-08-28 19:47:00"
---

> Source: https://open.dingtalk.com/document/development/intelligent-recruitment-talent-through-train-task
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 智能招聘人才直通车任务
> Updated: 2025-08-28 19:47:00

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.corpId`（string）：企业标识。
- `data.talentSearchConditionsVO`（object）：人才检索信息。
- `data.talentSearchConditionsVO.maxSalary`（integer，必填）：最大薪资。
- `data.talentSearchConditionsVO.education`（array，必填）：教育经历枚举。
- `data.talentSearchConditionsVO.maxAge`（integer，必填）：最大年龄。
- `data.talentSearchConditionsVO.minAge`（integer，必填）：最小年龄。
- `data.talentSearchConditionsVO.workingYear`（array，必填）：工作年限枚举。
- `data.talentSearchConditionsVO.minSalary`（integer，必填）：最小薪资。
- `data.jobId`（string）：职位标识。
- `data.configId`（string）：配置标识。
- `data.taskId`（string）：任务标识。
- `data.userId`（string）：员工userId。
- `data.autoChatSettingVO`（object）：开聊设置。
- `data.autoChatSettingVO.chatNum`（integer，必填）：开聊人数。
- `data.autoChatSettingVO.chatWord`（string，必填）：开聊语。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.corpId`（string）：企业标识。
- `biz_data.talentSearchConditionsVO`（object）：人才检索信息。
- `biz_data.talentSearchConditionsVO.maxSalary`（integer，必填）：最大薪资。
- `biz_data.talentSearchConditionsVO.education`（array，必填）：教育经历枚举。
- `biz_data.talentSearchConditionsVO.maxAge`（integer，必填）：最大年龄。
- `biz_data.talentSearchConditionsVO.minAge`（integer，必填）：最小年龄。
- `biz_data.talentSearchConditionsVO.workingYear`（array，必填）：工作年限枚举。
- `biz_data.talentSearchConditionsVO.minSalary`（integer，必填）：最小薪资。
- `biz_data.jobId`（string）：职位标识。
- `biz_data.configId`（string）：配置标识。
- `biz_data.taskId`（string）：任务标识。
- `biz_data.userId`（string）：员工userId。
- `biz_data.autoChatSettingVO`（object）：开聊设置。
- `biz_data.autoChatSettingVO.chatNum`（integer，必填）：开聊人数。
- `biz_data.autoChatSettingVO.chatWord`（string，必填）：开聊语。

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
