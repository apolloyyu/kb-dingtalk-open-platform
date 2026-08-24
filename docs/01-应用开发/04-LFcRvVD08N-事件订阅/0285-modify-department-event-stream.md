---
title: "修改部门事件"
source_url: "https://open.dingtalk.com/document/development/modify-department-event-stream"
namespace: "development"
slug: "modify-department-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 修改部门事件"
doc_id: "NoYUiijm9v"
updated_at: "2025-10-16 14:32:09"
---

> Source: https://open.dingtalk.com/document/development/modify-department-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 修改部门事件
> Updated: 2025-10-16 14:32:09

# 修改部门事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 修改部门事件 |
| 英文名称 | org\_dept\_modify |

## 功能描述

该数据为在授权的第三方企业应用中，当eventType为org\_dept\_modify，表示企业修改部门的推送信息，字段值来自于[获取部门详情](https://open.dingtalk.com/document/isvapp/query-department-details0-v2)接口。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `brief`（string）：部门简介。
- `userPermits`（string）：用户的权限。
- `outerDept`（boolean）：是否为仅自己可见部门：  
  - true：是  
  - false ：否
- `errcode`（integer，必填）：返回码。
- `errmsg`（string）：返回码描述。
- `deptManagerUseridList`（string）：部门管理员列表。
- `parentid`（long）：父部门ID。
- `groupContainSubDept`（boolean）：部门群是否包含子部门。
- `outerPermitUsers`（string）：仅自己可见部门的用户列表。
- `autoApproveApply`（string）：当部门群已经创建后，是否有新人加入部门会自动加入该群：  
  - true：自动加入群  
  - false：不会自动加入群
- `outerPermitDepts`（string）：配置的部门员工可见部门Id列表。
- `deptPerimits`（string）：配置可见userId列表。
- `createDeptGroup`（boolean）：是否同步创建一个关联此部门的企业群：  
  - true：创建  
  - false：不创建
- `name`（string）：部门名称。
- `id`（long）：部门id。
- `autoAddUser`（boolean）：当部门群已经创建后，是否有新人加入部门会自动加入该群：  
  - true：自动加入群  
  - false：不会自动加入群
- `deptHiding`（boolean）：部门权限是否开启。
- `order`（long）：在父部门中的次序值。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "org_dept_modify",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "brief": "部门介绍",
    "errcode": 0,
    "userPermits": "",
    "outerDept": false,
    "errmsg": "ok",
    "deptManagerUseridList": "123|234",
    "parentid": 1123,
    "groupContainSubDept": false,
    "outerPermitUsers": "",
    "autoApproveApply": "true",
    "outerPermitDepts": "123|234",
    "deptPerimits": "",
    "createDeptGroup": true,
    "name": "测试部门",
    "id": 123455,
    "autoAddUser": true,
    "deptHiding": false,
    "order": 12345
  }
}
```
