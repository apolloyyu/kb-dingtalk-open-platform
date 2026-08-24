---
title: "人事档案变动"
source_url: "https://open.dingtalk.com/document/development/personnel-file-change"
namespace: "development"
slug: "personnel-file-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 人事档案变动"
doc_id: "svQy1D6hNE"
updated_at: "2025-08-28 19:47:02"
---

> Source: https://open.dingtalk.com/document/development/personnel-file-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 人事档案变动
> Updated: 2025-08-28 19:47:02

# 人事档案变动

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事档案变动 |
| 英文名称 | hrm\_user\_record\_change |

## 功能描述

智能人事相关事件，eventType为hrm\_user\_record\_change，表示人事档案变动事件数据。

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
- `data.actionType`（string）：触发事件的动作类型。
- `data.staffId`（string）：发生人事变更的员工的ID。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "hrm_user_record_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "actionType": "userInfoChange",
    "staffId": "15996141263318674"
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
- `actionType`（string）：触发事件的动作类型。
- `staffId`（string）：发生人事变更的员工的ID。

### **事件体示例**

```
{
  "EventType": "hrm_user_record_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "actionType": "userInfoChange",
  "staffId": "15996141263318674"
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
- `biz_data.actionType`（string）：触发事件的动作类型。
- `biz_data.staffId`（string）：发生人事变更的员工的ID。

### **biz\_data数据示例(biz\_type=309)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 309,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "actionType": "userInfoChange",
    "syncAction": "hrm_user_record_change",
    "staffId": "15996141263318674"
  }
}
```
