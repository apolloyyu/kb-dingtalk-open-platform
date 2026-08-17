---
title: "Agoal新增目标进展事件"
source_url: "https://open.dingtalk.com/document/development/events-agoal-objectiveprogress-add"
namespace: "development"
slug: "events-agoal-objectiveprogress-add"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "Agoal > Agoal新增目标进展事件"
doc_id: "p1TA5ggbM4"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-agoal-objectiveprogress-add
> Path: 应用开发 / 事件订阅 / Agoal > Agoal新增目标进展事件
> Updated: 2022-01-19 19:29:22

# Agoal新增目标进展事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Agoal新增目标进展事件 |
| 英文名称 | agoal\_objectiveProgress\_add |

## 功能描述

Agoal新增目标进展事件：当用户在Agoal中新增目标进展时，会发送事件通知订阅方目标进展的信息，主要是用来给三方合作伙伴使用，合作伙伴接收事件以同步新增目标进展相关信息。

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
  "eventType": "agoal_objectiveProgress_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding23980uodfijladkfja",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "1774522643",
    "body": {
      "progressId": "234584cs33xd368xxx",
      "objectiveId": "57834cs33dd318xxx"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "agoal_objectiveProgress_add",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "ding23980uodfijladkfja",
  "bizid": "djk23894jfkleuid8djf",
  "eventTime": "1774522643",
  "body": {
    "progressId": "234584cs33xd368xxx",
    "objectiveId": "57834cs33dd318xxx"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=455)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 455,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "ding23980uodfijladkfja",
    "syncAction": "agoal_objectiveProgress_add",
    "bizid": "djk23894jfkleuid8djf",
    "eventTime": "1774522643",
    "body": {
      "progressId": "234584cs33xd368xxx",
      "objectiveId": "57834cs33dd318xxx"
    }
  }
}
```
