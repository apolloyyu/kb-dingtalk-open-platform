---
title: "打卡任务结束"
source_url: "https://open.dingtalk.com/document/development/events-edu-card-end"
namespace: "development"
slug: "events-edu-card-end"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 打卡任务结束"
doc_id: "Ub1QWJewRL"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-edu-card-end
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 打卡任务结束
> Updated: 2022-01-19 19:29:22

# 打卡任务结束

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 打卡任务结束 |
| 英文名称 | edu\_card\_end |

## 功能描述

新教育2.0，当打卡任务被提前结束时，触发此事件的推送。

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
  "eventType": "edu_card_end",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding123aefXXXef2c",
    "bizid": "c_123_end",
    "eventTime": 1783561094858,
    "eventType": "edu_card_end",
    "body": {
      "opsType": "end",
      "corpId": "ding123aefXXXef2c",
      "cardId": 123,
      "bizid": "c_123_end",
      "operatorName": "张三"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "edu_card_end",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "event_type": "edu_card_end",
  "corpid": "ding123aefXXXef2c",
  "bizid": "c_123_end",
  "body": {
    "opsType": "end",
    "corpId": "ding123aefXXXef2c",
    "cardId": 123,
    "bizid": "c_123_end",
    "operatorName": "张三"
  },
  "event_time": 1783561094858
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=500)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 500,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "event_type": "edu_card_end",
    "corpid": "ding123aefXXXef2c",
    "syncAction": "edu_card_end",
    "bizid": "c_123_end",
    "body": {
      "opsType": "end",
      "corpId": "ding123aefXXXef2c",
      "cardId": 123,
      "bizid": "c_123_end",
      "operatorName": "张三"
    },
    "event_time": 1783561094858
  }
}
```
