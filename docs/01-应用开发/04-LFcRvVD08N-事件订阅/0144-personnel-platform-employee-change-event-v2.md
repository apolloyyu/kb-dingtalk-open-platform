---
title: "人事平台员工异动事件v2"
source_url: "https://open.dingtalk.com/document/development/personnel-platform-employee-change-event-v2"
namespace: "development"
slug: "personnel-platform-employee-change-event-v2"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 人事平台员工异动事件v2"
doc_id: "oPN9R3rzip"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/personnel-platform-employee-change-event-v2
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 人事平台员工异动事件v2
> Updated: 2022-01-19 19:29:22

# 人事平台员工异动事件v2

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事平台员工异动事件v2 |
| 英文名称 | hrm\_mdm\_user\_change |

## 功能描述

eventType为hrm\_mdm\_user\_change，表示人事平台员工异动事件v2数据。

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
  "eventType": "hrm_mdm_user_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "changeType": 4,
    "staffId": "01301xxxx140"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "hrm_mdm_user_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "changeType": 4,
  "staffId": "01301xxxx140"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=137)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 137,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "syncAction": "hrm_mdm_user_change",
    "changeType": 4,
    "staffId": "01301xxxx140"
  }
}
```
