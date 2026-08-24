---
title: "智能财务审批模版变更事件"
source_url: "https://open.dingtalk.com/document/development/smart-financial-approval-template-change-event"
namespace: "development"
slug: "smart-financial-approval-template-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 智能财务审批模版变更事件"
doc_id: "e0kenaxbsM"
updated_at: "2025-08-28 19:47:07"
---

> Source: https://open.dingtalk.com/document/development/smart-financial-approval-template-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 智能财务审批模版变更事件
> Updated: 2025-08-28 19:47:07

# 智能财务审批模版变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能财务审批模版变更事件 |
| 英文名称 | smart\_finance\_form\_change |

## 功能描述

当智能财务相关审批模版发生变更时，钉钉会通过事件订阅的方式将审批模版变更的信息推送给开发者，用于监听审批模版变更信息。

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
- `data.corpId`（string）：组织id。
- `data.formCode`（string）：模版id。
- `data.changeType`（string）：变更操作类型。
- `data.suiteId`（string）：套件id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "smart_finance_form_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "suiteId": "dingtalk.businessFinance.noPayment",
    "corpId": "dingfb6ad2302da7ab8824f2f5cc6abecb85",
    "formCode": "PROC-EB81447A-B0E3-4A2F-A719-0A85EFD09184",
    "changeType": "PUBLISHED"
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
- `biz_data.corpId`（string）：组织id。
- `biz_data.formCode`（string）：模版id。
- `biz_data.changeType`（string）：变更操作类型。
- `biz_data.suiteId`（string）：套件id。

### **biz\_data数据示例(biz\_type=347)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 347,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "suiteId": "dingtalk.businessFinance.noPayment",
    "corpId": "dingfb6ad2302da7ab8824f2f5cc6abecb85",
    "syncAction": "smart_finance_form_change",
    "formCode": "PROC-EB81447A-B0E3-4A2F-A719-0A85EFD09184",
    "changeType": "PUBLISHED"
  }
}
```
