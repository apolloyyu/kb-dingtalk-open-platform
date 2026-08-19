---
title: "服务窗取关事件"
source_url: "https://open.dingtalk.com/document/development/service-window-close-event"
namespace: "development"
slug: "service-window-close-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 服务窗 > 服务窗取关事件"
doc_id: "oxwJ0QGLJD"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/service-window-close-event
> Path: 应用开发 / 事件订阅 / 组织关系 > 服务窗 > 服务窗取关事件
> Updated: 2022-01-19 19:29:22

# 服务窗取关事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务窗取关事件 |
| 英文名称 | official\_account\_unfollow |

## 功能描述

用户取消关注服务窗时,钉钉服务器会向回调服务推送的服务窗取消关注事件数据。

> **[!NOTE]**
>
> 服务窗事件回调，要求在服务窗自建应用中订阅，才可以正常接收回调信息。服务窗自建应用请参考[自建服务窗应用](../02-4a8AMF6u2A-服务端API/1279-self-built-service-window-application.md)。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "official_account_unfollow",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "data": [
      {
        "name": "李四",
        "type": "official_account_unfollow",
        "userId": "opzb26bxl6jcrejastvnia7300",
        "timestamp": 1654740668600
      }
    ]
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "official_account_unfollow",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "data": [
    {
      "name": "李四",
      "type": "official_account_unfollow",
      "userId": "opzb26bxl6jcrejastvnia7300",
      "timestamp": 1654740668600
    }
  ]
}
```
