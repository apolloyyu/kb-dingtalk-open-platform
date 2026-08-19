---
title: "获取管理员通讯录权限范围"
source_url: "https://open.dingtalk.com/document/development/query-permissions-of-the-administrator-address-book"
namespace: "development"
slug: "query-permissions-of-the-administrator-address-book"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 获取管理员通讯录权限范围"
doc_id: "Cc3Z5oksvb"
updated_at: "2026-06-08 09:28:41"
---

> Source: https://open.dingtalk.com/document/development/query-permissions-of-the-administrator-address-book
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 获取管理员通讯录权限范围
> Updated: 2026-06-08 09:28:41

# 获取管理员通讯录权限范围

调用本接口获取管理员通讯录权限范围。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/user/get\_admin\_scope |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manger123 | 管理员的userid，可调用[获取管理员列表](0068-query-the-administrator-list.md)接口获取当前企业下的管理员ID。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/user/get_admin_scope" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f928c8b2-5f41-4c92-908a-01fee1f20450' \
-d 'userid=manager7078'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/get_admin_scope");
OapiUserGetAdminScopeRequest req = new OapiUserGetAdminScopeRequest();
req.setUserid("manger123");
OapiUserGetAdminScopeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserGetAdminScopeRequest("https://oapi.dingtalk.com/topapi/user/get_admin_scope")

req.userid="manager7078"
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
$req = new OapiUserGetAdminScopeRequest;
$req->setUserid("manager7078");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/user/get_admin_scope");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/get_admin_scope");
OapiUserGetAdminScopeRequest req = new OapiUserGetAdminScopeRequest();
req.Userid = "manager7078";
OapiUserGetAdminScopeResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | zpucraudovy0 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| dept\_ids | Number[] | [1] | 可管理的部门ID列表。 |

### **响应体示例**

```
{
  "dept_ids": [
    1
  ],
  "errcode": 0,
  "errmsg": "ok",
  "request_id": "zpucraudovy0"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 60121 | 找不到员工 | 请确认userId是否正确 |
| 40036 | 参数为空 | 请确认必填参数填写完整 |
| 400001 | 系统错误 | 请稍后再试 |
