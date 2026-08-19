---
title: "获取内购订单信息"
source_url: "https://open.dingtalk.com/document/development/obtain-information-about-internal-purchase-orders"
namespace: "development"
slug: "obtain-information-about-internal-purchase-orders"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 应用内购 > 获取内购订单信息"
doc_id: "364iIXP90d"
updated_at: "2026-06-08 09:43:54"
---

> Source: https://open.dingtalk.com/document/development/obtain-information-about-internal-purchase-orders
> Path: 应用开发 / 服务端API / 应用市场 > 应用内购 > 获取内购订单信息
> Updated: 2026-06-08 09:43:54

# 获取内购订单信息

调用本接口可获取企业内购商品的订单详情，包括订单状态、支付信息、服务周期及购买企业等数据。

## **接口调用说明**

非内购订单请不要使用该接口。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/appstore/internal/order/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_appstore\_internal-开通应用在应用市场的内购订单的数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用本接口的访问凭证，通过调用获[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| biz\_order\_id | Number | 是 | 313111111111 | 内购商品订单号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/appstore/internal/order/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=6b417f7a-8513-424b-a024-dc63bcb94071' \
-d 'biz_order_id=313111111111'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/order/get");
OapiAppstoreInternalOrderGetRequest req = new OapiAppstoreInternalOrderGetRequest();
req.setBizOrderId(313111111111L);
OapiAppstoreInternalOrderGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAppstoreInternalOrderGetRequest("https://oapi.dingtalk.com/topapi/appstore/internal/order/get")

req.biz_order_id=313111111111
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
$req = new OapiAppstoreInternalOrderGetRequest;
$req->setBizOrderId("313111111111");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/appstore/internal/order/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/order/get");
OapiAppstoreInternalOrderGetRequest req = new OapiAppstoreInternalOrderGetRequest();
req.BizOrderId = 313111111111L;
OapiAppstoreInternalOrderGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | InAppGoodsOrderVo |  | 订单信息。 |
| create\_timestamp | Number | 1553576399000 | 订单创建时间。 |
| paid\_timestamp | Number | 1553576399000 | 订单支付时间。 |
| quantity | Number | 12 | 订购数量，周期型商品此字段为空。 |
| status | Number | 3 | 订单状态：   - 0：订单关闭 - 3：订单支付 - 4：订单创建 |
| total\_actual\_pay\_fee | Number | 121212 | 实际支付总金额，单位为分(RMB)。 |
| item\_code | String | DD\_I\_1111 | 内购商品规格码。 |
| corp\_id | String | ding392039212lak2 | 购买商品的企业开放ID。 |
| biz\_order\_id | Number | 3131111111 | 内购商品订单号。 |
| end\_timestamp | Number | 1553576399000 | 订购的服务结束时间。 |
| start\_timestamp | Number | 1553576399000 | 订购的服务开始时间。 |
| goods\_code | String | DD\_GOODS-11 | 内购商品码。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "result":{
    "item_code":"DD_I_1111",
    "quantity":"12",
    "create_timestamp":"1553576399000",
    "end_timestamp":"1553576399000",
    "start_timestamp":"1553576399000",
    "goods_code":"DD_GOODS-11",
    "paid_timestamp":"1553576399000",
    "total_actual_pay_fee":"121212",
    "corp_id":"ding392039212lak2",
    "biz_order_id":"3131111111",
    "status":"3"
  },
  "errcode":"0",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
