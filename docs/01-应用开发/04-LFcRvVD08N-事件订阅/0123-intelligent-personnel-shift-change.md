---
title: "班次变更"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-shift-change"
namespace: "development"
slug: "intelligent-personnel-shift-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 班次变更"
doc_id: "JCfseyI8zQ"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-shift-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 班次变更
> Updated: 2022-01-19 19:29:22

# 班次变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 班次变更 |
| 英文名称 | attend\_shift\_change |

## 功能描述

班次变更事件数据。

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
  "eventType": "attend_shift_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "dingxxxx",
    "name": "班次A",
    "action": "attend_group_delete",
    "id": "11112222"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "attend_shift_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "corpid": "dingxxxx",
  "name": "班次A",
  "action": "attend_group_delete",
  "id": "11112222"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=153)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 153,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "corpid": "dingxxxx",
    "syncAction": "attend_shift_change",
    "name": "班次A",
    "action": "attend_group_delete",
    "id": "11112222"
  }
}
```
