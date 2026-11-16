---
title: "荣誉授予"
source_url: "https://open.dingtalk.com/document/development/honor-confer"
namespace: "development"
slug: "honor-confer"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "企业文化 > 荣誉授予"
doc_id: "Jfbmni81Lz"
updated_at: "2025-08-28 19:47:18"
---

> Source: https://open.dingtalk.com/document/development/honor-confer
> Path: 应用开发 / 事件订阅 / 企业文化 > 荣誉授予
> Updated: 2025-08-28 19:47:18

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

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.honorId`（string）：荣誉id。
- `data.grantTaskId`（string）：授予荣誉的任务id。
- `data.grantReason`（string）：授予荣誉原因。
- `data.senderUserid`（string）：荣誉发放人的userId。
- `data.honorDesc`（string）：荣誉描述。
- `data.honorName`（string）：荣誉名称。
- `data.optTime`（long）：操作时间。
- `data.autoWear`（string）：自动佩戴到头像：  
  - true：自动佩戴  
  - false：不自动佩戴
- `data.receiverUserid`（string）：荣誉接收人的userId。

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

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `honorId`（string）：荣誉id。
- `grantTaskId`（string）：授予荣誉的任务id。
- `grantReason`（string）：授予荣誉原因。
- `senderUserid`（string）：荣誉发放人的userId。
- `honorDesc`（string）：荣誉描述。
- `honorName`（string）：荣誉名称。
- `optTime`（long）：操作时间。
- `autoWear`（string）：自动佩戴到头像：  
  - true：自动佩戴  
  - false：不自动佩戴
- `receiverUserid`（string）：荣誉接收人的userId。

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

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.honorId`（string）：荣誉id。
- `biz_data.grantTaskId`（string）：授予荣誉的任务id。
- `biz_data.grantReason`（string）：授予荣誉原因。
- `biz_data.senderUserid`（string）：荣誉发放人的userId。
- `biz_data.honorDesc`（string）：荣誉描述。
- `biz_data.honorName`（string）：荣誉名称。
- `biz_data.optTime`（long）：操作时间。
- `biz_data.autoWear`（string）：自动佩戴到头像：  
  - true：自动佩戴  
  - false：不自动佩戴
- `biz_data.receiverUserid`（string）：荣誉接收人的userId。

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
