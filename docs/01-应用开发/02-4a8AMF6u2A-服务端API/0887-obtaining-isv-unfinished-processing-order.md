---
title: "获取未处理的已支付订单"
source_url: "https://open.dingtalk.com/document/development/obtaining-isv-unfinished-processing-order"
namespace: "development"
slug: "obtaining-isv-unfinished-processing-order"
group: "应用开发"
tab: "服务端API"
breadcrumb: "应用市场 > 应用内购 > 获取未处理的已支付订单"
doc_id: "T7YyaWfMgi"
updated_at: "2026-06-08 09:43:56"
---

> Source: https://open.dingtalk.com/document/development/obtaining-isv-unfinished-processing-order
> Path: 应用开发 / 服务端API / 应用市场 > 应用内购 > 获取未处理的已支付订单
> Updated: 2026-06-08 09:43:56

# 获取未处理的已支付订单

通过本接口可获取尚未处理的已支付订单列表，适用于需要在订单完成支付后执行后续业务逻辑，如开通服务的场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-isvapi\_appstore\_internal-开通应用在应用市场的内购订单的数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可调用[获取第三方企业应用的suite\_access\_token](1447-obtain-application-suite-ticket.md)接口获得。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| item\_code | String | 否 | DD\_I\_111 | 商品规格码。 |
| page | Number | 是 | 1 | 分页查询页码，起始页码为1。 |
| page\_size | Number | 是 | 10 | 分页查询每页大小，最大限制100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d00a9a1e-f3dd-4c83-b3c4-edd91704593a' \
-d 'item_code=DD_I_111' \
-d 'page=1' \
-d 'page_size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list");
OapiAppstoreInternalUnfinishedorderListRequest req = new OapiAppstoreInternalUnfinishedorderListRequest();
req.setItemCode("DD_I_111");
req.setPage(1L);
req.setPageSize(10L);
OapiAppstoreInternalUnfinishedorderListResponse rsp = client.execute(req, suite_access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAppstoreInternalUnfinishedorderListRequest("https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list")

req.item_code="DD_I_111"
req.page=1
req.page_size=10
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
$req = new OapiAppstoreInternalUnfinishedorderListRequest;
$req->setItemCode("DD_I_111");
$req->setPage("1");
$req->setPageSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/appstore/internal/unfinishedorder/list");
OapiAppstoreInternalUnfinishedorderListRequest req = new OapiAppstoreInternalUnfinishedorderListRequest();
req.ItemCode = "DD_I_111";
req.Page = 1L;
req.PageSize = 10L;
OapiAppstoreInternalUnfinishedorderListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageModel |  | 查询结果。 |
| total | Number | 100 | 总记录数。 |
| items | InAppGoodsOrderVO[] | items | 订单信息列表。 |
| create\_timestamp | Number | 1553575800111 | 订单创建时间戳。 |
| paid\_timestamp | Number | 1553575800333 | 订单支付时间戳。 |
| quantity | Number | 12 | 订购数量，周期型商品该字段为空。 |
| status | Number | 3 | 订单状态：   - 3：已支付状态 |
| total\_actual\_pay\_fee | Number | 888 | 实际支付总金额，CNY(分)。 |
| item\_code | String | DD\_I\_111 | 内购商品规格码。 |
| corp\_id | String | ding2323klsd2 | 购买商品的企业开放ID。 |
| biz\_order\_id | Number | 100000001 | 订单号。 |
| goods\_code | String | DD\_GOODS-199 | 商品码。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result": {
    "total": 100,
    "items": [
      {
        "item_code": "DD_I_111",
        "quantity": 12,
        "create_timestamp": 1553575800111,
        "goods_code": "DD_GOODS-199",
        "paid_timestamp": 1553575800333,
        "total_actual_pay_fee": 888,
        "corp_id": "ding2323xxxx",
        "biz_order_id": 100000001,
        "status": 3
      }
    ]
  },
  "errcode": 0,
  "errmsg": "success"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
