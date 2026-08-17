---
title: "Teambiton工时变更事件"
source_url: "https://open.dingtalk.com/document/development/teambiton-work-change-event"
namespace: "development"
slug: "teambiton-work-change-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > Teambition项目事件 > Teambiton工时变更事件"
doc_id: "i0XQrtD6vo"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/teambiton-work-change-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > Teambition项目事件 > Teambiton工时变更事件
> Updated: 2022-01-19 19:29:22

# Teambiton工时变更事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | Teambiton工时变更事件 |
| 英文名称 | project\_worktime\_updated |
| 事件BizType | 297 |

## 功能描述

当Teambiton项目中工时属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中工时属性内容的变更推送给开发者，用于监听项目中工时属性更新的信息。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### 企业内部应用

### **事件体示例**

```
{
  "CorpId": "1663**351222567",
  "eventSubType": "worktime.create",
  "EventType": "project_worktime_updated",
  "executorId": "0715153011125xxxx",
  "created": "2023-04-13T00:00:00Z",
  "approveOpenId": "63c7f91f6ff268bcab40xxxx",
  "dates": "2023-04-13T00:00:00Z",
  "userId": "0715153011125xxxx",
  "workTime": 100000,
  "EventTime": 1663143335567,
  "action": "re-submit",
  "BizId": "1663**35567",
  "updated": "2023-04-13T00:00:00Z",
  "taskId": "63c7f91f6ff268bcab40xxxx",
  "workTimeIds": [
    "63c7f91f6ff268bcab40xxxx"
  ]
}
```

### 第三方企业应用(biz\_type=297)

数据为RDS和SyncHTTP推送的事件体，当为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### **biz\_data数据示例如下:**

```
{
  "eventSubType": "worktime.create",
  "syncAction": "project_worktime_updated",
  "executorId": "0715153011125xxxx",
  "created": "2023-04-13T00:00:00Z",
  "approveOpenId": "63c7f91f6ff268bcab40xxxx",
  "action": "re-submit",
  "dates": "2023-04-13T00:00:00Z",
  "userId": "0715153011125xxxx",
  "updated": "2023-04-13T00:00:00Z",
  "workTime": 100000,
  "taskId": "63c7f91f6ff268bcab40xxxx",
  "workTimeIds": [
    "63c7f91f6ff268bcab40xxxx"
  ]
}
```
