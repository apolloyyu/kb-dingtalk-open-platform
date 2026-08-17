---
title: "人事解决方案变更事件"
source_url: "https://open.dingtalk.com/document/development/personnel-solution-change-event"
namespace: "development"
slug: "personnel-solution-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 人事解决方案变更事件"
doc_id: "Y5NNdMBg4M"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/personnel-solution-change-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 人事解决方案变更事件
> Updated: 2022-01-19 19:29:22

# 人事解决方案变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事解决方案变更事件 |
| 英文名称 | hrm\_solution\_manage |

## 功能描述

人事解决方案变更事件数据。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "hrm_solution_manage",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "ding57935b18bfd13e9735cxxxxxxxxxx",
    "staffIds": [
      "157087xxxxxxxx"
    ],
    "solutionType": "onboarding",
    "solutionStatus": "start"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "hrm_solution_manage",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpId": "ding57935b18bfd13e9735cxxxxxxxxxx",
  "staffIds": [
    "157087xxxxxxxx"
  ],
  "solutionType": "onboarding",
  "solutionStatus": "start"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=175)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 175,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "ding57935b18bfd13e9735cxxxxxxxxxx",
    "staffIds": [
      "157087xxxxxxxx"
    ],
    "syncAction": "hrm_solution_manage",
    "solutionType": "onboarding",
    "solutionStatus": "start"
  }
}
```
