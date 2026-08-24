---
title: "专属钉钉数据迁移"
source_url: "https://open.dingtalk.com/document/development/dedicated-dingtalk-data-migration"
namespace: "development"
slug: "dedicated-dingtalk-data-migration"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 专属钉钉数据迁移"
doc_id: "AhY6a5g1UV"
updated_at: "2025-08-28 19:47:33"
---

> Source: https://open.dingtalk.com/document/development/dedicated-dingtalk-data-migration
> Path: 应用开发 / 事件订阅 / 专属开放 > 专属钉钉数据迁移
> Updated: 2025-08-28 19:47:33

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.success`（boolean）：是否成功。
- `data.userId`（string）：员工userId。

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `UserId`（string，必填）：员工userId。
- `Success`（boolean，必填）：是否成功。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.UserId`（string）：员工userId。
- `biz_data.Success`（boolean）：是否成功。

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
