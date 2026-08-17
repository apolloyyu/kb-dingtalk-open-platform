---
title: "第三方企业应用删除"
source_url: "https://open.dingtalk.com/document/development/third-party-enterprise-app-deletion-stream"
namespace: "development"
slug: "third-party-enterprise-app-deletion-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 第三方企业状态 > 第三方企业应用删除"
doc_id: "2Adb3UmO2M"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/third-party-enterprise-app-deletion-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 第三方企业状态 > 第三方企业应用删除
> Updated: 2022-01-19 19:29:22

# 第三方企业应用删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 第三方企业应用删除 |
| 英文名称 | org\_micro\_app\_remove |

## 功能描述

数据为第三方企业应用的最新状态，eventType为org\_micro\_app\_remove表示第三方企业应用删除，保留企业对第三方企业应用的授权。

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
  "eventType": "org_micro_app_remove",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "agentId": 12345677
  }
}
```
