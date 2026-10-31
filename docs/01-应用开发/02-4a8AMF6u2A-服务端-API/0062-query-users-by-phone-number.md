---
title: "根据手机号查询用户"
source_url: "https://open.dingtalk.com/document/development/query-users-by-phone-number"
namespace: "development"
slug: "query-users-by-phone-number"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 根据手机号查询用户"
doc_id: "zXvwrLZnWq"
updated_at: "2026-06-08 09:28:38"
---

> Source: https://open.dingtalk.com/document/development/query-users-by-phone-number
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 根据手机号查询用户
> Updated: 2026-06-08 09:28:38

# 根据手机号查询用户

调用本接口，根据手机号可以查询在职员工的userId。如果员工离职，无法根据手机号获取用户的userId。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/getbymobile |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_get\_member\_by\_mobile-根据手机号获取成员基本信息权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3Fxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| mobile | String | 是 | 1\*\*\*\*\*\*\*543 | 用户的手机号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/getbymobile" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2015ca04-c84e-4855-9e52-330b98eb35f5' \
-d 'mobile=18513027676'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/getbymobile");
OapiV2UserGetbymobileRequest req = new OapiV2UserGetbymobileRequest();
req.setMobile("1*******543");
OapiV2UserGetbymobileResponse rsp = client.execute(req, acces_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2UserGetbymobileRequest("https://oapi.dingtalk.com/topapi/v2/user/getbymobile")

req.mobile="18513027676"
req.support_exclusive_account_search=true
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
$req = new OapiV2UserGetbymobileRequest;
$req->setMobile("18513027676");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/getbymobile");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/getbymobile");
OapiV2UserGetbymobileRequest req = new OapiV2UserGetbymobileRequest();
req.Mobile = "18513027676";
OapiV2UserGetbymobileResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5w82ciuur781 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | Object |  | 返回结果。 |
| userid | String | zhangsan | 员工的userId。 |

### **响应体示例**

```
{
  "errcode":"0",
  "result":{
    "userid":"xiaoding"
  },
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | 无效的参数 | 请确认参数是否按照上述文档要求填写 |
| 40104 | 企业中无效的手机号 | 请检查手机号是否正确 |
| 60121 | 未找到该用户 | 请确认信息填写是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
