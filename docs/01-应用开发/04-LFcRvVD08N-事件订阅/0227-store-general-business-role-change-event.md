---
title: "门店通业务角色变更事件"
source_url: "https://open.dingtalk.com/document/development/store-general-business-role-change-event"
namespace: "development"
slug: "store-general-business-role-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 行业通用 > 门店通业务角色变更事件"
doc_id: "7Ca54gBrPx"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/store-general-business-role-change-event
> Path: 应用开发 / 事件订阅 / 行业开放 > 行业通用 > 门店通业务角色变更事件
> Updated: 2022-01-19 19:29:22

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
