---
title: "智能财务企业多主体信息变更"
source_url: "https://open.dingtalk.com/document/development/intelligent-financial-enterprise-multi-subject-information-change"
namespace: "development"
slug: "intelligent-financial-enterprise-multi-subject-information-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 智能财务企业多主体信息变更"
doc_id: "OaHttzvQE2"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/intelligent-financial-enterprise-multi-subject-information-change
> Path: 应用开发 / 事件订阅 / 智能财务 > 智能财务企业多主体信息变更
> Updated: 2022-01-19 19:29:22

# 智能财务企业多主体信息变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能财务企业多主体信息变更 |
| 英文名称 | smart\_finance\_multi\_company\_info\_change |

## 功能描述

智能财务的企业主体变更时，会通过该事件通知业务方。

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
  "eventType": "smart_finance_multi_company_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "companyInfo": {
      "companyCode": "COM_DEFAULT",
      "advancedSettingList": [
        {
          "advancedSettingName": "关联发票",
          "advancedSettingKey": "relatedInvoice",
          "deadline": "123456789",
          "value": true
        }
      ],
      "creator": "5041234654",
      "taxNature": "generalTaxpayer",
      "companyName": "钉钉",
      "remark": "备注",
      "taxNo": "1234567890",
      "status": "状态"
    },
    "changeType": "update",
    "beforeCompanyInfo": {
      "companyCode": "COM_DEFAULT",
      "advancedSettingList": [
        {
          "advancedSettingName": "关联发票",
          "advancedSettingKey": "relatedInvoice",
          "deadline": "123456789",
          "value": true
        }
      ],
      "creator": "5041234654",
      "taxNature": "generalTaxpayer",
      "companyName": "钉钉",
      "remark": "备注",
      "taxNo": "1234567890",
      "status": "valid"
    }
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=309)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 309,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "smart_finance_multi_company_info_change",
    "companyInfo": {
      "companyCode": "COM_DEFAULT",
      "advancedSettingList": [
        {
          "advancedSettingName": "关联发票",
          "advancedSettingKey": "relatedInvoice",
          "deadline": "123456789",
          "value": true
        }
      ],
      "creator": "5041234654",
      "taxNature": "generalTaxpayer",
      "companyName": "钉钉",
      "remark": "备注",
      "taxNo": "1234567890",
      "status": "状态"
    },
    "changeType": "update",
    "beforeCompanyInfo": {
      "companyCode": "COM_DEFAULT",
      "advancedSettingList": [
        {
          "advancedSettingName": "关联发票",
          "advancedSettingKey": "relatedInvoice",
          "deadline": "123456789",
          "value": true
        }
      ],
      "creator": "5041234654",
      "taxNature": "generalTaxpayer",
      "companyName": "钉钉",
      "remark": "备注",
      "taxNo": "1234567890",
      "status": "valid"
    }
  }
}
```
