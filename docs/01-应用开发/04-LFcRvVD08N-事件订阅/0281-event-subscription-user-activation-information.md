---
title: "用户激活信息"
source_url: "https://open.dingtalk.com/document/development/event-subscription-user-activation-information"
namespace: "development"
slug: "event-subscription-user-activation-information"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 用户激活信息"
doc_id: "GH1C0r1aAm"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-user-activation-information
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 用户激活信息
> Updated: 2022-01-19 19:29:22

# 用户激活信息

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 用户激活信息 |
| 英文名称 | user\_active\_org |

## 功能描述

企业内部用户变更事件，eventType为user\_active\_org时表示用户加入企业后的激活信息，active字段为true时表示已激活，字段值来自于[根据userId获取用户详情](https://open.dingtalk.com/document/isvapp/address-book-events)接口 。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "user_active_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "unionEmpExt": {
      "corpId": "ding351234",
      "unionEmpMapList": [
        {
          "corpId": "ding351234",
          "staffId": "12345"
        }
      ],
      "staffId": "1234"
    },
    "unionid": "m8axYHBIiSxxxx",
    "exclusiveAccount": false,
    "orderInDepts": "{1234:12345}",
    "dingId": "$:LWCP_v1:$LT",
    "active": true,
    "errmsg": "ok",
    "avatar": "http://xxxxx",
    "isAdmin": true,
    "userid": "user123",
    "isHide": true,
    "jobnumber": "12345",
    "isLeaderInDepts": "{1:false}",
    "isBoss": false,
    "isSenior": true,
    "name": "钉钉",
    "position": "钉钉技术支持",
    "department": [
      1,
      2
    ],
    "realAuthed": true
  }
}
```
