---
title: "获取管理员列表"
source_url: "https://open.dingtalk.com/document/development/query-the-administrator-list"
namespace: "development"
slug: "query-the-administrator-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 获取管理员列表"
doc_id: "I7F8cy4Y1o"
updated_at: "2026-06-08 09:28:40"
---

> Source: https://open.dingtalk.com/document/development/query-the-administrator-list
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 获取管理员列表
> Updated: 2026-06-08 09:28:40

# 获取管理员列表

调用本接口查询管理员列表。

## **接口调用说明**

本接口不受通讯录权限范围限制。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/user/listadmin |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/user/listadmin" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ba1dfdcc-8a86-4b95-bcb8-af2f9f91ae12'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listadmin");
OapiUserListadminRequest req = new OapiUserListadminRequest();
OapiUserListadminResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserListadminRequest("https://oapi.dingtalk.com/topapi/user/listadmin")
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
$req = new OapiUserListadminRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/user/listadmin");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listadmin");
OapiUserListadminRequest req = new OapiUserListadminRequest();
OapiUserListadminResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4f9md9obopn2 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | ListAdminResponse[] |  | 返回结果。 |
| userid | String | 203xxxx1 | 管理员的userid。 |
| sys\_level | Number | 1 | 管理员角色：   - **1**：主管理员 - **2**：子管理员 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "sys_level": 2,
      "userid": "203xxxx1"
    },
    {
      "sys_level": 1,
      "userid": "mxxxxx0"
    }
  ],
  "request_id": "4f9md9obopn2"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 需要授权 | 请确认access\_token是否有权限进行操作 |
| -1 | 系统繁忙 | 请稍后重试 |
