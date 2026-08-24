---
title: "公告发送"
source_url: "https://open.dingtalk.com/document/development/events-blackboard-sent"
namespace: "development"
slug: "events-blackboard-sent"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 公告 > 公告发送"
doc_id: "16t95tbE8i"
updated_at: "2025-08-27 16:11:02"
---

> Source: https://open.dingtalk.com/document/development/events-blackboard-sent
> Path: 应用开发 / 事件订阅 / 协同 > 公告 > 公告发送
> Updated: 2025-08-27 16:11:02

# 公告发送

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 公告发送 |
| 英文名称 | blackboard\_sent |

## 功能描述

发送公告的事件数据。如果选择了定时发布，那么会在公告真正被发出来的时候才会触发。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.unionId`（string）：公告发送人 unionId。
- `data.receivers`（object）：公告接收人。
- `data.receivers.deptIds`（string，必填）：发送到部门，部门 id。
- `data.receivers.staffIds`（string，必填）：发送给员工，员工 userId。
- `data.receivers.openConversationIds`（string，必填）：发送到群聊，群会话 openConversationId 列表。
- `data.receivers.labelIds`（string，必填）：发送给角色，角色 id。
- `data.receivers.dgCodes`（string，必填）：发送给动态用户组，动态用户组 code。
- `data.blackboardType`（string）：公告类型：  
    
  \* blackboard：自定义内容的图文公告；  
  \* link：链接类型公告；  
  \* alidoc：钉钉文档类型公告。
- `data.dentry`（object）：公告类型是钉钉文档时会有值，导入的钉钉文档的信息。
- `data.dentry.sourceDentryUuid`（string，必填）：源文档的 id。
- `data.blackboardId`（string）：公告 id。
- `data.categoryId`（string）：公告分类 id。
- `data.categoryName`（string）：公告分类名称。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "blackboard_sent",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "AlmxxxxwiEiE",
    "receivers": {
      "openConversationIds": "[\"12345\"]",
      "labelIds": "[100]",
      "staffIds": "[\"20240418\",\"20240419\"]",
      "dgCodes": "[\"abc\"]",
      "deptIds": "[123,456]"
    },
    "blackboardType": "blackboard",
    "dentry": {
      "sourceDentryUuid": "O0002Gg0l5BW7Z9XEdgk8v000YbnKEek"
    },
    "blackboardId": "300a540d6b94005d8638f16e00603ae9",
    "categoryName": "规则制度",
    "categoryId": "e000462b5a92c1000d63b1f2dd00029e"
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
- `unionId`（string，必填）：公告发送人 unionId。
- `receivers`（object，必填）：公告接收人。
- `receivers.deptIds`（string，必填）：发送到部门，部门 id。
- `receivers.staffIds`（string，必填）：发送给员工，员工 userId。
- `receivers.openConversationIds`（string，必填）：发送到群聊，群会话 openConversationId 列表。
- `receivers.labelIds`（string，必填）：发送给角色，角色 id。
- `receivers.dgCodes`（string，必填）：发送给动态用户组，动态用户组 code。
- `blackboardType`（string，必填）：公告类型：  
    
  \* blackboard：自定义内容的图文公告；  
  \* link：链接类型公告；  
  \* alidoc：钉钉文档类型公告。
- `dentry`（object）：公告类型是钉钉文档时会有值，导入的钉钉文档的信息。
- `dentry.sourceDentryUuid`（string，必填）：源文档的 id。
- `blackboardId`（string，必填）：公告 id。
- `categoryId`（string）：公告分类 id。
- `categoryName`（string）：公告分类名称。

### **事件体示例**

```
{
  "EventType": "blackboard_sent",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "AlmxxxxwiEiE",
  "receivers": {
    "openConversationIds": "[\"12345\"]",
    "labelIds": "[100]",
    "staffIds": "[\"20240418\",\"20240419\"]",
    "dgCodes": "[\"abc\"]",
    "deptIds": "[123,456]"
  },
  "blackboardType": "blackboard",
  "dentry": {
    "sourceDentryUuid": "O0002Gg0l5BW7Z9XEdgk8v000YbnKEek"
  },
  "blackboardId": "300a540d6b94005d8638f16e00603ae9",
  "categoryName": "规则制度",
  "categoryId": "e000462b5a92c1000d63b1f2dd00029e"
}
```
