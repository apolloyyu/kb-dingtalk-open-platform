---
title: "CRM元数据"
source_url: "https://open.dingtalk.com/document/development/event-ding-crm-object-meta"
namespace: "development"
slug: "event-ding-crm-object-meta"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "客户管理 > CRM元数据"
doc_id: "u3baa4pGyq"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-ding-crm-object-meta
> Path: 应用开发 / 事件订阅 / 客户管理 > CRM元数据
> Updated: 2022-01-19 19:29:22

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
