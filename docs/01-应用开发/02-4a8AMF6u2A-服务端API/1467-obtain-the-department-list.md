---
title: "获取部门列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-department-list"
namespace: "development"
slug: "obtain-the-department-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 获取部门列表"
doc_id: "KhbCeV8Bub"
updated_at: "2026-08-25 09:36:59"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-department-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 获取部门列表
> Updated: 2026-08-25 09:36:59

# 获取部门列表

调用本接口获取部门列表信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/department/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |
| lang | String | 否 | zh\_CN | 通讯录语言，默认zh\_CN。 |
| fetch\_child | Boolean | 否 | true | 是否递归部门的全部子部门。  **[!NOTE]**  第三方应用固定传递false。 |
| id | String | 否 | 1 | 父部门ID。  如果不传，默认部门为根部门，根部门ID为1。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| department | Department[] |  | 部门列表信息。 |
| id | Number | 399388496 | 部门ID。 |
| name | String | 技术支持 | 部门名称。 |
| parentid | Number | 1 | 父部门ID，1为根部门。 |
| createDeptGroup | Boolean | false | 是否创建一个关联此部门的企业群，默认为false。 |
| autoAddUser | Boolean | false | 当群已经创建后，是否有新人加入部门时会自动加入该群：   - **true**：自动加入群 - **false**：不会自动加入群 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/department/list?access_token=ACCESS_TOKEN&lang=zh_CN&fetch_child=true&id=1
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/department/list");
OapiDepartmentListRequest req = new OapiDepartmentListRequest();
req.setLang("zh_CN");
req.setFetchChild(true);
req.setId("1");
req.setHttpMethod("GET");
OapiDepartmentListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0, 
  "errmsg": "ok", 
  "department": [
    {
      "sourceIdentifier": "111", 
      "createDeptGroup": false, 
      "name": "财务部", 
      "id": 420727358, 
      "autoAddUser": false, 
      "parentid": 1
    }, 
    {
      "createDeptGroup": true, 
      "name": "市场部", 
      "id": 379661095, 
      "autoAddUser": true, 
      "parentid": 1
    }, 
    {
      "createDeptGroup": true, 
      "name": "技术支持", 
      "id": 399388496, 
      "autoAddUser": true, 
      "parentid": 1
    }, 
    {
      "createDeptGroup": false, 
      "name": "文档部门", 
      "id": 400887483, 
      "autoAddUser": false, 
      "parentid": 1
    }, 
    {
      "createDeptGroup": false, 
      "name": "文档", 
      "id": 404279847, 
      "autoAddUser": false, 
      "parentid": 1
    }, 
    {
      "createDeptGroup": false, 
      "name": "研发", 
      "id": 411048776, 
      "autoAddUser": false, 
      "parentid": 1
    }
  ]
}
```
