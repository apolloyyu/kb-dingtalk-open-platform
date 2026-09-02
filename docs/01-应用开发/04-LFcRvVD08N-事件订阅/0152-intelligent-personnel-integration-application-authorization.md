---
title: "智能人事一体化应用授权"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-integration-application-authorization"
namespace: "development"
slug: "intelligent-personnel-integration-application-authorization"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 智能人事一体化应用授权"
doc_id: "0J8ECOGOBr"
updated_at: "2025-08-28 19:47:05"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-integration-application-authorization
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 智能人事一体化应用授权
> Updated: 2025-08-28 19:47:05

# 智能人事一体化应用授权

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能人事一体化应用授权 |
| 英文名称 | hrm\_app\_authorize |

## 功能描述

人事一体化数据授权事件：企业将三方应用数据授权给人事主数据平台后的事件通知。

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
- `data.appDataAuthorize`（boolean）：是否已经授权成功

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "hrm_app_authorize",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "appDataAuthorize": true
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
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.app_data_authorize`（boolean）：是否已经授权成功

### **biz\_data数据示例(biz\_type=123)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 123,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "hrm_app_authorize",
    "app_data_authorize": true
  }
}
```
