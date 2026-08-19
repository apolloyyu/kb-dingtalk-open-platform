---
title: "获取第三方企业应用的suite_access_token"
source_url: "https://open.dingtalk.com/document/development/obtain-application-suite-ticket"
namespace: "development"
slug: "obtain-application-suite-ticket"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 获取第三方企业应用的suite_access_token"
doc_id: "pEN2VC7PiA"
updated_at: "2026-07-22 16:25:43"
---

> Source: https://open.dingtalk.com/document/development/obtain-application-suite-ticket
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 获取访问凭证 > 获取第三方企业应用的suite_access_token
> Updated: 2026-07-22 16:25:43

# **获取第三方企业应用的suite\_access\_token**

调用本接口获取第三方企业应用的suite\_access\_token。

## **接口调用说明**

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**获取访问凭证**相关接口规范进行升级，本接口仅保持现有功能，不再新增支持其他能力：
>
> - 如果未使用本接口，推荐使用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)新版规范接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

该suite\_access\_token主要用于获取第三方企业应用的信息，在调用以下接口时会使用第三方企业应用的suite\_access\_token：

- [获取授权应用的基本信息](0043-obtains-application-information-of-an-enterprise.md)
- [获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/service/get\_suite\_token |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 无 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_key | String | 是 | suitefcurkdvkc1nxxxx | 第三方应用的suiteKey。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| suite\_secret | String | 是 | y1ie2Rfb54xxxx | 第三方应用的suiteSecret，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| suite\_ticket | String | 是 | test | 钉钉开放平台会向应用的回调URL推送的suite\_ticket（约5个小时推送一次），详细内容请参考[数据格式biz\_type=2](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-dqx-ue5-0f8)。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/service/get_suite_token" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'suite_key=suitefcurkdvkc1nxxxx' \
-d 'suite_secret=y1ie2Rfb54xxxx' \
-d 'suite_ticket=test'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_suite_token");
OapiServiceGetSuiteTokenRequest req = new OapiServiceGetSuiteTokenRequest();
req.setSuiteKey("suitefcurkdvkc1nxxxx");
req.setSuiteSecret("y1ie2Rfb54xxxx");
req.setSuiteTicket("test");
OapiServiceGetSuiteTokenResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceGetSuiteTokenRequest("https://oapi.dingtalk.com/service/get_suite_token")

req.suite_key="suitefcurkdvkc1nxxxx"
req.suite_secret="y1ie2Rfb54xxxx"
req.suite_ticket="test"
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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiServiceGetSuiteTokenRequest;
$req->setSuiteKey("suitefcurkdvkc1nxxxx");
$req->setSuiteSecret("y1ie2Rfb54xxxx");
$req->setSuiteTicket("test");
$resp = $c->execute($req,"https://oapi.dingtalk.com/service/get_suite_token");
```

Node.js

```
TopClient = require('./topClient').TopClient;
var client = new TopClient({
  'appkey': 'appkey',
  'appsecret': 'secret',
  'url': 'http://gw.api.taobao.com/router/rest'
});

client.execute('dingtalk.oapi.service.get_suite_token', {
  'suite_key':'suitefcurkdvkc1nxxxx',
  'suite_secret':'y1ie2Rfb54xxxx',
  'suite_ticket':'test'
}, function(error, response) {
  if (!error) console.log(response);
  else console.log(error);
})
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_suite_token");
OapiServiceGetSuiteTokenRequest req = new OapiServiceGetSuiteTokenRequest();
req.SuiteKey = "suitefcurkdvkc1nxxxx";
req.SuiteSecret = "y1ie2Rfb54xxxx";
req.SuiteTicket = "test";
OapiServiceGetSuiteTokenResponse rsp = client.Execute(req);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| suite\_access\_token | String | token | 第三方企业应用的凭证。 |
| expires\_in | Number | 7200 | 第三方企业应用的凭证过期时间，单位秒。  **[!NOTE]**  suite\_access\_token有效期为7200秒，过期之前建议服务端做定时器主动更新，而不是依赖钉钉的定时推送。 |

### **响应体示例**

```
{
        "errcode":0,
        "errmsg":"ok",
        "suite_access_token":"67477fed82e63563a320xxxx",
        "expires_in":7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
