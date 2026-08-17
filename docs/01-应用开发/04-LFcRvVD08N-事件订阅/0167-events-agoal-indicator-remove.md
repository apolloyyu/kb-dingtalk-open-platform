---
title: "Agoal删除指标事件"
source_url: "https://open.dingtalk.com/document/development/events-agoal-indicator-remove"
namespace: "development"
slug: "events-agoal-indicator-remove"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal删除指标事件"
doc_id: "ngOs2Fjpeu"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-agoal-indicator-remove
> Path: 应用开发 / 事件订阅 / Agoal > Agoal删除指标事件
> Updated: 2022-01-19 19:29:22

# Agoal删除指标事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal删除指标事件 |
| 英文名称 | agoal\_indicator\_remove |

## 功能描述

Agoal删除指标事件：当Agoal管理员在Agoal中删除指标时，会发送事件通知订阅方被删除指标的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步被删除指标相关信息。

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
  "eventType": "agoal_indicator_remove",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "dingsdlkfwoerlsdfjo09u4902385",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "23124234234234",
    "body": {
      "code": "code_k8j7h9j6h8kk987",
      "id": "h73h4ydgh47fh546d"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "agoal_indicator_remove",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "dingsdlkfwoerlsdfjo09u4902385",
  "bizid": "djk23894jfkleuid8djf",
  "body": {
    "code": "code_k8j7h9j6h8kk987",
    "id": "h73h4ydgh47fh546d"
  },
  "event_time": "23124234234234"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=452)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 452,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "dingsdlkfwoerlsdfjo09u4902385",
    "syncAction": "agoal_indicator_remove",
    "bizid": "djk23894jfkleuid8djf",
    "body": {
      "code": "code_k8j7h9j6h8kk987",
      "id": "h73h4ydgh47fh546d"
    },
    "event_time": "23124234234234"
  }
}
```
