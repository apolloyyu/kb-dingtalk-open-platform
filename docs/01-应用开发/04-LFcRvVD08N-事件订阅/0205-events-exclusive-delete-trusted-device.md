---
title: "专属可信设备删除推送事件"
source_url: "https://open.dingtalk.com/document/development/events-exclusive-delete-trusted-device"
namespace: "development"
slug: "events-exclusive-delete-trusted-device"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "专属开放 > 专属可信设备删除推送事件"
doc_id: "f0FYuC0aqR"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/events-exclusive-delete-trusted-device
> Path: 应用开发 / 事件订阅 / 专属开放 > 专属可信设备删除推送事件
> Updated: 2022-01-19 19:29:22

# 专属可信设备删除推送事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 专属可信设备删除推送事件 |
| 英文名称 | exclusive\_delete\_trusted\_device |

## 功能描述

删除专属可信设备时触发该事件。

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
  "eventType": "exclusive_delete_trusted_device",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "macAddress": "11-22-33-44-55-66",
    "serialNumber": "ABCD",
    "id": "123",
    "title": "设备标题",
    "staffId": "staffId123",
    "platform": "Win",
    "status": "2"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "exclusive_delete_trusted_device",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "macAddress": "11-22-33-44-55-66",
  "serialNumber": "ABCD",
  "id": "123",
  "title": "设备标题",
  "staffId": "staffId123",
  "platform": "Win",
  "status": "2"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=492)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 492,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "macAddress": "11-22-33-44-55-66",
    "serialNumber": "ABCD",
    "syncAction": "exclusive_delete_trusted_device",
    "id": "123",
    "title": "设备标题",
    "staffId": "staffId123",
    "platform": "Win",
    "status": "2"
  }
}
```
