---
title: "新教育人员更新"
source_url: "https://open.dingtalk.com/document/development/new-education-staff-update"
namespace: "development"
slug: "new-education-staff-update"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "行业开放 > 教育 > 新教育人员更新"
doc_id: "UySsQyAyoX"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/new-education-staff-update
> Path: 应用开发 / 事件订阅 / 行业开放 > 教育 > 新教育人员更新
> Updated: 2022-01-19 19:29:22

# 新教育人员更新

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 新教育人员更新 |
| 英文名称 | edu\_user\_update |

## 功能描述

家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。教育人员更新事件表示在某个班级中人员相关身份更新触发的事件推送的数据。

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
  "eventType": "edu_user_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "classId": 12345,
    "role": "guardian",
    "unionid": "FzyqbxFafVOEExxxwiEiE",
    "feature": "{}",
    "name": "小明爸爸",
    "errmsg": "ok",
    "userid": "123344"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "edu_user_update",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "errcode": 0,
  "classId": 12345,
  "role": "guardian",
  "unionid": "FzyqbxFafVOEExxxwiEiE",
  "feature": "{}",
  "name": "小明爸爸",
  "errmsg": "ok",
  "userid": "123344"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=51)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 51,
  "biz_data": {
    "errcode": 0,
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "classId": 12345,
    "role": "guardian",
    "unionid": "FzyqbxFafVOEExxxwiEiE",
    "feature": "{}",
    "syncAction": "edu_user_update",
    "name": "小明爸爸",
    "errmsg": "ok",
    "userid": "123344"
  }
}
```
