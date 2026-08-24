---
title: "打卡任务删除"
source_url: "https://open.dingtalk.com/document/development/events-edu-card-delete"
namespace: "development"
slug: "events-edu-card-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 打卡任务删除"
doc_id: "aPlz0LcrF7"
updated_at: "2026-07-10 09:48:40"
---

> Source: https://open.dingtalk.com/document/development/events-edu-card-delete
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 打卡任务删除
> Updated: 2026-07-10 09:48:40

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.corpid`（string）：产生事件的组织id
- `data.bizid`（string）：事件id，全局唯一，无业务意义
- `data.eventTime`（string）：事件发生时间
- `data.eventType`（string）：额外字段，用于问题排查
- `data.body`（object）：消息体
- `data.body.bizid`（string，必填）：事件id，方便问题排查，由c\_{recordId}\_{opsType}组成
- `data.body.operatorName`（string，必填）：操作人名称
- `data.body.corpid`（string，必填）：产生事件的组织id
- `data.body.opsType`（string，必填）：操作类型
- `data.body.cardid`（long，必填）：删除的cardId

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `event_type`（string，必填）：额外字段，用于问题排查
- `corpid`（string，必填）：产生事件的组织id
- `bizid`（string，必填）：事件id，全局唯一，无业务意义
- `event_time`（string，必填）：事件发生时间
- `body`（object）：消息体
- `body.bizid`（string，必填）：事件id，方便问题排查，由c\_{recordId}\_{opsType}组成
- `body.operatorName`（string，必填）：操作人名称
- `body.corpid`（string，必填）：产生事件的组织id
- `body.opsType`（string，必填）：操作类型
- `body.cardid`（long，必填）：删除的cardId

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.event_type`（string）：额外字段，用于问题排查
- `biz_data.corpid`（string）：产生事件的组织id
- `biz_data.bizid`（string）：事件id，全局唯一，无业务意义
- `biz_data.event_time`（string）：事件发生时间
- `biz_data.body`（object）：消息体
- `biz_data.body.bizid`（string，必填）：事件id，方便问题排查，由c\_{recordId}\_{opsType}组成
- `biz_data.body.operatorName`（string，必填）：操作人名称
- `biz_data.body.corpid`（string，必填）：产生事件的组织id
- `biz_data.body.opsType`（string，必填）：操作类型
- `biz_data.body.cardid`（long，必填）：删除的cardId

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
