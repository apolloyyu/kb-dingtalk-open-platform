---
title: "人事档案变动"
source_url: "https://open.dingtalk.com/document/development/personnel-file-change"
namespace: "development"
slug: "personnel-file-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能人事 > 人事档案变动"
doc_id: "svQy1D6hNE"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/personnel-file-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能人事 > 人事档案变动
> Updated: 2022-01-19 19:29:22

# 人事档案变动

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 人事档案变动 |
| 英文名称 | hrm\_user\_record\_change |

## 功能描述

智能人事相关事件，eventType为hrm\_user\_record\_change，表示人事档案变动事件数据。

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
  "eventType": "hrm_user_record_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "actionType": "userInfoChange",
    "staffId": "15996141263318674"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "hrm_user_record_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "actionType": "userInfoChange",
  "staffId": "15996141263318674"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=309)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 309,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "actionType": "userInfoChange",
    "syncAction": "hrm_user_record_change",
    "staffId": "15996141263318674"
  }
}
```
