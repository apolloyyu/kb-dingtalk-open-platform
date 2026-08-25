---
title: "外部联系人修改"
source_url: "https://open.dingtalk.com/document/development/external-contact-modification"
namespace: "development"
slug: "external-contact-modification"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 外部联系人 > 外部联系人修改"
doc_id: "VQx6BcLzi7"
updated_at: "2025-08-28 19:46:28"
---

> Source: https://open.dingtalk.com/document/development/external-contact-modification
> Path: 应用开发 / 事件订阅 / 通讯录 > 外部联系人 > 外部联系人修改
> Updated: 2025-08-28 19:46:28

# 外部联系人修改

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 外部联系人修改 |
| 英文名称 | contact\_modify\_org |

## 功能描述

该数据为在授权的第三方企业应用中，企业修改外部联系人的推送信息。

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
- `data.errcode`（integer）：返回码。
- `data.errmsg`（string）：返回码说明。
- `data.shareUserIds`（array）：共享给的员工userid列表。
- `data.companyName`（string）：外部联系人的企业名称。
- `data.mobile`（string）：手机号。
- `data.userId`（string）：userId。
- `data.shareDeptIds`（array）：共享部门id列表。
- `data.labelIds`（array）：标签列表。
- `data.followerUserId`（string）：负责内部用户userId。
- `data.name`（string）：客户名称。
- `data.stateCode`（string）：手机号国家码。

### **事件体示例**

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
      123
    ],
    "shareUserIds": [
      "dsadad"
    ],
    "followerUserId": "2000121002668",
    "companyName": "企业1",
    "name": "潜在客户小张",
    "mobile": "12345678910",
    "errmsg": "ok",
    "stateCode": "86",
    "userId": "12345",
    "shareDeptIds": [
      123
    ]
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
- `biz_data.errcode`（integer）：返回码。
- `biz_data.errmsg`（string）：返回码说明。
- `biz_data.shareUserIds`（array）：共享给的员工userid列表。
- `biz_data.companyName`（string）：外部联系人的企业名称。
- `biz_data.mobile`（string）：手机号。
- `biz_data.userId`（string）：userId。
- `biz_data.shareDeptIds`（array）：共享部门id列表。
- `biz_data.labelIds`（array）：标签列表。
- `biz_data.followerUserId`（string）：负责内部用户userId。
- `biz_data.name`（string）：客户名称。
- `biz_data.stateCode`（string）：手机号国家码。

### **biz\_data数据示例(biz\_type=20)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 20,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "shareUserIds": [
      "dsadad"
    ],
    "syncAction": "contact_modify_org",
    "companyName": "企业1",
    "mobile": "12345678910",
    "errmsg": "ok",
    "userId": "12345",
    "shareDeptIds": [
      123
    ],
    "labelIds": [
      123
    ],
    "followerUserId": "2000121002668",
    "name": "潜在客户小张",
    "stateCode": "86"
  }
}
```
