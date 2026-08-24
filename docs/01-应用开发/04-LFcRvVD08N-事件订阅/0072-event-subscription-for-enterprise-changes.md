---
title: "企业变更"
source_url: "https://open.dingtalk.com/document/development/event-subscription-for-enterprise-changes"
namespace: "development"
slug: "event-subscription-for-enterprise-changes"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业变更"
doc_id: "Ih7w9LinIN"
updated_at: "2025-12-08 17:39:57"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-for-enterprise-changes
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业变更
> Updated: 2025-12-08 17:39:57

# 企业变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业变更 |
| 英文名称 | org\_update |

## 功能描述

数据为企业的最新状态。该数据为在授权的第三方企业应用中，企业信息发生变更的时刻推送。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
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
- `data.errcode`（integer）：返回码。
- `data.corpid`（string）：企业corpid。
- `data.authLevel`（integer）：企业认证级别：  
  - 0：未认证  
  - 1： 高级认证  
  - 2： 中级认证  
  - 3 ：初级认证
- `data.errmsg`（string）：返回码描述。
- `data.isAuthenticated`（boolean）：企业是否认证：  
  - true ：已认证  
  - false ： 未认证
- `data.corpName`（string）：企业名称。
- `data.corpLogoUrl`（string）：企业图标url。
- `data.industry`（string）：企业所属行业。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "corpLogoUrl": "https://static.xxx.com",
    "corpid": "dingxxx2cff796",
    "errmsg": "ok",
    "industry": "信息技术咨询",
    "corpName": "企业1",
    "isAuthenticated": true,
    "authLevel": 2
  }
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
- `biz_data.errcode`（integer）：返回码。
- `biz_data.corpid`（string）：企业corpid。
- `biz_data.auth_level`（integer）：企业认证级别：  
  - 0：未认证  
  - 1： 高级认证  
  - 2： 中级认证  
  - 3 ：初级认证
- `biz_data.errmsg`（string）：返回码描述。
- `biz_data.is_authenticated`（boolean）：企业是否认证：  
  - true ：已认证  
  - false ： 未认证
- `biz_data.corp_name`（string）：企业名称。
- `biz_data.corp_logo_url`（string）：企业图标url。
- `biz_data.industry`（string）：企业所属行业。

### **biz\_data数据示例(biz\_type=16)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 16,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "dingxxx2cff796",
    "syncAction": "org_update",
    "auth_level": 2,
    "errmsg": "ok",
    "industry": "信息技术咨询",
    "is_authenticated": true,
    "corp_name": "企业1",
    "corp_logo_url": "https://static.xxx.com"
  }
}
```
