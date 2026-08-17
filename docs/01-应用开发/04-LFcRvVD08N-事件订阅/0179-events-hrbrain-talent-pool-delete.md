---
title: "组织大脑人才池删除"
source_url: "https://open.dingtalk.com/document/development/events-hrbrain-talent-pool-delete"
namespace: "development"
slug: "events-hrbrain-talent-pool-delete"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织大脑 > 组织大脑人才池删除"
doc_id: "b3EUVvT4KJ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-hrbrain-talent-pool-delete
> Path: 应用开发 / 事件订阅 / 组织大脑 > 组织大脑人才池删除
> Updated: 2022-01-19 19:29:22

# 组织大脑人才池删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 组织大脑人才池删除 |
| 英文名称 | hrbrain\_talent\_pool\_delete |

## 功能描述

人才池删除的事件，当组织大脑人才池删除时，会通知订阅方

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
  "eventType": "hrbrain_talent_pool_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "syncAction": "hrbrain_talent_pool_delete",
    "body": {}
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "hrbrain_talent_pool_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "syncAction": "hrbrain_talent_pool_delete",
  "body": {}
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=482)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 482,
  "biz_data": {
    "syncAction": "hrbrain_talent_pool_delete",
    "body": {}
  }
}
```
