---
title: "员工角色管理范围变更事件"
source_url: "https://open.dingtalk.com/document/development/events-emp-label-scope-change"
namespace: "development"
slug: "events-emp-label-scope-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 角色管理 > 员工角色管理范围变更事件"
doc_id: "HIC8Hd2zsh"
updated_at: "2026-08-20 13:58:08"
---

> Source: https://open.dingtalk.com/document/development/events-emp-label-scope-change
> Path: 应用开发 / 事件订阅 / 通讯录 > 角色管理 > 员工角色管理范围变更事件
> Updated: 2026-08-20 13:58:08

# 员工角色管理范围变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 员工角色管理范围变更事件 |
| 英文名称 | emp\_label\_scope\_change |

## 功能描述

员工角色管理范围发生变更时，发送这个事件

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |
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
- `data.corpId`（string）：企业corpId
- `data.postDeptIds`（array）：变更后的部门id列表，可空
- `data.labelId`（long）：角色ID
- `data.userId`（string）：员工UserId
- `data.preDeptIds`（array）：变更前的部门id列表，可空

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "emp_label_scope_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "preDeptIds": [
      12345
    ],
    "corpId": "ding12345",
    "labelId": 12345,
    "userId": "abc123",
    "postDeptIds": [
      54321
    ]
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `corpId`（string，必填）：企业corpId
- `postDeptIds`（array）：变更后的部门id列表，可空
- `labelId`（long，必填）：角色ID
- `userId`（string，必填）：员工UserId
- `preDeptIds`（array）：变更前的部门id列表，可空

### **事件体示例**

```
{
  "EventType": "emp_label_scope_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "preDeptIds": [
    12345
  ],
  "corpId": "ding12345",
  "labelId": 12345,
  "userId": "abc123",
  "postDeptIds": [
    54321
  ]
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
- `biz_data.corpId`（string）：企业corpId
- `biz_data.postDeptIds`（array）：变更后的部门id列表，可空
- `biz_data.labelId`（long）：角色ID
- `biz_data.userId`（string）：员工UserId
- `biz_data.preDeptIds`（array）：变更前的部门id列表，可空

### **biz\_data数据示例(biz\_type=505)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 505,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "preDeptIds": [
      12345
    ],
    "corpId": "ding12345",
    "labelId": 12345,
    "syncAction": "emp_label_scope_change",
    "userId": "abc123",
    "postDeptIds": [
      54321
    ]
  }
}
```
