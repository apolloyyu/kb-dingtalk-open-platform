---
title: "荣誉审核结果"
source_url: "https://open.dingtalk.com/document/development/honor-review-results"
namespace: "development"
slug: "honor-review-results"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "企业文化 > 荣誉审核结果"
doc_id: "Xduk7osk1G"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/honor-review-results
> Path: 应用开发 / 事件订阅 / 企业文化 > 荣誉审核结果
> Updated: 2022-01-19 19:29:22

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
