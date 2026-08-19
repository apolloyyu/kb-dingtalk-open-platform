---
title: "根据unionid获取用户userid"
source_url: "https://open.dingtalk.com/document/development/query-a-user-by-the-union-id"
namespace: "development"
slug: "query-a-user-by-the-union-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 根据unionid获取用户userid"
doc_id: "lueURRh6KT"
updated_at: "2026-06-08 09:28:39"
---

> Source: https://open.dingtalk.com/document/development/query-a-user-by-the-union-id
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 根据unionid获取用户userid
> Updated: 2026-06-08 09:28:39

# 根据unionid获取用户userid

调用本接口根据unionid获取用户的userid。

## **接口调用说明**

unionid是员工在当前开发者企业账号范围内的唯一标识，由系统生成：

- 同一个企业员工，在不同的开发者企业账号下，unionid是不相同的。
- 在同一个开发者企业账号下，unionid是唯一且不变的，例如同一个服务商开发的多个应用，或者是扫码登录等场景的多个App账号。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/user/getbyunionid |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3Fxxxx | 调用该接口的应用凭证。  **[!NOTE]**  如果是通过**免登方式**获取的unionid，则不能使用免登获取的 token 调用该接口，需要使用下方的接口重新获取。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | z21HjQliSzpw0Yxxxx | 员工在当前开发者企业账号范围内的唯一标识，系统生成，不会改变。可通过调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获取unionid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/user/getbyunionid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=6348d21e-fb41-4745-a214-95bcf8c118f0' \
-d 'unionid=z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/getbyunionid");
OapiUserGetbyunionidRequest req = new OapiUserGetbyunionidRequest();
req.setUnionid("z21HjQliSzpw0Yxxxxxx");
OapiUserGetbyunionidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserGetbyunionidRequest("https://oapi.dingtalk.com/topapi/user/getbyunionid")
req.unionid="z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ"
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
$req = new OapiUserGetbyunionidRequest;
$req->setUnionid("z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/user/getbyunionid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/getbyunionid");
OapiUserGetbyunionidRequest req = new OapiUserGetbyunionidRequest();
req.Unionid = "z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ";
OapiUserGetbyunionidResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | zcqi5450rpit | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | UserGetByUnionIdResponse |  | 返回结果。 |
| contact\_type | Number | 0 | 联系类型：   - **0**：企业内部员工 - **1**：企业外部联系人 |
| userid | String | zhangsan | 用户的userid。 |

### **响应体示例**

```
{
  "errcode":"0",
  "errmsg":"ok",
  "result":{
   "contact_type":"0",
   "userid":"zhangsan"
  },
  "request_id": "zcqi5450rpit"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 60121 | 未找到对应员工 | 请检查unionId是否正确 |
| 400002 | 无效的参数 | 请检查unionId是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
