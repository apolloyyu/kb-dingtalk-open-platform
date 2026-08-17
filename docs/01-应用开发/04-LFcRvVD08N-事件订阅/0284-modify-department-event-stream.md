---
title: "修改部门事件"
source_url: "https://open.dingtalk.com/document/development/modify-department-event-stream"
namespace: "development"
slug: "modify-department-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 修改部门事件"
doc_id: "NoYUiijm9v"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/modify-department-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 修改部门事件
> Updated: 2022-01-19 19:29:22

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

### data部分(事件业务信息)

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
