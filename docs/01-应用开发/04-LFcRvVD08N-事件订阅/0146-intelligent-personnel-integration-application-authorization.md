---
title: "智能人事一体化应用授权"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-integration-application-authorization"
namespace: "development"
slug: "intelligent-personnel-integration-application-authorization"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 智能人事一体化应用授权"
doc_id: "0J8ECOGOBr"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-integration-application-authorization
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 智能人事一体化应用授权
> Updated: 2022-01-19 19:29:22

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
