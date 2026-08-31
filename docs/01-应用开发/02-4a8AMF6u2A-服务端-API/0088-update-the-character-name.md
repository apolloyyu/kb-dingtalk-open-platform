---
title: "更新角色名称"
source_url: "https://open.dingtalk.com/document/development/update-the-character-name"
namespace: "development"
slug: "update-the-character-name"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 更新角色名称"
doc_id: "LeDSh2tuq3"
updated_at: "2026-05-27 13:09:21"
---

> Source: https://open.dingtalk.com/document/development/update-the-character-name
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 更新角色名称
> Updated: 2026-05-27 13:09:21

# 更新角色名称

调用本接口，更新角色名称，该接口不允许修改“默认”分组内的角色，包括负责人、主管、主管理员和子管理员。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/role/update\_role |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| roleId | Number | 是 | 1560985325 | 要更新的角色ID，可以调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取。  “默认”分组内的角色不支持修改，包括：负责人、主管、主管理员、子管理员。 |
| roleName | String | 是 | 服装制造 | 修改的角色名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/role/update_role" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=bb0d689c-e415-4fa5-b5d8-e16741e12b87' \
-d 'roleId=1' \
-d 'roleName=11'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/update_role");
OapiRoleUpdateRoleRequest req = new OapiRoleUpdateRoleRequest();
req.setRoleId(1560985325L);
req.setRoleName("服装制造");
OapiRoleUpdateRoleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleUpdateRoleRequest("https://oapi.dingtalk.com/role/update_role")

req.roleId=1
req.roleName="11"
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
$req = new OapiRoleUpdateRoleRequest;
$req->setRoleId("1");
$req->setRoleName("11");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/role/update_role");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/update_role");
OapiRoleUpdateRoleRequest req = new OapiRoleUpdateRoleRequest();
req.RoleId = 1L;
req.RoleName = "11";
OapiRoleUpdateRoleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 660000 | 参数为空 | 请补全参数 |
| 33011 | 无效的roleId | 请检查roleId是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
