---
title: "Teambiton工时变更事件"
source_url: "https://open.dingtalk.com/document/development/event-project-worktime-updated"
namespace: "development"
slug: "event-project-worktime-updated"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 项目管理 > Teambiton工时变更事件"
doc_id: "SLcSImeuQx"
updated_at: "2025-08-27 16:10:54"
---

> Source: https://open.dingtalk.com/document/development/event-project-worktime-updated
> Path: 应用开发 / 事件订阅 / 协同 > 项目管理 > Teambiton工时变更事件
> Updated: 2025-08-27 16:10:54

# Teambiton工时变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Teambiton工时变更事件 |
| 英文名称 | project\_worktime\_updated |

## 功能描述

当Teambiton项目中工时属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中工时属性内容的变更推送给开发者，用于监听项目中工时属性更新的信息。

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
- `data.eventSubType`（string）：事件子类型：  
  \* \*\*worktime.create\*\*：工时创建。  
  \* \*\*worktime.approve\*\*：工时审批。
- `data.executorId`（string）：工时执行人。
- `data.userId`（string）：操作人。
- `data.taskId`（string）：tb任务id。
- `data.workTimeIds`（array）：工时id集合。
- `data.workTime`（integer）：实际工时数，单位：ms。
- `data.dates`（string）：填报日期。
- `data.approveOpenId`（string）：tb侧关联ID，回写状态时入参。
- `data.action`（string）：触发动作：  
    
  \* \*\*create\*\*：创建时触发。  
  \* \*\*re-submit\*\*：再次提交。
- `data.created`（string）：创建时间。
- `data.updated`（string）：更新时间。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "project_worktime_updated",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "eventSubType": "worktime.create",
    "executorId": "0715153011125xxxx",
    "created": "2023-04-13T00:00:00Z",
    "approveOpenId": "63c7f91f6ff268bcab40xxxx",
    "action": "re-submit",
    "dates": "2023-04-13T00:00:00Z",
    "userId": "0715153011125xxxx",
    "updated": "2023-04-13T00:00:00Z",
    "workTime": 100000,
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "workTimeIds": [
      "63c7f91f6ff268bcab40xxxx"
    ]
  }
}
```

HTTP推送

### data

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `eventSubType`（string，必填）：事件子类型：  
  \* \*\*worktime.create\*\*：工时创建。  
  \* \*\*worktime.approve\*\*：工时审批。
- `executorId`（string，必填）：工时执行人。
- `userId`（string，必填）：操作人。
- `taskId`（string，必填）：tb任务id。
- `workTimeIds`（array，必填）：工时id集合。
- `workTime`（integer，必填）：实际工时数，单位：ms。
- `dates`（string，必填）：填报日期。
- `approveOpenId`（string，必填）：tb侧关联ID，回写状态时入参。
- `action`（string，必填）：触发动作：  
    
  \* \*\*create\*\*：创建时触发。  
  \* \*\*re-submit\*\*：再次提交。
- `created`（string，必填）：创建时间。
- `updated`（string，必填）：更新时间。

### **事件体示例**

```
{
  "EventType": "project_worktime_updated",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventSubType": "worktime.create",
  "executorId": "0715153011125xxxx",
  "created": "2023-04-13T00:00:00Z",
  "approveOpenId": "63c7f91f6ff268bcab40xxxx",
  "action": "re-submit",
  "dates": "2023-04-13T00:00:00Z",
  "userId": "0715153011125xxxx",
  "updated": "2023-04-13T00:00:00Z",
  "workTime": 100000,
  "taskId": "63c7f91f6ff268bcab40xxxx",
  "workTimeIds": [
    "63c7f91f6ff268bcab40xxxx"
  ]
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### data

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.eventSubType`（string）：事件子类型：  
  \* \*\*worktime.create\*\*：工时创建。  
  \* \*\*worktime.approve\*\*：工时审批。
- `biz_data.executorId`（string）：工时执行人。
- `biz_data.userId`（string）：操作人。
- `biz_data.taskId`（string）：tb任务id。
- `biz_data.workTimeIds`（array）：工时id集合。
- `biz_data.workTime`（integer）：实际工时数，单位：ms。
- `biz_data.dates`（string）：填报日期。
- `biz_data.approveOpenId`（string）：tb侧关联ID，回写状态时入参。
- `biz_data.action`（string）：触发动作：  
    
  \* \*\*create\*\*：创建时触发。  
  \* \*\*re-submit\*\*：再次提交。
- `biz_data.created`（string）：创建时间。
- `biz_data.updated`（string）：更新时间。

### **biz\_data数据示例(biz\_type=297)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 297,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "eventSubType": "worktime.create",
    "syncAction": "project_worktime_updated",
    "executorId": "0715153011125xxxx",
    "created": "2023-04-13T00:00:00Z",
    "approveOpenId": "63c7f91f6ff268bcab40xxxx",
    "dates": "2023-04-13T00:00:00Z",
    "userId": "0715153011125xxxx",
    "workTime": 100000,
    "action": "re-submit",
    "updated": "2023-04-13T00:00:00Z",
    "taskId": "63c7f91f6ff268bcab40xxxx",
    "workTimeIds": [
      "63c7f91f6ff268bcab40xxxx"
    ]
  }
}
```
