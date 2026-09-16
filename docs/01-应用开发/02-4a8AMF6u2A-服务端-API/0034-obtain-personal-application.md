---
title: "获取第三方个人应用的access_token"
source_url: "https://open.dingtalk.com/document/development/obtain-personal-application"
namespace: "development"
slug: "obtain-personal-application"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 访问凭证 > 应用身份凭证 > 获取第三方个人应用的access_token"
doc_id: "RxpXOYkmwL"
updated_at: "2026-04-29 22:27:40"
---

> Source: https://open.dingtalk.com/document/development/obtain-personal-application
> Path: 应用开发 / 服务端 API / 认证与授权 > 访问凭证 > 应用身份凭证 > 获取第三方个人应用的access_token
> Updated: 2026-04-29 22:27:40

# 获取第三方个人应用的access\_token

调用本接口可获取第三方个人应用的全局唯一凭证 `access_token`，用于后续调用钉钉开放平台提供的用户身份识别、数据获取等开放能力，

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/sns/gettoken |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方个人应用 |
| 权限要求 | 无 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| appid | String | 是 | ding1234 | 创建的第三方个人应用的标识，详情参考[创建和配置应用](../01-XOnnmGCTbn-开发指南/0005-create-and-configure-an-application.md)。 |
| appsecret | String | 是 | 1234 | 创建的第三方个人应用的密钥。appid和appsecret可在[钉钉开发者后台](https://open-dev.dingtalk.com/)的应用详情页面获取。 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/sns/gettoken" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'appid=ding1234' \
-d 'appsecret=1234'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/gettoken");
OapiSnsGettokenRequest req = new OapiSnsGettokenRequest();
req.setAppid("ding1234");
req.setAppsecret("1234");
req.setHttpMethod("GET");
OapiSnsGettokenResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiSnsGettokenRequest("https://oapi.dingtalk.com/sns/gettoken")
req.appid="ding1234"
req.appsecret="1234"
try:
	resp= req.getResponse()
	print(resp)
except Exception,e:
	print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_GET , DingTalkConstant::$FORMAT_JSON);
$req = new OapiSnsGettokenRequest;
$req->setAppid("ding1234");
$req->setAppsecret("1234");
$resp = $c->execute($req, "https://oapi.dingtalk.com/sns/gettoken");
```

Node.js

```
let { Config, OapiSnsGettokenParams, OapiSnsGettokenRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/sns/gettoken'
  const params = new OapiSnsGettokenParams();
  params.appid = 'ding1234';
  params.appsecret("1234");
  const request = new OapiSnsGettokenRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiSnsGettoken(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/gettoken");
OapiSnsGettokenRequest req = new OapiSnsGettokenRequest();
req.Appid = "ding1234";
req.Appsecret = "1234";
req.SetHttpMethod("GET");
OapiSnsGettokenResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| access\_token | String | fw8ef8we8f76e6f7s8dxxxx | 生成的access\_token。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
    "errcode": 0,
    "access_token": "fw8ef8we8f76e6f7s8dxxxx",
    "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
