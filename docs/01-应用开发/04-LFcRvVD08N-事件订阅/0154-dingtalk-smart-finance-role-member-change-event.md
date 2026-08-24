---
title: "钉钉智能财务角色成员变更事件"
source_url: "https://open.dingtalk.com/document/development/dingtalk-smart-finance-role-member-change-event"
namespace: "development"
slug: "dingtalk-smart-finance-role-member-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 钉钉智能财务角色成员变更事件"
doc_id: "JuX6PG8xYr"
updated_at: "2025-08-28 19:47:10"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-smart-finance-role-member-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 钉钉智能财务角色成员变更事件
> Updated: 2025-08-28 19:47:10

# 钉钉智能财务角色成员变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉智能财务角色成员变更事件 |
| 英文名称 | smart\_finance\_role\_member\_change |

## 功能描述

数据为智能财务的角色成员变更事件相关数据。

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
- `data.addUserIdList`（array）：新增的成员userId信息。
- `data.changeType`（string）：变更类型：  
  - add：新增  
  - remove：移除  
  - addAndRemove：新增和移除
- `data.roleCode`（string）：角色标识code。
- `data.finalUserIdList`（array）：最终的成员userId信息。
- `data.removeUserIdList`（array）：删除的成员userId信息。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "smart_finance_role_member_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "addUserIdList": [
      "01274xxx22009194681"
    ],
    "roleCode": "accountantManager",
    "changeType": "add",
    "finalUserIdList": [
      "01274xxx022009194681"
    ],
    "removeUserIdList": [
      "01274555410xx4681"
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
- `biz_data.addUserIdList`（array）：新增的成员userId信息。
- `biz_data.changeType`（string）：变更类型：  
  - add：新增  
  - remove：移除  
  - addAndRemove：新增和移除
- `biz_data.roleCode`（string）：角色标识code。
- `biz_data.finalUserIdList`（array）：最终的成员userId信息。
- `biz_data.removeUserIdList`（array）：删除的成员userId信息。

### **biz\_data数据示例(biz\_type=203)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 203,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "addUserIdList": [
      "01274xxx22009194681"
    ],
    "syncAction": "smart_finance_role_member_change",
    "roleCode": "accountantManager",
    "changeType": "add",
    "finalUserIdList": [
      "01274xxx022009194681"
    ],
    "removeUserIdList": [
      "01274555410xx4681"
    ]
  }
}
```
