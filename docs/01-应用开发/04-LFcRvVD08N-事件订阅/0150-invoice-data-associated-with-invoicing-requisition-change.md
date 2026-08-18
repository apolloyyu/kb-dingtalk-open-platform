---
title: "开票申请单关联发票数据变更"
source_url: "https://open.dingtalk.com/document/development/invoice-data-associated-with-invoicing-requisition-change"
namespace: "development"
slug: "invoice-data-associated-with-invoicing-requisition-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 开票申请单关联发票数据变更"
doc_id: "zr63RWYZR2"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/invoice-data-associated-with-invoicing-requisition-change
> Path: 应用开发 / 事件订阅 / 智能财务 > 开票申请单关联发票数据变更
> Updated: 2022-01-19 19:29:22

# 开票申请单关联发票数据变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 开票申请单关联发票数据变更 |
| 英文名称 | smart\_finance\_application\_invoice\_update |

## 功能描述

该事件用于给ISV推送在智能财务侧完成的开票申请单的发票数据，用户ISV配合钉钉侧完成后续业务逻辑。

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
  "eventType": "smart_finance_application_invoice_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "invoiceList": [
      {
        "amount": 123.33,
        "electronicUrl": "https://static.cdn.xxx.com",
        "drewDate": "2023-11-11",
        "invoiceNo": "011123",
        "taxAmount": "4",
        "amountWithTax": 134.12,
        "invoiceCode": "01231"
      }
    ],
    "instanceId": "abc",
    "source": "APPROVAL",
    "type": "bind"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=308)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 308,
  "biz_data": {
    "invoiceList": [
      {
        "amount": 123.33,
        "electronicUrl": "https://static.cdn.xxx.com",
        "drewDate": "2023-11-11",
        "invoiceNo": "011123",
        "taxAmount": "4",
        "amountWithTax": 134.12,
        "invoiceCode": "01231"
      }
    ],
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "instanceId": "abc",
    "syncAction": "smart_finance_application_invoice_update",
    "source": "APPROVAL",
    "type": "bind"
  }
}
```
