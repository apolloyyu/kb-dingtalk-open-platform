---
title: "招聘业务平台配置变更"
source_url: "https://open.dingtalk.com/document/development/event-ats-config-change"
namespace: "development"
slug: "event-ats-config-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 招聘业务平台配置变更"
doc_id: "bNMtcrNpEM"
updated_at: "2025-10-17 16:25:07"
---

> Source: https://open.dingtalk.com/document/development/event-ats-config-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 招聘业务平台配置变更
> Updated: 2025-10-17 16:25:07

# 招聘业务平台配置变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 招聘业务平台配置变更 |
| 英文名称 | ats\_config\_change |

## 功能描述

招聘业务平台配置变更事件的相关推送的数据说明。

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
- `data.configKey`（string）：配置项。
- `data.corpId`（string）：企业标识。
- `data.configValue`（string）：配置内容。
- `data.gmtModifiedTime`（string）：配置变更时间。
- `data.eventId`（string）：事件唯一eventId。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "ats_config_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "eventId": "dsaafkkdxd",
    "configKey": "rpa_resume_collect",
    "corpId": "ding2c01587xxxxxxxx",
    "configValue": "enabled",
    "gmtModifiedTime": "1688442884234"
  }
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
- `biz_data.configKey`（string）：配置项。
- `biz_data.corpId`（string）：企业标识。
- `biz_data.configValue`（string）：配置内容。
- `biz_data.gmtModifiedTime`（string）：配置变更时间。
- `biz_data.eventId`（string）：事件唯一eventId。

### **biz\_data数据示例(biz\_type=136)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 136,
  "biz_data": {
    "eventId": "dsaafkkdxd",
    "configKey": "rpa_resume_collect",
    "corpId": "ding2c01587xxxxxxxx",
    "syncAction": "ats_config_change",
    "configValue": "enabled",
    "gmtModifiedTime": "1688442884234"
  }
}
```
