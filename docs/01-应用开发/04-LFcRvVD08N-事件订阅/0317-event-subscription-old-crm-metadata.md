---
title: "CRM元数据"
source_url: "https://open.dingtalk.com/document/development/event-subscription-old-crm-metadata"
namespace: "development"
slug: "event-subscription-old-crm-metadata"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 客户管理事件 > CRM元数据"
doc_id: "BpIT25y42H"
updated_at: "2025-12-08 15:53:36"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-old-crm-metadata
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 客户管理事件 > CRM元数据
> Updated: 2025-12-08 15:53:36

# CRM元数据

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM元数据 |
| 英文名称 | ding\_crm\_object\_meta |

## 功能描述

客户管理元数据回调事件，当用户进入客户管理后台编辑并发布客户、联系人、跟进记录表单时会触发推送本事件，该事件的eventType为ding\_crm\_object\_meta。
![图片](https://img.alicdn.com/imgextra/i1/O1CN01GX0Gda1Ggf3dKNESN_!!6000000000652-2-tps-2268-1472.png)

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 入参

- `type`（string，必填）：元数据事件类型：  
  \* ding\_paas\_object\_create：创建元数据  
  \* ding\_paas\_object\_update：更新元数据  
  \* ding\_paas\_object\_delete：删除元数据
- `objectName`（string，必填）：元数据标识：  
  \* crm\_customer：企业客户  
  \* crm\_customer\_personal：个人客户  
  \* crm\_contact：联系人  
  \* crm\_follow\_record：跟进记录
- `name`（string，必填）：元数据名称。
- `customized`（boolean，必填）：是否自定义元数据：  
  \* true：自定义  
  \* false：标准
- `status`（string，必填）：元数据状态：  
  \* PUBLISHED：已发布  
  \* INVALID：已停用
- `fields`（array，必填）：元数据字段列表。
- `fields[].name`（string，必填）：字段bizAlias。
- `fields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `fields[].id`（string，必填）：字段id。
- `fields[].label`（string，必填）：字段名称。
- `fields[].type`（string，必填）：字段类型：  
  \* Text：单行输入框  
  \* Textarea：多行输入框  
  \* TextNote：说明文字  
  \* Select：单选  
  \* MultiSelect：多选  
  \* Date：日期  
  \* DateRange：日期区间  
  \* Number：数字  
  \* Money：金额  
  \* Photo：图片  
  \* Attachment：附件  
  \* Calculate：计算  
  \* InnerContact：联系人  
  \* Department：部门  
  \* TimeAndLocation：定位  
  \* Invoice：发票  
  \* RecipientAccount：收款账户  
  \* Tag：标签  
  \* MasterDetail：明细  
  \* Lookup：关联表单字段
- `fields[].nillable`（boolean，必填）：字段是否必填：   
  \* true：非必填   
  \* false：必填
- `fields[].format`（string，必填）：Date日期字段的格式。
- `fields[].quote`（boolean，必填）：Lookup关联表单字段的关联模式：  
  \* true：引用模式  
  \* false：拷贝模式
- `fields[].referenceToCode`（string，必填）：关联的表单Code。
- `fields[].invisible`（boolean，必填）：字段是否可见：  
  \* true：不可见  
  \* false：可见
- `fields[].rollUpSummaryFields`（array，必填）：MasterDetail明细字段的汇总字段。
- `fields[].rollUpSummaryFields[].name`（string，必填）：要汇总的字段id。
- `fields[].rollUpSummaryFields[].aggregator`（string，必填）：汇总方法：  
  \* SUM：表示求和
- `fields[].referenceFields`（array，必填）：关联表单信息（关联单表单）。
- `fields[].referenceFields[].name`（string，必填）：字段bizAlias。
- `fields[].referenceFields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `fields[].referenceFields[].id`（string，必填）：字段id。
- `fields[].referenceFields[].label`（string，必填）：字段名称。
- `fields[].referenceFields[].type`（string，必填）：字段类型：  
  \* Text：单行输入框  
  \* Textarea：多行输入框  
  \* TextNote：说明文字  
  \* Select：单选  
  \* MultiSelect：多选  
  \* Date：日期  
  \* DateRange：日期区间  
  \* Number：数字  
  \* Money：金额  
  \* Photo：图片  
  \* Attachment：附件  
  \* Calculate：计算  
  \* InnerContact：联系人  
  \* Department：部门  
  \* TimeAndLocation：定位  
  \* Invoice：发票  
  \* RecipientAccount：收款账户  
  \* Tag：标签  
  \* MasterDetail：明细  
  \* Lookup：关联表单字段
- `fields[].referenceFields[].nillable`（string，必填）：字段是否必填：  
  \* true：非必填  
  \* false：必填
- `fields[].relatedFormFields`（array，必填）：关联表单信息（关联多表单）。
- `fields[].relatedFormFields[].relatedFields`（array，必填）：关联表单字段列表。
- `fields[].relatedFormFields[].relatedFields[].name`（string，必填）：字段bizAlias。
- `fields[].relatedFormFields[].relatedFields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `fields[].relatedFormFields[].relatedFields[].id`（string，必填）：字段id。
- `fields[].relatedFormFields[].relatedFields[].label`（string，必填）：字段名称。
- `fields[].relatedFormFields[].relatedFields[].type`（string，必填）：字段类型：  
  \* Text：单行输入框  
  \* Textarea：多行输入框  
  \* TextNote：说明文字  
  \* Select：单选  
  \* MultiSelect：多选  
  \* Date：日期  
  \* DateRange：日期区间  
  \* Number：数字  
  \* Money：金额  
  \* Photo：图片  
  \* Attachment：附件  
  \* Calculate：计算  
  \* InnerContact：联系人  
  \* Department：部门  
  \* TimeAndLocation：定位  
  \* Invoice：发票  
  \* RecipientAccount：收款账户  
  \* Tag：标签  
  \* MasterDetail：明细  
  \* Lookup：关联表单字段
- `fields[].relatedFormFields[].relatedFields[].nillable`（boolean，必填）：字段是否必填：   
  \* true：非必填   
  \* false：必填
- `fields[].relatedFormFields[].formName`（string，必填）：关联表单的formCode。
- `fields[].selectOptions`（array，必填）：选项列表。
- `fields[].selectOptions[].key`（string，必填）：选项key。
- `fields[].selectOptions[].value`（string，必填）：选项显示名。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ding_crm_object_meta",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "customized": false,
    "name": "企业客户",
    "objectName": "crm_customer",
    "type": "ding_paas_object_update",
    "fields": [
      {
        "customized": false,
        "quote": true,
        "referenceToCode": "PROC-2627EB94-8FD1-43D0-AC1D-214CBF2E6819",
        "relatedFormFields": [
          {
            "relatedFields": [
              {
                "customized": false,
                "name": "customer_name",
                "id": "TextField-K2U5DHAA",
                "label": "客户名称",
                "type": "Text",
                "nillable": false
              }
            ],
            "formName": "crm_customer"
          },
          {
            "relatedFields": [
              {
                "customized": false,
                "name": "customer_name",
                "id": "TextField-K2U5DHAA",
                "label": "客户姓名",
                "type": "Text",
                "nillable": false
              }
            ],
            "formName": "crm_customer_personal"
          }
        ],
        "name": "contact_related_customer",
        "referenceFields": [
          {
            "customized": false,
            "name": "customer_name",
            "id": "TextField-K2U5DHAA",
            "label": "客户名称",
            "type": "Text",
            "nillable": false
          }
        ],
        "id": "FormRelateField-K2U5O2WK",
        "label": "客户",
        "type": "Lookup",
        "referenceTo": "crm_customer",
        "nillable": false
      },
      {
        "customized": false,
        "name": "contact_name",
        "id": "TextField-K2U5O2WI",
        "label": "联系人姓名",
        "type": "Text",
        "nillable": false
      },
      {
        "customized": false,
        "name": "contact_phone",
        "id": "TextField-K2U5O2WJ",
        "label": "手机号",
        "type": "Phone",
        "nillable": true
      }
    ],
    "status": "PUBLISHED"
  }
}
```
