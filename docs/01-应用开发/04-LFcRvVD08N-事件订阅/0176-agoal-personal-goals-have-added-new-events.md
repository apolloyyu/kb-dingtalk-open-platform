---
title: "Agoal个人目标新增事件"
source_url: "https://open.dingtalk.com/document/development/agoal-personal-goals-have-added-new-events"
namespace: "development"
slug: "agoal-personal-goals-have-added-new-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal个人目标新增事件"
doc_id: "uIinEeaBrr"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/agoal-personal-goals-have-added-new-events
> Path: 应用开发 / 事件订阅 / Agoal > Agoal个人目标新增事件
> Updated: 2022-01-19 19:29:22

# Agoal个人目标新增事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal个人目标新增事件 |
| 英文名称 | agoal\_objective\_add |

## 功能描述

Agoal个人目标新增事件：当用户在Agoal的员工目标下录入目标时，会发送事件通知订阅方个人目标的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步更新目标相关信息。

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
  "eventType": "agoal_objective_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding9f50b15bxxxx16741",
    "bizid": "dif3423847924dds",
    "eventTime": "1773423492",
    "body": {
      "dingUserId": "2639400000-1812711000",
      "periodId": "662e006fe4b0f579bbcccccc",
      "objectiveId": "662e006fe4b0f579bbcxxxxx",
      "objectiveRuleId": "662e006fe4b0f579bbcbbbbb"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "agoal_objective_add",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "ding9f50b15bxxxx16741",
  "bizid": "dif3423847924dds",
  "eventTime": "1773423492",
  "body": {
    "dingUserId": "2639400000-1812711000",
    "periodId": "662e006fe4b0f579bbcccccc",
    "objectiveId": "662e006fe4b0f579bbcxxxxx",
    "objectiveRuleId": "662e006fe4b0f579bbcbbbbb"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=422)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 422,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "ding9f50b15bxxxx16741",
    "syncAction": "agoal_objective_add",
    "bizid": "dif3423847924dds",
    "eventTime": "1773423492",
    "body": {
      "dingUserId": "2639400000-1812711000",
      "periodId": "662e006fe4b0f579bbcccccc",
      "objectiveId": "662e006fe4b0f579bbcxxxxx",
      "objectiveRuleId": "662e006fe4b0f579bbcbbbbb"
    }
  }
}
```
