---
title: "获取角色详情"
source_url: "https://open.dingtalk.com/document/development/queries-role-details"
namespace: "development"
slug: "queries-role-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 获取角色详情"
doc_id: "5sZArHG6MW"
updated_at: "2026-05-27 13:09:28"
---

> Source: https://open.dingtalk.com/document/development/queries-role-details
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 获取角色详情
> Updated: 2026-05-27 13:09:28

# 获取角色详情

调用本接口，根据角色ID获取指定角色详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/getrole |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_member-通讯录部门成员读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| roleId | Number | 是 | 1581321999 | 角色ID，可调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/getrole" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2c9ecxxxx4210' \
-d 'roleId=1001'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/getrole");
OapiRoleGetroleRequest req = new OapiRoleGetroleRequest();
req.setRoleId(1507113578L);
OapiRoleGetroleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleGetroleRequest("https://oapi.dingtalk.com/topapi/role/getrole")

req.roleId=1001
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
$req = new OapiRoleGetroleRequest;
$req->setRoleId("1001");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/getrole");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/getrole");
OapiRoleGetroleRequest req = new OapiRoleGetroleRequest();
req.RoleId = 1001L;
OapiRoleGetroleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| role | OpenRole |  | 角色信息。 |
| name | String | 负责人 | 角色名称。 |
| groupId | Number | 1507113577 | 所属的角色组ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 4cmr6app8ujf | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "role":{
    "groupId":1507113577,
    "name":"负责人"
  },
  "request_id":"4cmr6app8ujf"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33011 | 无效的roleId | 请校验roleId是否正确 |
| 43007 | 需要操作权限 | 请确认access\_token是否有权限 |
| 400001 | 系统错误 | 请稍后再试 |
