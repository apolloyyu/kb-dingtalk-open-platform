---
title: "重新授权未激活应用的企业"
source_url: "https://open.dingtalk.com/document/development/re-authorize-enterprises-whose-applications-are-not-activated"
namespace: "development"
slug: "re-authorize-enterprises-whose-applications-are-not-activated"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用授权 > 重新授权未激活应用的企业"
doc_id: "YdbBqjemf4"
updated_at: "2026-04-29 22:27:46"
---

> Source: https://open.dingtalk.com/document/development/re-authorize-enterprises-whose-applications-are-not-activated
> Path: 应用开发 / 服务端API / 应用授权 > 重新授权未激活应用的企业
> Updated: 2026-04-29 22:27:46

# 重新授权未激活应用的企业

通过此接口，第三方企业应用可对之前未完成授权或已失效授权的企业重新发起授权流程，恢复服务对接。适用于服务商在升级服务包、客户重新开通服务等场景下批量处理历史企业的授权状态。

## **接口调用说明**

当企业用户曾拒绝授权或授权过期后，可通过此接口再次发起授权流程，以恢复服务对接。

适用于第三方ISV在客户企业重新开通服务时调用。例如：当服务商为多个历史客户升级服务版本后，需对尚未激活应用的企业批量重发授权邀请，确保其能继续使用新功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/service/reauth\_corp |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_base-三方应用开通使用基础权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 6ed1bxxxx | 第三方企业应用的suite\_access\_token，可调用[获取第三方企业应用的suite\_access\_token](1447-obtain-application-suite-ticket.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| app\_id | String | 否 | 123 | 套件下的微应用ID，可以在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/provider/eapp/57453/1)查看。 |
| corpid\_list | String[] | 否 | ["ding123"] | 授权未激活应用的CorpId列表，可以调用[获取应用未激活的企业列表](0046-obtains-a-list-of-enterprises-whose-applications-are-not-activated.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/service/reauth_corp?suite_access_token=SUITE_ACCESS_TOKEN" \
-H 'Content-Type:application/json' \
-d '{
    "app_id": "123",
    "corpid_list": ["ding123", "ding456"]
}'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/reauth_corp?suite_access_token=SUITE_ACCESS_TOKEN");
OapiServiceReauthCorpRequest req = new OapiServiceReauthCorpRequest();
req.setAppId("123");
req.setCorpidList(Arrays.asList("ding123","ding456"));
OapiServiceReauthCorpResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

url = "https://oapi.dingtalk.com/service/reauth_corp?suite_access_token=YOUR_TOKEN"
req = dingtalk.api.OapiServiceReauthCorpRequest(url)
req.app_id = "123"
req.corpid_list = ["ding123"]
try:
	resp = req.getResponse()
	print(resp)
except Exception,e:
	print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiServiceReauthCorpRequest;
$req->setAppId("123");
$req->setCorpidList(["ding123"]); 
$resp = $c->execute($req,"https://oapi.dingtalk.com/service/reauth_corp");
```

Node.js

```
let { Config, OapiServiceReauthCorpParams, OapiServiceReauthCorpRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/service/reauth_corps?suite_access_token=SUITE_ACCESS_TOKEN'
  const params = new OapiServiceReauthCorpParams();
  params.app_id = '23aa6xxxxc1b56c'
  params.corpid_list = [  "ding123","ding456"]
  const request = new OapiServiceReauthCorpRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiServiceReauthCorp(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/reauth_corp?suite_access_token=YOUR_SUITE_TOKEN");
OapiServiceReauthCorpRequest req = new OapiServiceReauthCorpRequest();
req.AppId = "123";
req.CorpidList = new List<string> { "ding123" }; 
OapiServiceReauthCorpResponse rsp = client.Execute(req);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 调用失败时返回的错误信息。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
