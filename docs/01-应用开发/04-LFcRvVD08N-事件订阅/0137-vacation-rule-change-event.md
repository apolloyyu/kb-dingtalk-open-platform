---
title: "假期规则变更事件"
source_url: "https://open.dingtalk.com/document/development/vacation-rule-change-event"
namespace: "development"
slug: "vacation-rule-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 假期规则变更事件"
doc_id: "UOoeFOLX6K"
updated_at: "2025-08-28 19:46:56"
---

> Source: https://open.dingtalk.com/document/development/vacation-rule-change-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 假期规则变更事件
> Updated: 2025-08-28 19:46:56

# 假期规则变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 假期规则变更事件 |
| 英文名称 | leave\_rule\_change |

## 功能描述

当假期规则变更时，钉钉通过事件订阅的方式将规则变更内容推送给开发者。
规则变更包括：增、删、改

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
- `data.corpId`（string）：企业Id。
- `data.leaveCodes`（array）：假期类型。
- `data.action`（string）：规则更改类型：  
  \* init：初始  
  \* add：增加  
  \* delete：删除  
  \* modify：修改

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "leave_rule_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "dingxxxxx",
    "leaveCodes": [
      "xxxx"
    ],
    "action": "add"
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
- `corpId`（string，必填）：企业Id。
- `leaveCodes`（array，必填）：假期类型。
- `action`（string，必填）：规则更改类型：  
  \* init：初始  
  \* add：增加  
  \* delete：删除  
  \* modify：修改

### **事件体示例**

```
{
  "EventType": "leave_rule_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpId": "dingxxxxx",
  "leaveCodes": [
    "xxxx"
  ],
  "action": "add"
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
- `biz_data.corpId`（string）：企业Id。
- `biz_data.leaveCodes`（array）：假期类型。
- `biz_data.action`（string）：规则更改类型：  
  \* init：初始  
  \* add：增加  
  \* delete：删除  
  \* modify：修改

### **biz\_data数据示例(biz\_type=346)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 346,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "dingxxxxx",
    "syncAction": "leave_rule_change",
    "leaveCodes": [
      "xxxx"
    ],
    "action": "add"
  }
}
```
