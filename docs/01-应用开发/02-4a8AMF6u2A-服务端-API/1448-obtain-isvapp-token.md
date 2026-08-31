---
title: "服务商获取第三方应用授权企业的access_token"
source_url: "https://open.dingtalk.com/document/development/obtain-isvapp-token"
namespace: "development"
slug: "obtain-isvapp-token"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 获取访问凭证 > 服务商获取第三方应用授权企业的access_token"
doc_id: "NrZCOOaMBH"
updated_at: "2026-08-25 09:36:30"
---

> Source: https://open.dingtalk.com/document/development/obtain-isvapp-token
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 获取访问凭证 > 服务商获取第三方应用授权企业的access_token
> Updated: 2026-08-25 09:36:30

# 服务商获取第三方应用授权企业的access\_token

产品方案商可通过此接口获取授权企业的access\_token。调用服务端API获取应用资源时，需要通过access\_token来鉴权调用者身份进行授权。

## **接口调用说明**

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版 [获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口，已接入用户不受影响。

在使用access\_token时，请注意：

- access\_token的有效期为7200秒（2小时），有效期内重复获取会返回新的access\_token。
- 开发者需要缓存access\_token，用于后续接口的调用。因为每个应用的access\_token是彼此独立的，所以进行缓存时需要区分应用来进行存储。
- 不能频繁调用gettoken接口，否则会受到频率拦截。

推荐使用SDK调用本接口：

- HTTP调用方式必须设置**signature**参数，钉钉会对请求进行签名验证，以保证安全。签名计算方式，请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。
- SDK调用方式无需自行进行签名计算，钉钉SDK已自带签名功能。**推荐**使用钉钉提供的SDK进行调用，SDK下载地址参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/service/get\_corp\_token |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用（委托产品方案商）appType-第三方企业应用 |
| 权限要求 | 无 |

### **请求体**

#### **SDK请求**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| accessKey | String | 是 | suitexxxxyun | - 如果是定制应用，输入定制应用的CustomKey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 - 如果是第三方企业应用，输入第三方企业应用的SuiteKey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| accessSecret | String | 是 | \_FPxxxxj3e | - 如果是定制应用，输入定制应用的CustomSecret，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 - 如果是第三方企业应用，输入第三方企业应用的SuiteSecret，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| suiteTicket | String | 是 | test | 钉钉推送的suiteTicket。   - 定制应用可随意填写。 - 第三方企业应用使用钉钉开放平台向应用推送的suite\_ticket，请参考[数据格式biz\_type=2](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-dqx-ue5-0f8)。   **[!NOTE]**  suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。 |
| auth\_corpid | String | 是 | ding123456 | 授权企业的CorpId。   - 定制应用可以在[钉钉开发者后台定制应用页面](https://open-dev.dingtalk.com/#/list-custom)查看。 - 第三方企业应用使用钉钉开放平台向应用推送的授权企业的corpid，请参考[数据格式biz\_type=4](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-ca8-x7n-gdw)。 |

#### **HTTP请求**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| accessKey | String | 是 | suitexxxxyun | - 如果是定制应用，输入定制应用的CustomKey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 - 如果是第三方企业应用，输入第三方企业应用的SuiteKey，可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/appMgr/custom/h5/951603110/1)的应用详情页获取。 |
| timestamp | Number | 是 | 1527130370219 | 当前时间戳，单位是毫秒。 |
| suiteTicket | String | 是 | test | 钉钉推送的suiteTicket。   - 定制应用可随意填写。 - 第三方企业应用使用钉钉开放平台向应用推送的suite\_ticket，请参考[数据格式biz\_type=2](../04-LFcRvVD08N-事件订阅/0005-development-data-format-help.md#section-dqx-ue5-0f8)。   **[!NOTE]**  suiteTicket是有有效期的，调用接口要确保从推送源中读取最新推送的suiteTicket值，一般五个小时推送一次。 |
| signature | String | 是 |  | 签名，签名计算方式请参考[第三方访问接口的签名计算方法](1429-the-signature-calculation-method-of-the-third-party-access-interface.md)。 |
| auth\_corpid | String | 是 | ding123456 | 授权企业的CorpId。  1，定制应用可以在[钉钉开发者后台定制应用页面](https://open-dev.dingtalk.com/#/list-custom)查看。  2，授权开通第三方企业应用的授权企业corpid   - 如果是微应用，在微应用首页地址后面拼接?corpId=$CORPID$，再在页面内js解析获取当前企业corpid（仅支持工作台进入应用时使用） - 如果是小程序，在小程序app.js的onLaunch方法内会自动获取当前企业corpId，只需要解析即可获取 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/service/get_corp_token" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'accessKey=suitexxxxyun' \
-d 'accessSecret=_FPxxxxj3e' \
-d 'suiteTicket=test' \
-d 'auth_corpid=ding1234' \
```

Java

```
DefaultDingTalkClient client= new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_corp_token");
OapiServiceGetCorpTokenRequest req= new OapiServiceGetCorpTokenRequest();
req.setAuthCorpid("dingc365fcxxxx");
OapiServiceGetCorpTokenResponse execute= client.execute(req,"accessKey","accessSecret","suiteTicket");
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceGetCorpTokenRequest("https://oapi.dingtalk.com/service/get_corp_token")

req.auth_corpid="ding1234"
req.accessKey="suitexxxxyun"
req.accessSecret="_FPxxxxj3e"
req.suiteTicket="test"
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
$req = new OapiServiceGetCorpTokenRequest;
$req->setAuthCorpid("ding1234");
$req->setAccessKey("suitexxxxyun");
$req->setAccessSecret("_FPxxxxj3e");
$req->setSuiteTicket("test");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/service/get_corp_token");
```

Node.js

```
TopClient = require('./topClient').TopClient;
var client = new TopClient({
  'appkey': 'appkey',
  'appsecret': 'secret',
  'url': 'http://gw.api.taobao.com/router/rest'
});

client.execute('dingtalk.oapi.service.get_corp_token', {
  'auth_corpid':'ding1234',
  'accessKey':'suitexxxxyun',
  'accessSecret':'_FPxxxxj3e',
  'suiteTicket':'test',
}, function(error, response) {
  if (!error) console.log(response);
  else console.log(error);
})
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/service/get_corp_token");
OapiServiceGetCorpTokenRequest req = new OapiServiceGetCorpTokenRequest();
req.AuthCorpid = "ding1234";
OapiServiceGetCorpTokenResponse rsp = client.Execute(req,"accessKey","accessSecret","suiteTicket");
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| expires\_in | Number | 7200 | 授权企业的access\_token超时时间，单位秒。 |
| access\_token | String | 1cc1bb3xxxx | 授权企业的access\_token。 |
| errmsg | String | ok | 返回码的描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "access_token":"1cc1bb3xxxx",
  "errcode":0,
  "errmsg":"ok",
  "expires_in":7200
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
