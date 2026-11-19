---
title: "A1行业版设备绑定状态变更事件"
source_url: "https://open.dingtalk.com/document/development/events-aone-industry-device-bind-changed"
namespace: "development"
slug: "events-aone-industry-device-bind-changed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能硬件 > DingTalk A1 > A1行业版设备绑定状态变更事件"
doc_id: "SY8nGNT1ee"
updated_at: "2026-08-28 16:59:03"
---

> Source: https://open.dingtalk.com/document/development/events-aone-industry-device-bind-changed
> Path: 应用开发 / 事件订阅 / 智能硬件 > DingTalk A1 > A1行业版设备绑定状态变更事件
> Updated: 2026-08-28 16:59:03

# A1行业版设备绑定状态变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | A1行业版设备绑定状态变更事件 |
| 英文名称 | aone\_industry\_device\_bind\_changed |

## 功能描述

当行业版A1设备的绑定状态发生变化时，向三方组织推送该变更事件。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
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
- `data.deviceType`（string）：行业版本标识（如 edu）
- `data.actionType`（string）：事件动作：  
  - bind 绑定  
  - unbind 解绑
- `data.unionId`（string）：关联钉钉用户UnionId，按接收事件的行业应用ISV身份域编码；设备未关联用户时可为空
- `data.snCode`（string）：设备SN
- `data.hardwareName`（string）：设备名称（用户设置的展示名称）
- `data.corpId`（string）：设备归属企业corpId
- `data.isValid`（long）：硬件有效状态：  
  - 0 作废  
  - 1 正常  
    
  设备被删除/作废时推送 unbind 且 is\_valid=0；正常解绑为 unbind 且 is\_valid=1
- `data.bizId`（string）：事件ID；同一逻辑事件在行业定向绑定事件流内重投时保持稳定，且与企业绑定事件流的事件ID相互独立
- `data.userName`（string）：关联钉钉用户名称；设备未关联用户时可为空

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "aone_industry_device_bind_changed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "deviceType": "edu",
    "actionType": "bind",
    "snCode": "2010A1*********26",
    "hardwareName": "DingTalk A1",
    "corpId": "企业corpId",
    "isValid": 1,
    "bizId": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.hardware_name`（string）：设备名称（用户设置的展示名称）
- `biz_data.action_type`（string）：事件动作：  
  - bind 绑定  
  - unbind 解绑
- `biz_data.user_name`（string）：关联钉钉用户名称；设备未关联用户时可为空
- `biz_data.is_valid`（long）：硬件有效状态：  
  - 0 作废  
  - 1 正常  
    
  设备被删除/作废时推送 unbind 且 is\_valid=0；正常解绑为 unbind 且 is\_valid=1
- `biz_data.union_id`（string）：关联钉钉用户UnionId，按接收事件的行业应用ISV身份域编码；设备未关联用户时可为空
- `biz_data.sn_code`（string）：设备SN
- `biz_data.device_type`（string）：行业版本标识（如 edu）
- `biz_data.biz_id`（string）：事件ID；同一逻辑事件在行业定向绑定事件流内重投时保持稳定，且与企业绑定事件流的事件ID相互独立
- `biz_data.corp_id`（string）：设备归属企业corpId

### **biz\_data数据示例(biz\_type=510)**

```
{
  "biz_type": 510,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "hardware_name": "DingTalk A1",
    "syncAction": "aone_industry_device_bind_changed",
    "action_type": "bind",
    "is_valid": 1,
    "sn_code": "2010A1*********26",
    "device_type": "edu",
    "biz_id": "a1_device_8ddfa6cfe90f2fcb3cd0adccf25582ee",
    "corp_id": "企业corpId"
  }
}
```
