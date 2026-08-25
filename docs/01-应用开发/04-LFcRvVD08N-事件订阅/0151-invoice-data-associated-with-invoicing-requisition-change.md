---
title: "开票申请单关联发票数据变更"
source_url: "https://open.dingtalk.com/document/development/invoice-data-associated-with-invoicing-requisition-change"
namespace: "development"
slug: "invoice-data-associated-with-invoicing-requisition-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 开票申请单关联发票数据变更"
doc_id: "zr63RWYZR2"
updated_at: "2025-08-28 19:47:07"
---

> Source: https://open.dingtalk.com/document/development/invoice-data-associated-with-invoicing-requisition-change
> Path: 应用开发 / 事件订阅 / 智能财务 > 开票申请单关联发票数据变更
> Updated: 2025-08-28 19:47:07

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.instanceId`（string）：开票申请单instanceId， 在发票来源为审批开票时，该字段不为空
- `data.type`（string）：开票申请单关联发票操作类型，例如 bind、unbind。
- `data.source`（string）：发票来源：审批开票、收款码开票、销项发票修复、订单开票、数电开票（含批量、清单、草稿箱、红冲等其他）
- `data.invoiceList`（array）：发票列表。
- `data.invoiceList[].amount`（double，必填）：不含税金额。
- `data.invoiceList[].invoiceNo`（string，必填）：发票号码。
- `data.invoiceList[].amountWithTax`（double，必填）：含税金额。
- `data.invoiceList[].invoiceCode`（string，必填）：发票代码。
- `data.invoiceList[].electronicUrl`（string，必填）：发票下载地址。
- `data.invoiceList[].drewDate`（string，必填）：开票日期。
- `data.invoiceList[].taxAmount`（string，必填）：税额。

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

### 入参

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.instanceId`（string）：开票申请单instanceId， 在发票来源为审批开票时，该字段不为空
- `biz_data.type`（string）：开票申请单关联发票操作类型，例如 bind、unbind。
- `biz_data.source`（string）：发票来源：审批开票、收款码开票、销项发票修复、订单开票、数电开票（含批量、清单、草稿箱、红冲等其他）
- `biz_data.invoiceList`（array）：发票列表。
- `biz_data.invoiceList[].amount`（double，必填）：不含税金额。
- `biz_data.invoiceList[].invoiceNo`（string，必填）：发票号码。
- `biz_data.invoiceList[].amountWithTax`（double，必填）：含税金额。
- `biz_data.invoiceList[].invoiceCode`（string，必填）：发票代码。
- `biz_data.invoiceList[].electronicUrl`（string，必填）：发票下载地址。
- `biz_data.invoiceList[].drewDate`（string，必填）：开票日期。
- `biz_data.invoiceList[].taxAmount`（string，必填）：税额。

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
