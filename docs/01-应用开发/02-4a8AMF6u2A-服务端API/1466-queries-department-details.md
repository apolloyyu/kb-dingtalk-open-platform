---
title: "获取部门详情"
source_url: "https://open.dingtalk.com/document/development/queries-department-details"
namespace: "development"
slug: "queries-department-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 获取部门详情"
doc_id: "2X9se7Ed9v"
updated_at: "2026-08-25 09:36:58"
---

> Source: https://open.dingtalk.com/document/development/queries-department-details
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 获取部门详情
> Updated: 2026-08-25 09:36:58

# 获取部门详情

调用本接口获取部门详细信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取部门详情](0081-query-department-details0-v2.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/department/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |
| id | String | 是 | 1 | 部门ID，可调用[获取部门列表](1467-obtain-the-department-list.md)接口获取。 |
| lang | String | 否 | zh\_CN | 通讯录语言，默认zh\_CN。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| id | Number | 1 | 部门ID，1为根部门。 |
| name | String | 销售一部 | 部门名称。 |
| order | Number | 0 | 在父部门中的次序值，order值小的排序靠前。 |
| parentid | Number | 1 | 父部门ID，1为根部门。  **[!NOTE]**  第三方企业应用不返回该参数。 |
| sourceIdentifier | String | 2353453 | 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。 |
| createDeptGroup | Boolean | false | 是否创建一个关联此部门的企业群，默认为**false**。 |
| autoAddUser | Boolean | false | 当群已经创建后，是否有新人加入部门时会自动加入该群：   - **true**：自动加入群 - **false**：不会自动加入群 |
| autoApproveApply | Boolean | false | 是否默认同意加入该部门的申请：   - **true：**表示加入该部门的申请将默认同意 - **false：**表示加入该部门的申请需要有权限的管理员同意 |
| groupContainSubDept | Boolean | false | 部门群是否包含子部门：   - **true**：包含 - **false**：不包含 |
| orgDeptOwner | String | manager4220 | 企业群群主的userid。 |
| deptGroupChatId | String | chat7795efa07307exxxx | 创建部门群自动生成的id。 |
| deptManagerUseridList | String | manager4220|2222 | 部门的主管列表，取值为由主管的userid组成的字符串，不同的userid使用"|"符号进行分隔。 |
| outerDept | Boolean | true | 是否限制本部门成员查看通讯录：   - **true**：开启限制，开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制 |
| outerPermitUsers | String | userid3|userid4 | 当**outerDept**为**true**时（即开启本部门成员只能看到限定范围内的通讯录），配置的部门员工可见员工列表。 |
| outerPermitDepts | String | 1 | 当**outerDept**为**true**时（即开启本部门成员只能看到限定范围内的通讯录），配置的部门员工可见部门列表。 |
| deptHiding | Boolean | true | 是否隐藏部门：   - **true**：隐藏，隐藏本部门开启后，本部门将不会显示在公司通讯录中 - **false**：显示 |
| deptPermits | String | 1 | 当**deptHiding**为**true**时（即开启隐藏本部门），配置的允许在通讯录中查看本部门的部门列表。 |
| userPermits | String | 2 | 当**deptHiding**为**true**时（即开启隐藏本部门），配置的允许在通讯录中查看本部门的员工列表。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/department/get?access_token=ACCESS_TOKEN&id=123&lang=zh_CN
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/department/get");
OapiDepartmentGetRequest req = new OapiDepartmentGetRequest();
req.setId("123");
req.setLang("zh_CN");
req.setHttpMethod("GET");
OapiDepartmentGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

- 企业内部应用

  ```
  {
      "errcode": 0,
      "sourceIdentifier": "2353453",
      "userPermits": "user123",
      "orgDeptOwner": "manager4220",
      "outerDept": true,
      "errmsg": "ok",
      "deptManagerUseridList": "manager4220",
      "parentid": 1,
      "groupContainSubDept": false,
      "outerPermitUsers": "",
      "outerPermitDepts": "420606536",
      "createDeptGroup": true,
      "name": "销售一部",
      "deptGroupChatId": "chat3d322af37b1d20447cf382add2062dec",
      "id": 420606536,
      "autoAddUser": true,
      "deptHiding": true,
      "deptPermits": "420682732",
      "order": 2353453
  }
  ```
- 第三方企业应用

  ```
  {
      "errcode": 0,
      "sourceIdentifier": "2353453",
      "userPermits": "user123",
      "orgDeptOwner": "29375012-1450266659",
      "outerDept": true,
      "errmsg": "ok",
      "deptManagerUseridList": "",
      "groupContainSubDept": false,
      "outerPermitUsers": "",
      "outerPermitDepts": "420606536",
      "deptPerimits": "",
      "createDeptGroup": true,
      "name": "销售一部",
      "deptGroupChatId": "chat3d322af37b1d20447cf382add2062dec",
      "id": 420606536,
      "autoAddUser": true,
      "deptHiding": true,
      "deptPermits": "",
      "order": 2353453
  }
  ```
