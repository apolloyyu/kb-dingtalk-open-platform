---
title: "修改角色或者角色组"
source_url: "https://open.dingtalk.com/document/development/modify-a-role-or-role-group"
namespace: "development"
slug: "modify-a-role-or-role-group"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "组织关系 > 通讯录 > 修改角色或者角色组"
doc_id: "xpCfCEsjJp"
updated_at: "2025-08-28 19:46:36"
---

> Source: https://open.dingtalk.com/document/development/modify-a-role-or-role-group
> Path: 应用开发 / 事件订阅 / 组织关系 > 通讯录 > 修改角色或者角色组
> Updated: 2025-08-28 19:46:36

# 修改角色或者角色组

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 修改角色或者角色组 |
| 英文名称 | label\_conf\_modify |

## 功能描述

该数据为在授权的企业内部应用中，修改角色或者角色组的推送数据说明。

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
- `data.postLabelList`（array）：变更前的角色或者角色组。
- `data.preLabelList`（array）：变更后的角色或者角色组。
- `data.labelIdList`（array）：角色或者角色组id列表。
- `data.scope`（string）：管理范围。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "label_conf_modify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "postLabelList": [
      "{\"deleted\":false,\"color\":-11687445,\"hidden\":false,\"level\":1,\"scope\":1,\"name\":\"测试\",\"id\":1688607309,\"parentId\":1688611118,\"extraInfo\":{}}"
    ],
    "preLabelList": [
      "{\"hidden\":false,\"name\":\"test\",\"id\":1688607309,\"extraInfo\":{}}"
    ],
    "scope": "1",
    "labelIdList": [
      1234
    ]
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
- `postLabelList`（array，必填）：变更前的角色或者角色组。
- `preLabelList`（array，必填）：变更后的角色或者角色组。
- `labelIdList`（array，必填）：角色或者角色组id列表。
- `scope`（string，必填）：管理范围。

### **事件体示例**

```
{
  "EventType": "label_conf_modify",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "postLabelList": [
    "{\"deleted\":false,\"color\":-11687445,\"hidden\":false,\"level\":1,\"scope\":1,\"name\":\"测试\",\"id\":1688607309,\"parentId\":1688611118,\"extraInfo\":{}}"
  ],
  "preLabelList": [
    "{\"hidden\":false,\"name\":\"test\",\"id\":1688607309,\"extraInfo\":{}}"
  ],
  "scope": "1",
  "labelIdList": [
    1234
  ]
}
```
