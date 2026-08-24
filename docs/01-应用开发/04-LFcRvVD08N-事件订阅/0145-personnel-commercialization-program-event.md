---
title: "人事商业化方案事件"
source_url: "https://open.dingtalk.com/document/development/personnel-commercialization-program-event"
namespace: "development"
slug: "personnel-commercialization-program-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 人事商业化方案事件"
doc_id: "KgTl28k3IR"
updated_at: "2025-08-28 19:47:04"
---

> Source: https://open.dingtalk.com/document/development/personnel-commercialization-program-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 人事商业化方案事件
> Updated: 2025-08-28 19:47:04

# 人事商业化方案事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事商业化方案事件 |
| 英文名称 | commercial\_solution |

## 功能描述

人事商业化方案事件，为人事商业化方案的数据变更时的数据的推送数据。

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
- `data.solutionId`（string）：解决方案ID。
- `data.solutionStatus`（string）：解决方案状态：  
  - ENABLE：启用  
  - DISABLE：停用

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "commercial_solution",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "solutionId": "HRM_COMMERCIAL_SOLUTION_ON_BOARDING_TRAIN",
    "solutionStatus": "ENABLE"
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
- `biz_data.solutionId`（string）：解决方案ID。
- `biz_data.solutionStatus`（string）：解决方案状态：  
  - ENABLE：启用  
  - DISABLE：停用

### **biz\_data数据示例(biz\_type=224)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 224,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "commercial_solution",
    "solutionId": "HRM_COMMERCIAL_SOLUTION_ON_BOARDING_TRAIN",
    "solutionStatus": "ENABLE"
  }
}
```
