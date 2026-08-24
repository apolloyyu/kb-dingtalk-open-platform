---
title: "服务群自定义表单删除实例"
source_url: "https://open.dingtalk.com/document/development/service-group-custom-form-delete-instance"
namespace: "development"
slug: "service-group-custom-form-delete-instance"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "服务群 > 服务群自定义表单删除实例"
doc_id: "wLAQadVLmQ"
updated_at: "2025-08-28 19:46:13"
---

> Source: https://open.dingtalk.com/document/development/service-group-custom-form-delete-instance
> Path: 应用开发 / 事件订阅 / 服务群 > 服务群自定义表单删除实例
> Updated: 2025-08-28 19:46:13

# 服务群自定义表单删除实例

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 服务群自定义表单删除实例 |
| 英文名称 | servicegroup\_custom\_object\_delete |

## 功能描述

服务群自定义表单删除实例推送的数据。

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
- `data.spiCrmModel.externalBizId`（string）：外部数据id。
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
- `data.spiCrmModel.operatorNickName`（string）：操作者昵称。
- `data.spiCrmModel.operatorUnionId`（string）：加密的操作者unionId。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "servicegroup_custom_object_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "spiCrmModel": {
      "openTeamId": "iPxxxxxxx",
      "externalBizId": "xxxx",
      "formScene": "DING_CUSTOMER",
      "openDataInstanceId": "exxxxxxxxxx",
      "operateType": "DELETE_CUSTOM",
      "operatorNickName": "李四",
      "operatorUnionId": "4kIxxxxxxxxxxxxxxx"
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
- `spiCrmModel.externalBizId`（string）：外部数据id。
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
- `spiCrmModel.operatorNickName`（string）：操作者昵称。
- `spiCrmModel.operatorUnionId`（string）：加密的操作者unionId。

### **事件体示例**

```
{
  "EventType": "servicegroup_custom_object_delete",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "spiCrmModel": {
    "openTeamId": "iPxxxxxxx",
    "externalBizId": "xxxx",
    "formScene": "DING_CUSTOMER",
    "openDataInstanceId": "exxxxxxxxxx",
    "operateType": "DELETE_CUSTOM",
    "operatorNickName": "李四",
    "operatorUnionId": "4kIxxxxxxxxxxxxxxx"
  }
}
```
