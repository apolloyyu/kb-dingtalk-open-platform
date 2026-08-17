---
title: "CRM元数据"
source_url: "https://open.dingtalk.com/document/development/crm-metadata"
namespace: "development"
slug: "crm-metadata"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 客户管理事件 > CRM元数据"
doc_id: "c6k3n3d4Re"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/crm-metadata
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 客户管理事件 > CRM元数据
> Updated: 2022-01-19 19:29:22

# CRM元数据

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | CRM元数据 |
| 英文名称 | ding\_crm\_object\_meta |
| 事件BizType | 293 |

## 功能描述

客户管理元数据回调事件，当用户进入客户管理后台编辑并发布客户、联系人、跟进记录表单时会触发推送本事件。
![](https://img.alicdn.com/imgextra/i1/O1CN01GX0Gda1Ggf3dKNESN_!!6000000000652-2-tps-2268-1472.png)

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### 企业内部应用

### **事件体示例**

```
{
  "CorpId": "1663**351222567",
  "customized": false,
  "EventType": "ding_crm_object_meta",
  "EventTime": 1663143335567,
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
  "BizId": "1663**35567",
  "status": "PUBLISHED"
}
```

### 第三方企业应用(biz\_type=293)

数据为RDS和SyncHTTP推送的事件体，当为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例如下:**

```
{
  "customized": false,
  "syncAction": "ding_crm_object_meta",
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
```
