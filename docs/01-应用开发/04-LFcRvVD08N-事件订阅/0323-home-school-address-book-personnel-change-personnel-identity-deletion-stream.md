---
title: "家校通讯录人员变更(人员身份删除)"
source_url: "https://open.dingtalk.com/document/development/home-school-address-book-personnel-change-personnel-identity-deletion-stream"
namespace: "development"
slug: "home-school-address-book-personnel-change-personnel-identity-deletion-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录人员变更(人员身份删除)"
doc_id: "iEEeCl5kvE"
updated_at: "2025-10-16 15:06:51"
---

> Source: https://open.dingtalk.com/document/development/home-school-address-book-personnel-change-personnel-identity-deletion-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录人员变更(人员身份删除)
> Updated: 2025-10-16 15:06:51

# 家校通讯录人员变更(人员身份删除)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 家校通讯录人员变更(人员身份删除) |
| 英文名称 | edu\_user\_delete |

## 功能描述

家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。eventType为edu\_user\_delete时，表示在某个班级中人员相关身份删除事件数据。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 支持 |
| 第三方企业应用 | 不支持 |

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

- `errcode`（integer）：返回码。
- `isGraduate`（integer）：- 0：表示正常的删除。  
  - 1：表示由于毕业业务导致的人员删除。
- `classId`（long）：班级id。
- `role`（string）：此人在家校的角色类型。  
  - teacher：老师角色  
  - guardian：监护人  
  - student：学生
- `feature`（string）：扩展属性，老师身份提前下有效。
- `errmsg`（string）：返回码说明。
- `userid`（string）：用户的userid。

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "edu_user_delete",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "isGraduate": 0,
    "classId": 12345,
    "role": "guardian",
    "feature": "{}",
    "errmsg": "ok",
    "userid": "123456"
  }
}
```
