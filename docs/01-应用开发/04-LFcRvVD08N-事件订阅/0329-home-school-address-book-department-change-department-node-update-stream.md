---
title: "家校通讯录部门变更(部门节点更新)"
source_url: "https://open.dingtalk.com/document/development/home-school-address-book-department-change-department-node-update-stream"
namespace: "development"
slug: "home-school-address-book-department-change-department-node-update-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录部门变更(部门节点更新)"
doc_id: "g0FvcG69bz"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/home-school-address-book-department-change-department-node-update-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录部门变更(部门节点更新)
> Updated: 2022-01-19 19:29:22

# 家校通讯录部门变更(部门节点更新)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 家校通讯录部门变更(部门节点更新) |
| 英文名称 | edu\_dept\_update |

## 功能描述

家校通讯录2.0部门信息变更，家校通讯录架构中各个部门发生变更时的信息,当eventType为edu\_dept\_update时数据为部门节点更新事件。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### data部分(事件业务信息)

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_dept_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "nick": "苹果班",
    "errcode": 0,
    "chain": "[123,456]",
    "feature": "{\"grade_level\":0,\"start_year\":\"2023\"}",
    "name": "一年级2班（苹果班）",
    "deptId": 123456,
    "errmsg": "ok",
    "contactType": "classic",
    "deptType": "grade"
  }
}
```
