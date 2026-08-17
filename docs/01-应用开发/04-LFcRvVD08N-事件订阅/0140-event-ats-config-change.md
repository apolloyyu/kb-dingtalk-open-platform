---
title: "招聘业务平台配置变更"
source_url: "https://open.dingtalk.com/document/development/event-ats-config-change"
namespace: "development"
slug: "event-ats-config-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能人事 > 智能招聘 > 招聘业务平台配置变更"
doc_id: "bNMtcrNpEM"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/event-ats-config-change
> Path: 应用开发 / 事件订阅 / 智能人事 > 智能招聘 > 招聘业务平台配置变更
> Updated: 2022-01-19 19:29:22

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
