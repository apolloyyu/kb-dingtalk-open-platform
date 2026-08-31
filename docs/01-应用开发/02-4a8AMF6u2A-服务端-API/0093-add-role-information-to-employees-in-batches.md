---
title: "批量增加员工角色"
source_url: "https://open.dingtalk.com/document/development/add-role-information-to-employees-in-batches"
namespace: "development"
slug: "add-role-information-to-employees-in-batches"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 批量增加员工角色"
doc_id: "6ImP1pWE1K"
updated_at: "2026-05-27 13:09:22"
---

> Source: https://open.dingtalk.com/document/development/add-role-information-to-employees-in-batches
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 批量增加员工角色
> Updated: 2026-05-27 13:09:22

# 批量增加员工角色

调用本接口，批量增加员工角色，不允许增加“默认”分组内的角色，包括负责人、主管、主管理员和子管理员。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/addrolesforemps |
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
| roleIds | String | 是 | 1507113584 | 角色roleId列表，可调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取。  多个roleId用英文逗号（,）分隔，最多可传20个。 |
| userIds | String | 是 | user1 | 员工的userId，可通过调用[根据手机号查询用户](0063-query-users-by-phone-number.md)获取。  多个userId用英文逗号（,）分隔，最多可传20个。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/addrolesforemps" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8f577dxxxx76f2a3a2' \
-d 'roleIds=1507113584' \
-d 'userIds=user1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/addrolesforemps");
OapiRoleAddrolesforempsRequest req = new OapiRoleAddrolesforempsRequest();
req.setRoleIds("1507113584,1507113589");
req.setUserIds("user1,user2");
OapiRoleAddrolesforempsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleAddrolesforempsRequest("https://oapi.dingtalk.com/topapi/role/addrolesforemps")

req.roleIds="1507113584"
req.userIds="user1"
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
$req = new OapiRoleAddrolesforempsRequest;
$req->setRoleIds("1507113584");
$req->setUserIds("user1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/addrolesforemps");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/addrolesforemps");
OapiRoleAddrolesforempsRequest req = new OapiRoleAddrolesforempsRequest();
req.RoleIds = "1507113584";
req.UserIds = "user1";
OapiRoleAddrolesforempsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | emhw6ma4xmeg | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "request_id": "emhw6ma4xmeg"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33011 | 无效的roleIds | 请检查roleIds是否正确 |
| 33012 | 无效的userIds | 请检查userId是否正确 |
| 12012 | 该企业不存在 | 请确认access\_token是否正确 |
| 1002 | 系统繁忙 | 请稍后再试 |
