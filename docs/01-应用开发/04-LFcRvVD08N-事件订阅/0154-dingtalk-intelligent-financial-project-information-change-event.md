---
title: "钉钉智能财务项目信息变更事件"
source_url: "https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-project-information-change-event"
namespace: "development"
slug: "dingtalk-intelligent-financial-project-information-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 钉钉智能财务项目信息变更事件"
doc_id: "gIH9EWD6Bs"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-project-information-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 钉钉智能财务项目信息变更事件
> Updated: 2022-01-19 19:29:22

# 钉钉智能财务项目信息变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉智能财务项目信息变更事件 |
| 英文名称 | smart\_finance\_project\_change |

## 功能描述

数据为智能财务的项目变更相关数据。该数据用于告知合作伙伴，企业的项目信息进行了更新，便于数据实时同步。

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
  "eventType": "smart_finance_project_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "projectInfo": {
      "userDefineCode": "2106009",
      "code": "PROJ_XXXXXXX",
      "corpId": "dingXXXXX",
      "createTime": 1656646242898,
      "name": "项目实例",
      "description": "备注实例"
    },
    "changeType": "add"
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例(biz\_type=208)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 208,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "projectInfo": {
      "userDefineCode": "2106009",
      "code": "PROJ_XXXXXXX",
      "corpId": "dingXXXXX",
      "createTime": 1656646242898,
      "name": "项目实例",
      "description": "备注实例"
    },
    "syncAction": "smart_finance_project_change",
    "changeType": "add"
  }
}
```
