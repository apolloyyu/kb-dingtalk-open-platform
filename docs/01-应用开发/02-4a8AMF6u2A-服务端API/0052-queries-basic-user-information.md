---
title: "获取用户基本信息"
source_url: "https://open.dingtalk.com/document/development/queries-basic-user-information"
namespace: "development"
slug: "queries-basic-user-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 获取用户基本信息"
doc_id: "tFhHW163Vd"
updated_at: "2026-06-08 09:28:27"
---

> Source: https://open.dingtalk.com/document/development/queries-basic-user-information
> Path: 应用开发 / 服务端API / 通讯录管理 > 获取用户基本信息
> Updated: 2026-06-08 09:28:27

# 获取用户基本信息

调用本接口通过免登授权码获取用户基本信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/sns/getuserinfo\_bycode |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-open\_app\_api\_base-获取钉钉开放接口用户访问凭证的基础权限 |

### **查询参数**

| 参数 | **参数类型** | 是否必选 | 描述 |
| --- | --- | --- | --- |
| accessKey | String | 是 | 应用的AppId。 |
| timestamp | String | 是 | 当前时间戳, 单位毫秒。 |
| signature | String | 是 | 用timestamp+"\n"+AppSecret为签名字符串，AppSecret为签名密钥，使用算法HmacSHA256计算的签名值。 |

### **请求体**

| 参数 | 参数类型 | 是否必选 | 描述 |
| --- | --- | --- | --- |
| tmp\_auth\_code | String | 是 | 用户授权给钉钉开放应用的免登授权码，通过调用JSAPI `dd.getAuthCode`获取，参考[免登授权码](../03-Ogu5SlPY4t-客户端JSAPI/0515-mini-program-free-login.md)。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/sns/getuserinfo_bycode" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'tmp_auth_code=abcdef'
```

Java

```
DefaultDingTalkClient  client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/getuserinfo_bycode");
// 如果您使用的SDK中不存在该类，请下载最新的SDK
OapiSnsGetuserinfoBycodeRequest req = new OapiSnsGetuserinfoBycodeRequest();
req.setTmpAuthCode("4a2c5695b78738d495f47b5fee9160cd");
OapiSnsGetuserinfoBycodeResponse response = client.execute(req,"yourAppId","yourAppSecret");
```

Python

```
import dingtalk.api

req = dingtalk.api.OapiSnsGetuserinfoBycodeRequest("https://oapi.dingtalk.com/sns/getuserinfo_bycode")
req.tmp_auth_code = "abcdef"
try:
  resp = req.getResponse("yourAppId", "yourAppSecret")
  print(resp)
except Exception as e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiSnsGetuserinfoBycodeRequest;
$req->setTmpAuthCode("abcdef");
$resp = $c->execute($req,"yourAppId","yourAppSecret", "https://oapi.dingtalk.com/sns/getuserinfo_bycode");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/sns/getuserinfo_bycode");
OapiSnsGetuserinfoBycodeRequest req = new OapiSnsGetuserinfoBycodeRequest();
req.TmpAuthCode = "abcdef";
OapiSnsGetuserinfoBycodeResponse rsp = client.Execute(req, "yourAppId", "yourAppSecret");
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "user_info": {
    "nick": "杨XX",
    "unionid": "Wzh9KbyaCZxxx",
    "openid": "EtiiaAu3Yf9Ruxxx",
    "main_org_auth_high_level": true
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| **错误码** | **说明** |
| --- | --- |
| 853002 | timestamp参数不合法，该参数值与钉钉服务器当前时间相差超过1分钟 |
| 853001 | timestamp参数格式不正确，必须是当前时间的毫秒数 |
| 853003 | accessKey参数不合法，必须是钉钉开放平台存在的appId |
| 853004 | signature参数不正确，与钉钉服务端计算出来的签名不一致，注意该参数传递时必须urlEncode |
