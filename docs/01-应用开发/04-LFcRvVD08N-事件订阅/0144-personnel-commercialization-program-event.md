---
title: "人事商业化方案事件"
source_url: "https://open.dingtalk.com/document/development/personnel-commercialization-program-event"
namespace: "development"
slug: "personnel-commercialization-program-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 人事商业化方案事件"
doc_id: "KgTl28k3IR"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/personnel-commercialization-program-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 人事商业化方案事件
> Updated: 2022-01-19 19:29:22

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
