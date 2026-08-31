---
title: "获取应用未激活的企业列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-enterprises-whose-applications-are-not-activated"
namespace: "development"
slug: "obtains-a-list-of-enterprises-whose-applications-are-not-activated"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "应用授权 > 获取应用未激活的企业列表"
doc_id: "bDd1OaC8fS"
updated_at: "2026-07-02 10:35:38"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-enterprises-whose-applications-are-not-activated
> Path: 应用开发 / 服务端 API / 应用授权 > 获取应用未激活的企业列表
> Updated: 2026-07-02 10:35:38

# 获取应用未激活的企业列表

通过此接口，第三方服务商可以获取尚未激活指定应用的企业（Corp）列表，用于后续的激活引导、数据统计或运营分析。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/service/get\_unactive\_corp |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_base-三方应用开通使用基础权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 6ed1bxxxx | 第三方企业应用的suite\_access\_token，可调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取凭证。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| app\_id | Number | 否 | 123 | 套件下的微应用ID，可以在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/provider/eapp/57453/1)查看。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/service/get_unactive_corp?suite_access_token=6ed1bxxxx" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'app_id=123''
```

Java

```
DingTalkClient client = new DefaultDingTalkClient(
"https://oapi.dingtalk.com/service/get_unactive_corp?suite_access_token=6ed1bxxxx");
OapiServiceGetUnactiveCorpRequest req = new OapiServiceGetUnactiveCorpRequest();
req.setAppId(123L);
OapiServiceGetUnactiveCorpResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiServiceGetUnactiveCorpRequest("https://oapi.dingtalk.com/service/get_unactive_corp?suite_access_token=6ed1bxxxx")
req.app_id=123
try:
  resp= req.getResponse()
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
<?php

$url = 'https://oapi.dingtalk.com/service/get_unactive_corp?suite_access_token=6ed1bxxxx';

$data = array(
  'app_id' => 123
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
  'Content-Type: application/json'
));
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$errno = curl_errno($ch);
curl_close($ch);

if ($errno) {
  echo "Error: $errno";
} else {
  echo $response;
}
?>
```

Node.js

```
let { Config, OapiServiceGetUnactiveCorpParams, OapiServiceGetUnactiveCorpRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/service/get_unactive_corp?suite_access_token=6ed1bxxxx'
  const params = new OapiServiceGetUnactiveCorpParams();
  params.appId = 123

  const request = new OapiServiceGetUnactiveCorpRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiServiceGetUnactiveCorp(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_unactive_corp?suite_access_token=6ed1bxxxx");
OapiServiceGetUnactiveCorpRequest req = new OapiServiceGetUnactiveCorpRequest();
req.AppId = 123L;
OapiServiceGetUnactiveCorpResponse rsp = client.Execute(req);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| app\_id | Number | 57453 | 微应用ID。 |
| corp\_list | String[] | ["ding123","ding456"] | 授权未激活应用的CorpId列表。 |
| has\_more | Boolean | false | 是否还有更多数据。 |
| errmsg | String | ok | 调用失败时返回的错误信息。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode": 0,
  "corp_list": [
    "ding123",
    "ding456"
  ],
  "errmsg": "ok",
  "has_more": false,
  "app_id": 57453
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
