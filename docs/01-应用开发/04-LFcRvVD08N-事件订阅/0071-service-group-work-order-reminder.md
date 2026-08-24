---
title: "服务群工单催办"
source_url: "https://open.dingtalk.com/document/development/service-group-work-order-reminder"
namespace: "development"
slug: "service-group-work-order-reminder"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群工单催办"
doc_id: "eE8N4R2fgp"
updated_at: "2025-08-28 19:46:18"
---

> Source: https://open.dingtalk.com/document/development/service-group-work-order-reminder
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群工单催办
> Updated: 2025-08-28 19:46:18

# 服务群工单催办

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群工单催办 |
| 英文名称 | servicegroup\_ticket\_urge |

## 功能描述

服务群工单催办的推送数据。

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
- `data.spiTicketModel`（object）
- `data.spiTicketModel.openTicketId`（string）：工单ID。
- `data.spiTicketModel.operateData`（object）
- `data.spiTicketModel.operateData.receivers`（array）：接收人。
- `data.spiTicketModel.operateData.receivers[].nickName`（string）：昵称。
- `data.spiTicketModel.operateData.receivers[].unionId`（string）：ID。
- `data.spiTicketModel.operateMemo`（object）：备注内容。
- `data.spiTicketModel.operateMemo.attachments`（array）：附件。
- `data.spiTicketModel.operateMemo.attachments[].fileName`（string）：文件名。
- `data.spiTicketModel.operateMemo.attachments[].key`（string）：文件。
- `data.spiTicketModel.operateMemo.attachments[].type`（string）：文件类型。
- `data.spiTicketModel.operateMemo.memo`（string）：备注-文字版。
- `data.spiTicketModel.operatorNickName`（string）：操作人昵称。
- `data.spiTicketModel.operatorUnionId`（string）：操作人ID。
- `data.spiTicketModel.operateType`（string）：操作类型。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_ticket_urge",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiTicketModel": {
      "operateData": {
        "receivers": [
          {
            "unionId": "1AE3AiiPwsBZSKB3lvssfOgiEiE",
            "nickName": "李航宇"
          }
        ]
      },
      "operateType": "URGE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
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
- `spiTicketModel`（object）
- `spiTicketModel.openTicketId`（string）：工单ID。
- `spiTicketModel.operateData`（object）
- `spiTicketModel.operateData.receivers`（array）：接收人。
- `spiTicketModel.operateData.receivers[].nickName`（string）：昵称。
- `spiTicketModel.operateData.receivers[].unionId`（string）：ID。
- `spiTicketModel.operateMemo`（object）：备注内容。
- `spiTicketModel.operateMemo.attachments`（array）：附件。
- `spiTicketModel.operateMemo.attachments[].fileName`（string）：文件名。
- `spiTicketModel.operateMemo.attachments[].key`（string）：文件。
- `spiTicketModel.operateMemo.attachments[].type`（string）：文件类型。
- `spiTicketModel.operateMemo.memo`（string）：备注-文字版。
- `spiTicketModel.operatorNickName`（string）：操作人昵称。
- `spiTicketModel.operatorUnionId`（string）：操作人ID。
- `spiTicketModel.operateType`（string）：操作类型。

### **事件体示例**

```
{
  "EventType": "servicegroup_ticket_urge",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiTicketModel": {
    "operateData": {
      "receivers": [
        {
          "unionId": "1AE3AiiPwsBZSKB3lvssfOgiEiE",
          "nickName": "李航宇"
        }
      ]
    },
    "operateType": "URGE",
    "operatorNickName": "王鸿程",
    "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
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

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### root

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.spiTicketModel`（object）
- `biz_data.spiTicketModel.openTicketId`（string）：工单ID。
- `biz_data.spiTicketModel.operateData`（object）
- `biz_data.spiTicketModel.operateData.receivers`（array）：接收人。
- `biz_data.spiTicketModel.operateData.receivers[].nickName`（string）：昵称。
- `biz_data.spiTicketModel.operateData.receivers[].unionId`（string）：ID。
- `biz_data.spiTicketModel.operateMemo`（object）：备注内容。
- `biz_data.spiTicketModel.operateMemo.attachments`（array）：附件。
- `biz_data.spiTicketModel.operateMemo.attachments[].fileName`（string）：文件名。
- `biz_data.spiTicketModel.operateMemo.attachments[].key`（string）：文件。
- `biz_data.spiTicketModel.operateMemo.attachments[].type`（string）：文件类型。
- `biz_data.spiTicketModel.operateMemo.memo`（string）：备注-文字版。
- `biz_data.spiTicketModel.operatorNickName`（string）：操作人昵称。
- `biz_data.spiTicketModel.operatorUnionId`（string）：操作人ID。
- `biz_data.spiTicketModel.operateType`（string）：操作类型。

### **biz\_data数据示例(biz\_type=122)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 122,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "servicegroup_ticket_urge",
    "spiTicketModel": {
      "operateData": {
        "receivers": [
          {
            "unionId": "1AE3AiiPwsBZSKB3lvssfOgiEiE",
            "nickName": "李航宇"
          }
        ]
      },
      "operateType": "URGE",
      "operatorNickName": "王鸿程",
      "operatorUnionId": "9dQurQX3VspSKB3lvssfOgiEiE",
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
