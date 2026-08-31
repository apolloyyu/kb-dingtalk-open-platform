---
title: "获取用户授权的持久授权码"
source_url: "https://open.dingtalk.com/document/development/persistent-authorization-code"
namespace: "development"
slug: "persistent-authorization-code"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 访问凭证 > 用户个人身份凭证 > 获取用户授权的持久授权码"
doc_id: "kytMMp88e1"
updated_at: "2026-06-30 16:49:02"
---

> Source: https://open.dingtalk.com/document/development/persistent-authorization-code
> Path: 应用开发 / 服务端 API / 认证与授权 > 访问凭证 > 用户个人身份凭证 > 获取用户授权的持久授权码
> Updated: 2026-06-30 16:49:02

# 获取用户授权的持久授权码

调用本接口可使用临时授权码（`tmp_auth_code`）换取用户的持久化授权凭证（`persistent_code`），用于后续长期访问用户数据。该接口通常在用户完成OAuth授权后调用，是第三方个人应用实现用户身份绑定的关键步骤之一

## 使用场景

本接口**仅适用于第三方个人应用**，用于将前端获取的临时授权码转换为可长期使用的持久授权码。

持久授权码（`persistent_code`）无过期时间，可用于后续调用开放平台 接口，进而代表用户执行操作。

典型业务场景包括：

- 用户首次登录时建立长期授权关系；
- 实现跨设备或服务间的身份同步；
- 需要后台异步访问用户数据的服务架构。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/sns/get\_persistent\_code |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方个人应用 |
| 权限要求 | 无 |

### **查询参数**

| 名称 | 参数类型 | 是否必选 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 5c5e303c-xxxx83ff1f7bef | 应用的授权凭证，调用[获取第三方个人应用的access\_token](0035-obtain-personal-application.md)接口获取。 |

### **请求体**

| 参数 | 类型 | 是否必选 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| tmp\_auth\_code | String | 是 | 23152698ea18304xxxx | 用户授权给钉钉开放应用的临时授权码。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/sns/get_persistent_code" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=5c5e303c-xxxx83ff1f7bef' \
-d 'tmp_auth_code=23152698ea18304da4d0ce1xxxxx'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/get_persistent_code");
OapiSnsGetPersistentCodeRequest req = new OapiSnsGetPersistentCodeRequest();
req.setTmpAuthCode("23152698ea18304da4d0ce1xxxxx");
OapiSnsGetPersistentCodeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiSnsGetPersistentCodeRequest("https://oapi.dingtalk.com/sns/get_persistent_code")

req.tmp_auth_code="23152698ea18304da4d0ce1xxxxx"
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
$req = new OapiSnsGetPersistentCodeRequest;
$req->setTmpAuthCode("23152698ea18304da4d0ce1xxxxx");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/sns/get_persistent_code");
```

Node.js

```
let { Config, OapiSnsGetPersistentCodeParams, OapiSnsGetPersistentCodeRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/sns/get_persistent_code'
  config.session = 'access_token'
  const params = new OapiSnsGetPersistentCodeParams();
  params.tmpAuthCode = '23152698ea18304xxxx'

  const request = new OapiSnsGetPersistentCodeRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiSnsGetPersistentCode(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/get_persistent_code");
OapiSnsGetPersistentCodeRequest req = new OapiSnsGetPersistentCodeRequest();
req.TmpAuthCode = "23152698ea18304da4d0ce1xxxxx";
OapiSnsGetPersistentCodeResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 参数 | 类型 | 示例值 | 说明 |
| --- | --- | --- | --- |
| persistent\_code | String | liSii8KCxxxxx | 用户给开放应用授权的持久授权码，此码目前无过期时间。 |
| openid | String | dsa-d-asdaxxxxnINIn-ssdasd | 用户在当前开放应用内的唯一标识 |
| unionid | String | 7Huu46kk | 用户在当前钉钉开放平台账号范围内的唯一标识。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
    "errcode":0,
    "errmsg":"ok",
    "persistent_code":"liSii8KCxxxxx",
    "openid":"dsa-d-asdaxxxxnINIn-ssdasd",
    "unionid":"7Huu46kk"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
