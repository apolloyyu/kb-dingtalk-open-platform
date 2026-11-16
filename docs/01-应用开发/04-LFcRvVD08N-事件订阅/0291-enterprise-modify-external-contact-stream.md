---
title: "企业修改外部联系人"
source_url: "https://open.dingtalk.com/document/development/enterprise-modify-external-contact-stream"
namespace: "development"
slug: "enterprise-modify-external-contact-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业修改外部联系人"
doc_id: "WeU6FmCdF7"
updated_at: "2025-10-16 14:32:14"
---

> Source: https://open.dingtalk.com/document/development/enterprise-modify-external-contact-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业修改外部联系人
> Updated: 2025-10-16 14:32:14

# 企业修改外部联系人

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业修改外部联系人 |
| 英文名称 | contact\_modify\_org |

## 功能描述

该数据为在授权的第三方企业应用中，当eventType为contact\_modify\_org，表示企业修改外部联系人的推送信息。

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

- `errcode`（integer）：返回码。
- `labelIds`（array）：标签列表。
- `shareUserIds`（array）：共享给的员工userid列表。
- `followerUserId`（string）：负责内部用户userId。
- `companyName`（string）：外部联系人的企业名称。
- `name`（string）：客户名称。
- `mobile`（string）：手机号。
- `errmsg`（string）：返回码说明。
- `stateCode`（string）：手机号国家码。
- `userId`（string）：userId。
- `shareDeptIds`（array）：共享部门id列表。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "contact_modify_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "labelIds": [
      123,
      124
    ],
    "shareUserIds": [],
    "followerUserId": "2000121002668",
    "companyName": "企业1",
    "name": "潜在客户小张",
    "mobile": "12345678910",
    "errmsg": "ok",
    "stateCode": "86",
    "userId": "12345",
    "shareDeptIds": [
      112334
    ]
  }
}
```
