---
title: "家校通讯录人员变更(人员身份更新)"
source_url: "https://open.dingtalk.com/document/development/home-school-address-book-personnel-change-personnel-identity-update-stream"
namespace: "development"
slug: "home-school-address-book-personnel-change-personnel-identity-update-stream"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录人员变更(人员身份更新)"
doc_id: "A21pjySsZt"
updated_at: "2022-01-19 19:29:22"
---

> Source: https://open.dingtalk.com/document/development/home-school-address-book-personnel-change-personnel-identity-update-stream
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 家校通讯录事件 > 家校通讯录人员变更(人员身份更新)
> Updated: 2022-01-19 19:29:22

# 家校通讯录人员变更(人员身份更新)

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 家校通讯录人员变更(人员身份更新) |
| 英文名称 | edu\_user\_update |

## 功能描述

家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。eventType为edu\_user\_update，表示在某个班级中人员相关身份更新数据。

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
  "eventType": "edu_user_update",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "classId": 12345,
    "role": "guardian",
    "unionid": "FzyqbxFafVOEExxxwiEiE",
    "feature": "{}",
    "name": "小明爸爸",
    "errmsg": "ok",
    "userid": "123344"
  }
}
```
