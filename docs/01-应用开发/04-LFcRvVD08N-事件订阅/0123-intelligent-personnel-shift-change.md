---
title: "班次变更"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-shift-change"
namespace: "development"
slug: "intelligent-personnel-shift-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 班次变更"
doc_id: "JCfseyI8zQ"
updated_at: "2025-12-08 17:42:04"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-shift-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 班次变更
> Updated: 2025-12-08 17:42:04

# 班次变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 班次变更 |
| 英文名称 | attend\_shift\_change |

## 功能描述

班次变更事件数据。

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
- `data.corpid`（string）：企业corpId。
- `data.name`（string）：班次名称。
- `data.action`（string）：班次动作简要信息：  
  - attend\_shift\_create：企业增加班次之后的简要信息  
  - attend\_shift\_update：企业修改班次之后的简要信息  
  - attend\_shift\_delete：企业删除班次之后的简要信息
- `data.id`（number）：班次id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "attend_shift_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "dingxxxx",
    "name": "班次A",
    "action": "attend_group_delete",
    "id": "11112222"
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
- `corpid`（string）：企业corpId。
- `name`（string）：班次名称。
- `action`（string）：班次动作简要信息：  
  - attend\_shift\_create：企业增加班次之后的简要信息  
  - attend\_shift\_update：企业修改班次之后的简要信息  
  - attend\_shift\_delete：企业删除班次之后的简要信息
- `id`（number）：班次id。

### **事件体示例**

```
{
  "EventType": "attend_shift_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "dingxxxx",
  "name": "班次A",
  "action": "attend_group_delete",
  "id": "11112222"
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
- `biz_data.corpid`（string）：企业corpId。
- `biz_data.name`（string）：班次名称。
- `biz_data.action`（string）：班次动作简要信息：  
  - attend\_shift\_create：企业增加班次之后的简要信息  
  - attend\_shift\_update：企业修改班次之后的简要信息  
  - attend\_shift\_delete：企业删除班次之后的简要信息
- `biz_data.id`（number）：班次id。

### **biz\_data数据示例(biz\_type=153)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 153,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "dingxxxx",
    "syncAction": "attend_shift_change",
    "name": "班次A",
    "action": "attend_group_delete",
    "id": "11112222"
  }
}
```
