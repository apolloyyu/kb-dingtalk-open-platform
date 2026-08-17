---
title: "招聘平台职位投递变更事件"
source_url: "https://open.dingtalk.com/document/development/recruitment-platform-position-delivery-change-event"
namespace: "development"
slug: "recruitment-platform-position-delivery-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 招聘平台职位投递变更事件"
doc_id: "FcUHuJtzX2"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/recruitment-platform-position-delivery-change-event
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 招聘平台职位投递变更事件
> Updated: 2022-01-19 19:29:22

# 招聘平台职位投递变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 招聘平台职位投递变更事件 |
| 英文名称 | ats\_job\_deliver\_change |

## 功能描述

数据为招聘平台职位投递变更事件。该数据为招聘平台职位投递相关的数据变更时推送。

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
  "eventType": "ats_job_deliver_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {}
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "ats_job_deliver_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=236)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 236,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "ats_job_deliver_change"
  }
}
```
