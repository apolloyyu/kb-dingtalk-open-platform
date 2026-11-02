---
title: "考勤组变更"
source_url: "https://open.dingtalk.com/document/development/event-subscription-attendance-group-changes"
namespace: "development"
slug: "event-subscription-attendance-group-changes"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 考勤事件 > 考勤组变更"
doc_id: "VfbhCgU0ZD"
updated_at: "2025-12-08 14:58:12"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-attendance-group-changes
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 考勤事件 > 考勤组变更
> Updated: 2025-12-08 14:58:12

# 考勤组变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 考勤组变更 |
| 英文名称 | attend\_group\_change |

## 功能描述

eventType为attend\_group\_change，表示考勤组变更事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 支持 |

## **事件体描述**

### header部分

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。

### data部分(事件业务信息)

### 字段说明

- `corpid`（string）：企业corpId。
- `name`（string）：考勤组名称。
- `action`（string）：考勤组动作简要信息：  
  - attend\_group\_create：企业增加考勤组之后的简要信息  
  - attend\_group\_update：企业修改考勤组之后的简要信息  
  - attend\_group\_delete：企业删除考勤组之后的简要信息
- `id`（long）：考勤组id。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "attend_group_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "corpid": "dingxxxx",
    "name": "考勤组A",
    "action": "attend_group_delete",
    "id": 11112222
  }
}
```
