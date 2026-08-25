---
title: "企业增加角色"
source_url: "https://open.dingtalk.com/document/development/businesses-increase-roles"
namespace: "development"
slug: "businesses-increase-roles"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 企业管理 > 企业增加角色"
doc_id: "zoQjEtIxPO"
updated_at: "2025-08-28 19:46:22"
---

> Source: https://open.dingtalk.com/document/development/businesses-increase-roles
> Path: 应用开发 / 事件订阅 / 通讯录 > 企业管理 > 企业增加角色
> Updated: 2025-08-28 19:46:22

# 企业增加角色

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业增加角色 |
| 英文名称 | org\_role\_add |

## 功能描述

数据为企业角色的最新状态。该数据为在授权的第三方企业应用中，发生角色的增加的时刻推送。

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
- `data.roleId`（long）：角色Id。
- `data.groupId`（long）：角色组id。
- `data.roleName`（string）：角色名称。
- `data.groupName`（string）：角色组名称。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_role_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "groupName": "默认角色组",
    "roleId": 12345,
    "groupId": 1,
    "roleName": "角色01"
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
- `biz_data.role_name`（string）：角色名称。
- `biz_data.role_id`（long）：角色Id。
- `biz_data.group_id`（long）：角色组id。
- `biz_data.group_name`（string）：角色组名称。

### **biz\_data数据示例(biz\_type=15)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 15,
  "biz_data": {
    "role_name": "角色01",
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "org_role_add",
    "role_id": 12345,
    "group_id": 1,
    "group_name": "默认角色组"
  }
}
```
