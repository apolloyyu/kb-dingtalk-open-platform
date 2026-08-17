---
title: "异步转译通讯录id任务完成通知"
source_url: "https://open.dingtalk.com/document/development/asynchronous-translation-address-book-stream"
namespace: "development"
slug: "asynchronous-translation-address-book-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 异步转译通讯录id任务完成通知"
doc_id: "SJghM45VRi"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/asynchronous-translation-address-book-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 异步转译通讯录id任务完成通知
> Updated: 2022-01-19 19:29:22

# 异步转译通讯录id任务完成通知

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 异步转译通讯录id任务完成通知 |
| 英文名称 | transfer\_contact\_id\_job\_result |

## 功能描述

eventType为transfer\_contact\_id\_job\_result，表示企业异步转译通讯录id任务完成，发送的异步转译通讯录事件数据。

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
  "eventType": "transfer_contact_id_job_result",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "jobId": "seejaRmXY8RQgo2SJSHS92xxxxxxx",
    "status": "1"
  }
}
```
