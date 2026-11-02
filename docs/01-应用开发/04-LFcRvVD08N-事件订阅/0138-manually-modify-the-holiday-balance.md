---
title: "手动修改假期余额"
source_url: "https://open.dingtalk.com/document/development/manually-modify-the-holiday-balance"
namespace: "development"
slug: "manually-modify-the-holiday-balance"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 手动修改假期余额"
doc_id: "UWPphUQxv3"
updated_at: "2025-08-28 19:46:56"
---

> Source: https://open.dingtalk.com/document/development/manually-modify-the-holiday-balance
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 手动修改假期余额
> Updated: 2025-08-28 19:46:56

# 手动修改假期余额

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 手动修改假期余额 |
| 英文名称 | leave\_quota\_update |
| 事件BizType | 353 |

## 功能描述

当管理员手动修改假期余额时，钉钉通过事件订阅的方式将规则变更内容推送给开发者。

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
- `data.leaveCode`（string）：假期唯一标识。
- `data.opUserId`（string）：操作人userId。
- `data.userId`（string）：员工userId。
- `data.updateType`（string）：余额更新类型：  
  - add：添加  
  - delete：删除  
  - update：更新

### **事件体示例**

```
{
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "data": {
    "leaveCode": "abcdef-ghdsfc-123",
    "opUserId": "111",
    "userId": "123",
    "updateType": "ADD"
  },
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventType": "leave_quota_update",
  "eventBornTime": 1683533823336
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `leaveCode`（string，必填）：假期唯一标识。
- `opUserId`（string，必填）：操作人userId。
- `userId`（string，必填）：员工userId。
- `updateType`（string，必填）：余额更新类型：  
  - add：添加  
  - delete：删除  
  - update：更新

### **事件体示例**

```
{
  "CorpId": "1663**351222567",
  "EventType": "leave_quota_update",
  "EventTime": 1663143335567,
  "leaveCode": "abcdef-ghdsfc-123",
  "opUserId": "111",
  "userId": "123",
  "BizId": "1663**35567",
  "updateType": "ADD"
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
- `biz_data.leaveCode`（string）：假期唯一标识。
- `biz_data.opUserId`（string）：操作人userId。
- `biz_data.userId`（string）：员工userId。
- `biz_data.updateType`（string）：余额更新类型：  
  - add：添加  
  - delete：删除  
  - update：更新

### **biz\_data数据示例(biz\_type=353)**

```
{
  "biz_type": 353,
  "biz_id": "1663**35567",
  "biz_data": {
    "syncAction": "leave_quota_update",
    "leaveCode": "abcdef-ghdsfc-123",
    "opUserId": "111",
    "userId": "123",
    "updateType": "ADD"
  },
  "corp_id": "1663**351222567"
}
```
