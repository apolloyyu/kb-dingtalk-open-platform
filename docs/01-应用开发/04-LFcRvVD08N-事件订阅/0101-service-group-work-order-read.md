---
title: "服务群工单已读"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-read"
namespace: "development"
slug: "service-group-work-order-read"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单已读"
doc_id: "FLX3DP5Q5P"
updated_at: "2025-08-28 19:46:16"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-read
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单已读
> Updated: 2025-08-28 19:46:16

# 服务群工单已读

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单已读 |
| 英文名称 | servicegroup\_ticket\_read |

## 功能描述

服务群工单已读事件。

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
- `data.spiTicketModel`（object）：工单事件模型
- `data.spiTicketModel.openTicketId`（string）：工单ID
- `data.spiTicketModel.operateData`（object）：操作数据
- `data.spiTicketModel.operateData.operate`（string）：卡片操作
- `data.spiTicketModel.operateData.ticketSnapshot`（object）：工单快照
- `data.spiTicketModel.operateData.ticketSnapshot.stage`（string）：阶段
- `data.spiTicketModel.operateData.ticketSnapshot.processor`（object）：当前处理人
- `data.spiTicketModel.operateData.ticketSnapshot.processor.nickName`（string）：昵称
- `data.spiTicketModel.operateData.ticketSnapshot.processor.unionId`（string）：ID
- `data.spiTicketModel.operateData.ticketSnapshot.takers`（array）：待处理人
- `data.spiTicketModel.operateData.ticketSnapshot.takers[].nickName`（string）：昵称
- `data.spiTicketModel.operateData.ticketSnapshot.takers[].unionId`（string）：ID
- `data.spiTicketModel.operatorNickName`（string）：操作人
- `data.spiTicketModel.operatorUnionId`（string）：操作人ID
- `data.spiTicketModel.operateType`（string）：操作类型

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_ticket_read",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateData": {
        "operate": "CREATE",
        "ticketSnapshot": {
          "takers": [
            {
              "unionId": "1111",
              "nickName": "张三"
            }
          ],
          "stage": "PROCESSING",
          "processor": {
            "unionId": "1111",
            "nickName": "张三"
          }
        }
      },
      "operateType": "READ",
      "operatorNickName": "张三",
      "operatorUnionId": "11111",
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
- `spiTicketModel`（object）：工单事件模型
- `spiTicketModel.openTicketId`（string）：工单ID
- `spiTicketModel.operateData`（object）：操作数据
- `spiTicketModel.operateData.operate`（string）：卡片操作
- `spiTicketModel.operateData.ticketSnapshot`（object）：工单快照
- `spiTicketModel.operateData.ticketSnapshot.stage`（string）：阶段
- `spiTicketModel.operateData.ticketSnapshot.processor`（object）：当前处理人
- `spiTicketModel.operateData.ticketSnapshot.processor.nickName`（string）：昵称
- `spiTicketModel.operateData.ticketSnapshot.processor.unionId`（string）：ID
- `spiTicketModel.operateData.ticketSnapshot.takers`（array）：待处理人
- `spiTicketModel.operateData.ticketSnapshot.takers[].nickName`（string）：昵称
- `spiTicketModel.operateData.ticketSnapshot.takers[].unionId`（string）：ID
- `spiTicketModel.operatorNickName`（string）：操作人
- `spiTicketModel.operatorUnionId`（string）：操作人ID
- `spiTicketModel.operateType`（string）：操作类型

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_read",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "operate": "CREATE",
      "ticketSnapshot": {
        "takers": [
          {
            "unionId": "1111",
            "nickName": "张三"
          }
        ],
        "stage": "PROCESSING",
        "processor": {
          "unionId": "1111",
          "nickName": "张三"
        }
      }
    },
    "operateType": "READ",
    "operatorNickName": "张三",
    "operatorUnionId": "11111",
    "openTicketId": "ISeGR7JOP8IiE"
  }
}
```
