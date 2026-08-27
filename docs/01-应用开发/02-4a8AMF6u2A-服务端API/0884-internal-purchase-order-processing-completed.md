---
title: "内购商品订单处理完成"
source_url: "https://open.dingtalk.com/document/development/internal-purchase-order-processing-completed"
namespace: "development"
slug: "internal-purchase-order-processing-completed"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 应用内购 > 内购商品订单处理完成"
doc_id: "xavlQIbzA5"
updated_at: "2026-06-08 09:43:53"
---

> Source: https://open.dingtalk.com/document/development/internal-purchase-order-processing-completed
> Path: 应用开发 / 服务端API / 应用市场 > 应用内购 > 内购商品订单处理完成
> Updated: 2026-06-08 09:43:53

# 内购商品订单处理完成

调用本接口完成内购商品订单处理。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/appstore/internal/order/finish |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_appstore\_internal-开通应用在应用市场的内购订单的数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用本接口的访问凭证，通过调用获[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| biz\_order\_id | Number | 是 | 313111111111111 | 内购订单号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/appstore/internal/order/finish" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=4727f623-9f4d-4b7f-8ead-399ffcfe5e3f' \
-d 'biz_order_id=313111111111111'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/order/finish");
OapiAppstoreInternalOrderFinishRequest req = new OapiAppstoreInternalOrderFinishRequest();
req.setBizOrderId(313111111111111L);
OapiAppstoreInternalOrderFinishResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAppstoreInternalOrderFinishRequest("https://oapi.dingtalk.com/topapi/appstore/internal/order/finish")

req.biz_order_id=313111111111111
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
$req = new OapiAppstoreInternalOrderFinishRequest;
$req->setBizOrderId("313111111111111");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/appstore/internal/order/finish");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/order/finish");
OapiAppstoreInternalOrderFinishRequest req = new OapiAppstoreInternalOrderFinishRequest();
req.BizOrderId = 313111111111111L;
OapiAppstoreInternalOrderFinishResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":"0",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
