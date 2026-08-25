---
title: "企业修改员工部门后员工信息事件"
source_url: "https://open.dingtalk.com/document/development/employee-information-event-after-enterprise-modifies-employee-department"
namespace: "development"
slug: "employee-information-event-after-enterprise-modifies-employee-department"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "通讯录 > 企业管理 > 企业修改员工部门后员工信息事件"
doc_id: "BHGGZfY0oe"
updated_at: "2026-07-22 16:25:38"
---

> Source: https://open.dingtalk.com/document/development/employee-information-event-after-enterprise-modifies-employee-department
> Path: 应用开发 / 事件订阅 / 通讯录 > 企业管理 > 企业修改员工部门后员工信息事件
> Updated: 2026-07-22 16:25:38

# 企业修改员工部门后员工信息事件

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 企业修改员工部门后员工信息事件 |
| 英文名称 | user\_dept\_change |

## 功能描述

数据为企业员工的最新状态。该数据为在授权的第三方企业应用中，用户所在部门变更的推送信息，字段值来自于[获取部门详情](../02-4a8AMF6u2A-服务端API/0081-query-department-details0-v2.md)接口。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 第三方企业应用 | 支持 | 不支持 | 支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.errcode`（integer）：返回码。
- `data.errmsg`（string）：返回信息。
- `data.unionEmpExt`（object）：关联组织信息。
- `data.unionEmpExt.corpId`（string）：使用的哪家企业的员工信息。
- `data.unionEmpExt.unionEmpMapList`（array）：关联企业orgId与StaffId的映射关系。
- `data.unionEmpExt.unionEmpMapList[].corpId`（string）：来源企业id。
- `data.unionEmpExt.unionEmpMapList[].staffId`（string）：来源企业内的staffId。
- `data.unionEmpExt.staffId`（string）：真实员工信息的staffId。
- `data.exclusiveAccount`（boolean）：是否专属帐号。
- `data.unionid`（string）：员工在当前开发者企业账号范围内的唯一标识。
- `data.orderInDepts`（string）：部门列表。
- `data.dingId`（string）：钉钉ID。
- `data.active`（boolean）：是否已经激活：  
  - true 已经激活。  
  - false 未激活。
- `data.avatar`（string）：头像URL。
- `data.isAdmin`（boolean）：是否为企业的管理员：  
  \* true：是  
  \* false：不是
- `data.userid`（string）：员工在当前企业内的唯一标识，也称staffId。
- `data.isHide`（boolean）：是否号码隐藏：  
  \* true：隐藏   
  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。  
  \* false：不隐藏
- `data.isLeaderInDepts`（string）：在对应的部门中是否为主管。  
    
  key是部门的ID，value是人员在这个部门中是否为主管，true表示是，false表示不是。
- `data.jobnumber`（string）：员工工号，对应显示到OA后台和客户端个人资料的工号栏目。
- `data.isBoss`（boolean）：是否为企业的老板：  
  \* true：表示是  
  \* false：表示不是
- `data.isSenior`（boolean）：是否开启高管模式:  
    
  \* true：开启  
    
   开启后，手机号码对所有员工隐藏。普通员工无法对其发DING、发起钉钉免费商务电话。高管之间不受影响。  
  \* false：不开启
- `data.name`（string）：成员名称。
- `data.position`（string）：职位名称。
- `data.department`（array）：数组类型，数组里面值为整型，成员所属部门ID列表。
- `data.realAuthed`（boolean）：是否实名认证：  
  \* true：是  
  \* false：否

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "user_dept_change",
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
    "jobnumber": "1",
    "isLeaderInDepts": "{1:false}",
    "isBoss": true,
    "isSenior": false,
    "name": "张三",
    "position": "技术支持",
    "department": [
      1
    ],
    "realAuthed": true
  }
}
```

SyncHTTP/RDS推送

为RDS推送方式时，数据插入表open\_sync\_biz\_data\_medium中。

### 字段说明

- `corp_id`（String）：企业corp\_id。
- `biz_id`（String）：biz\_id无业务意义，幂等。
- `biz_type`（Integer）：事件bizType。
- `biz_data`（object）：事件bizData介绍。
- `biz_data.syncAction`（String）：事件英文名。
- `biz_data.eventId`（String）：事件的唯一Id。
- `biz_data.errcode`（integer）：返回码。
- `biz_data.errmsg`（string）：返回信息。
- `biz_data.unionEmpExt`（object）：关联组织信息。
- `biz_data.unionEmpExt.corpId`（string）：使用的哪家企业的员工信息。
- `biz_data.unionEmpExt.unionEmpMapList`（array）：关联企业orgId与StaffId的映射关系。
- `biz_data.unionEmpExt.unionEmpMapList[].corpId`（string）：来源企业id。
- `biz_data.unionEmpExt.unionEmpMapList[].staffId`（string）：来源企业内的staffId。
- `biz_data.unionEmpExt.staffId`（string）：真实员工信息的staffId。
- `biz_data.exclusiveAccount`（boolean）：是否专属帐号。
- `biz_data.unionid`（string）：员工在当前开发者企业账号范围内的唯一标识。
- `biz_data.orderInDepts`（string）：部门列表。
- `biz_data.dingId`（string）：钉钉ID。
- `biz_data.active`（boolean）：是否已经激活：  
  - true 已经激活。  
  - false 未激活。
- `biz_data.avatar`（string）：头像URL。
- `biz_data.isAdmin`（boolean）：是否为企业的管理员：  
  \* true：是  
  \* false：不是
- `biz_data.userid`（string）：员工在当前企业内的唯一标识，也称staffId。
- `biz_data.isHide`（boolean）：是否号码隐藏：  
  \* true：隐藏   
  隐藏手机号后，手机号在个人资料页隐藏，但仍可对其发DING、发起钉钉免费商务电话。  
  \* false：不隐藏
- `biz_data.isLeaderInDepts`（string）：在对应的部门中是否为主管。  
    
  key是部门的ID，value是人员在这个部门中是否为主管，true表示是，false表示不是。
- `biz_data.jobnumber`（string）：员工工号，对应显示到OA后台和客户端个人资料的工号栏目。
- `biz_data.isBoss`（boolean）：是否为企业的老板：  
  \* true：表示是  
  \* false：表示不是
- `biz_data.isSenior`（boolean）：是否开启高管模式:  
    
  \* true：开启  
    
   开启后，手机号码对所有员工隐藏。普通员工无法对其发DING、发起钉钉免费商务电话。高管之间不受影响。  
  \* false：不开启
- `biz_data.name`（string）：成员名称。
- `biz_data.position`（string）：职位名称。
- `biz_data.department`（array）：数组类型，数组里面值为整型，成员所属部门ID列表。
- `biz_data.realAuthed`（boolean）：是否实名认证：  
  \* true：是  
  \* false：否

### **biz\_data数据示例(biz\_type=13)**

```
{
  "corp_id": "ding9f50b15bxxxx16741",
  "biz_id": "1663**35567",
  "biz_type": 13,
  "biz_data": {
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
    "eventId": "c7c7120f2c07419**ebdba0318c8",
    "unionid": "m8axYHBIiSxxxx",
    "exclusiveAccount": false,
    "syncAction": "user_dept_change",
    "orderInDepts": "{1234:12345}",
    "dingId": "$:LWCP_v1:$LT",
    "active": true,
    "errmsg": "ok",
    "avatar": "http://xxxxx",
    "isAdmin": true,
    "userid": "user123",
    "isHide": true,
    "jobnumber": "1",
    "isLeaderInDepts": "{1:false}",
    "isBoss": true,
    "isSenior": false,
    "name": "张三",
    "position": "技术支持",
    "department": [
      1
    ],
    "realAuthed": true
  }
}
```
