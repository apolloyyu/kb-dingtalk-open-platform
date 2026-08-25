---
title: "服务群群信息变更"
source_url: "https://open.dingtalk.com/document/development/event-servicegroup-group-info-change"
namespace: "development"
slug: "event-servicegroup-group-info-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群群信息变更"
doc_id: "D2XGfGz6eo"
updated_at: "2025-08-28 19:46:11"
---

> Source: https://open.dingtalk.com/document/development/event-servicegroup-group-info-change
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群群信息变更
> Updated: 2025-08-28 19:46:11

# 服务群群信息变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群群信息变更 |
| 英文名称 | servicegroup\_group\_info\_change |

## 功能描述

服务群群信息变更事件数据信息。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.spiGroupModel`（object）：群信息变更数据。
- `data.spiGroupModel.operateData`（object）：业务相关数据。  
  >各操作数据不同，无数据是为{}。
- `data.spiGroupModel.operateData.bizId`（string）：群绑定的业务ID
- `data.spiGroupModel.openTeamId`（string）：开放团队id。
- `data.spiGroupModel.operateType`（string）：操作类型。
- `data.spiGroupModel.operatorNickName`（string）：操作者昵称。
- `data.spiGroupModel.operatorUnionId`（string）：操作者的unionId。
- `data.spiGroupModel.openConversationId`（string）：群会话id。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_group_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiGroupModel": {
      "operateData": {
        "bizId": "11222"
      },
      "openTeamId": "exxxxxxwsKEiE",
      "operateType": "BIZ_ID_BIND_CHANGE",
      "operatorNickName": "xxxx",
      "operatorUnionId": "NK0qMkt7e03wGiS26tiPxxxxxxxx",
      "openConversationId": "cidcxxxxxad4PB5ziwAOzgZGw\u003d\u003d"
    }
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
- `spiGroupModel`（object）：群信息变更数据。
- `spiGroupModel.operateData`（object）：业务相关数据。  
  >各操作数据不同，无数据是为{}。
- `spiGroupModel.operateData.bizId`（string）：群绑定的业务ID
- `spiGroupModel.openTeamId`（string）：开放团队id。
- `spiGroupModel.operateType`（string）：操作类型。
- `spiGroupModel.operatorNickName`（string）：操作者昵称。
- `spiGroupModel.operatorUnionId`（string）：操作者的unionId。
- `spiGroupModel.openConversationId`（string）：群会话id。

### **事件体示例**

```
{
  "EventType": "servicegroup_group_info_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiGroupModel": {
    "operateData": {
      "bizId": "11222"
    },
    "openTeamId": "exxxxxxwsKEiE",
    "operateType": "BIZ_ID_BIND_CHANGE",
    "operatorNickName": "xxxx",
    "operatorUnionId": "NK0qMkt7e03wGiS26tiPxxxxxxxx",
    "openConversationId": "cidcxxxxxad4PB5ziwAOzgZGw\u003d\u003d"
  }
}
```
