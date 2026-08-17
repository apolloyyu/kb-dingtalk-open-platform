---
title: "企业删除员工"
source_url: "https://open.dingtalk.com/document/development/enterprise-deletes-the-employee"
namespace: "development"
slug: "enterprise-deletes-the-employee"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业删除员工"
doc_id: "sWW12Ab3UY"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-deletes-the-employee
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业删除员工
> Updated: 2022-01-19 19:29:22

# 企业删除员工

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业删除员工 |
| 英文名称 | user\_leave\_org |

## 功能描述

企业内部用户变更事件，当eventType为user\_leave\_org时表示企业删除员工推送信息。

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
  "eventType": "user_leave_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionid": "zvLdpxxxxxiEiE",
    "dingId": "$:LWCP_v1:$G5YX0l5yOKZ2oxxxx"
  }
}
```
