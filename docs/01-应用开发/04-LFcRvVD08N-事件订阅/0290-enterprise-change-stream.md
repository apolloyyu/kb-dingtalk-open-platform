---
title: "企业变更"
source_url: "https://open.dingtalk.com/document/development/enterprise-change-stream"
namespace: "development"
slug: "enterprise-change-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业变更"
doc_id: "BZobmVqyYE"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/enterprise-change-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业变更
> Updated: 2022-01-19 19:29:22

# 企业变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业变更 |
| 英文名称 | org\_update |

## 功能描述

该数据为在授权的第三方企业应用中，当eventType为org\_update，表示企业信息发生变更的推送信息。

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
  "eventType": "org_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "corpLogoUrl": "https://static.xxx.com",
    "corpid": "dingxxx2cff796",
    "errmsg": "ok",
    "corpName": "企业1",
    "industry": "建筑安装",
    "isAuthenticated": true,
    "authLevel": 2
  }
}
```
