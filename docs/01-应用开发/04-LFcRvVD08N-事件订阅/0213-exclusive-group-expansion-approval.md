---
title: "专属群扩容审批"
source_url: "https://open.dingtalk.com/document/development/exclusive-group-expansion-approval"
namespace: "development"
slug: "exclusive-group-expansion-approval"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 专属群扩容审批"
doc_id: "HtKpAXDIVC"
updated_at: "2025-08-28 19:47:32"
---

> Source: https://open.dingtalk.com/document/development/exclusive-group-expansion-approval
> Path: 应用开发 / 事件订阅 / 专属开放 > 专属群扩容审批
> Updated: 2025-08-28 19:47:32

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.eventType`（string）：事件类型
- `data.params`（object）
- `data.params.groupName`（string，必填）：群聊名称
- `data.params.groupOwner`（string，必填）：群主工号
- `data.params.remark`（string，必填）：申请描述
- `data.params.openCid`（string，必填）：群聊cid
- `data.processInstanceId`（string）：审批实例id
- `data.corpId`（string）：审批实例所在的企业corpId
- `data.createTime`（long）：创建审批实例时间。时间戳，单位毫秒。
- `data.title`（string）：审批实例标题
- `data.approveType`（string）：类型，approveType为start表示审批实例开始。
- `data.staffId`（string）：发起审批实例的员工userId
- `data.url`（string）：审批实例url，可在钉钉内跳转到审批页面。(由接入方提供)
- `data.approvers`（array）：流程审核人工号列表

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventType`（string，必填）：事件类型
- `params`（object，必填）
- `params.groupName`（string，必填）：群聊名称
- `params.groupOwner`（string，必填）：群主工号
- `params.remark`（string，必填）：申请描述
- `params.openCid`（string，必填）：群聊cid
- `processInstanceId`（string，必填）：审批实例id
- `corpId`（string，必填）：审批实例所在的企业corpId
- `createTime`（long）：创建审批实例时间。时间戳，单位毫秒。
- `title`（string，必填）：审批实例标题
- `approveType`（string，必填）：类型，approveType为start表示审批实例开始。
- `staffId`（string，必填）：发起审批实例的员工userId
- `url`（string，必填）：审批实例url，可在钉钉内跳转到审批页面。(由接入方提供)
- `approvers`（array，必填）：流程审核人工号列表

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventType`（string）：事件类型
- `biz_data.params`（object）
- `biz_data.params.groupName`（string，必填）：群聊名称
- `biz_data.params.groupOwner`（string，必填）：群主工号
- `biz_data.params.remark`（string，必填）：申请描述
- `biz_data.params.openCid`（string，必填）：群聊cid
- `biz_data.processInstanceId`（string）：审批实例id
- `biz_data.corpId`（string）：审批实例所在的企业corpId
- `biz_data.createTime`（long）：创建审批实例时间。时间戳，单位毫秒。
- `biz_data.title`（string）：审批实例标题
- `biz_data.approveType`（string）：类型，approveType为start表示审批实例开始。
- `biz_data.staffId`（string）：发起审批实例的员工userId
- `biz_data.url`（string）：审批实例url，可在钉钉内跳转到审批页面。(由接入方提供)
- `biz_data.approvers`（array）：流程审核人工号列表

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
