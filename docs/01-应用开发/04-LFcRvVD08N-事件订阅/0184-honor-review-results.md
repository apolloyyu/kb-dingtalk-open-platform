---
title: "荣誉审核结果"
source_url: "https://open.dingtalk.com/document/development/honor-review-results"
namespace: "development"
slug: "honor-review-results"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "企业文化 > 荣誉审核结果"
doc_id: "Xduk7osk1G"
updated_at: "2025-08-28 19:47:18"
---

> Source: https://open.dingtalk.com/document/development/honor-review-results
> Path: 应用开发 / 事件订阅 / 企业文化 > 荣誉审核结果
> Updated: 2025-08-28 19:47:18

# 荣誉审核结果

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 荣誉审核结果 |
| 英文名称 | honor\_audit |

## 功能描述

荣誉审核结果事件数据。

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
- `data.honorId`（string）：荣誉勋章模板id。
- `data.auditStatus`（boolean）：审核结果：  
  - true：审核通过  
  - false：审核拒绝
- `data.remark`（string）：审核拒绝原因。  
  >当auditStatus为false时，该字段有值。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "honor_audit",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "honorId": "216***02",
    "auditStatus": false,
    "remark": "文案中包含敏感词，请查看《钉钉荣誉规范条款》"
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
- `honorId`（string）：荣誉勋章模板id。
- `auditStatus`（boolean）：审核结果：  
  - true：审核通过  
  - false：审核拒绝
- `remark`（string）：审核拒绝原因。  
  >当auditStatus为false时，该字段有值。

### **事件体示例**

```
{
  "EventType": "honor_audit",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "honorId": "216***02",
  "auditStatus": false,
  "remark": "文案中包含敏感词，请查看《钉钉荣誉规范条款》"
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
- `biz_data.honorId`（string）：荣誉勋章模板id。
- `biz_data.auditStatus`（boolean）：审核结果：  
  - true：审核通过  
  - false：审核拒绝
- `biz_data.remark`（string）：审核拒绝原因。  
  >当auditStatus为false时，该字段有值。

### **biz\_data数据示例(biz\_type=270)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 270,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "honorId": "216***02",
    "syncAction": "honor_audit",
    "auditStatus": false,
    "remark": "文案中包含敏感词，请查看《钉钉荣誉规范条款》"
  }
}
```
