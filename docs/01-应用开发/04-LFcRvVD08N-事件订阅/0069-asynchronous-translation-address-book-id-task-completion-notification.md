---
title: "异步转译通讯录id任务完成通知"
source_url: "https://open.dingtalk.com/document/development/asynchronous-translation-address-book-id-task-completion-notification"
namespace: "development"
slug: "asynchronous-translation-address-book-id-task-completion-notification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 通讯录ID转译 > 异步转译通讯录id任务完成通知"
doc_id: "9Qe771g0Dk"
updated_at: "2025-08-28 19:46:29"
---

> Source: https://open.dingtalk.com/document/development/asynchronous-translation-address-book-id-task-completion-notification
> Path: 应用开发 / 事件订阅 / 通讯录 > 通讯录ID转译 > 异步转译通讯录id任务完成通知
> Updated: 2025-08-28 19:46:29

# 异步转译通讯录id任务完成通知

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 异步转译通讯录id任务完成通知 |
| 英文名称 | transfer\_contact\_id\_job\_result |

## 功能描述

企业异步转译通讯录id任务完成，发送的异步转译通讯录事件数据。

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
- `data.jobId`（string）：任务ID。
- `data.status`（string）：任务状态。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "transfer_contact_id_job_result",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "jobId": "seejaRmXY8RQgo2SJSHS92xxxxxxx",
    "status": "1"
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
- `biz_data.jobId`（string）：任务ID。
- `biz_data.status`（string）：任务状态。

### **biz\_data数据示例(biz\_type=139)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 139,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "jobId": "seejaRmXY8RQgo2SJSHS92xxxxxxx",
    "syncAction": "transfer_contact_id_job_result",
    "status": "1"
  }
}
```
