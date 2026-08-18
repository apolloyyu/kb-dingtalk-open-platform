---
title: "智能财务企业信息变更"
source_url: "https://open.dingtalk.com/document/development/intelligent-financial-enterprise-information-change"
namespace: "development"
slug: "intelligent-financial-enterprise-information-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 智能财务企业信息变更"
doc_id: "qY7awzb49g"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/intelligent-financial-enterprise-information-change
> Path: 应用开发 / 事件订阅 / 智能财务 > 智能财务企业信息变更
> Updated: 2022-01-19 19:29:22

# 智能财务企业信息变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能财务企业信息变更 |
| 英文名称 | smart\_finance\_company\_info\_change |

## 功能描述

数据为智能财务企业信息变更相关数据。该数据用于告知合作伙伴，企业的信息进行了更新，便于数据实时同步。

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
  "eventType": "smart_finance_company_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "companyInfo": {
      "taxNature": "smallScaleTaxpayer",
      "companyName": "智财测试02-12",
      "taxNo": "111111111111111"
    },
    "changeType": "update"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=228)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 228,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "smart_finance_company_info_change",
    "companyInfo": {
      "taxNature": "smallScaleTaxpayer",
      "companyName": "智财测试02-12",
      "taxNo": "111111111111111"
    },
    "changeType": "update"
  }
}
```
