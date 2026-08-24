---
title: "服务群入群表单保存"
source_url: "https://open.dingtalk.com/document/development/event-servicegroup-contact-join-group-form"
namespace: "development"
slug: "event-servicegroup-contact-join-group-form"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群入群表单保存"
doc_id: "179vyWHv92"
updated_at: "2025-08-28 19:46:12"
---

> Source: https://open.dingtalk.com/document/development/event-servicegroup-contact-join-group-form
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群入群表单保存
> Updated: 2025-08-28 19:46:12

# 服务群入群表单保存

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群入群表单保存 |
| 英文名称 | servicegroup\_contact\_join\_group\_form |

## 功能描述

服务群入群表单事件推送的数据。

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
- `data.spiCrmModel`（object）：业务数据模型。
- `data.spiCrmModel.openTeamId`（string）：开放团队ID。
- `data.spiCrmModel.formScene`（string）：表单实例场景：  
  - DING\_CUSTOMER：客户实例  
  - DING\_CONTACT：联系人实例  
  - DING\_JOIN\_GROUP：入群表单实例
- `data.spiCrmModel.openDataInstanceId`（string）：加密的数据实例id。
- `data.spiCrmModel.operateType`（string）：操作类型：  
  - CREATE\_CUSTOM：创建实例  
  - EDIT\_CUSTOM：编辑实例  
  - DELETE\_CUSTOM：删除实例  
  - CONTACT\_RELATE\_CUSTOMER：联系人关联客户  
  - CONTACT\_JOIN\_GROUP\_FORM：入群表单填写
- `data.spiCrmModel.formData`（object）：业务相关数据，各操作数据不同，取决于表单配置的表单项。
- `data.spiCrmModel.formData.dINGCUSTOMER`（object）：此key代表为客户相关数据，此字段数据为动态数据，个数和key取决于表单配置的表单项code。
- `data.spiCrmModel.formData.dINGCUSTOMER.dingCustomerId`（string）：加密的创建者uid。
- `data.spiCrmModel.formData.dINGCUSTOMER.customerName`（string）：客户名称。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_contact_join_group_form",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiCrmModel": {
      "openTeamId": "iPxxxxxxxx",
      "formScene": "DING_JOIN_GROUP",
      "openDataInstanceId": "qsxxxxxxxxxxx",
      "operateType": "CONTACT_JOIN_GROUP_FORM",
      "formData": {
        "dINGCUSTOMER": {
          "dingCustomerId": "Oidxxxxxxxx",
          "customerName": "李四"
        }
      }
    }
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
- `spiCrmModel`（object）：业务数据模型。
- `spiCrmModel.openTeamId`（string）：开放团队ID。
- `spiCrmModel.formScene`（string）：表单实例场景：  
  - DING\_CUSTOMER：客户实例  
  - DING\_CONTACT：联系人实例  
  - DING\_JOIN\_GROUP：入群表单实例
- `spiCrmModel.openDataInstanceId`（string）：加密的数据实例id。
- `spiCrmModel.operateType`（string）：操作类型：  
  - CREATE\_CUSTOM：创建实例  
  - EDIT\_CUSTOM：编辑实例  
  - DELETE\_CUSTOM：删除实例  
  - CONTACT\_RELATE\_CUSTOMER：联系人关联客户  
  - CONTACT\_JOIN\_GROUP\_FORM：入群表单填写
- `spiCrmModel.formData`（object）：业务相关数据，各操作数据不同，取决于表单配置的表单项。
- `spiCrmModel.formData.DING_CUSTOMER`（object）：此key代表为客户相关数据，此字段数据为动态数据，个数和key取决于表单配置的表单项code。
- `spiCrmModel.formData.DING_CUSTOMER.ding_customer_id`（string）：加密的创建者uid。
- `spiCrmModel.formData.DING_CUSTOMER.customer_name`（string）：客户名称。

### **事件体示例**

```
{
  "EventType": "servicegroup_contact_join_group_form",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiCrmModel": {
    "openTeamId": "iPxxxxxxxx",
    "formScene": "DING_JOIN_GROUP",
    "openDataInstanceId": "qsxxxxxxxxxxx",
    "operateType": "CONTACT_JOIN_GROUP_FORM",
    "formData": {
      "DING_CUSTOMER": {
        "ding_customer_id": "Oidxxxxxxxx",
        "customer_name": "李四"
      }
    }
  }
}
```
