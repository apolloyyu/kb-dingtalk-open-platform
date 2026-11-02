---
title: "智能工牌自定义AI分析项完成事件"
source_url: "https://open.dingtalk.com/document/development/events-dvi-custom-ai-analysis-completed"
namespace: "development"
slug: "events-dvi-custom-ai-analysis-completed"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "视听智能服务 > 智能工牌自定义AI分析项完成事件"
doc_id: "oFPNTMRdJ7"
updated_at: "2026-07-28 17:49:26"
---

> Source: https://open.dingtalk.com/document/development/events-dvi-custom-ai-analysis-completed
> Path: 应用开发 / 事件订阅 / 视听智能服务 > 智能工牌自定义AI分析项完成事件
> Updated: 2026-07-28 17:49:26

# 智能工牌自定义AI分析项完成事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 智能工牌自定义AI分析项完成事件 |
| 英文名称 | dvi\_custom\_ai\_analysis\_completed |

## 功能描述

智能工牌应用中客户自定义的AI分析项分析完成的通知事件

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.entityType`（string）：分析的实体类型，例如服务记录、客户
- `data.teamCode`（string）：团队code
- `data.outBizData`（string）：外部数据信息，用于和外部系统打通时的关联数据字段
- `data.analysisResult`（string）：AI分析的结果
- `data.entityId`（string）：分析的实体ID，例如服务记录id或客户id
- `data.userId`（string）：分析实体所归属的员工userId

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "dvi_custom_ai_analysis_completed",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "entityType": "SERVICE_RECORD",
    "teamCode": "8fee9555-7341-4586-b72b-3714e7301da4",
    "outBizData": "customerId:xxxx-yyyy",
    "analysisResult": "AI分析的结果，可能是mardown文本也能是json文本，取决于分析规则中的配置",
    "entityId": "8fee9555-7341-4586-b72b-3714e7301da4",
    "userId": "123456789"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `entityType`（string，必填）：分析的实体类型，例如服务记录、客户
- `teamCode`（string，必填）：团队code
- `outBizData`（string，必填）：外部数据信息，用于和外部系统打通时的关联数据字段
- `analysisResult`（string，必填）：AI分析的结果
- `entityId`（string，必填）：分析的实体ID，例如服务记录id或客户id
- `userId`（string，必填）：分析实体所归属的员工userId

### **事件体示例**

```
{
  "EventType": "dvi_custom_ai_analysis_completed",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "entityType": "SERVICE_RECORD",
  "teamCode": "8fee9555-7341-4586-b72b-3714e7301da4",
  "outBizData": "customerId:xxxx-yyyy",
  "analysisResult": "AI分析的结果，可能是mardown文本也能是json文本，取决于分析规则中的配置",
  "entityId": "8fee9555-7341-4586-b72b-3714e7301da4",
  "userId": "123456789"
}
```
