---
title: "CRM元数据"
source_url: "https://open.dingtalk.com/document/development/event-ding-crm-object-meta"
namespace: "development"
slug: "event-ding-crm-object-meta"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "客户管理 > CRM元数据"
doc_id: "u3baa4pGyq"
updated_at: "2025-08-28 19:47:17"
---

> Source: https://open.dingtalk.com/document/development/event-ding-crm-object-meta
> Path: 应用开发 / 事件订阅 / 客户管理 > CRM元数据
> Updated: 2025-08-28 19:47:17

# CRM元数据

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM元数据 |
| 英文名称 | ding\_crm\_object\_meta |

## 功能描述

客户管理元数据回调事件，当用户进入客户管理后台编辑并发布客户、联系人、跟进记录表单时会触发推送本事件。
![图片](https://img.alicdn.com/imgextra/i1/O1CN01GX0Gda1Ggf3dKNESN_!!6000000000652-2-tps-2268-1472.png)

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
- `data.type`（string）：元数据事件类型：  
  \* ding\_paas\_object\_create：创建元数据  
  \* ding\_paas\_object\_update：更新元数据  
  \* ding\_paas\_object\_delete：删除元数据
- `data.objectName`（string）：元数据标识：  
  \* crm\_customer：企业客户  
  \* crm\_customer\_personal：个人客户  
  \* crm\_contact：联系人  
  \* crm\_follow\_record：跟进记录
- `data.name`（string）：元数据名称。
- `data.customized`（boolean）：是否自定义元数据：  
  \* true：自定义  
  \* false：标准
- `data.status`（string）：元数据状态：  
  \* PUBLISHED：已发布  
  \* INVALID：已停用
- `data.fields`（array）：元数据字段列表。
- `data.fields[].name`（string，必填）：字段bizAlias。
- `data.fields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `data.fields[].id`（string，必填）：字段id。
- `data.fields[].label`（string，必填）：字段名称。
- `data.fields[].type`（string，必填）：字段类型：  
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
- `data.fields[].nillable`（boolean，必填）：字段是否必填：   
  \* true：非必填   
  \* false：必填
- `data.fields[].format`（string，必填）：Date日期字段的格式。
- `data.fields[].quote`（boolean，必填）：Lookup关联表单字段的关联模式：  
  \* true：引用模式  
  \* false：拷贝模式
- `data.fields[].referenceToCode`（string，必填）：关联的表单Code。
- `data.fields[].invisible`（boolean，必填）：字段是否可见：  
  \* true：不可见  
  \* false：可见
- `data.fields[].rollUpSummaryFields`（array，必填）：MasterDetail明细字段的汇总字段。
- `data.fields[].rollUpSummaryFields[].name`（string，必填）：要汇总的字段id。
- `data.fields[].rollUpSummaryFields[].aggregator`（string，必填）：汇总方法：  
  \* SUM：表示求和
- `data.fields[].referenceFields`（array，必填）：关联表单信息（关联单表单）。
- `data.fields[].referenceFields[].name`（string，必填）：字段bizAlias。
- `data.fields[].referenceFields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `data.fields[].referenceFields[].id`（string，必填）：字段id。
- `data.fields[].referenceFields[].label`（string，必填）：字段名称。
- `data.fields[].referenceFields[].type`（string，必填）：字段类型：  
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
- `data.fields[].referenceFields[].nillable`（string，必填）：字段是否必填：  
  \* true：非必填  
  \* false：必填
- `data.fields[].relatedFormFields`（array，必填）：关联表单信息（关联多表单）。
- `data.fields[].relatedFormFields[].relatedFields`（array，必填）：关联表单字段列表。
- `data.fields[].relatedFormFields[].relatedFields[].name`（string，必填）：字段bizAlias。
- `data.fields[].relatedFormFields[].relatedFields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `data.fields[].relatedFormFields[].relatedFields[].id`（string，必填）：字段id。
- `data.fields[].relatedFormFields[].relatedFields[].label`（string，必填）：字段名称。
- `data.fields[].relatedFormFields[].relatedFields[].type`（string，必填）：字段类型：  
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
- `data.fields[].relatedFormFields[].relatedFields[].nillable`（boolean，必填）：字段是否必填：   
  \* true：非必填   
  \* false：必填
- `data.fields[].relatedFormFields[].formName`（string，必填）：关联表单的formCode。
- `data.fields[].selectOptions`（array，必填）：选项列表。
- `data.fields[].selectOptions[].key`（string，必填）：选项key。
- `data.fields[].selectOptions[].value`（string，必填）：选项显示名。

### **事件体示例**

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
        "customized": true,
        "referenceToCode": "code**673",
        "selectOptions": [
          {
            "value": "已完结",
            "key": "Option_done"
          }
        ],
        "relatedFormFields": [
          {
            "relatedFields": [
              {
                "customized": true,
                "name": "customer_name",
                "id": "TextField-XXXXXX",
                "label": "联系人姓名",
                "type": "Text",
                "nillable": false
              }
            ],
            "formName": "PROC-XXXX-XXXX-XXXX"
          }
        ],
        "format": "yyyy-MM-dd",
        "invisible": false,
        "referenceFields": [
          {
            "customized": true,
            "name": "customer_name",
            "id": "TextField-XXXXXX",
            "label": "联系人姓名",
            "type": "Text",
            "nillable": "false"
          }
        ],
        "label": "联系人姓名",
        "type": "Text",
        "nillable": false,
        "rollUpSummaryFields": [
          {
            "aggregator": "SUM",
            "name": "MoneyField_1N0FRK785F11C"
          }
        ],
        "quote": true,
        "name": "contact_name",
        "id": "TextField-XXXXXX"
      }
    ],
    "status": "PUBLISHED"
  }
}
```

HTTP推送

### 入参

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
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

### **事件体示例**

```
{
  "EventType": "ding_crm_object_meta",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "customized": false,
  "name": "企业客户",
  "objectName": "crm_customer",
  "type": "ding_paas_object_update",
  "fields": [
    {
      "customized": true,
      "referenceToCode": "code**673",
      "selectOptions": [
        {
          "value": "已完结",
          "key": "Option_done"
        }
      ],
      "relatedFormFields": [
        {
          "relatedFields": [
            {
              "customized": true,
              "name": "customer_name",
              "id": "TextField-XXXXXX",
              "label": "联系人姓名",
              "type": "Text",
              "nillable": false
            }
          ],
          "formName": "PROC-XXXX-XXXX-XXXX"
        }
      ],
      "format": "yyyy-MM-dd",
      "invisible": false,
      "referenceFields": [
        {
          "customized": true,
          "name": "customer_name",
          "id": "TextField-XXXXXX",
          "label": "联系人姓名",
          "type": "Text",
          "nillable": "false"
        }
      ],
      "label": "联系人姓名",
      "type": "Text",
      "nillable": false,
      "rollUpSummaryFields": [
        {
          "aggregator": "SUM",
          "name": "MoneyField_1N0FRK785F11C"
        }
      ],
      "quote": true,
      "name": "contact_name",
      "id": "TextField-XXXXXX"
    }
  ],
  "status": "PUBLISHED"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 入参

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.type`（string）：元数据事件类型：  
  \* ding\_paas\_object\_create：创建元数据  
  \* ding\_paas\_object\_update：更新元数据  
  \* ding\_paas\_object\_delete：删除元数据
- `biz_data.objectName`（string）：元数据标识：  
  \* crm\_customer：企业客户  
  \* crm\_customer\_personal：个人客户  
  \* crm\_contact：联系人  
  \* crm\_follow\_record：跟进记录
- `biz_data.name`（string）：元数据名称。
- `biz_data.customized`（boolean）：是否自定义元数据：  
  \* true：自定义  
  \* false：标准
- `biz_data.status`（string）：元数据状态：  
  \* PUBLISHED：已发布  
  \* INVALID：已停用
- `biz_data.fields`（array）：元数据字段列表。
- `biz_data.fields[].name`（string，必填）：字段bizAlias。
- `biz_data.fields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `biz_data.fields[].id`（string，必填）：字段id。
- `biz_data.fields[].label`（string，必填）：字段名称。
- `biz_data.fields[].type`（string，必填）：字段类型：  
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
- `biz_data.fields[].nillable`（boolean，必填）：字段是否必填：   
  \* true：非必填   
  \* false：必填
- `biz_data.fields[].format`（string，必填）：Date日期字段的格式。
- `biz_data.fields[].quote`（boolean，必填）：Lookup关联表单字段的关联模式：  
  \* true：引用模式  
  \* false：拷贝模式
- `biz_data.fields[].referenceToCode`（string，必填）：关联的表单Code。
- `biz_data.fields[].invisible`（boolean，必填）：字段是否可见：  
  \* true：不可见  
  \* false：可见
- `biz_data.fields[].rollUpSummaryFields`（array，必填）：MasterDetail明细字段的汇总字段。
- `biz_data.fields[].rollUpSummaryFields[].name`（string，必填）：要汇总的字段id。
- `biz_data.fields[].rollUpSummaryFields[].aggregator`（string，必填）：汇总方法：  
  \* SUM：表示求和
- `biz_data.fields[].referenceFields`（array，必填）：关联表单信息（关联单表单）。
- `biz_data.fields[].referenceFields[].name`（string，必填）：字段bizAlias。
- `biz_data.fields[].referenceFields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `biz_data.fields[].referenceFields[].id`（string，必填）：字段id。
- `biz_data.fields[].referenceFields[].label`（string，必填）：字段名称。
- `biz_data.fields[].referenceFields[].type`（string，必填）：字段类型：  
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
- `biz_data.fields[].referenceFields[].nillable`（string，必填）：字段是否必填：  
  \* true：非必填  
  \* false：必填
- `biz_data.fields[].relatedFormFields`（array，必填）：关联表单信息（关联多表单）。
- `biz_data.fields[].relatedFormFields[].relatedFields`（array，必填）：关联表单字段列表。
- `biz_data.fields[].relatedFormFields[].relatedFields[].name`（string，必填）：字段bizAlias。
- `biz_data.fields[].relatedFormFields[].relatedFields[].customized`（boolean，必填）：是否自定义字段：  
  \* true：自定义字段，可删除  
  \* false：系统字段，不可删除
- `biz_data.fields[].relatedFormFields[].relatedFields[].id`（string，必填）：字段id。
- `biz_data.fields[].relatedFormFields[].relatedFields[].label`（string，必填）：字段名称。
- `biz_data.fields[].relatedFormFields[].relatedFields[].type`（string，必填）：字段类型：  
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
- `biz_data.fields[].relatedFormFields[].relatedFields[].nillable`（boolean，必填）：字段是否必填：   
  \* true：非必填   
  \* false：必填
- `biz_data.fields[].relatedFormFields[].formName`（string，必填）：关联表单的formCode。
- `biz_data.fields[].selectOptions`（array，必填）：选项列表。
- `biz_data.fields[].selectOptions[].key`（string，必填）：选项key。
- `biz_data.fields[].selectOptions[].value`（string，必填）：选项显示名。

### **biz\_data数据示例(biz\_type=293)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 293,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "customized": false,
    "syncAction": "ding_crm_object_meta",
    "name": "企业客户",
    "objectName": "crm_customer",
    "type": "ding_paas_object_update",
    "fields": [
      {
        "customized": true,
        "referenceToCode": "code**673",
        "selectOptions": [
          {
            "value": "已完结",
            "key": "Option_done"
          }
        ],
        "relatedFormFields": [
          {
            "relatedFields": [
              {
                "customized": true,
                "name": "customer_name",
                "id": "TextField-XXXXXX",
                "label": "联系人姓名",
                "type": "Text",
                "nillable": false
              }
            ],
            "formName": "PROC-XXXX-XXXX-XXXX"
          }
        ],
        "format": "yyyy-MM-dd",
        "invisible": false,
        "referenceFields": [
          {
            "customized": true,
            "name": "customer_name",
            "id": "TextField-XXXXXX",
            "label": "联系人姓名",
            "type": "Text",
            "nillable": "false"
          }
        ],
        "label": "联系人姓名",
        "type": "Text",
        "nillable": false,
        "rollUpSummaryFields": [
          {
            "aggregator": "SUM",
            "name": "MoneyField_1N0FRK785F11C"
          }
        ],
        "quote": true,
        "name": "contact_name",
        "id": "TextField-XXXXXX"
      }
    ],
    "status": "PUBLISHED"
  }
}
```
