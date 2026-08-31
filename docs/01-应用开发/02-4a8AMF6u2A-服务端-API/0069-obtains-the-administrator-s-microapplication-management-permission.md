---
title: "获取管理员的应用管理权限"
source_url: "https://open.dingtalk.com/document/development/obtains-the-administrator-s-microapplication-management-permission"
namespace: "development"
slug: "obtains-the-administrator-s-microapplication-management-permission"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 获取管理员的应用管理权限"
doc_id: "vpxATy6NQB"
updated_at: "2026-06-08 09:28:42"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-administrator-s-microapplication-management-permission
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 获取管理员的应用管理权限
> Updated: 2026-06-08 09:28:42

# 获取管理员的应用管理权限

调用本接口获取管理员的应用管理权限。

## **接口调用说明**

在调用该接口前，请确保：

- 应用必须是产品方案商所开发。可在[**钉钉开发者后台**](https://open-dev.dingtalk.com/#/appMgr/provider/eapp/53642/1) **> 第三方企业应用**的应用详情页获取AppId。
- 在调用该接口前，可以调用[获取管理员列表](0068-query-the-administrator-list.md)接口获取当前企业下的管理员ID。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/user/can\_access\_microapp |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| appId | Number | 是 | 2000121xxxx | 应用ID。可在[**钉钉开发者后台**](https://open-dev.dingtalk.com/#/appMgr/provider/eapp/53642/1) **> 第三方企业应用**的应用详情页获取AppID。 |
| userId | String | 是 | 2000121xxxx | 要查询的管理员员工ID，可调用[获取管理员列表](0068-query-the-administrator-list.md)接口获取userid参数值。 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/user/can_access_microapp" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c54ee841-199a-459e-8146-3d08c1830a10' \
-d 'appId=1' \
-d 'userId=1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/can_access_microapp");
OapiUserCanAccessMicroappRequest req = new OapiUserCanAccessMicroappRequest();
req.setAppId(1L);
req.setUserId("1");
req.setHttpMethod("GET");
OapiUserCanAccessMicroappResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserCanAccessMicroappRequest("https://oapi.dingtalk.com/user/can_access_microapp")

req.appId=1
req.userId="1"
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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_GET , DingTalkConstant::$FORMAT_JSON);
$req = new OapiUserCanAccessMicroappRequest;
$req->setAppId("1");
$req->setUserId("1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/user/can_access_microapp");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/user/can_access_microapp");
OapiUserCanAccessMicroappRequest req = new OapiUserCanAccessMicroappRequest();
req.AppId = 1L;
req.UserId = "1";
req.SetHttpMethod("GET");
OapiUserCanAccessMicroappResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4f9md9obopn2 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 系统错误 | 返回码描述。 |
| canAccess | Boolean | true | 是否有管理权限：   - **true**：有管理权限 - **false**：没有管理权限 |

### **响应体示例**

```
{
  "errcode":0,
  "canAccess":"true",
  "request_id":"4f9md9obopn2"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
