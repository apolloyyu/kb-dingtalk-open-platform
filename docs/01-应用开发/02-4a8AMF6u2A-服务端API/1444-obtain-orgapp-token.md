---
title: "获取企业内部应用的access_token"
source_url: "https://open.dingtalk.com/document/development/obtain-orgapp-token"
namespace: "development"
slug: "obtain-orgapp-token"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 获取企业内部应用的access_token"
doc_id: "FRuKfO9tOP"
updated_at: "2026-07-22 16:25:42"
---

> Source: https://open.dingtalk.com/document/development/obtain-orgapp-token
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 获取访问凭证 > 获取企业内部应用的access_token
> Updated: 2026-07-22 16:25:42

# 获取企业内部应用的access\_token

企业内部应用调用本接口获取access\_token。调用服务端API获取应用资源时，需要通过access\_token来鉴权调用者身份进行授权。

> **[!IMPORTANT]**
>
> 为提升使用体验，相关接口规范已完成升级：
>
> - 新用户请直接使用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)新版接口；
> - 存量用户建议评估后按需切换至新版，以获得更好的服务体验。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/gettoken |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | 无 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| appkey | String | 是 | dingeqqpkv3xxxx | 已创建的企业内部应用的 Client ID，获取方式可参考[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)文档说明。 |
| appsecret | String | 是 | GT-lsu-taDAsTsxxxx | 已创建的企业内部应用的 Client Secre ，获取方式可参考[Client ID/Client Secret](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)文档说明。 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/gettoken" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a22a8fc4-abaa-4af4-9c3c-cc0cd9fc7c1c' \
-d 'appkey=appkey' \
-d 'appsecret=appsecret'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
OapiGettokenRequest req = new OapiGettokenRequest();
req.setAppkey("appkey");
req.setAppsecret("appsecret");
req.setHttpMethod("GET");
OapiGettokenResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
JAVAPHP.NETCURLPythonNodeJSC/C++Python3GOPHP7JAVA8.NET6
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
req.appkey="appkey"
req.appsecret="appsecret"
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
$req = new OapiGettokenRequest;
$req->setAppkey("appkey");
$req->setAppsecret("appsecret");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/gettoken");
```

Node.js

```
let { Config, OapiGettokenParams, OapiGettokenRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/gettoken'
  config.session = 'access_token'
  const params = new OapiGettokenParams();
  params.appKey = 'bab02f63c1e030fbbxxxx'
  params.appSecret = 'bab02f63c1e030fbbxxxx'
  const request = new OapiGettokenRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiGettoken(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
OapiGettokenRequest req = new OapiGettokenRequest();
req.Appkey = "appkey";
req.Appsecret = "appsecret";
req.SetHttpMethod("GET");
OapiGettokenResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| access\_token | String | fw8ef8we8f76e6f7s8dxxxx | 生成的access\_token。  **[!NOTE]**  在使用access\_token时，请注意：   - access\_token的有效期为7200秒（2小时），有效期内重复获取会返回相同结果并自动续期，过期后获取会返回新的access\_token。 - 开发者需要缓存access\_token，用于后续接口的调用。因为每个应用的access\_token是彼此独立的，所以进行缓存时需要区分应用来进行存储。 - 不能频繁调用gettoken接口，否则会受到频率拦截。 |
| expires\_in | Number | 7200 | access\_token的过期时间，单位秒。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
    "errcode": 0,
    "access_token": "96fc7a7axxx",
    "errmsg": "ok",
    "expires_in": 7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
