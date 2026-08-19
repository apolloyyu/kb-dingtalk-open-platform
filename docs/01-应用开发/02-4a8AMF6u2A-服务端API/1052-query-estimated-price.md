---
title: "查询预估价"
source_url: "https://open.dingtalk.com/document/development/query-estimated-price"
namespace: "development"
slug: "query-estimated-price"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 查询预估价"
doc_id: "kASRCCipw6"
updated_at: "2026-06-03 09:51:48"
---

> Source: https://open.dingtalk.com/document/development/query-estimated-price
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 查询预估价
> Updated: 2026-06-03 09:51:48

# 查询预估价

通过本接口，企业可查询员工在商旅出行前的机票、酒店或火车行程预估费用，用于预算控制、差标合规性判断及审批流程中的费用决策支持。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query |
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
| req | OpenApiIntervalPriceRq | 是 |  | 请求对象，封装具体的查询条件。 |
| corpid | String | 是 | ding14xxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| from\_where | String | 是 | 杭州 | 出发地点名称。 |
| userid | String | 是 | user123 | 发起请求的用户userid。 |
| itinerary\_id | String | 否 | 1245 | 行程ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| start\_time | Date | 是 | 2020-11-11 00:00:00 | 出发时间，格式为`yyyy-MM-dd HH:mm:ss`。 |
| end\_time | Date | 是 | 2020-12-12 00:00:00 | 返程时间，格式为`yyyy-MM-dd HH:mm:ss`。 |
| to\_where | String | 是 | 上海 | 目的地名称。 |
| category | String | 是 | flight | 类目：   - **flight**：机票 - **hotel**：酒店 - **train**：火车 |
| query\_key | String | 否 | abc | 根据key查询。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9ef701xxxx963eedb' \
-d 'req=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query");
OapiAlitripBtripPriceQueryRequest req = new OapiAlitripBtripPriceQueryRequest();
OpenApiIntervalPriceRq obj1 = new OpenApiIntervalPriceRq();
obj1.setCorpid("corpid");
obj1.setFromWhere("杭州");
obj1.setUserid("ding12345");
obj1.setItineraryId("1245");
obj1.setStartTime(StringUtils.parseDateTime("2020-11-11 00:00:00"));
obj1.setEndTime(StringUtils.parseDateTime("2020-12-12 00:00:00"));
obj1.setToWhere("上海");
obj1.setCategory("flight");
obj1.setQueryKey("abc");
req.setReq(obj1);
OapiAlitripBtripPriceQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripPriceQueryRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query")

req.req=""
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
$req = new OapiAlitripBtripPriceQueryRequest;
$req = new OpenApiIntervalPriceRq;
$req->corpid="corpid";
$req->from_where="杭州";
$req->userid="ding12345";
$req->itinerary_id="1245";
$req->start_time="2020-11-11 00:00:00";
$req->end_time="2020-12-12 00:00:00";
$req->to_where="上海";
$req->category="flight";
$req->query_key="abc";
$req->setReq($req);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/price/query");
OapiAlitripBtripPriceQueryRequest req = new OapiAlitripBtripPriceQueryRequest();
OapiAlitripBtripPriceQueryRequest.OpenApiIntervalPriceRqDomain obj1 = new OapiAlitripBtripPriceQueryRequest.OpenApiIntervalPriceRqDomain();
obj1.Corpid = "corpid";
obj1.FromWhere = "杭州";
obj1.Userid = "ding12345";
obj1.ItineraryId = "1245";
obj1.StartTime = DateTime.Parse(2020-11-11 00:00:00");
obj1.EndTime = DateTime.Parse(2020-12-12 00:00:00");
obj1.ToWhere = "上海";
obj1.Category = "flight";
obj1.QueryKey = "abc";
req.Req_ = obj1;
OapiAlitripBtripPriceQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| success | Boolean | true | 操作是否成功。 |
| module | Module |  | 预估价信息。 |
| hotel\_fee\_detail | HotelFeeDetail[] |  | 酒店差标。 |
| criterion | Number | 30000 | 费用。 |
| city | String | 杭州 | 城市。 |
| traffic\_fee | TrafficFee |  | 费用。 |
| btrip\_routes | BtripRoutes[] | [] | 行程费用。 |
| most\_expensive | MostExpensive | {} | 最高价。 |
| vehicle\_no | String | G7391 | 班次。 |
| seat\_grade | String | 商务座 | 坐席级别。 |
| dep\_time | String | 18:18 | 出发时间。 |
| fee | Number | 23350 | 费用。 |
| arr\_time | String | 19:39 | 到达时间。 |
| success | Boolean | true | 查询是否成功。 |
| cheapest | Cheapest |  | 最低价。 |
| vehicle\_no | String | K1185 | 班次。 |
| seat\_grade | String | 硬座 | 坐席级别。 |
| dep\_time | String | 08:51 | 出发时间。 |
| fee | Number | 2450 | 费用。 |
| arr\_time | String | 10:46 | 到达时间。 |
| dest\_city | String | 杭州 | 目的地。 |
| org\_city | String | 上海 | 出发地。 |
| err\_msg | String | ok | 错误信息。 |
| dep\_date | Date | 2020-12-12 00:00:00 | 出发时间。 |
| success | Boolean | true | 是否成功。 |
| err\_msg | String | demo | 错误信息。 |
| query\_key | String | abc | 异步查询key。  需要client再次尝试请求。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result":{
    "errcode":"0",
    "success":"true",
    "module":{
      "traffic_fee":{
        "btrip_routes":{
          "dest_city":"杭州",
          "org_city":"上海",
          "success":"true",
          "cheapest":{
            "seat_grade":"硬座",
            "vehicle_no":"K1185",
            "dep_time":"08:51",
            "fee":"2450",
            "arr_time":"10:46"
          },
          "err_msg":"demo",
          "most_expensive":{
            "seat_grade":"商务座",
            "vehicle_no":"G7391",
            "dep_time":"18:18",
            "fee":"23350",
            "arr_time":"19:39"
          },
          "dep_date":"2020-12-12 00:00:00"
        },
        "success":"true",
        "err_msg":"demo"
      },
      "query_key":"abc",
      "hotel_fee_detail":{
        "criterion":"30000",
        "city":"杭州"
      }
    },
    "errmsg":"demo"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
