---
title: "企业增加员工事件"
source_url: "https://open.dingtalk.com/document/development/event-subscription-enterprises-increase-employee-events"
namespace: "development"
slug: "event-subscription-enterprises-increase-employee-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业增加员工事件"
doc_id: "hGxWCyCR5Q"
updated_at: "2025-12-08 14:46:57"
---

> Source: https://open.dingtalk.com/document/development/event-subscription-enterprises-increase-employee-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > Stream推送 > 通讯录事件 > 企业增加员工事件
> Updated: 2025-12-08 14:46:57

# 企业增加员工事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业增加员工事件 |
| 英文名称 | user\_add\_org |

## 功能描述

企业内部用户变更事件，eventType为user\_add\_org，表示企业发生员工增加时的推送的数据，字段值来自于[根据userId获取用户详情](https://open.dingtalk.com/document/isvapp/address-book-events)接口 。

## 支持应用类型

| 应用类型 | 是否支持 |
| --- | --- |
| 企业内部应用 | 不支持 |
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

- `unionEmpExt`（object）：关联组织信息。  
  >用户所在企业存在关联关系的企业，返回该字段。
- `unionEmpExt.corpId`（string）：使用的哪家企业的员工信息。
- `unionEmpExt.unionEmpMapList`（array，必填）：关联企业orgId与StaffId的映射关系。
- `unionEmpExt.unionEmpMapList[].corpId`（string，必填）：来源企业id。
- `unionEmpExt.unionEmpMapList[].staffId`（string，必填）：来源企业内的staffId。
- `unionEmpExt.staffId`（string）：真实员工信息的staffId。
- `unionid`（string）：员工在当前开发者企业账号范围内的唯一标识。
- `exclusiveAccount`（boolean）：是否专属帐号。
- `orderInDepts`（string）：部门列表。
- `dingId`（string）：钉钉ID。
- `active`（boolean）：是否已经激活：  
  - true：已经激活  
  - false ：未激活
- `errcode`（integer）：返回码。
- `errmsg`（string）：返回码信息。
- `avatar`（string）：头像URL。
- `isAdmin`（boolean）：是否为企业的管理员：  
  - true：是  
  - false：不是
- `userid`（string）：员工在当前企业内的唯一标识，也称staffId。
- `isHide`（boolean）：是否号码隐藏：  
  - true：隐藏  
  >隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。  
  - false：不隐藏
- `jobnumber`（string）：员工工号，对应显示到OA后台和客户端个人资料的工号栏目。
- `isLeaderInDepts`（string）：在对应的部门中是否为主管。  
    
  key是部门的ID，value是人员在这个部门中是否为主管，true表示是，false表示不是。
- `isBoss`（boolean）：是否为企业的老板：  
  - true：表示是  
  - false：表示不是
- `isSenior`（boolean）：是否开启高管模式:  
  - true：开启  
  >开启后，手机号码对所有员工隐藏。普通员工无法对其发DING、发起钉钉免费商务电话。高管之间不受影响。  
  - false：不开启
- `name`（string）：成员名称。
- `position`（string）：职位名称。
- `department`（array）：数组类型，数组里面值为整型，成员所属部门ID列表。
- `realAuthed`（boolean）：是否实名认证：  
  - true：是  
  - false：否

### **事件体数据示例如下:**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "user_add_org",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "errcode": 0,
    "unionEmpExt": {
      "corpId": "ding351234",
      "unionEmpMapList": [
        {
          "corpId": "ding351234",
          "staffId": "12345"
        }
      ],
      "staffId": "1234"
    },
    "unionid": "m8axYHBIiSxxxx",
    "exclusiveAccount": false,
    "orderInDepts": "{1234:12345}",
    "dingId": "$:LWCP_v1:$LT",
    "active": true,
    "errmsg": "ok",
    "avatar": "http://xxxxx",
    "isAdmin": true,
    "userid": "user123",
    "isHide": true,
    "jobnumber": "12345",
    "isLeaderInDepts": "{1:false}",
    "isBoss": false,
    "isSenior": true,
    "name": "钉钉",
    "position": "钉钉技术支持",
    "department": [
      1,
      2
    ],
    "realAuthed": true
  }
}
```
