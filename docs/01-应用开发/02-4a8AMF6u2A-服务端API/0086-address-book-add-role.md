---
title: "创建角色"
source_url: "https://open.dingtalk.com/document/development/address-book-add-role"
namespace: "development"
slug: "address-book-add-role"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 角色管理 > 创建角色"
doc_id: "IzZ9nGx5sJ"
updated_at: "2026-05-27 13:09:19"
---

> Source: https://open.dingtalk.com/document/development/address-book-add-role
> Path: 应用开发 / 服务端API / 通讯录管理 > 角色管理 > 创建角色
> Updated: 2026-05-27 13:09:19

# 创建角色

调用本接口，创建新角色。

![新增角色](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9985197361/p358772.png)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/role/add\_role |
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
| roleName | String | 是 | 服务 | 角色名称。 |
| groupId | Number | 是 | 1507113595 | 角色组ID。   - 如果要加入的角色组已存在，调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取。 - 如果尚未创建角色组，先调用[创建角色组](0091-add-a-role-group.md)接口创建角色组，并获取角色组ID。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/role/add_role" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2e3f55xxxx6e34' \
-d 'groupId=11' \
-d 'roleName=test'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/add_role");
OapiRoleAddRoleRequest req = new OapiRoleAddRoleRequest();
req.setRoleName("测试1");
req.setGroupId(1507113595L);
OapiRoleAddRoleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleAddRoleRequest("https://oapi.dingtalk.com/role/add_role")

req.roleName="test"
req.groupId=11
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
$req = new OapiRoleAddRoleRequest;
$req->setRoleName("test");
$req->setGroupId("11");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/role/add_role");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/add_role");
OapiRoleAddRoleRequest req = new OapiRoleAddRoleRequest();
req.RoleName = "test";
req.GroupId = 11L;
OapiRoleAddRoleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| roleId | Number | 1688611118 | 角色ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode":0,
  "roleId":1688611118,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 34018 | 角色不能为空 | 请填上roleName和groupId |
| 34020 | 无效的groupId | 请检查groupId是否正确 |
| 34021 | 角色名称已存在 | 请检查roleName是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
