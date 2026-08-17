---
title: "打卡任务更新"
source_url: "https://open.dingtalk.com/document/development/events-edu-card-update"
namespace: "development"
slug: "events-edu-card-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 打卡任务更新"
doc_id: "V1OsYir4zv"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-edu-card-update
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 打卡任务更新
> Updated: 2022-01-19 19:29:22

# 打卡任务更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 打卡任务更新 |
| 英文名称 | edu\_card\_update |

## 功能描述

新教育2.0，对已创建且未结束、未删除的打卡任务进行信息更新时，触发此事件的推送。

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
  "eventType": "edu_card_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding2fecXXX3acb6",
    "bizid": "c_123_update",
    "eventTime": 1783561906863,
    "eventType": "edu_card_update",
    "body": {
      "opsType": "update",
      "corpId": "ding2fecXXX3acb6",
      "cardId": 123,
      "bizid": "c_123_update",
      "opertorName": "张三"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "edu_card_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "event_type": "edu_card_update",
  "corpid": "ding2fecXXX3acb6",
  "bizid": "c_123_update",
  "body": {
    "opsType": "update",
    "corpId": "ding2fecXXX3acb6",
    "cardId": 123,
    "bizid": "c_123_update",
    "opertorName": "张三"
  },
  "event_time": 1783561906863
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=501)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 501,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "event_type": "edu_card_update",
    "corpid": "ding2fecXXX3acb6",
    "syncAction": "edu_card_update",
    "bizid": "c_123_update",
    "body": {
      "opsType": "update",
      "corpId": "ding2fecXXX3acb6",
      "cardId": 123,
      "bizid": "c_123_update",
      "opertorName": "张三"
    },
    "event_time": 1783561906863
  }
}
```
