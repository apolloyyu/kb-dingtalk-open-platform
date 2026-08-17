---
title: "请假、加班、出差、外出状态变更事件"
source_url: "https://open.dingtalk.com/document/development/leave-overtime-business-trip-out-of-office-status-change-events"
namespace: "development"
slug: "leave-overtime-business-trip-out-of-office-status-change-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 考勤 > 请假、加班、出差、外出状态变更事件"
doc_id: "LQyk61FQ8g"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/leave-overtime-business-trip-out-of-office-status-change-events
> Path: 应用开发 / 事件订阅 / 智能人事 > 考勤 > 请假、加班、出差、外出状态变更事件
> Updated: 2022-01-19 19:29:22

# 请假、加班、出差、外出状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 请假、加班、出差、外出状态变更事件 |
| 英文名称 | attendance\_approve\_status\_change |

## 功能描述

当钉钉审批单状态变更时，钉钉通过事件订阅的方式将审批单变更内容推送给开发者。
状态变更包括：发起、审批完成、撤销、删除

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
  "eventType": "attendance_approve_status_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "approveType": "LEAVE",
    "processInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "mainProcessInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "corpId": "dingxxxx",
    "processCode": "xxxx",
    "status": "start"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "attendance_approve_status_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "approveType": "LEAVE",
  "processInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
  "mainProcessInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
  "corpId": "dingxxxx",
  "processCode": "xxxx",
  "status": "start"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=344)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 344,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "approveType": "LEAVE",
    "processInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "mainProcessInstanceId": "xxxx-fdr-3423-casdfasg-xxx",
    "corpId": "dingxxxx",
    "syncAction": "attendance_approve_status_change",
    "processCode": "xxxx",
    "status": "start"
  }
}
```
