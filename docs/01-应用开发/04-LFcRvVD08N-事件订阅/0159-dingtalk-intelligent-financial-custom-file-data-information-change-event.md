---
title: "钉钉智能财务自定义档案数据信息变更事件"
source_url: "https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-custom-file-data-information-change-event"
namespace: "development"
slug: "dingtalk-intelligent-financial-custom-file-data-information-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "智能财务 > 钉钉智能财务自定义档案数据信息变更事件"
doc_id: "cl6cIsnNAV"
updated_at: "2025-08-28 19:47:13"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-intelligent-financial-custom-file-data-information-change-event
> Path: 应用开发 / 事件订阅 / 智能财务 > 钉钉智能财务自定义档案数据信息变更事件
> Updated: 2025-08-28 19:47:13

# 钉钉智能财务自定义档案数据信息变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 钉钉智能财务自定义档案数据信息变更事件 |
| 英文名称 | smart\_finance\_define\_data\_info\_change |

## 功能描述

数据为智能财务的自定义档案具体数据信息变更相关数据。该数据用于告知合作伙伴，企业的自定义档案具体数据信息进行了更新，便于数据实时同步。

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
- `data.defineDataInfo`（object）：自定义档案数据信息。
- `data.defineDataInfo.defineCode`（string，必填）：自定义档案信息唯一编码。
- `data.defineDataInfo.dataCode`（string，必填）：自定义档案具体数据唯一编码。
- `data.defineDataInfo.name`（string，必填）：自定义数据名称。
- `data.defineDataInfo.parentDataCode`（string，必填）：自定义档案数据信息父级唯一编码。
- `data.defineDataInfo.remark`（string，必填）：详细备注描述。
- `data.defineDataInfo.status`（string，必填）：状态：  
  - valid  
  - delete
- `data.changeType`（string）：变更类型：  
  - add：新增  
  - update：更新  
  - delete：移除

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "smart_finance_define_data_info_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "defineDataInfo": {
      "defineCode": "DEF_123456",
      "name": "xx路1店",
      "remark": "xx路1店",
      "parentDataCode": "DA_123456",
      "dataCode": "DA_123456",
      "status": "valid"
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
- `biz_data.defineDataInfo`（object）：自定义档案数据信息。
- `biz_data.defineDataInfo.defineCode`（string，必填）：自定义档案信息唯一编码。
- `biz_data.defineDataInfo.dataCode`（string，必填）：自定义档案具体数据唯一编码。
- `biz_data.defineDataInfo.name`（string，必填）：自定义数据名称。
- `biz_data.defineDataInfo.parentDataCode`（string，必填）：自定义档案数据信息父级唯一编码。
- `biz_data.defineDataInfo.remark`（string，必填）：详细备注描述。
- `biz_data.defineDataInfo.status`（string，必填）：状态：  
  - valid  
  - delete
- `biz_data.changeType`（string）：变更类型：  
  - add：新增  
  - update：更新  
  - delete：移除

### **biz\_data数据示例(biz\_type=419)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 419,
  "biz_data": {
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "defineDataInfo": {
      "defineCode": "DEF_123456",
      "name": "xx路1店",
      "remark": "xx路1店",
      "parentDataCode": "DA_123456",
      "dataCode": "DA_123456",
      "status": "valid"
    },
    "syncAction": "smart_finance_define_data_info_change",
    "changeType": "add"
  }
}
```
