---
title: "获取通讯录权限范围"
source_url: "https://open.dingtalk.com/document/development/obtain-corpsecret-authorization-scope"
namespace: "development"
slug: "obtain-corpsecret-authorization-scope"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 获取通讯录权限范围"
doc_id: "qIwLk5OKUf"
updated_at: "2026-05-26 08:58:21"
---

> Source: https://open.dingtalk.com/document/development/obtain-corpsecret-authorization-scope
> Path: 应用开发 / 服务端API / 通讯录管理 > 获取通讯录权限范围
> Updated: 2026-05-26 08:58:21

# 获取通讯录权限范围

调用通讯录相关接口前，需要添加通讯录接口权限，可通过当前接口获取通讯录权限范围。

## 接口调用说明

> **[!IMPORTANT]**
>
> 本文接口是旧版规范服务端API，如何调用参见[旧版API VS 新版API](https://open.dingtalk.com/document/development/how-to-call-apis#section-8lr-id4-rbz)。

对于通讯录相关的接口，在调用前管理员必须在[钉钉开发者后台](https://open-dev.dingtalk.com/#/index)先申请对应的接口权限，并指定这些接口可以获取哪些通讯录范围。

如下图所示，当前应用的access\_token只具备管理部门A的通讯录权限。开发者可以先调用本接口查看应用的通讯录授权范围。![通信录示意图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7184498951/p149136.png)开发者在调用通讯录接口时，只能获取到在授权范围内的员工通讯录信息，获取非授权范围内的员工通讯录信息会提示`获取部门/员工不在授权范围内`。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/auth/scopes |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/auth/scopes" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2314cdxxxxbcd10713'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/auth/scopes");
OapiAuthScopesRequest req = new OapiAuthScopesRequest();
req.setHttpMethod("GET");
OapiAuthScopesResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAuthScopesRequest("https://oapi.dingtalk.com/auth/scopes")
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
$req = new OapiAuthScopesRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/auth/scopes");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/auth/scopes");
OapiAuthScopesRequest req = new OapiAuthScopesRequest();
req.SetHttpMethod("GET");
OapiAuthScopesResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| auth\_org\_scopes | AuthOrgScopes |  | 授权信息。 |
| authed\_user | String[] | ["user1","user"] | 授权可获取通信录信息的员工userid列表。 |
| authed\_dept | Number[] | [1,2,3] | 授权可获取通信录信息的部门ID列表。 |
| auth\_user\_field | String[] | ["name","email"] | 授权可获取的企业用户字段。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
        "errcode":0,
        "condition_field":[],
        "auth_user_field":[
                "jobnumber",
                "isLeader",
                "name",
                "position",
                "isAdmin",
                "avatar",
                "department",
                "userid",
                "deviceId",
                "isHide"
        ],
        "auth_org_scopes":{
                "authed_user":[],
                "authed_dept":[
                        1
                ]
        },
        "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
