---
title: "企业删除外部联系人"
source_url: "https://open.dingtalk.com/document/development/enterprise-delete-external-contact-stream"
namespace: "development"
slug: "enterprise-delete-external-contact-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业删除外部联系人"
doc_id: "oKFCFOqEUY"
updated_at: "2025-10-16 14:32:15"
---

> Source: https://open.dingtalk.com/document/development/enterprise-delete-external-contact-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业删除外部联系人
> Updated: 2025-10-16 14:32:15

# 企业删除外部联系人

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除外部联系人 |
| 英文名称 | contact\_leave\_org |

## 功能描述

该数据为在授权的第三方企业应用中，当eventType=contact\_leave\_org，表示企业外部联系人删除的推送信息。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
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

### 字段说明

（object）

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "contact_leave_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {}
}
```
