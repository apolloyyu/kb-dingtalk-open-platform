---
title: "服务群工单添加备注"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-add-comment"
namespace: "development"
slug: "service-group-work-order-add-comment"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单添加备注"
doc_id: "5KsDtGVSkE"
updated_at: "2025-08-28 19:46:15"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-add-comment
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单添加备注
> Updated: 2025-08-28 19:46:15

# 服务群工单添加备注

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单添加备注 |
| 英文名称 | servicegroup\_ticket\_memo\_add |

## 功能描述

服务群工单添加备注的推送数据。

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
- `data.spiTicketModel`（object）：工单事件数据。
- `data.spiTicketModel.openTicketId`（string）：工单ID。
- `data.spiTicketModel.operateMemo`（object）：工单备注。
- `data.spiTicketModel.operateMemo.attachments`（array）：附件。
- `data.spiTicketModel.operateMemo.attachments[].fileName`（string）：文件名称。
- `data.spiTicketModel.operateMemo.attachments[].key`（string）：文件key。
- `data.spiTicketModel.operateMemo.attachments[].type`（string）：文件类型。
- `data.spiTicketModel.operateMemo.memo`（string）：备注-文字。
- `data.spiTicketModel.operatorNickName`（string）：操作人昵称。
- `data.spiTicketModel.operatorUnionId`（string）：操作人ID。
- `data.spiTicketModel.operateType`（string）：操作类型。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_ticket_memo_add",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateType": "ADD_MEMO",
      "operatorNickName": "张宇航小号",
      "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
      "openTicketId": "ISeGR7JOP8IiE",
      "operateMemo": {
        "attachments": [
          {
            "fileName": "01d11e438f03410d53693fcf5efed334.jpeg",
            "type": "img",
            "key": "ticket/image/41661019/123001/8812788f16574d9d891f6186d7b629e4_1626174465926.jpeg"
          }
        ],
        "memo": "测试"
      }
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
- `spiTicketModel`（object）：工单事件数据。
- `spiTicketModel.openTicketId`（string）：工单ID。
- `spiTicketModel.operateMemo`（object）：工单备注。
- `spiTicketModel.operateMemo.attachments`（array）：附件。
- `spiTicketModel.operateMemo.attachments[].fileName`（string）：文件名称。
- `spiTicketModel.operateMemo.attachments[].key`（string）：文件key。
- `spiTicketModel.operateMemo.attachments[].type`（string）：文件类型。
- `spiTicketModel.operateMemo.memo`（string）：备注-文字。
- `spiTicketModel.operatorNickName`（string）：操作人昵称。
- `spiTicketModel.operatorUnionId`（string）：操作人ID。
- `spiTicketModel.operateType`（string）：操作类型。

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_memo_add",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateType": "ADD_MEMO",
    "operatorNickName": "张宇航小号",
    "operatorUnionId": "NK0qMkt7e03wGiS26tiPf8hgiEiE",
    "openTicketId": "ISeGR7JOP8IiE",
    "operateMemo": {
      "attachments": [
        {
          "fileName": "01d11e438f03410d53693fcf5efed334.jpeg",
          "type": "img",
          "key": "ticket/image/41661019/123001/8812788f16574d9d891f6186d7b629e4_1626174465926.jpeg"
        }
      ],
      "memo": "测试"
    }
  }
}
```
