---
title: "专属群扩容审批"
source_url: "https://open.dingtalk.com/document/development/exclusive-group-expansion-approval"
namespace: "development"
slug: "exclusive-group-expansion-approval"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 专属群扩容审批"
doc_id: "HtKpAXDIVC"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/exclusive-group-expansion-approval
> Path: 应用开发 / 事件订阅 / 专属开放 > 专属群扩容审批
> Updated: 2022-01-19 19:29:22

# 专属群扩容审批

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 专属群扩容审批 |
| 英文名称 | approve\_open\_group\_expansion |
| 事件BizType | 320 |

## 功能描述

专属钉钉群规模扩容审批开放

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
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "data": {
    "approveType": "start",
    "processInstanceId": "ad253df6-e175caf-xxxxxxxxxxxx",
    "corpId": "corpidxxxxxxxxxxxxx",
    "createTime": 1495592259000,
    "approvers": [
      "er5876"
    ],
    "eventType": "approve_open_group_expansion",
    "title": "群规模扩容申请",
    "params": {
      "openCid": "cidhoEzLAXnkhNZYlHg6PqcTzSlxxxdsfs",
      "groupName": "xxx群",
      "groupOwner": "er5875",
      "remark": "群规模达到上限，申请扩容"
    },
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm",
    "staffId": "er5875"
  },
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventType": "approve_open_group_expansion",
  "eventBornTime": 1683533823336
}
```

HTTP推送

### **事件体示例**

```
{
  "approveType": "start",
  "processInstanceId": "ad253df6-e175caf-xxxxxxxxxxxx",
  "CorpId": "1663**351222567",
  "corpId": "corpidxxxxxxxxxxxxx",
  "EventType": "approve_open_group_expansion",
  "approvers": [
    "er5876"
  ],
  "eventType": "approve_open_group_expansion",
  "title": "群规模扩容申请",
  "params": {
    "openCid": "cidhoEzLAXnkhNZYlHg6PqcTzSlxxxdsfs",
    "groupName": "xxx群",
    "groupOwner": "er5875",
    "remark": "群规模达到上限，申请扩容"
  },
  "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm",
  "createTime": 1495592259000,
  "EventTime": 1663143335567,
  "BizId": "1663**35567",
  "staffId": "er5875"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=320)**

```
{
  "biz_type": 320,
  "biz_data": {
    "approveType": "start",
    "processInstanceId": "ad253df6-e175caf-xxxxxxxxxxxx",
    "corpId": "corpidxxxxxxxxxxxxx",
    "syncAction": "approve_open_group_expansion",
    "createTime": 1495592259000,
    "approvers": [
      "er5876"
    ],
    "eventType": "approve_open_group_expansion",
    "title": "群规模扩容申请",
    "params": {
      "openCid": "cidhoEzLAXnkhNZYlHg6PqcTzSlxxxdsfs",
      "groupName": "xxx群",
      "groupOwner": "er5875",
      "remark": "群规模达到上限，申请扩容"
    },
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm",
    "staffId": "er5875"
  },
  "biz_id": "1663**35567",
  "corp_id": "1663**351222567"
}
```
