---
title: "删除角色"
source_url: "https://open.dingtalk.com/document/development/delete-role-information"
namespace: "development"
slug: "delete-role-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 删除角色"
doc_id: "3DYvhICUzT"
updated_at: "2026-05-27 13:09:23"
---

> Source: https://open.dingtalk.com/document/development/delete-role-information
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 删除角色
> Updated: 2026-05-27 13:09:23

# 删除角色

调用本接口，根据角色ID删除指定的角色。

## **接口调用说明**

- 在调用该接口前，确保与要删除的角色关联的员工都已删除该角色。
- 不允许删除默认角色组下的角色。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/deleterole |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| role\_id | Number | 是 | 1581321999 | 要删除的角色ID，可以调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取。  “默认”分组内的角色不支持修改，包括：负责人、主管、主管理员、子管理员 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/deleterole" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f5326exxxxbe8d071' \
-d 'role_id=11'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/deleterole");
OapiRoleDeleteroleRequest req = new OapiRoleDeleteroleRequest();
req.setRoleId(1581321999L);
OapiRoleDeleteroleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleDeleteroleRequest("https://oapi.dingtalk.com/topapi/role/deleterole")

req.role_id=11
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
$req = new OapiRoleDeleteroleRequest;
$req->setRoleId("11");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/deleterole");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/deleterole");
OapiRoleDeleteroleRequest req = new OapiRoleDeleteroleRequest();
req.RoleId = 11L;
OapiRoleDeleteroleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | zw9fhpj3m32u | 请求ID。 |

### **响应体示例**

```
{
  "errcode":"0",
  "request_id":"zw9fhpj3m32u"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33011 | 无效的role\_id | 请校验role\_id是否正确 |
| 23004 | 不允许编辑系统标签 | 请校验role\_id是否合法 |
| 1002 | 系统繁忙 | 请稍后再试 |
