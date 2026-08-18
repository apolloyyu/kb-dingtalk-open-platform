---
title: "荣誉授予"
source_url: "https://open.dingtalk.com/document/development/honor-confer"
namespace: "development"
slug: "honor-confer"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "企业文化 > 荣誉授予"
doc_id: "Jfbmni81Lz"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/honor-confer
> Path: 应用开发 / 事件订阅 / 企业文化 > 荣誉授予
> Updated: 2022-01-19 19:29:22

# 荣誉授予

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 荣誉授予 |
| 英文名称 | honor\_grant |

## 功能描述

授予企业成员荣誉勋章时，推送的荣誉授予事件内容。

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
  "eventType": "honor_grant",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "honorId": "10000xxx",
    "grantTaskId": "cf65cc8e-fd6e-xxxx-8e08-a27799aca74c",
    "grantReason": "工作优秀",
    "senderUserid": "manager7675",
    "honorDesc": "在工作上有突出表现的人员",
    "honorName": "优秀个人",
    "optTime": 1648710973596,
    "autoWear": "false",
    "receiverUserid": "3238503xxxxxx0810685"
  }
}
```

HTTP推送

### **事件体示例**

```
{
  "EventType": "honor_grant",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "honorId": "10000xxx",
  "grantTaskId": "cf65cc8e-fd6e-xxxx-8e08-a27799aca74c",
  "grantReason": "工作优秀",
  "senderUserid": "manager7675",
  "honorDesc": "在工作上有突出表现的人员",
  "honorName": "优秀个人",
  "optTime": 1648710973596,
  "autoWear": "false",
  "receiverUserid": "3238503xxxxxx0810685"
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=172)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 172,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "honorId": "10000xxx",
    "grantTaskId": "cf65cc8e-fd6e-xxxx-8e08-a27799aca74c",
    "grantReason": "工作优秀",
    "syncAction": "honor_grant",
    "senderUserid": "manager7675",
    "honorDesc": "在工作上有突出表现的人员",
    "honorName": "优秀个人",
    "optTime": 1648710973596,
    "autoWear": "false",
    "receiverUserid": "3238503xxxxxx0810685"
  }
}
```
