---
title: "通讯录事件"
source_url: "https://open.dingtalk.com/document/development/address-book-events"
namespace: "development"
slug: "address-book-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 通讯录事件"
doc_id: "sljlC6hbyg"
updated_at: "2025-10-16 15:06:31"
---

> Source: https://open.dingtalk.com/document/development/address-book-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 通讯录事件
> Updated: 2025-10-16 15:06:31

# 通讯录事件

本文介绍了通讯录RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 通讯录数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 13 | xxxxx\_0 | corpxxxx | user123 | 13 | 企业用户变更，包含用户添加、修改、删除 |
| 14 | xxxxx\_0 | corpxxxx | dept123 | 14 | 企业部门变更，包含部门添加、修改、删除 |
| 15 | xxxxx\_0 | corpxxxx | role123 | 15 | 企业角色变更，包含角色添加、修改、删除 |
| 16 | xxxxx\_0 | corpxxxx | corpxxxx | 16 | 企业变更，包含企业修改、删除 |
| 20 | xxxxx\_0 | corpxxxx | user123 | 20 | 企业外部联系人变更，包含添加、修改、删除 |
| 139 | xxxxx\_0 | corpxxxx | xxxxx | 139 | 异步转译通讯录id任务完成通知 |

## biz\_type=13

当biz\_type=13时，数据为企业员工的最新状态。

该数据为在授权的第三方企业应用中，发生员工的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 员工的userid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种Json格式，企业增加或修改员工，字段值来自于[根据userId获取用户详情](https://open.dingtalk.com/document/isvapp-server/query-user-details#topic-1960047)接口 。

- 增加企业员工：

  其中**syncAction**字段取值含义如下：

  - user\_add\_org：企业增加员工事件之后的员工信息
  - user\_modify\_org：企业修改员工事件之后的员工信息
  - user\_dept\_change：企业修改员工所在部门事件之后的员工信息
  - user\_role\_change：企业修改员工所在角色（包括管理员变更）事件之后的员工信息
  - user\_active\_org：用户加入企业后的激活信息，active字段为true时表示已激活

  ```
  {
      "errcode": 0,
      "unionid": "m8axYHBIiSxxxx",
      "syncAction": "user_modify_org",
      "openId": "kiPw6f4Awmxxxx",
      "roles": [{
          "id": 289179322,
          "name": "角色01",
          "groupName": "职务01",
          "type": 0
      }],
      "userid": "1234567",
      "isCustomizedPortal": true,
      "isLeaderInDepts": "{1234567:false}",
      "isBoss": false,
      "isSenior": false,
      "department": [1234567],
      "email": "",
      "orderInDepts": "{1234567:23422}",
      "mobile": "186xxxxxxxx",
      "errmsg": "ok",
      "active": true,
      "avatar": "http://static.dingtalk.com/media/lADOD3zI380B080B0w_467_467.jpg",
      "isAdmin": false,
      "isHide": false,
      "jobnumber": "90010100999",
      "name": "暖心",
      "stateCode": "86",
      "position": "1111"
  }
  ```
- 企业删除员工

  ```
  {
      "syncAction":"user_leave_org"
      // 删除员工userid从biz_id中获取
  }
  ```

## biz\_type=14

当biz\_type=14时，数据为企业部门的最新状态。

该数据为在授权的第三方企业应用中，发生部门的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 部门ID。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种Json格式，企业增加或修改部门，字段值来自于[获取部门详情](https://open.dingtalk.com/document/isvapp-server/query-department-details0-v2#topic-1936778)接口 。

- 企业增加部门：

  其中**syncAction**字段取值含义如：

  - org\_dept\_create：创建部门
  - org\_dept\_modify：修改部门

  ```
  {
      "errcode": 0,
      "userPerimits": "",
      "syncAction": "org_dept_create",
      "orgDeptOwner": "0541092856786053",
      "outerDept": false,
      "errmsg": "ok",
      "deptManagerUseridList": "",
      "parentid": 60398183,
      "groupContainSubDept": false,
      "outerPermitUsers": "",
      "outerPermitDepts": "",
      "deptPerimits": "",
      "createDeptGroup": true,
      "name": "部门02",
      "id": 60397224,
      "autoAddUser": true,
      "deptHiding": false,
      "order": 60397224
  }
  ```
- 企业删除部门

  ```
  {
      "syncAction":"org_dept_remove"
  }
  ```

## biz\_type=15

当biz\_type=15时，数据为企业角色的最新状态。

该数据为在授权的第三方企业应用中，发生角色的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 角色ID。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种Json格式：

- 企业增加/修改角色：企业增加角色事件之后的角色信息

  ```
  {
      "role_name": "角色01",
      "role_id": 12345,
      "group_id": 1,
      "group_name": "默认角色组",
      "syncAction": "org_role_add"
  }
  ```
- 企业删除角色：企业修改角色事件之后的角色信息

  ```
  {
      "syncAction":"org_role_remove"
  }
  ```

## biz\_type=16

当biz\_type=16时，数据为企业的最新状态。

该数据为在授权的第三方企业应用中，企业信息发生变更的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 企业的corpid。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种 Json格式：

- 企业变更

  ```
  {
      "errcode": 0,
      "corpid": "dingxxxxxxxxxxxxxx",
      "auth_level": 1,
      "syncAction": "org_update",
      "errmsg": "ok",
      "industry": "信息技术咨询",
      "is_authenticated": true,
      "corp_name": "XX企业",
      "corp_logo_url": "http://static.dingtalk.com/media/lALPBY0V4xtagzFgYA_96_96.png"
  }
  ```
- 企业删除

  ```
  {
      "syncAction": "org_remove"
  }
  ```

## biz\_type=20

当biz\_type=20时，数据为企业外部联系人的最新状态。

该数据为在授权的第三方企业应用中，发生外部联系人的增加、删除、修改的时刻推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 外部联系人的userId。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据为如下两种 Json格式：

- 企业增加/修改外部联系人：

  - 当syncAction为contact\_add\_org时表示企业增加外部联系人事件之后的联系人信息。
  - 当syncAction为contact\_modify\_org时表示企业修改外部联系人事件之后的联系人信息。

    ```
    {
        "errcode": 0,
        "shareUserIds": [],
        "syncAction": "contact_modify_org",
        "mobile": "186xxx11111",
        "errmsg": "ok",
        "remark": "",
        "title": "",
        "userId": "2012130422-811754543",
        "shareDeptIds": [62039002],
        "labelIds": [83029],
        "followerUserId": "2000121002668",
        "name": "潜在客户小张",
        "stateCode": "86"
    }
    ```
- 企业删除外部联系人

  ```
  {"syncAction":"contact_leave_org"}
  ```

## biz\_type=139

当biz\_type=139时，数据为异步转译通讯录id的相关数据。

该数据为企业发生异步转译通讯录id的任务完成的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值139，表示发生异步转译通讯录id的任务完成的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
   "syncAction":"transfer_contact_id_job_result",
   "jobId":"seejaRmZxVb4pjd4BtM255iIqXY8RQg090G0IAMMsxgzGCyho2SJSHS92xxxxxxx",
   "status":"1"
}
```

字段说明：

| 参数String | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | `transfer_contact_id_job_result`：  表示异步转译通讯录id的任务完成推送事件。 |
| jobId | String | 任务ID。 |
| status | String | 任务状态。 |
