---
title: "查询用户是否参与企业步数排行榜"
source_url: "https://open.dingtalk.com/document/development/check-whether-dingtalk-is-enabled"
namespace: "development"
slug: "check-whether-dingtalk-is-enabled"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 钉钉运动 > 查询用户是否参与企业步数排行榜"
doc_id: "sC1eWsVZg7"
updated_at: "2026-06-01 09:15:27"
---

> Source: https://open.dingtalk.com/document/development/check-whether-dingtalk-is-enabled
> Path: 应用开发 / 服务端API / 企业文化 > 钉钉运动 > 查询用户是否参与企业步数排行榜
> Updated: 2026-06-01 09:15:27

# 查询用户是否参与企业步数排行榜

调用本接口，查询用户是否参与企业的步数排行榜。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_health\_read-钉钉用户运动步数查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager1 | 要查询的用户userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=068d2xxxxd947' \
-d 'userid=manager1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus");
OapiHealthStepinfoGetuserstatusRequest req = new OapiHealthStepinfoGetuserstatusRequest();
req.setUserid("manager1");
OapiHealthStepinfoGetuserstatusResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiHealthStepinfoGetuserstatusRequest("https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus")

req.userid="manager1"
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
$req = new OapiHealthStepinfoGetuserstatusRequest;
$req->setUserid("manager1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/health/stepinfo/getuserstatus");
OapiHealthStepinfoGetuserstatusRequest req = new OapiHealthStepinfoGetuserstatusRequest();
req.Userid = "manager1";
OapiHealthStepinfoGetuserstatusResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 13zgfcfk0m7ia | 请求ID。 |
| status | Boolean | true | 是否开启钉钉运动。   - **true**：已开启 - **false**：未开启 |

### **响应体示例**

```
{
  "errcode": 0,
  "status": true,
  "request_id": "13zgfcfk0m7ia"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
