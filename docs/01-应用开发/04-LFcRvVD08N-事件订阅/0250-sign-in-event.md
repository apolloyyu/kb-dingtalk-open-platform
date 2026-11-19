---
title: "签到事件"
source_url: "https://open.dingtalk.com/document/development/sign-in-event"
namespace: "development"
slug: "sign-in-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 签到事件"
doc_id: "CFdwiBO4lo"
updated_at: "2025-10-16 14:31:55"
---

> Source: https://open.dingtalk.com/document/development/sign-in-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 企业内部应用回调事件 > 签到事件
> Updated: 2025-10-16 14:31:55

# 签到事件

本文介绍了签到事件的相关说明。

用户签到事件发生，并且注册回调事件时填写的事件类型“call\_back\_tag”包含签到事件，比如call\_back\_tag字段为“check\_in”，用户签到后，钉钉服务器会向url推送事件。

## 事件类型

| **事件类型** | **说明** |
| --- | --- |
| check\_in | 用户签到。 |

**POST数据解密后示例：**

```
{
    "EventType": "check_in",
    "TimeStamp": 1495542282000,
    "CorpId": "dinge8a56572f80b02a8ffe93478xxxx",
    "StaffId": "08058xxxxxx"
  }
```

**参数说明：**

| **参数** | **说明** |
| --- | --- |
| EventType | 事件类型。 |
| TimeStamp | 签到时间。 |
| CorpId | 签到企业id。 |
| StaffId | 签到用户id。 |
