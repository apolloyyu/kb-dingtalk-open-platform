---
title: "CRM客户动态"
source_url: "https://open.dingtalk.com/document/development/crm-customer-dynamics"
namespace: "development"
slug: "crm-customer-dynamics"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "客户管理 > CRM客户动态"
doc_id: "gisJXJVwNW"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/crm-customer-dynamics
> Path: 应用开发 / 事件订阅 / 客户管理 > CRM客户动态
> Updated: 2022-01-19 19:29:22

# CRM客户动态

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM客户动态 |
| 英文名称 | crm\_customer\_track |

## 功能描述

CRM客户动态相关信息发生变更时，钉钉通过事件订阅的方式将CRM客户动态相关变更内容推送给开发者。CRM客户动态事件数据推送说明。

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
  "eventType": "crm_customer_track",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "tracks": [
      {
        "creator": "manager1234",
        "corpId": "ding9axxx",
        "customerId": "84c75568-xxx-xxx",
        "subType": 0,
        "type": 107,
        "gmtCreate": 1630474492814
      }
    ]
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=133)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 133,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "crm_customer_track",
    "tracks": [
      {
        "creator": "manager1234",
        "corpId": "ding9axxx",
        "customerId": "84c75568-xxx-xxx",
        "subType": 0,
        "type": 107,
        "gmtCreate": 1630474492814
      }
    ]
  }
}
```
