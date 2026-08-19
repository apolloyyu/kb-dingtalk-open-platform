---
title: "获取授权应用的基本信息"
source_url: "https://open.dingtalk.com/document/development/obtains-application-information-of-an-enterprise"
namespace: "development"
slug: "obtains-application-information-of-an-enterprise"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用授权 > 获取授权应用的基本信息"
doc_id: "QpAVnHmVl3"
updated_at: "2026-04-29 22:27:45"
---

> Source: https://open.dingtalk.com/document/development/obtains-application-information-of-an-enterprise
> Path: 应用开发 / 服务端API / 应用授权 > 获取授权应用的基本信息
> Updated: 2026-04-29 22:27:45

# 获取授权应用的基本信息

通过本接口，可获取已授权企业的指定应用的基本信息，如 LOGO、名称和描述。

## **接口调用说明**

### **使用场景**

适用于第三方服务商在接收到企业授权开通事件后，调用本接口获取该企业下特定应用的基础配置信息，用于本地系统初始化或应用状态同步。

例如：当企业用户完成应用授权后，服务商可通过解析[企业授权开通应用事件]中的 `auth_corpid` 和 `agentid`，调用此接口拉取应用的名称、图标等展示信息，实现自动化配置。

### **功能说明**

- 在使用HTTP调用本接口时，必须设置**signature**参数，钉钉会对请求进行签名验证，用以提升安全水位。签名计算方式，请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。
- 在使用SDK调用本接口时，无需自行进行签名计算，钉钉SDK已自带签名功能**。**推荐使用钉钉提供的SDK进行调用，SDK下载地址参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/service/get\_agent |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_base-三方应用开通使用基础权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_access\_token | String | 是 | 68fbxxxx | 第三方企业应用的suite\_access\_token，可通过[获取第三方企业应用的suite\_access\_token](1445-obtain-application-suite-ticket.md)接口获取。 |
| timestamp | String | 是 | 1598359962000 | 当前时间戳, 单位毫秒。  **[!NOTE]**  使用SDK调用时，不需要传递此参数。 |
| suiteTicket | String | 是 | test | 钉钉开放平台向应用的回调URL推送的suite\_ticket，详细内容请参考[数据格式biz\_type=2](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md)。 |
| signature | String | 是 | xxxx | 签名。签名计算方式请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。  **[!IMPORTANT]**  计算出签名以后，需要进行urlencode，才能把签名参数拼接到url中。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agentid | String | 是 | 852381775 | 授权企业方应用ID，有以下两种获取方式：   - 调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 - 从[企业授权开通应用事件](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md)中获取。 |
| auth\_corpid | String | 是 | ding1234 | 授权企业的CorpId，从[企业授权开通应用事件](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md)中获取。 |
| suite\_key | String | 是 | suitezx8sttxxx | 第三方应用的Suitekey。  可在[钉钉开发者后台](https://open-dev.dingtalk.com/)的第三方应用详情页面获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/service/get_agent" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'agentid=123' \
-d 'auth_corpid=ding1234' \
-d 'suite_key=key'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_agent");
OapiServiceGetAgentRequest req = new OapiServiceGetAgentRequest();
req.setAgentid("852381775");
req.setAuthCorpid("ding1234");
req.setSuiteKey("key");
OapiServiceGetAgentResponse rsp = client.execute(req);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiServiceGetAgentRequest("https://oapi.dingtalk.com/service/get_agent")

req.agentid="123"
req.auth_corpid="ding1234"
req.suite_key="key"
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
$req = new OapiServiceGetAgentRequest;
$req->setAgentid("123");
$req->setAuthCorpid("ding1234");
$req->setSuiteKey("key");
$resp = $c->execute($req, "https://oapi.dingtalk.com/service/get_agent");
```

Node.js

```
let { Config, OapiServiceGetAgentGetParams, OapiServiceGetAgentRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/service/get_agent'
  config.session = 'access_token'
  const params = new OapiServiceGetAgentGetParams();
  params.agentid = '852381775';
  params.auth_corpid = 'ding1234';
  params.suite_key = 'suitezx8sttxxx';

  const request = new OapiServiceGetAgentRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiServiceGetAgentGet(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_agent");
OapiServiceGetAgentRequest req = new OapiServiceGetAgentRequest();
req.Agentid = "123";
req.AuthCorpid = "ding1234";
req.SuiteKey = "key";
OapiServiceGetAgentResponse rsp = client.Execute(req);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| agentid | Number | 852381775 | 企业应用ID。 |
| name | String | 钉钉小程序 | 企业应用名称。 |
| logo\_url | String | https://static-legacy.dingtalk.com/xxx | 企业应用头像。 |
| description | String | 钉钉应用 | 企业应用描述。 |
| close | Number | 1 | 授权方企业应用是否被禁用：   - **0**：禁用 - **1**：正常 - **2**：待激活 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":0,
  "agentid":852381775,
  "logo_url":"https://static-legacy.dingtalk.com/media/lADPDefRxxj6mvVUVg_86_84.jpg",
  "name":"钉钉小程序",
  "errmsg":"ok",
  "description":"钉钉应用",
  "close":1
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
