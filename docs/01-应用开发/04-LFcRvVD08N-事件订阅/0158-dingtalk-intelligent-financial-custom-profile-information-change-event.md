---
title: "钉钉智能财务自定义档案信息变更事件"
source_url: "https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-custom-profile-information-change-event"
namespace: "development"
slug: "dingtalk-intelligent-financial-custom-profile-information-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 钉钉智能财务自定义档案信息变更事件"
doc_id: "drJSezCPIQ"
updated_at: "2025-08-28 19:47:12"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-custom-profile-information-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 钉钉智能财务自定义档案信息变更事件
> Updated: 2025-08-28 19:47:12

# 钉钉智能财务自定义档案信息变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉智能财务自定义档案信息变更事件 |
| 英文名称 | smart\_finance\_define\_info\_change |

## 功能描述

数据为智能财务的自定义档案类别信息变更相关数据。该数据用于告知合作伙伴，企业的自定义档案类别信息进行了更新，便于数据实时同步。

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
- `data.defineInfo`（object）：自定义档案信息。
- `data.defineInfo.defineCode`（string，必填）：自定义档案唯一编码。
- `data.defineInfo.name`（string，必填）：自定义档案名称。
- `data.defineInfo.remark`（string）：自定义档案备注。
- `data.changeType`（string）：变更类型：  
  - add：新增  
  - update：更新  
  - delete：移除

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "smart_finance_define_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "defineInfo": {
      "defineCode": "DEF_123456",
      "name": "门店",
      "remark": "企业门店信息"
    },
    "changeType": "add"
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
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.defineInfo`（object）：自定义档案信息。
- `biz_data.defineInfo.defineCode`（string，必填）：自定义档案唯一编码。
- `biz_data.defineInfo.name`（string，必填）：自定义档案名称。
- `biz_data.defineInfo.remark`（string）：自定义档案备注。
- `biz_data.changeType`（string）：变更类型：  
  - add：新增  
  - update：更新  
  - delete：移除

### **biz\_data数据示例(biz\_type=418)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 418,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "defineInfo": {
      "defineCode": "DEF_123456",
      "name": "门店",
      "remark": "企业门店信息"
    },
    "syncAction": "smart_finance_define_info_change",
    "changeType": "add"
  }
}
```
