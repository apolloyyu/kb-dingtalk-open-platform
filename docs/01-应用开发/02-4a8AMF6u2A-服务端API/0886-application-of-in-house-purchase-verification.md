---
title: "应用内购商品核销"
source_url: "https://open.dingtalk.com/document/development/application-of-in-house-purchase-verification"
namespace: "development"
slug: "application-of-in-house-purchase-verification"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 应用内购 > 应用内购商品核销"
doc_id: "ReZ3ovkC4C"
updated_at: "2026-06-08 09:43:55"
---

> Source: https://open.dingtalk.com/document/development/application-of-in-house-purchase-verification
> Path: 应用开发 / 服务端API / 应用市场 > 应用内购 > 应用内购商品核销
> Updated: 2026-06-08 09:43:55

# 应用内购商品核销

通过本接口可在应用内购流程中对订购商品进行核销操作，适用于第三方SaaS服务商根据客户实际使用情况（如开通人数、使用时长等）定期核销已使用的订购额度的业务场景。每次成功调用将记录一条核销流水，确保订单使用状态可追溯。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/appstore/internal/order/consume |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_appstore\_internal-开通应用在应用市场的内购订单的数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用本接口的访问凭证，通过调用[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| biz\_order\_id | Number | 是 | 3131111111 | 内购商品订单号。 |
| request\_id | String | 是 | 1199291922 | 核销请求ID，由ISV生成，用于请求幂等。 |
| quantity | Number | 是 | 12 | 订购商品核销数量。 |
| userid | String | 是 | user123 | 员工在当前企业内的唯一标识，也称staffId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/appstore/internal/order/consume" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=df4dbaeb-dbd2-4454-809f-bbb3b6c9e09b' \
-d 'biz_order_id=3131111111' \
-d 'quantity=12' \
-d 'request_id=1199291922' \
-d 'userid=1111'
```

Java

```
DefaultDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/order/consume");
OapiAppstoreInternalOrderConsumeRequest request = new OapiAppstoreInternalOrderConsumeRequest();
request.setBizOrderId(3131111111L);
request.setQuantity(12L);
request.setRequestId("1199291922");
request.setUserid("user123");
OapiAppstoreInternalOrderConsumeResponse response = client.execute(request, access_token);
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAppstoreInternalOrderConsumeRequest("https://oapi.dingtalk.com/topapi/appstore/internal/order/consume")

req.biz_order_id=3131111111
req.request_id="1199291922"
req.quantity=12
req.userid="1111"
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
$req = new OapiAppstoreInternalOrderConsumeRequest;
$req->setBizOrderId("3131111111");
$req->setRequestId("1199291922");
$req->setQuantity("12");
$req->setUserid("1111");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/appstore/internal/order/consume");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/order/consume");
OapiAppstoreInternalOrderConsumeRequest req = new OapiAppstoreInternalOrderConsumeRequest();
req.BizOrderId = 3131111111L;
req.RequestId = "1199291922";
req.Quantity = 12L;
req.Userid = "1111";
OapiAppstoreInternalOrderConsumeResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":0,
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
