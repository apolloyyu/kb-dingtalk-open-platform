---
title: "群模板被启用或停用"
source_url: "https://open.dingtalk.com/document/development/group-templates-are-enabled-or-disabled"
namespace: "development"
slug: "group-templates-are-enabled-or-disabled"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 会话管理 > 群模板被启用或停用"
doc_id: "m6hhdsEUUr"
updated_at: "2025-08-28 19:46:45"
---

> Source: https://open.dingtalk.com/document/development/group-templates-are-enabled-or-disabled
> Path: 应用开发 / 事件订阅 / 即时通讯 > 会话管理 > 群模板被启用或停用
> Updated: 2025-08-28 19:46:45

# 群模板被启用或停用

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群模板被启用或停用 |
| 英文名称 | chat\_template\_change |

## 功能描述

群模板被启用或停用时，给订阅了该事件的开发者推送的数据。

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
- `data.timeStamp`（long）：时间戳。
- `data.operatorUnionId`（string）：操作人员的unionId。
- `data.templateId`（string）：群模板ID。
- `data.changedTimeStamp`（long）：变更时间戳。
- `data.openConversationId`（string）：群ID。
- `data.operator`（string）：操作人员的userid。
- `data.status`（string）：群模板状态。  
  - on表示启用群模板  
  - off表示停用群模板

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "chat_template_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": 43535463645,
    "operatorUnionId": "evdsxxx",
    "templateId": "1111abcd-1234-1234-dcba-123456789012",
    "changedTimeStamp": 43535463645,
    "openConversationId": "cidff2312123ee",
    "operator": "manager0112",
    "status": "on"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `timeStamp`（long）：时间戳。
- `operatorUnionId`（string）：操作人员的unionId。
- `templateId`（string）：群模板ID。
- `changedTimeStamp`（long）：变更时间戳。
- `openConversationId`（string）：群ID。
- `operator`（string）：操作人员的userid。
- `status`（string）：群模板状态。  
  - on表示启用群模板  
  - off表示停用群模板

### **事件体示例**

```
{
  "EventType": "chat_template_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": 43535463645,
  "operatorUnionId": "evdsxxx",
  "templateId": "1111abcd-1234-1234-dcba-123456789012",
  "changedTimeStamp": 43535463645,
  "openConversationId": "cidff2312123ee",
  "operator": "manager0112",
  "status": "on"
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
- `biz_data.timeStamp`（long）：时间戳。
- `biz_data.operatorUnionId`（string）：操作人员的unionId。
- `biz_data.templateId`（string）：群模板ID。
- `biz_data.changedTimeStamp`（long）：变更时间戳。
- `biz_data.openConversationId`（string）：群ID。
- `biz_data.operator`（string）：操作人员的userid。
- `biz_data.status`（string）：群模板状态。  
  - on表示启用群模板  
  - off表示停用群模板

### **biz\_data数据示例(biz\_type=306)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 306,
  "biz_data": {
    "timeStamp": 43535463645,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "chat_template_change",
    "operatorUnionId": "evdsxxx",
    "templateId": "1111abcd-1234-1234-dcba-123456789012",
    "changedTimeStamp": 43535463645,
    "openConversationId": "cidff2312123ee",
    "operator": "manager0112",
    "status": "on"
  }
}
```
