---
title: "直播信息修改"
source_url: "https://open.dingtalk.com/document/development/live-modify-information-event-stream"
namespace: "development"
slug: "live-modify-information-event-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 直播事件 > 直播信息修改"
doc_id: "BU15pc7eCl"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/live-modify-information-event-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 直播事件 > 直播信息修改
> Updated: 2022-01-19 19:29:22

# 直播信息修改

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 直播信息修改 |
| 英文名称 | live\_update\_event |

## 功能描述

eventType为live\_update\_event时，表示直播修改信息事件数据。

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
  "eventType": "live_update_event",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "coverUrl": "http://xxx.png",
    "preEndTime": 1660268147000,
    "title": "测试直播",
    "liveId": "1fc2eaca-****-****-****-b23e1bda4225",
    "preStartTime": 1660266147700,
    "introduction": "测试直播简介"
  }
}
```
