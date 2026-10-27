---
title: "获取企业授权信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-basic-information-of-an-enterprise"
namespace: "development"
slug: "obtains-the-basic-information-of-an-enterprise"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "应用授权 > 获取企业授权信息"
doc_id: "B89UHBjcli"
updated_at: "2026-04-29 22:27:44"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-basic-information-of-an-enterprise
> Path: 应用开发 / 服务端 API / 应用授权 > 获取企业授权信息
> Updated: 2026-04-29 22:27:44

# 获取企业授权信息

产品方案商为企业开发企业内部应用时，调用本接口获取企业授权信息。

## **接口调用说明**

### **使用场景**

本接口适用于产品方案商或第三方ISV在完成企业授权后，获取该企业的组织架构、管理员信息及已授权应用详情。典型业务场景包括：

- 企业内部应用初始化配置：根据企业实际信息定制首页展示内容、权限体系和功能模块。
- 多租户SaaS系统集成：识别不同企业租户的身份与认证等级，提供差异化服务策略。
- 渠道拉新统计分析：通过`invite_code`和`auth_channel_type`字段追踪企业来源渠道，评估推广效果。
- 管理员身份校验：获取拥有微应用管理权限的管理员列表（`admin_list`），用于后续操作鉴权。

**注意事项**：

- 接口调用需使用具备合法权限的应用凭证（accessKey/accessSecret），建议优先使用钉钉官方SDK以避免手动签名错误。
- `suite_key`仅在调用第三方企业应用时需要填写；定制应用可不传。
- 返回结果中的敏感信息（如管理员userid）应妥善保管，遵循最小必要原则使用。

### **功能说明**

产品方案商为企业开发应用时，可通过本接口获取企业的授权信息，包括企业基本信息、管理员信息、已授权应用列表等数据，支持应用的个性化配置与权限管理。

> **[!NOTE]**
>
> - 在使用HTTP调用本接口时，必须设置**signature**参数，钉钉会对请求进行签名验证，用以提升安全水位。签名计算方式，请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。
> - 在使用SDK调用本接口时，无需自行进行签名计算，钉钉SDK已自带签名功能**。**推荐使用钉钉提供的SDK进行调用，SDK下载地址参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/service/get\_auth\_info |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用（委托产品方案商）appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_base-三方应用开通使用基础权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| accessKey | String | 是 | 6ed1bxxxx | - 第三方企业应用的SuiteKey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 - 定制应用的CustomKey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| timestamp | String | 是 | 1598359962000 | 当前时间戳，单位毫秒。 |
| suiteTicket | String | 是 | test | - 第三方企业应用，使用钉钉推送的suiteTicket。 - 定制应用，可指定任意值。 |
| signature | String | 是 | xxx | 签名。签名计算方式请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。  **[!NOTE]**  计算出签名以后，需要进行urlencode，才能把签名参数拼接到url中。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| suite\_key | String | 否 | suitefcurkdvkc1xxxx | 第三方应用的Suitekey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/)的第三方应用详情页面获取。 |
| auth\_corpid | String | 是 | ding1234 | 授权方的CorpId，可在[钉钉开发者后台](https://open-dev.dingtalk.com/)首页获取。 |

### **请求示例**

curl

```
curl -X POST 'https://oapi.dingtalk.com/service/get_auth_info?accessKey=6ed1bxxxx&timestamp=1598359962000&suiteTicket=test&signature=xxx' \
  -H 'Content-Type: application/json' \
  -d '{
    "suite_key": "suitep1f5lzyglm7fryxxxx",
    "auth_corpid": "_FP5PpZF3irDKjxxx"
  }'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_auth_info");
OapiServiceGetAuthInfoRequest req = new OapiServiceGetAuthInfoRequest();
req.setSuiteKey("suitefcurkdvkc1xxxx");
req.setAuthCorpid("ding1234");
OapiServiceGetAuthInfoResponse rsp = client.execute(req, "accessKey" ,"accessSecret" ,"suiteTicket");
System.out.println(rsp.getBody());
System.out.println(JSON.toJSONString(client));
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiServiceGetAuthInfoRequest("https://oapi.dingtalk.com/service/get_auth_info")

req.suite_key="suitefcurkdvkc1xxxx"
req.auth_corpid="ding1234"
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
$req = new OapiServiceGetAuthInfoRequest;
$req->setSuiteKey("key");
$req->setAuthCorpid("ding1234");
$resp = $c->execute($req, "https://oapi.dingtalk.com/service/get_auth_info");
```

Node.js

```
let { Config, OapiServiceGetAuthInfoParams, OapiServiceGetAuthInfoRequest } = require('./client.js');
let Client = require('./client.js').default
async function test() {
  const config = new Config()
  config.serverUrl = 'https://oapi.dingtalk.com/service/get_auth_info'
  const params = new OapiServiceGetAuthInfoParams();
  params.suite_key = 'suitefcurkdvkc1xxxx';
  params.auth_corpid = 'ding1234';
  const request = new OapiServiceGetAuthInfoRequest()
  request.params = params
  const client = new Client(config)
  try {
    const res = await client.oapiServiceGetAuthInfo(request)
    console.log(res.body)
  } catch (err) {
    console.log(err)
  }
}
test()
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_auth_info");
OapiServiceGetAuthInfoRequest req = new OapiServiceGetAuthInfoRequest();
req.SuiteKey = "key";
req.AuthCorpid = "ding1234";
OapiServiceGetAuthInfoResponse rsp = client.Execute(req);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| auth\_info | AuthInfo |  | 授权信息。 |
| agent | Agent[] |  | 授权的应用信息。 |
| agentid | Number | 835880322 | 授权方应用ID。 |
| logo\_url | String | https://staticXXX.jpg | 授权方应用头像。 |
| appid | Number | 0 | 应用ID。 |
| admin\_list | String[] | ["manager975"] | 对此微应用有管理权限的管理员userid。 |
| agent\_name | String | 小程序DEMO | 授权方应用名字。 |
| auth\_user\_info | AuthUserInfo |  | 授权方管理员信息。 |
| userId | String | manager975 | 管理员的userid。 |
| auth\_corp\_info | AuthCorpInfo |  | 授权方企业信息。 |
| corpid | String | dingbefxxxx | 授权企业的CorpId。 |
| invite\_code | String |  | 邀请码，只有自己邀请的企业才会返回邀请码，可用该邀请码统计不同渠道的拉新，否则值为空字符串。 |
| industry | String |  | 企业所属行业。 |
| corp\_name | String | 小程序体验HTTP | 授权方企业名称。 |
| license\_code | String |  | 序列号。 |
| auth\_channel | String |  | 渠道码。 |
| auth\_channel\_type | String | STAR\_ACTIVIT | 渠道类型。  为了避免渠道码重复，可与渠道码共同确认渠道。可能为空，非空时当前只有满天星类型，值为STAR\_ACTIVITY。 |
| is\_authenticated | Boolean | true | 企业是否认证。 |
| auth\_level | Number | 1 | 企业认证等级：   - **0**：未认证 - **1**：高级认证 - **2**：中级认证 - **3**：初级认证 |
| invite\_url | String | https://wx.dingtalk.com/invite-page/xxx | 企业邀请链接。 |
| corp\_logo\_url | String | https://static-legacy.dingtalk.com/xxx | 企业logo。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| channel\_auth\_info | ChannelAuthInfo |  | 授权的服务窗应用信息列表。 |
| channelAgent | Channelagent[] |  | 授权方应用名字。 |
| agent\_name | String | 小程序DEMO | 授权方应用名字。 |
| agentid | Number | 852381775 | 授权方应用ID。 |
| logo\_url | String | https://static-legacy.dingtalk.com/xxx | 授权方应用头像。 |
| appid | Number | 53642 | 应用appid。 |

### **响应体示例**

```
{
        "errcode":0,
        "auth_user_info":{
                "userId":"manager975"
        },
        "auth_corp_info":{
                "corp_type":0,
                "corpid":"dingbef1744b54241496ee0f45d8xxxx",
                "auth_level":0,
                "auth_channel":"",
                "industry":"",
                "full_corp_name":"小程序体验HTTP",
                "corp_name":"小程序体验HTTP",
                "invite_url":"https://wx.dingtalk.com/invite-page/index.html?bizSource=____source____&corpId=dingbef1744b54241496ee0f45d8e4f7c288&inviterUid=DFAD06727FD38CD894460A2FDF52346D",
                "auth_channel_type":"",
                "invite_code":"",
                "is_authenticated":false,
                "license_code":"",
                "corp_logo_url":""
        },
        "errmsg":"ok",
        "channel_auth_info":{
                "channelAgent":[]
        },
        "auth_info":{
                "agent":[
                        {
                                "agentid":852381775,
                                "agent_name":"小程序DEMO",
                                "logo_url":"https://static-legacy.dingtalk.com/media/lADPDefRxxj6mvVUVg_86_84.jpg",
                                "appid":53642,
                                "admin_list":[
                                        "manager975"
                                ]
                        }
                ]
        },
        "auth_market_info":{}
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
