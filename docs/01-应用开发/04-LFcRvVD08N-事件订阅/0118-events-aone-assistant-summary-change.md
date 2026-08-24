---
title: "DingTalkA1小助理总结完成事件"
source_url: "https://open.dingtalk.com/document/development/events-aone-assistant-summary-change"
namespace: "development"
slug: "events-aone-assistant-summary-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > DingTalk A1 > DingTalkA1小助理总结完成事件"
doc_id: "Neg0hWN3QK"
updated_at: "2026-07-01 17:49:27"
---

> Source: https://open.dingtalk.com/document/development/events-aone-assistant-summary-change
> Path: 应用开发 / 事件订阅 / 智能硬件 > DingTalk A1 > DingTalkA1小助理总结完成事件
> Updated: 2026-07-01 17:49:27

# DingTalkA1小助理总结完成事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | DingTalkA1小助理总结完成事件 |
| 英文名称 | aone\_assistant\_summary\_change |

## 功能描述

DingTalkA1小助理执行分析结果事件

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
- `data.agentId`（string）：A1小助理id
- `data.agentResult`（object）：A1小助理执行结果
- `data.agentResult.promptTemplateResults`（array）：提示词模板结果
- `data.agentResult.promptTemplateResults[].summary`（string）：总结内容
- `data.agentResult.promptTemplateResults[].templateId`（string）：提示词模板id
- `data.agentResult.promptTemplateResults[].title`（string）：总结标题
- `data.creatorUnionId`（string）：创建人unionId
- `data.fileId`（string）：A1文件id
- `data.minutesId`（string）：A1文件听记id

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aone_assistant_summary_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": "1234-test",
    "agentResult": {
      "promptTemplateResults": [
        {
          "summary": "测试总结内容",
          "title": "test-title",
          "templateId": "test-templateId"
        }
      ]
    },
    "creatorUnionId": "z8zszxxxxxQiEiE",
    "fileId": "54a7ff9f-xxxxxx-0",
    "minutesId": "763275696xxxxxx"
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
- `agentId`（string）：A1小助理id
- `agentResult`（object）：A1小助理执行结果
- `agentResult.promptTemplateResults`（array）：提示词模板结果
- `agentResult.promptTemplateResults[].summary`（string）：总结内容
- `agentResult.promptTemplateResults[].templateId`（string）：提示词模板id
- `agentResult.promptTemplateResults[].title`（string）：总结标题
- `creatorUnionId`（string）：创建人unionId
- `fileId`（string）：A1文件id
- `minutesId`（string）：A1文件听记id

### **事件体示例**

```
{
  "EventType": "aone_assistant_summary_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "agentId": "1234-test",
  "agentResult": {
    "promptTemplateResults": [
      {
        "summary": "测试总结内容",
        "title": "test-title",
        "templateId": "test-templateId"
      }
    ]
  },
  "creatorUnionId": "z8zszxxxxxQiEiE",
  "fileId": "54a7ff9f-xxxxxx-0",
  "minutesId": "763275696xxxxxx"
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
- `biz_data.agentId`（string）：A1小助理id
- `biz_data.agentResult`（object）：A1小助理执行结果
- `biz_data.agentResult.promptTemplateResults`（array）：提示词模板结果
- `biz_data.agentResult.promptTemplateResults[].summary`（string）：总结内容
- `biz_data.agentResult.promptTemplateResults[].templateId`（string）：提示词模板id
- `biz_data.agentResult.promptTemplateResults[].title`（string）：总结标题
- `biz_data.creatorUnionId`（string）：创建人unionId
- `biz_data.fileId`（string）：A1文件id
- `biz_data.minutesId`（string）：A1文件听记id

### **biz\_data数据示例(biz\_type=468)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 468,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "agentId": "1234-test",
    "syncAction": "aone_assistant_summary_change",
    "agentResult": {
      "promptTemplateResults": [
        {
          "summary": "测试总结内容",
          "title": "test-title",
          "templateId": "test-templateId"
        }
      ]
    },
    "creatorUnionId": "z8zszxxxxxQiEiE",
    "fileId": "54a7ff9f-xxxxxx-0",
    "minutesId": "763275696xxxxxx"
  }
}
```
