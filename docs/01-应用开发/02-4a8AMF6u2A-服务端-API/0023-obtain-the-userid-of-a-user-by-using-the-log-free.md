---
title: "通过免登码获取用户信息"
source_url: "https://open.dingtalk.com/document/development/obtain-the-userid-of-a-user-by-using-the-log-free"
namespace: "development"
slug: "obtain-the-userid-of-a-user-by-using-the-log-free"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 通过免登码获取用户信息"
doc_id: "H2mylS6eke"
updated_at: "2026-07-02 10:35:34"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-userid-of-a-user-by-using-the-log-free
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 通过免登码获取用户信息
> Updated: 2026-07-02 10:35:34

# 通过免登码获取用户信息

在第三方企业应用免登和企业内部应用免登场景中，开发者需要使用本接口通过access\_token和免登接口中获取的code来获取用户userid。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/user/getuserinfo |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| code | String | 是 | bab02f63c1e030fbbxxxx | 免登授权码，获取方式请参考：   - 小程序：[getAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0006-jsapi-get-auth-code.md) - 微应用：[requestAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md)   **[!NOTE]**  此授权码五分钟内有效，且只能使用一次。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/user/getuserinfo" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=417124xxxx2a3c270d5' \
-d 'code=123456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/getuserinfo");
OapiV2UserGetuserinfoRequest req = new OapiV2UserGetuserinfoRequest();
req.setCode("bab02f63c1e030fbbxxxx");
OapiV2UserGetuserinfoResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiV2UserGetuserinfoRequest("https://oapi.dingtalk.com/topapi/v2/user/getuserinfo")

req.code="123456"
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
$req = new OapiV2UserGetuserinfoRequest;
$req->setCode("123456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/user/getuserinfo");
```

Node.js

```
let { Config, OapiV2UserGetuserinfoParams, OapiV2UserGetuserinfoRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/topapi/v2/user/getuserinfo'
  config.session = 'access_token'
  const params = new OapiV2UserGetuserinfoParams();
  params.code = 'bab02f63c1e030fbbxxxx'

  const request = new OapiV2UserGetuserinfoRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiV2UserGetuserinfo(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/getuserinfo");
OapiV2UserGetuserinfoRequest req = new OapiV2UserGetuserinfoRequest();
req.Code = "123456";
OapiV2UserGetuserinfoResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | e8krly4vyiln | 请求ID。 |
| errcode | Number | 0 | 返回码**。** |
| errmsg | String | ok | 对返回码的文本描述内容。 |
| result | UserGetByCodeResponse |  | 返回结果。 |
| userid | String | user456 | 用户的userId。 |
| device\_id | String | 12drtfxxxxx | 设备ID。 |
| sys | Boolean | true | 是否是管理员。   - **true**：是 - **false**：不是 |
| sys\_level | Number | 1 | 级别。   - **1**：主管理员 - **2**：子管理员 - **100**：老板 - **0**：其他（如普通员工） |
| associated\_unionid | String | N2o5U3axxxx | 用户关联的unionId。 |
| unionid | String | gliiW002zUxxxx | 用户unionId。 |
| name | String | 张xx | 用户名字。 |

### **响应体示例**

```
{
  "errcode": 0, 
  "result": {
    "associated_unionid": "N2o5U3axxxx", 
    "unionid": "gliiW0piiii02zBUjUxxxx", 
    "device_id": "12drtfxxxxx", 
    "sys_level": 1, 
    "name": "张xx", 
    "sys": true, 
    "userid": "userid123"
  }, 
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
