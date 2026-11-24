---
title: "群内安装酷应用事件"
source_url: "https://open.dingtalk.com/document/development/install-cool-application-events-in-the-group"
namespace: "development"
slug: "install-cool-application-events-in-the-group"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "即时通讯 > 酷应用 > 群内安装酷应用事件"
doc_id: "FwNsEvXdAR"
updated_at: "2025-08-28 19:46:47"
---

> Source: https://open.dingtalk.com/document/development/install-cool-application-events-in-the-group
> Path: 应用开发 / 事件订阅 / 即时通讯 > 酷应用 > 群内安装酷应用事件
> Updated: 2025-08-28 19:46:47

# 群内安装酷应用事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 群内安装酷应用事件 |
| 英文名称 | im\_cool\_app\_install |

## 功能描述

群聊安装酷应用事件数据说明。

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
- `data.operateTime`（string）：操作时间。
- `data.coolAppCode`（string）：群扩展code。
- `data.openConversationCorpId`（string）：群会话企业corpId。
- `data.robotCode`（string）：机器人code。
- `data.openConversationId`（string）：群加密会话ID。
- `data.operator`（string）：操作人userId。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "im_cool_app_install",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
    "operateTime": "1641866135051",
    "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
    "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
    "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
    "operator": "0213454xxxx1745"
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
- `operateTime`（string）：操作时间。
- `coolAppCode`（string）：群扩展code。
- `openConversationCorpId`（string）：群会话企业corpId。
- `robotCode`（string）：机器人code。
- `openConversationId`（string）：群加密会话ID。
- `operator`（string）：操作人userId。

### **事件体示例**

```
{
  "EventType": "im_cool_app_install",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
  "operateTime": "1641866135051",
  "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
  "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
  "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
  "operator": "0213454xxxx1745"
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
- `biz_data.operateTime`（string）：操作时间。
- `biz_data.coolAppCode`（string）：群扩展code。
- `biz_data.openConversationCorpId`（string）：群会话企业corpId。
- `biz_data.robotCode`（string）：机器人code。
- `biz_data.openConversationId`（string）：群加密会话ID。
- `biz_data.operator`（string）：操作人userId。

### **biz\_data数据示例(biz\_type=158)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 158,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "im_cool_app_install",
    "coolAppCode": "COOLAPP-1-1018xxxxxxxxxxxxxxxx",
    "operateTime": "1641866135051",
    "openConversationCorpId": "ding9bd1bfb59xxxxxxxxxxxxxxxxxxx",
    "robotCode": "rBLBXuiaA2rn3xxxxxxxxxxxxxx",
    "openConversationId": "cidT461wC7yvGJxxxxxxxxxxxxxx",
    "operator": "0213454xxxx1745"
  }
}
```
