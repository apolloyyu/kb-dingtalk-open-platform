---
title: "企业删除"
source_url: "https://open.dingtalk.com/document/development/enterprise-delete-stream"
namespace: "development"
slug: "enterprise-delete-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业删除"
doc_id: "Rf10AwBArM"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-delete-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业删除
> Updated: 2022-01-19 19:29:22

# 企业删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除 |
| 英文名称 | org\_remove |

## 功能描述

该数据为在授权的第三方企业应用中，当eventType为org\_remove，表示企业删除的推送信息。

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
  "eventType": "org_remove",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": 2573019
  }
}
```
