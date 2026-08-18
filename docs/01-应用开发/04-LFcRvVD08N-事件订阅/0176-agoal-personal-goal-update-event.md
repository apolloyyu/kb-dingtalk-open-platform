---
title: "Agoal个人目标更新事件"
source_url: "https://open.dingtalk.com/document/development/agoal-personal-goal-update-event"
namespace: "development"
slug: "agoal-personal-goal-update-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal个人目标更新事件"
doc_id: "rtwKvTCaPv"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/agoal-personal-goal-update-event
> Path: 应用开发 / 事件订阅 / Agoal > Agoal个人目标更新事件
> Updated: 2022-01-19 19:29:22

# Agoal个人目标更新事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal个人目标更新事件 |
| 英文名称 | agoal\_objective\_change |

## 功能描述

Agoal个人目标更新事件：当用户在Agoal中修改个人目标内容或更新进展时，会发送事件通知订阅方个人目标的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步更新目标相关信息。

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
  "eventType": "agoal_objective_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding23124fdfwdhifhsdih",
    "bizid": "djidf24234237dsduhwe",
    "eventTime": "1774234239",
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
  "EventType": "agoal_objective_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "ding23124fdfwdhifhsdih",
  "bizid": "djidf24234237dsduhwe",
  "eventTime": "1774234239",
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

### **biz\_data数据示例(biz\_type=423)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 423,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "ding23124fdfwdhifhsdih",
    "syncAction": "agoal_objective_change",
    "bizid": "djidf24234237dsduhwe",
    "eventTime": "1774234239",
    "body": {
      "dingUserId": "2639400000-1812711000",
      "periodId": "662e006fe4b0f579bbcccccc",
      "objectiveId": "662e006fe4b0f579bbcxxxxx",
      "objectiveRuleId": "662e006fe4b0f579bbcbbbbb"
    }
  }
}
```
