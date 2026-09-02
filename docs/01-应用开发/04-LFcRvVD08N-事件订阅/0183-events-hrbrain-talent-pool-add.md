---
title: "组织大脑人才池新增"
source_url: "https://open.dingtalk.com/document/development/events-hrbrain-talent-pool-add"
namespace: "development"
slug: "events-hrbrain-talent-pool-add"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织大脑 > 组织大脑人才池新增"
doc_id: "KSlDZZHuwq"
updated_at: "2026-03-19 18:57:16"
---

> Source: https://open.dingtalk.com/document/development/events-hrbrain-talent-pool-add
> Path: 应用开发 / 事件订阅 / 组织大脑 > 组织大脑人才池新增
> Updated: 2026-03-19 18:57:16

# 组织大脑人才池新增

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 组织大脑人才池新增 |
| 英文名称 | hrbrain\_talent\_pool\_add |

## 功能描述

人才池创建的事件，当组织大脑人才池新增时，会通知订阅方

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
- `data.eventId`（string）：事件的唯一ID
- `data.corpid`（string）：钉钉组织ID
- `data.syncAction`（string）：事件英文名。
- `data.bizid`（string）：业务执行trace id
- `data.body`（object）
- `data.body.poolCode`（string，必填）：人才池code
- `data.body.poolTags`（array）：人才池标签
- `data.body.poolName`（string，必填）：人才池名称
- `data.eventTime`（string）：事件发生时的时间戳

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "hrbrain_talent_pool_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "syncAction": "hrbrain_talent_pool_add",
    "body": {
      "poolTags": [
        {}
      ]
    }
  }
}
```

HTTP推送

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（string）：事件的唯一ID
- `corpid`（string）：钉钉组织ID
- `syncAction`（string）：事件英文名。
- `bizid`（string）：业务执行trace id
- `body`（object）
- `body.poolCode`（string，必填）：人才池code
- `body.poolTags`（array）：人才池标签
- `body.poolName`（string，必填）：人才池名称
- `event_time`（string）：事件发生时的时间戳

### **事件体示例**

```
{
  "EventType": "hrbrain_talent_pool_add",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "syncAction": "hrbrain_talent_pool_add",
  "body": {
    "poolTags": [
      {}
    ]
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.eventId`（string）：事件的唯一ID
- `biz_data.corpid`（string）：钉钉组织ID
- `biz_data.syncAction`（string）：事件英文名。
- `biz_data.bizid`（string）：业务执行trace id
- `biz_data.body`（object）
- `biz_data.body.poolCode`（string，必填）：人才池code
- `biz_data.body.poolTags`（array）：人才池标签
- `biz_data.body.poolName`（string，必填）：人才池名称
- `biz_data.event_time`（string）：事件发生时的时间戳

### **biz\_data数据示例(biz\_type=480)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 480,
  "biz_data": {
    "syncAction": "hrbrain_talent_pool_add",
    "body": {
      "poolTags": [
        {}
      ]
    }
  }
}
```
