---
title: "通讯录用户更改"
source_url: "https://open.dingtalk.com/document/development/address-book-user-change"
namespace: "development"
slug: "address-book-user-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 用户管理 > 通讯录用户更改"
doc_id: "bDF8S1CMb3"
updated_at: "2025-08-28 19:46:30"
---

> Source: https://open.dingtalk.com/document/development/address-book-user-change
> Path: 应用开发 / 事件订阅 / 通讯录 > 用户管理 > 通讯录用户更改
> Updated: 2025-08-28 19:46:30

# 通讯录用户更改

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 通讯录用户更改 |
| 英文名称 | user\_modify\_org |

## 功能描述

该数据为在授权的企业内部应用中，通讯录用户更改事件数据推送说明文档。

> 说明：只有当前企业内的用户信息变更时才会触发此事件，用户的个人信息变更并不会触发，例如个人头像、个人昵称、钉钉号等。

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
- `data.timeStamp`（string）：事件时间戳。
- `data.userId`（array）：变更的userId列表。
- `data.diffInfo`（object）：事件变更差异信息。
- `data.diffInfo.prev`（object）：变更之前信息。
- `data.diffInfo.prev.name`（string，必填）：员工姓名。
- `data.diffInfo.prev.email`（string，必填）：员工邮箱。
- `data.diffInfo.prev.jobNumber`（string，必填）：员工工号。
- `data.diffInfo.prev.workPlace`（string，必填）：办公地点。
- `data.diffInfo.prev.remark`（string，必填）：备注。
- `data.diffInfo.prev.telephone`（string，必填）：分机号。
- `data.diffInfo.prev.extFields`（string，必填）：扩展属性。
- `data.diffInfo.prev.managerUserid`（string，必填）：员工的直属主管。
- `data.diffInfo.prev.hiredDate`（string，必填）：入职时间。
- `data.diffInfo.curr`（object）：当前用户信息。
- `data.diffInfo.curr.email`（string，必填）：员工邮箱。
- `data.diffInfo.curr.name`（string，必填）：员工姓名。
- `data.diffInfo.curr.hiredDate`（string，必填）：入职时间。
- `data.diffInfo.curr.managerUserid`（string，必填）：员工的直属主管。
- `data.diffInfo.curr.extFields`（string，必填）：扩展属性。
- `data.diffInfo.curr.telephone`（string，必填）：分机号。
- `data.diffInfo.curr.remark`（string，必填）：备注。
- `data.diffInfo.curr.workPlace`（string，必填）：办公地点。
- `data.diffInfo.curr.jobNumber`（string，必填）：员工工号。
- `data.diffInfo.userid`（string）：变更的userid。

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "user_modify_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "timeStamp": "1608017258073",
    "diffInfo": {
      "prev": {
        "managerUserid": "205xxx91",
        "hiredDate": "20xx-xx-xx",
        "name": "测试01",
        "telephone": "1234",
        "email": "xxx@xx.com",
        "jobNumber": "112x422",
        "workPlace": "北京"
      },
      "curr": {
        "managerUserid": "205xxx91",
        "hiredDate": "20xx-xx-xx",
        "name": "测试1",
        "email": "xxx@xx.com",
        "jobNumber": "112x422",
        "workPlace": "北京"
      },
      "userid": "user123456"
    },
    "userId": [
      "user123456"
    ]
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
- `timeStamp`（string）：事件时间戳。
- `userId`（array）：变更的userId列表。
- `diffInfo`（object）：事件变更差异信息。
- `diffInfo.prev`（object）：变更之前信息。
- `diffInfo.prev.name`（string，必填）：员工姓名。
- `diffInfo.prev.email`（string，必填）：员工邮箱。
- `diffInfo.prev.jobNumber`（string，必填）：员工工号。
- `diffInfo.prev.workPlace`（string，必填）：办公地点。
- `diffInfo.prev.remark`（string，必填）：备注。
- `diffInfo.prev.telephone`（string，必填）：分机号。
- `diffInfo.prev.extFields`（string，必填）：扩展属性。
- `diffInfo.prev.managerUserid`（string，必填）：员工的直属主管。
- `diffInfo.prev.hiredDate`（string，必填）：入职时间。
- `diffInfo.curr`（object）：当前用户信息。
- `diffInfo.curr.email`（string，必填）：员工邮箱。
- `diffInfo.curr.name`（string，必填）：员工姓名。
- `diffInfo.curr.hiredDate`（string，必填）：入职时间。
- `diffInfo.curr.managerUserid`（string，必填）：员工的直属主管。
- `diffInfo.curr.extFields`（string，必填）：扩展属性。
- `diffInfo.curr.telephone`（string，必填）：分机号。
- `diffInfo.curr.remark`（string，必填）：备注。
- `diffInfo.curr.workPlace`（string，必填）：办公地点。
- `diffInfo.curr.jobNumber`（string，必填）：员工工号。
- `diffInfo.userid`（string）：变更的userid。

### **事件体示例**

```
{
  "EventType": "user_modify_org",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "timeStamp": "1608017258073",
  "diffInfo": {
    "prev": {
      "managerUserid": "205xxx91",
      "hiredDate": "20xx-xx-xx",
      "name": "测试01",
      "telephone": "1234",
      "email": "xxx@xx.com",
      "jobNumber": "112x422",
      "workPlace": "北京"
    },
    "curr": {
      "managerUserid": "205xxx91",
      "hiredDate": "20xx-xx-xx",
      "name": "测试1",
      "email": "xxx@xx.com",
      "jobNumber": "112x422",
      "workPlace": "北京"
    },
    "userid": "user123456"
  },
  "userId": [
    "user123456"
  ]
}
```
