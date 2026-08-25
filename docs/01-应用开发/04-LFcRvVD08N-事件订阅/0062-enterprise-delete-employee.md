---
title: "企业删除员工"
source_url: "https://open.dingtalk.com/document/development/enterprise-delete-employee"
namespace: "development"
slug: "enterprise-delete-employee"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 企业管理 > 企业删除员工"
doc_id: "zk5JPMbMcS"
updated_at: "2025-08-28 19:46:25"
---

> Source: https://open.dingtalk.com/document/development/enterprise-delete-employee
> Path: 应用开发 / 事件订阅 / 通讯录 > 企业管理 > 企业删除员工
> Updated: 2025-08-28 19:46:25

# 企业删除员工

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除员工 |
| 英文名称 | user\_leave\_org |

## 功能描述

企业内部用户变更事件，该文档表示企业删除员工推送信息。

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
- `data.unionid`（string）：删除（离职）员工unionId。
- `data.dingId`（string）：删除（离职）员工dingId。
- `data.userId`（string）：删除（离职）员工userId。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "user_leave_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionid": "zvLdpxxxxxiEiE",
    "dingId": "$:LWCP_v1:$G5YX0l5yOKZ2oxxxx",
    "userId": "ding12345"
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
- `biz_data.unionid`（string）：删除（离职）员工unionId。
- `biz_data.dingId`（string）：删除（离职）员工dingId。
- `biz_data.userId`（string）：删除（离职）员工userId。

### **biz\_data数据示例(biz\_type=13)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 13,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionid": "zvLdpxxxxxiEiE",
    "syncAction": "user_leave_org",
    "dingId": "$:LWCP_v1:$G5YX0l5yOKZ2oxxxx",
    "userId": "ding12345"
  }
}
```
