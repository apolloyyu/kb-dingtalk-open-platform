---
title: "服务群工单申领"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-application"
namespace: "development"
slug: "service-group-work-order-application"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单申领"
doc_id: "5EvzTzUyLK"
updated_at: "2025-08-28 19:46:18"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-application
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单申领
> Updated: 2025-08-28 19:46:18

# 服务群工单申领

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单申领 |
| 英文名称 | servicegroup\_ticket\_take |

## 功能描述

服务群工单申领事件。

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
- `data.spiTicketModel`（object）：工单事件。
- `data.spiTicketModel.openTicketId`（string）：工单ID。
- `data.spiTicketModel.operateData`（object）
- `data.spiTicketModel.operateData.originTakers`（array）：原始可申领人数据集。
- `data.spiTicketModel.operateData.originTakers[].nickName`（string，必填）：可申领人昵称。
- `data.spiTicketModel.operateData.originTakers[].unionId`（string，必填）：可申领人ID。
- `data.spiTicketModel.operatorNickName`（string）：申领人昵称。
- `data.spiTicketModel.operatorUnionId`（string）：申领人ID。
- `data.spiTicketModel.operateType`（string）：操作类型。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_ticket_take",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateData": {
        "originTakers": [
          {
            "unionId": "9dQurQX3VspSKB3lvssfOgiEiE",
            "nickName": "王鸿程"
          }
        ]
      },
      "operateType": "TAKE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
      "openTicketId": "ISeGR7JOP8IiE"
    }
  }
}
```

HTTP推送

### root

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `spiTicketModel`（object）：工单事件。
- `spiTicketModel.openTicketId`（string）：工单ID。
- `spiTicketModel.operateData`（object）
- `spiTicketModel.operateData.originTakers`（array）：原始可申领人数据集。
- `spiTicketModel.operateData.originTakers[].nickName`（string，必填）：可申领人昵称。
- `spiTicketModel.operateData.originTakers[].unionId`（string，必填）：可申领人ID。
- `spiTicketModel.operatorNickName`（string）：申领人昵称。
- `spiTicketModel.operatorUnionId`（string）：申领人ID。
- `spiTicketModel.operateType`（string）：操作类型。

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_take",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "originTakers": [
        {
          "unionId": "9dQurQX3VspSKB3lvssfOgiEiE",
          "nickName": "王鸿程"
        }
      ]
    },
    "operateType": "TAKE",
    "operatorNickName": "王鸿程",
    "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
    "openTicketId": "ISeGR7JOP8IiE"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.spiTicketModel`（object）：工单事件。
- `biz_data.spiTicketModel.openTicketId`（string）：工单ID。
- `biz_data.spiTicketModel.operateData`（object）
- `biz_data.spiTicketModel.operateData.originTakers`（array）：原始可申领人数据集。
- `biz_data.spiTicketModel.operateData.originTakers[].nickName`（string，必填）：可申领人昵称。
- `biz_data.spiTicketModel.operateData.originTakers[].unionId`（string，必填）：可申领人ID。
- `biz_data.spiTicketModel.operatorNickName`（string）：申领人昵称。
- `biz_data.spiTicketModel.operatorUnionId`（string）：申领人ID。
- `biz_data.spiTicketModel.operateType`（string）：操作类型。

### **biz\_data数据示例(biz\_type=116)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 116,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "servicegroup_ticket_take",
    "spiTicketModel": {
      "operateData": {
        "originTakers": [
          {
            "unionId": "9dQurQX3VspSKB3lvssfOgiEiE",
            "nickName": "王鸿程"
          }
        ]
      },
      "operateType": "TAKE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
      "openTicketId": "ISeGR7JOP8IiE"
    }
  }
}
```
