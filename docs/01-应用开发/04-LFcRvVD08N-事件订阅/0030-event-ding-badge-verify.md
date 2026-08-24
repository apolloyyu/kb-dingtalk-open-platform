---
title: "钉工牌核验事件"
source_url: "https://open.dingtalk.com/document/development/event-ding-badge-verify"
namespace: "development"
slug: "event-ding-badge-verify"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > 钉工牌 > 钉工牌核验事件"
doc_id: "xPstROsVes"
updated_at: "2025-08-27 16:11:08"
---

> Source: https://open.dingtalk.com/document/development/event-ding-badge-verify
> Path: 应用开发 / 事件订阅 / 办公 > 钉工牌 > 钉工牌核验事件
> Updated: 2025-08-27 16:11:08

# 钉工牌核验事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉工牌核验事件 |
| 英文名称 | ding\_badge\_verify |

## 功能描述

钉工牌扫码核验事件。

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
- `data.corpId`（string）：企业ID
- `data.userCorpRelationType`（string）：用户企业关系
- `data.userIdentity`（string）：用户标识
- `data.codeIdentity`（string）：码标识
- `data.codeId`（string）：码ID
- `data.verifyNo`（string）：核验号
- `data.verifyResult`（string）：核验结果
- `data.verifyAmount`（string）：核验金额
- `data.verifyTime`（string）：核验时间
- `data.verifyLocation`（string）：核验地点
- `data.verifyEvent`（string）：核验事件

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ding_badge_verify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "codeId": "codexxxxxx",
    "verifyEvent": "Test",
    "corpId": "dingxxxxx",
    "codeIdentity": "PURE_IDENTITY_CODE",
    "verifyLocation": "钉网科技",
    "userCorpRelationType": "INTERNAL_STAFF",
    "verifyResult": "SUCCESS",
    "verifyNo": "123xxx",
    "verifyAmount": "100.00",
    "verifyTime": "2023-07-04 00:00:00",
    "userIdentity": "20xxx123"
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
- `biz_data.corpId`（string）：企业ID
- `biz_data.userCorpRelationType`（string）：用户企业关系
- `biz_data.userIdentity`（string）：用户标识
- `biz_data.codeIdentity`（string）：码标识
- `biz_data.codeId`（string）：码ID
- `biz_data.verifyNo`（string）：核验号
- `biz_data.verifyResult`（string）：核验结果
- `biz_data.verifyAmount`（string）：核验金额
- `biz_data.verifyTime`（string）：核验时间
- `biz_data.verifyLocation`（string）：核验地点
- `biz_data.verifyEvent`（string）：核验事件

### **biz\_data数据示例(biz\_type=174)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 174,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpId": "dingxxxxx",
    "codeIdentity": "PURE_IDENTITY_CODE",
    "syncAction": "ding_badge_verify",
    "verifyResult": "SUCCESS",
    "verifyTime": "2023-07-04 00:00:00",
    "userIdentity": "20xxx123",
    "codeId": "codexxxxxx",
    "verifyEvent": "Test",
    "verifyLocation": "钉网科技",
    "userCorpRelationType": "INTERNAL_STAFF",
    "verifyNo": "123xxx",
    "verifyAmount": "100.00"
  }
}
```
