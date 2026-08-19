---
title: "获取商旅访问地址"
source_url: "https://open.dingtalk.com/document/development/obtain-business-travel-access-addresses"
namespace: "development"
slug: "obtain-business-travel-access-addresses"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 阿里商旅跳转链接 > 获取商旅访问地址"
doc_id: "rwmpVbNl1g"
updated_at: "2026-06-08 09:47:20"
---

> Source: https://open.dingtalk.com/document/development/obtain-business-travel-access-addresses
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 阿里商旅跳转链接 > 获取商旅访问地址
> Updated: 2026-06-08 09:47:20

# 获取商旅访问地址

调用本接口获取各个场景预订访问地址，以及我的订单地址。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | OpenApiJumpInfoRq | 否 |  | 请求对象。 |
| corpid | String | 是 | ding23423 | 企业的corpid。 |
| userid | String | 是 | 34234 | 用户userid。 |
| type | Number | 是 | 1 | 类目类型：   - 1：机票 - 2：火车票 - 3：酒店 - 4：用车 |
| action\_type | Number | 是 | 1 | 操作类型：   - 1：预订 - 2：我的订单列表 - 3：商旅管理后台，如果需要获取该场景的地址，只需提供corpid，userid - 4：商旅h5主页 |
| itinerary\_id | String | 否 | 12345 | 第三方行程ID。  存在代表通过审批单预订，不存在代表特殊场景：普通员工是预览，特殊授权人和代订人是免审批预订场景。 |
| phone | String | 否 | 13XXXXXXXXX | 员工第一次使用用车需要手机号，与司机联系。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3867dfxxxxc47f8bda' \
-d 'request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get");
OapiAlitripBtripAddressGetRequest req = new OapiAlitripBtripAddressGetRequest();
OpenApiJumpInfoRq obj1 = new OpenApiJumpInfoRq();
obj1.setCorpid("ding23423");
obj1.setUserid("34234");
obj1.setType(1L);
obj1.setActionType(1L);
obj1.setItineraryId("12345");
obj1.setPhone("13XXXXXXXXX");
req.setRequest(obj1);
OapiAlitripBtripAddressGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripAddressGetRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get")

req.request=""
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
$req = new OapiAlitripBtripAddressGetRequest;
$request = new OpenApiJumpInfoRq;
$request->corpid="ding23423";
$request->userid="34234";
$request->type="1";
$request->action_type="1";
$request->itinerary_id="12345";
$request->phone="13XXXXXXXXX";
$req->setRequest($request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/address/get");
OapiAlitripBtripAddressGetRequest req = new OapiAlitripBtripAddressGetRequest();
OapiAlitripBtripAddressGetRequest.OpenApiJumpInfoRqDomain obj1 = new OapiAlitripBtripAddressGetRequest.OpenApiJumpInfoRqDomain();
obj1.Corpid = "ding23423";
obj1.Userid = "34234";
obj1.Type = 1L;
obj1.ActionType = 1L;
obj1.ItineraryId = "12345";
obj1.Phone = "13XXXXXXXXX";
req.Request_ = obj1;
OapiAlitripBtripAddressGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| result | OpenApiJumpInfoRs |  | 结果对象。 |
| url | String | https://xxxx | 访问地址。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "url": "https://trip-hisv.alitrip.com/ding/xxxx"
  },
  "success": true,
  "request_id": "ovsevlpetuw8"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
