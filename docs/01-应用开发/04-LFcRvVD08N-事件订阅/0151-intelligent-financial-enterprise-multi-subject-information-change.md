---
title: "智能财务企业多主体信息变更"
source_url: "https://open.dingtalk.com/document/development/intelligent-financial-enterprise-multi-subject-information-change"
namespace: "development"
slug: "intelligent-financial-enterprise-multi-subject-information-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 智能财务企业多主体信息变更"
doc_id: "OaHttzvQE2"
updated_at: "2025-08-28 19:47:08"
---

> Source: https://open.dingtalk.com/document/development/intelligent-financial-enterprise-multi-subject-information-change
> Path: 应用开发 / 事件订阅 / 智能财务 > 智能财务企业多主体信息变更
> Updated: 2025-08-28 19:47:08

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.companyInfo`（object）：本次变更后的主体信息。
- `data.companyInfo.companyCode`（string，必填）：企业主体唯一编号，默认主体为：COM\_DEFAULT。
- `data.companyInfo.advancedSettingList`（array）：高级选项列表。
- `data.companyInfo.advancedSettingList[].advancedSettingName`（string）：高级选项名字。
- `data.companyInfo.advancedSettingList[].value`（boolean）：属性值。
- `data.companyInfo.advancedSettingList[].advancedSettingKey`（string）：高级选项的key。
- `data.companyInfo.advancedSettingList[].deadline`（string）：过期时间。
- `data.companyInfo.creator`（string，必填）：创建人UserId。
- `data.companyInfo.taxNature`（string）：纳税人性质：  
  - generalTaxpayer:一般纳税人。  
  - smallScaleTaxpayer:小规模纳税人。
- `data.companyInfo.companyName`（string，必填）：企业主体名字。
- `data.companyInfo.remark`（string）：企业主体备注。
- `data.companyInfo.taxNo`（string）：纳税人识别号。
- `data.companyInfo.status`（string，必填）：状态：  
  - valid：正常。  
  - deleted：删除。
- `data.changeType`（string）：本次变更的类型。
- `data.beforeCompanyInfo`（object）：本次变更前的主体信息。
- `data.beforeCompanyInfo.companyCode`（string）：企业主体唯一编号，默认主体为：COM\_DEFAULT。
- `data.beforeCompanyInfo.advancedSettingList`（array）
- `data.beforeCompanyInfo.advancedSettingList[].advancedSettingName`（string）：高级选项名字。
- `data.beforeCompanyInfo.advancedSettingList[].deadline`（string）：过期时间。
- `data.beforeCompanyInfo.advancedSettingList[].value`（boolean）：属性值。
- `data.beforeCompanyInfo.advancedSettingList[].advancedSettingKey`（string）：高级选项的key。
- `data.beforeCompanyInfo.creator`（string）：创建人UserId。
- `data.beforeCompanyInfo.taxNature`（string）：纳税人性质：  
  - generalTaxpayer：一般纳税人。  
  - smallScaleTaxpayer：小规模纳税人。
- `data.beforeCompanyInfo.companyName`（string）：企业主体名字。
- `data.beforeCompanyInfo.remark`（string）：企业主体备注。
- `data.beforeCompanyInfo.taxNo`（string）：纳税人识别号。
- `data.beforeCompanyInfo.status`（string）：状态：  
  - valid：正常。  
  - deleted：删除。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.companyInfo`（object）：本次变更后的主体信息。
- `biz_data.companyInfo.companyCode`（string，必填）：企业主体唯一编号，默认主体为：COM\_DEFAULT。
- `biz_data.companyInfo.advancedSettingList`（array）：高级选项列表。
- `biz_data.companyInfo.advancedSettingList[].advancedSettingName`（string）：高级选项名字。
- `biz_data.companyInfo.advancedSettingList[].value`（boolean）：属性值。
- `biz_data.companyInfo.advancedSettingList[].advancedSettingKey`（string）：高级选项的key。
- `biz_data.companyInfo.advancedSettingList[].deadline`（string）：过期时间。
- `biz_data.companyInfo.creator`（string，必填）：创建人UserId。
- `biz_data.companyInfo.taxNature`（string）：纳税人性质：  
  - generalTaxpayer:一般纳税人。  
  - smallScaleTaxpayer:小规模纳税人。
- `biz_data.companyInfo.companyName`（string，必填）：企业主体名字。
- `biz_data.companyInfo.remark`（string）：企业主体备注。
- `biz_data.companyInfo.taxNo`（string）：纳税人识别号。
- `biz_data.companyInfo.status`（string，必填）：状态：  
  - valid：正常。  
  - deleted：删除。
- `biz_data.changeType`（string）：本次变更的类型。
- `biz_data.beforeCompanyInfo`（object）：本次变更前的主体信息。
- `biz_data.beforeCompanyInfo.companyCode`（string）：企业主体唯一编号，默认主体为：COM\_DEFAULT。
- `biz_data.beforeCompanyInfo.advancedSettingList`（array）
- `biz_data.beforeCompanyInfo.advancedSettingList[].advancedSettingName`（string）：高级选项名字。
- `biz_data.beforeCompanyInfo.advancedSettingList[].deadline`（string）：过期时间。
- `biz_data.beforeCompanyInfo.advancedSettingList[].value`（boolean）：属性值。
- `biz_data.beforeCompanyInfo.advancedSettingList[].advancedSettingKey`（string）：高级选项的key。
- `biz_data.beforeCompanyInfo.creator`（string）：创建人UserId。
- `biz_data.beforeCompanyInfo.taxNature`（string）：纳税人性质：  
  - generalTaxpayer：一般纳税人。  
  - smallScaleTaxpayer：小规模纳税人。
- `biz_data.beforeCompanyInfo.companyName`（string）：企业主体名字。
- `biz_data.beforeCompanyInfo.remark`（string）：企业主体备注。
- `biz_data.beforeCompanyInfo.taxNo`（string）：纳税人识别号。
- `biz_data.beforeCompanyInfo.status`（string）：状态：  
  - valid：正常。  
  - deleted：删除。

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
