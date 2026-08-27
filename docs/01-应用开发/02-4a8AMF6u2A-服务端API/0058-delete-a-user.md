---
title: "删除用户"
source_url: "https://open.dingtalk.com/document/development/delete-a-user"
namespace: "development"
slug: "delete-a-user"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 删除用户"
doc_id: "enDL3e3A5T"
updated_at: "2026-06-08 09:28:30"
---

> Source: https://open.dingtalk.com/document/development/delete-a-user
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 删除用户
> Updated: 2026-06-08 09:28:30

# 删除用户

调用本接口根据用户的userid删除指定用户。

## **接口调用说明**

调用本接口成功删除通讯录员工，同时会删除以下内容：

- 该员工所在的考勤组会同步删除该员工。
- 智能人事花名册会同步删除该员工，员工信息可以在智能人事已离职人员中查看。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | uxxxx3 | 员工的userid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0b8a6220-ef56-4427-83d5-5690431776e5' \
-d 'userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/delete");
OapiV2UserDeleteRequest req = new OapiV2UserDeleteRequest();
req.setUserid("user123");
OapiV2UserDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserDeleteRequest("https://oapi.dingtalk.com/topapi/v2/user/delete")

req.userid="zhangsan"
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
$req = new OapiV2UserDeleteRequest;
$req->setUserid("zhangsan");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/delete");
OapiV2UserDeleteRequest req = new OapiV2UserDeleteRequest();
req.Userid = "zhangsan";
OapiV2UserDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4f9md9obopn2 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 不合法的userid | 调用失败时返回的错误信息。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok"
  "request_id": "4f9md9obopn2"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33012 | 无效的userId | 请检查userId是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后再试 |
