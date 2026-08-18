---
title: "打卡任务删除"
source_url: "https://open.dingtalk.com/document/development/events-edu-card-delete"
namespace: "development"
slug: "events-edu-card-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 打卡任务删除"
doc_id: "aPlz0LcrF7"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-edu-card-delete
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 打卡任务删除
> Updated: 2022-01-19 19:29:22

# 打卡任务删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 打卡任务删除 |
| 英文名称 | edu\_card\_delete |

## 功能描述

新教育2.0，组织打卡任务删除事件。当已创建且未结束的打卡任务被删除时，触发此事件的推送。

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
  "eventType": "edu_card_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "ding2ecXXXa30eb",
    "bizid": "c_123_delete",
    "eventTime": "1783515295256",
    "eventType": "edu_card_delete",
    "body": {
      "opsType": "delete",
      "corpid": "ding2ecXXXa30eb",
      "cardid": 456789,
      "bizid": "c_123_delete",
      "operatorName": "张三"
    }
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "edu_card_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "event_type": "edu_card_delete",
  "corpid": "ding2ecXXXa30eb",
  "bizid": "c_123_delete",
  "body": {
    "opsType": "delete",
    "corpid": "ding2ecXXXa30eb",
    "cardid": 456789,
    "bizid": "c_123_delete",
    "operatorName": "张三"
  },
  "event_time": "1783515295256"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=499)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 499,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "event_type": "edu_card_delete",
    "corpid": "ding2ecXXXa30eb",
    "syncAction": "edu_card_delete",
    "bizid": "c_123_delete",
    "body": {
      "opsType": "delete",
      "corpid": "ding2ecXXXa30eb",
      "cardid": 456789,
      "bizid": "c_123_delete",
      "operatorName": "张三"
    },
    "event_time": "1783515295256"
  }
}
```
