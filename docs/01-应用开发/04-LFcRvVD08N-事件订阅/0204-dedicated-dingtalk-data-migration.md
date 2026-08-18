---
title: "专属钉钉数据迁移"
source_url: "https://open.dingtalk.com/document/development/dedicated-dingtalk-data-migration"
namespace: "development"
slug: "dedicated-dingtalk-data-migration"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 专属钉钉数据迁移"
doc_id: "AhY6a5g1UV"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/dedicated-dingtalk-data-migration
> Path: 应用开发 / 事件订阅 / 专属开放 > 专属钉钉数据迁移
> Updated: 2022-01-19 19:29:22

# 专属钉钉数据迁移

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 专属钉钉数据迁移 |
| 英文名称 | exclusive\_data\_transfer |

## 功能描述

本文介绍了专属钉钉数据迁移事件，专属钉钉数据迁移事件说明。

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
  "eventType": "exclusive_data_transfer",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "success": true,
    "userId": "01153741102xxxx"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "exclusive_data_transfer",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "UserId": "01153741102xxxx",
  "Success": true
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=219)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 219,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "exclusive_data_transfer",
    "UserId": "01153741102xxxx",
    "Success": true
  }
}
```
