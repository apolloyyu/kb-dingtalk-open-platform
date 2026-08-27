---
title: "创建角色组"
source_url: "https://open.dingtalk.com/document/development/add-a-role-group"
namespace: "development"
slug: "add-a-role-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 角色管理 > 创建角色组"
doc_id: "skpdJi9CsA"
updated_at: "2026-05-27 13:09:20"
---

> Source: https://open.dingtalk.com/document/development/add-a-role-group
> Path: 应用开发 / 服务端API / 通讯录管理 > 角色管理 > 创建角色组
> Updated: 2026-05-27 13:09:20

# 创建角色组

调用本接口，创建角色组。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/role/add\_role\_group |
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
| name | String | 是 | 制造 | 角色组名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/role/add_role_group" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e9df3de5-2ccb-4aaf-a685-04ba09fe746d' \
-d 'name=%E5%90%8D%E7%A7%B0'
```

Java

```
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/role/add_role_group");
  OapiRoleAddrolegroupRequest req = new OapiRoleAddrolegroupRequest();
  req.setName("制造");
  OapiRoleAddrolegroupResponse rsp = client.execute(req, access_token);
  System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleAddrolegroupRequest("https://oapi.dingtalk.com/role/add_role_group")

req.name="名称"
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
$req = new OapiRoleAddrolegroupRequest;
$req->setName("名称");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/role/add_role_group");
```

C#

```
import dingtalk.api

req=dingtalk.api.OapiRoleAddrolegroupRequest("https://oapi.dingtalk.com/role/add_role_group")

  req.name="名称"
  try:
resp= req.getResponse(access_token)
  print(resp)
  except Exception,e:
print(e)
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码ID。 |
| groupId | Number | 1560985325 | 创建的角色组ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "groupId":1560985325,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
