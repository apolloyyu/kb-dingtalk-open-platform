---
title: "智能财务审批模版变更事件"
source_url: "https://open.dingtalk.com/document/development/smart-financial-approval-template-change-event"
namespace: "development"
slug: "smart-financial-approval-template-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 智能财务审批模版变更事件"
doc_id: "e0kenaxbsM"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/smart-financial-approval-template-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 智能财务审批模版变更事件
> Updated: 2022-01-19 19:29:22

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
