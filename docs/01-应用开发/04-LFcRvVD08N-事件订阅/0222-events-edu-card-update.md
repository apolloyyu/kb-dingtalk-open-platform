---
title: "打卡任务更新"
source_url: "https://open.dingtalk.com/document/development/events-edu-card-update"
namespace: "development"
slug: "events-edu-card-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 打卡任务更新"
doc_id: "V1OsYir4zv"
updated_at: "2026-07-10 09:48:38"
---

> Source: https://open.dingtalk.com/document/development/events-edu-card-update
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 打卡任务更新
> Updated: 2026-07-10 09:48:38

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.bizid`（string）：全局唯一key，无实际业务意义
- `data.eventTime`（long）：事件产生事件
- `data.corpid`（string）：产生事件的组织id
- `data.eventType`（string）：事件类型
- `data.body`（object）：业务数据
- `data.body.cardId`（long，必填）：更新的打卡任务id
- `data.body.bizid`（string，必填）：全局唯一key，无实际业务意义，用于问题排查
- `data.body.opsType`（string，必填）：操作类型
- `data.body.corpId`（string，必填）：产生事件的组织id
- `data.body.opertorName`（string，必填）：操作人员名称

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `bizid`（string，必填）：全局唯一key，无实际业务意义
- `event_time`（long，必填）：事件产生事件
- `corpid`（string，必填）：产生事件的组织id
- `event_type`（string，必填）：事件类型
- `body`（object，必填）：业务数据
- `body.cardId`（long，必填）：更新的打卡任务id
- `body.bizid`（string，必填）：全局唯一key，无实际业务意义，用于问题排查
- `body.opsType`（string，必填）：操作类型
- `body.corpId`（string，必填）：产生事件的组织id
- `body.opertorName`（string，必填）：操作人员名称

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.bizid`（string）：全局唯一key，无实际业务意义
- `biz_data.event_time`（long）：事件产生事件
- `biz_data.corpid`（string）：产生事件的组织id
- `biz_data.event_type`（string）：事件类型
- `biz_data.body`（object）：业务数据
- `biz_data.body.cardId`（long，必填）：更新的打卡任务id
- `biz_data.body.bizid`（string，必填）：全局唯一key，无实际业务意义，用于问题排查
- `biz_data.body.opsType`（string，必填）：操作类型
- `biz_data.body.corpId`（string，必填）：产生事件的组织id
- `biz_data.body.opertorName`（string，必填）：操作人员名称

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
