---
title: "门店通业务角色变更事件"
source_url: "https://open.dingtalk.com/document/development/store-general-business-role-change-event"
namespace: "development"
slug: "store-general-business-role-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 行业通用 > 门店通业务角色变更事件"
doc_id: "7Ca54gBrPx"
updated_at: "2025-08-28 19:47:45"
---

> Source: https://open.dingtalk.com/document/development/store-general-business-role-change-event
> Path: 应用开发 / 事件订阅 / 行业开放 > 行业通用 > 门店通业务角色变更事件
> Updated: 2025-08-28 19:47:45

# 门店通业务角色变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 门店通业务角色变更事件 |
| 英文名称 | shop\_role\_event |

## 功能描述

门店通业务角色变更事件，包含业务角色的添加、更新、删除，以及角色对应的人员变更。

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
- `data.type`（string）：变更类型：  
    
  \* \*\*create\*\*：创建角色  
    
  \* \*\*update\*\*：更新角色  
    
  \* \*\*delete\*\*：删除角色  
    
  \* \*\*add\_user\*\*：角色下添加人员  
  \* \*\*remove\_user\*\*：角色下删除人员
- `data.roleId`（string）：角色Id。
- `data.userIdList`（array）：对应用户Id列表。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "shop_role_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "userIdList": [
      "09991122"
    ],
    "roleId": "122",
    "type": "remove_user"
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
- `biz_data.type`（string）：变更类型：  
    
  \* \*\*create\*\*：创建角色  
    
  \* \*\*update\*\*：更新角色  
    
  \* \*\*delete\*\*：删除角色  
    
  \* \*\*add\_user\*\*：角色下添加人员  
  \* \*\*remove\_user\*\*：角色下删除人员
- `biz_data.role_id`（string）：角色Id。
- `biz_data.user_id_list`（array）：对应用户Id列表。

### **biz\_data数据示例(biz\_type=295)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 295,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "user_id_list": [
      "09991122"
    ],
    "syncAction": "shop_role_event",
    "role_id": "122",
    "type": "remove_user"
  }
}
```
