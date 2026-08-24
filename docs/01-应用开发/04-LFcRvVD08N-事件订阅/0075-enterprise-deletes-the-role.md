---
title: "企业删除角色"
source_url: "https://open.dingtalk.com/document/development/enterprise-deletes-the-role"
namespace: "development"
slug: "enterprise-deletes-the-role"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 企业删除角色"
doc_id: "immyCpKMn3"
updated_at: "2025-12-08 14:22:04"
---

> Source: https://open.dingtalk.com/document/development/enterprise-deletes-the-role
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 企业删除角色
> Updated: 2025-12-08 14:22:04

# 企业删除角色

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除角色 |
| 英文名称 | org\_role\_remove |

## 功能描述

数据为企业角色的最新状态。该数据为在授权的第三方企业应用中，发生角色的删除的时刻推送。

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
- `data.roleId`（string）：角色id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_role_remove",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "roleId": "1234"
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
- `biz_data.role_id`（string）：角色id。

### **biz\_data数据示例(biz\_type=15)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 15,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "org_role_remove",
    "role_id": "1234"
  }
}
```
