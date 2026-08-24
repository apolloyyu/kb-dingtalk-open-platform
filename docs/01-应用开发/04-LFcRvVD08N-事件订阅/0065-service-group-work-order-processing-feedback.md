---
title: "服务群工单处理反馈"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-processing-feedback"
namespace: "development"
slug: "service-group-work-order-processing-feedback"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单处理反馈"
doc_id: "fHTHsiLiHT"
updated_at: "2025-08-28 19:46:15"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-processing-feedback
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单处理反馈
> Updated: 2025-08-28 19:46:15

# 服务群工单处理反馈

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单处理反馈 |
| 英文名称 | servicegroup\_ticket\_deal\_feedback |

## 功能描述

服务群工单处理反馈。

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
- `data.bizId`（string）：业务ID。
- `data.corpId`（string）：企业ID。
- `data.spiTicketModel`（object）：事件模型。
- `data.spiTicketModel.openTicketId`（string）：工单ID。
- `data.spiTicketModel.operateData`（object）
- `data.spiTicketModel.operateData.dealResult`（string）：处理反馈意见，解决/未解决
- `data.spiTicketModel.operateMemo`（object）：备注。
- `data.spiTicketModel.operateMemo.memo`（string）：备注内容。
- `data.spiTicketModel.operateType`（string）：操作类型。
- `data.spiTicketModel.operatorNickName`（string）：操作人昵称。
- `data.spiTicketModel.operatorUnionId`（string）：操作人ID。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_ticket_deal_feedback",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpId": "dingadc88253b4d581bd35c2f4657eb6378f",
    "bizId": "88888",
    "spiTicketModel": {
      "operateData": {
        "dealResult": "SOLVED"
      },
      "operateType": "DEAL_RESULT",
      "operatorNickName": "张宇航小号",
      "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
      "openTicketId": "dkp1jLhLpgMiE",
      "operateMemo": {
        "memo": "8888"
      }
    }
  }
}
```

HTTP推送

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `eventId`（String）：事件的唯一Id。
- `BizId`（string）：业务ID。
- `CorpId`（string）：企业ID。
- `spiTicketModel`（object）：事件模型。
- `spiTicketModel.openTicketId`（string）：工单ID。
- `spiTicketModel.operateData`（object）
- `spiTicketModel.operateData.dealResult`（string）：处理反馈意见，解决/未解决
- `spiTicketModel.operateMemo`（object）：备注。
- `spiTicketModel.operateMemo.memo`（string）：备注内容。
- `spiTicketModel.operateType`（string）：操作类型。
- `spiTicketModel.operatorNickName`（string）：操作人昵称。
- `spiTicketModel.operatorUnionId`（string）：操作人ID。

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_deal_feedback",
  "EventTime": 1663143335567,
  "CorpId": "dingadc88253b4d581bd35c2f4657eb6378f",
  "BizId": "88888",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "dealResult": "SOLVED"
    },
    "operateType": "DEAL_RESULT",
    "operatorNickName": "张宇航小号",
    "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
    "openTicketId": "dkp1jLhLpgMiE",
    "operateMemo": {
      "memo": "8888"
    }
  }
}
```
