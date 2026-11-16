---
title: "请假、加班、出差、外出状态变更事件"
source_url: "https://open.dingtalk.com/document/development/leave-overtime-business-trip-out-of-office-status-change-events"
namespace: "development"
slug: "leave-overtime-business-trip-out-of-office-status-change-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 请假、加班、出差、外出状态变更事件"
doc_id: "LQyk61FQ8g"
updated_at: "2025-08-28 19:46:58"
---

> Source: https://open.dingtalk.com/document/development/leave-overtime-business-trip-out-of-office-status-change-events
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 请假、加班、出差、外出状态变更事件
> Updated: 2025-08-28 19:46:58

# 请假、加班、出差、外出状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 请假、加班、出差、外出状态变更事件 |
| 英文名称 | attendance\_approve\_status\_change |

## 功能描述

当钉钉审批单状态变更时，钉钉通过事件订阅的方式将审批单变更内容推送给开发者。
状态变更包括：发起、审批完成、撤销、删除

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
- `data.corpId`（string）：企业ID。
- `data.processInstanceId`（string）：流程唯一标识。
- `data.mainProcessInstanceId`（string）：主流程实例标识。
- `data.processCode`（string）：流程标识。
- `data.approveType`（string）：审批单类型：  
  \* LEAVE：请假  
  \* OVERTIME：加班  
  \* TRAVEL：外出  
  \* OUT：出差
- `data.status`（string）：审批单状态：  
  \* start：发起  
  \* finish：审批完成  
  \* terminate：撤销  
  \* delete：删除

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "attendance_approve_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "approveType": "LEAVE",
    "processInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "mainProcessInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "corpId": "dingxxxx",
    "processCode": "xxxx",
    "status": "start"
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
- `corpId`（string，必填）：企业ID。
- `processInstanceId`（string，必填）：流程唯一标识。
- `mainProcessInstanceId`（string）：主流程实例标识。
- `processCode`（string，必填）：流程标识。
- `approveType`（string，必填）：审批单类型：  
  \* LEAVE：请假  
  \* OVERTIME：加班  
  \* TRAVEL：外出  
  \* OUT：出差
- `status`（string，必填）：审批单状态：  
  \* start：发起  
  \* finish：审批完成  
  \* terminate：撤销  
  \* delete：删除

### **事件体示例**

```
{
  "EventType": "attendance_approve_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "approveType": "LEAVE",
  "processInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
  "mainProcessInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
  "corpId": "dingxxxx",
  "processCode": "xxxx",
  "status": "start"
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
- `biz_data.corpId`（string）：企业ID。
- `biz_data.processInstanceId`（string）：流程唯一标识。
- `biz_data.mainProcessInstanceId`（string）：主流程实例标识。
- `biz_data.processCode`（string）：流程标识。
- `biz_data.approveType`（string）：审批单类型：  
  \* LEAVE：请假  
  \* OVERTIME：加班  
  \* TRAVEL：外出  
  \* OUT：出差
- `biz_data.status`（string）：审批单状态：  
  \* start：发起  
  \* finish：审批完成  
  \* terminate：撤销  
  \* delete：删除

### **biz\_data数据示例(biz\_type=344)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 344,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "approveType": "LEAVE",
    "processInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "mainProcessInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "corpId": "dingxxxx",
    "syncAction": "attendance_approve_status_change",
    "processCode": "xxxx",
    "status": "start"
  }
}
```
