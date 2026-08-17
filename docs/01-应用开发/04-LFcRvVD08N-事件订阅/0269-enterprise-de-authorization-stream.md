---
title: "企业解除授权"
source_url: "https://open.dingtalk.com/document/development/enterprise-de-authorization-stream"
namespace: "development"
slug: "enterprise-de-authorization-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 授权事件 > 企业解除授权"
doc_id: "i9yZi4Oddt"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-de-authorization-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 授权事件 > 企业解除授权
> Updated: 2022-01-19 19:29:22

# 企业解除授权

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业解除授权 |
| 英文名称 | org\_suite\_relieve |

## 功能描述

eventType为org\_suite\_relieve表示解除第三方企业应用授权时推送数据。

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
  "eventType": "org_suite_relieve",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {}
}
```
