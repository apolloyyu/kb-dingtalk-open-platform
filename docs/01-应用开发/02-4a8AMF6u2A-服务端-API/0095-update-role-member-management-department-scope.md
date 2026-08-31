---
title: "设定角色成员管理范围"
source_url: "https://open.dingtalk.com/document/development/update-role-member-management-department-scope"
namespace: "development"
slug: "update-role-member-management-department-scope"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 设定角色成员管理范围"
doc_id: "PymgjypaTM"
updated_at: "2026-05-27 13:09:25"
---

> Source: https://open.dingtalk.com/document/development/update-role-member-management-department-scope
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 设定角色成员管理范围
> Updated: 2026-05-27 13:09:25

# 设定角色成员管理范围

调用本接口，设定角色成员管理范围。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/scope/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | EMP123 | 员工在企业中的userId。 |
| role\_id | Number | 是 | 12345 | 角色ID，可以调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取id参数值。 |
| dept\_ids | String | 否 | 1231 | 部门ID列表，多个部门id之间使用逗号分隔。  最多支持50个部门ID，不传则设置范围为所有人。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/scope/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3100xxxx2280f5' \
-d 'dept_ids=1231' \
-d 'role_id=12345' \
-d 'userid=EMP123'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/scope/update");
OapiRoleScopeUpdateRequest req = new OapiRoleScopeUpdateRequest();
req.setUserid("EMP123");
req.setRoleId(12345L);
req.setDeptIds("1231,2423");
OapiRoleScopeUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleScopeUpdateRequest("https://oapi.dingtalk.com/topapi/role/scope/update")

req.userid="EMP123"
req.role_id=12345
req.dept_ids="1231"
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiRoleScopeUpdateRequest;
$req->setUserid("EMP123");
$req->setRoleId("12345");
$req->setDeptIds("1231,2423,53536");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/scope/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/scope/update");
OapiRoleScopeUpdateRequest req = new OapiRoleScopeUpdateRequest();
req.Userid = "EMP123";
req.RoleId = 12345L;
req.DeptIds = "1231";
OapiRoleScopeUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 4pe0h4hlsit9 | 请求ID。 |

### **响应体示例**

```
{
  "errcode":"0",
  "errmsg":"ok",
  "request_id":"4pe0h4hlsit9"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40003 | 无效的userId | 请检查userId是否正确 |
| 34018 | role\_id不能为空 | 请填上roleId |
| 60301 | 无效的role\_id | 请检查role\_id是否正确 |
| 60003 | 部门不存在 | 请检查dept\_ids是否正确 |
| 46004 | 员工不在组织当中 | 请检查参数是否正确 |
| 400002 | 无效的参数 | 请检查入参是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
