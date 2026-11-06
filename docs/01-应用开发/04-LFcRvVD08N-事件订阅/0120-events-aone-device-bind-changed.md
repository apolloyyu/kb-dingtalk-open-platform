---
title: "A1设备绑定状态变更事件"
source_url: "https://open.dingtalk.com/document/development/events-aone-device-bind-changed"
namespace: "development"
slug: "events-aone-device-bind-changed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > DingTalk A1 > A1设备绑定状态变更事件"
doc_id: "K69dOW4mZm"
updated_at: "2026-08-28 16:59:02"
---

> Source: https://open.dingtalk.com/document/development/events-aone-device-bind-changed
> Path: 应用开发 / 事件订阅 / 智能硬件 > DingTalk A1 > A1设备绑定状态变更事件
> Updated: 2026-08-28 16:59:02

# A1设备绑定状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | A1设备绑定状态变更事件 |
| 英文名称 | aone\_device\_bind\_changed |

## 功能描述

当企业内A1设备的绑定状态发生变化时，推送该事件。

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
- `data.deviceType`（string）：设备版本类型；当前代码固定为 a1，并预留行业版本标识（如 edu）
- `data.actionType`（string）：事件动作：  
  - bind 绑定  
  - unbind 解绑
- `data.unionId`（string）：关联钉钉用户UnionId，按设备归属企业身份域编码；设备未关联用户时可为空
- `data.snCode`（string）：设备SN
- `data.hardwareName`（string）：设备名称（用户设置的展示名称）
- `data.corpId`（string）：设备归属企业corpId
- `data.isValid`（long）：硬件有效状态：  
  - 0 作废  
  - 1 正常  
    
  设备被删除/作废时推送 unbind 且 is\_valid=0；正常解绑为 unbind 且 is\_valid=1
- `data.bizId`（string）：事件ID；同一逻辑事件在企业绑定事件流内重投时保持稳定
- `data.userName`（string）：关联钉钉用户名称；设备未关联用户时可为空

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aone_device_bind_changed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deviceType": "a1",
    "actionType": "bind",
    "unionId": "MxxxxxxxxiEiE",
    "snCode": "2010A1*********26",
    "hardwareName": "DingTalk A1",
    "corpId": "企业corpId",
    "isValid": 1,
    "bizId": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee",
    "userName": "三多"
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
- `hardware_name`（string，必填）：设备名称（用户设置的展示名称）
- `action_type`（string，必填）：事件动作：  
  - bind 绑定  
  - unbind 解绑
- `user_name`（string）：关联钉钉用户名称；设备未关联用户时可为空
- `is_valid`（long，必填）：硬件有效状态：  
  - 0 作废  
  - 1 正常  
    
  设备被删除/作废时推送 unbind 且 is\_valid=0；正常解绑为 unbind 且 is\_valid=1
- `union_id`（string）：关联钉钉用户UnionId，按设备归属企业身份域编码；设备未关联用户时可为空
- `sn_code`（string，必填）：设备SN
- `device_type`（string，必填）：设备版本类型；当前代码固定为 a1，并预留行业版本标识（如 edu）
- `biz_id`（string，必填）：事件ID；同一逻辑事件在企业绑定事件流内重投时保持稳定
- `corp_id`（string，必填）：设备归属企业corpId

### **事件体示例**

```
{
  "EventType": "aone_device_bind_changed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "hardware_name": "DingTalk A1",
  "action_type": "bind",
  "user_name": "三多",
  "is_valid": 1,
  "union_id": "MxxxxxxxxiEiE",
  "sn_code": "2010A1*********26",
  "device_type": "a1",
  "biz_id": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee",
  "corp_id": "企业corpId"
}
```
