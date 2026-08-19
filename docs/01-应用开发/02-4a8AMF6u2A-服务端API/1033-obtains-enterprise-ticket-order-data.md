---
title: "获取企业机票订单数据"
source_url: "https://open.dingtalk.com/document/development/obtains-enterprise-ticket-order-data"
namespace: "development"
slug: "obtains-enterprise-ticket-order-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取企业机票订单数据"
doc_id: "6RmT8riD9v"
updated_at: "2026-06-08 09:47:15"
---

> Source: https://open.dingtalk.com/document/development/obtains-enterprise-ticket-order-data
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取企业机票订单数据
> Updated: 2026-06-08 09:47:15

# 获取企业机票订单数据

获取企业差旅中的机票订单数据，支持按时间范围、用户、部门、申请单等条件查询。该接口适用于企业财务对账、报销审核、行程管理等业务场景，尤其适合使用阿里商旅进行统一差旅管控的中大型企业。建议在每日定时同步或用户提交报销时调用，以确保数据一致性。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search |
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
| rq | Object | 是 |  | 请求对象，封装所有查询条件。 |
| start\_time | String | 否 | 2017-05-01 00:00:00 | 查询的开始时间，格式为`yyyy-MM-dd HH:mm:ss`。 |
| apply\_id | Number | 否 | 12345 | 商旅申请单id，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| page | Number | 否 | 1 | 当前页码，从1开始计数。 |
| userid | String | 否 | user1 | 用户ID，用于筛选指定用户的订单。 |
| page\_size | Number | 否 | 10 | 每页数据量，默认10，最高50。 |
| deptid | String | 否 | dept1 | 企业ID，标识目标企业数据范围。 |
| end\_time | String | 否 | 2017-05-01 00:00:00 | 查询的结束时间，格式为`yyyy-MM-dd HH:mm:ss`。 |
| corpid | String | 是 | corp1 | 企业id。 |
| update\_end\_time | String | 否 | 2017-05-01 00:00:00 | 更新结束时间。 |
| update\_start\_time | String | 否 | 2017-05-01 00:00:00 | 更新开始时间。 |
| all\_apply | Boolean | 否 | true | false：仅搜索未报销的申请单。 |
| thirdpart\_apply\_id | String | 否 | 123 | 第三方申请单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=69c026xxxx401f03dc7' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search");
OapiAlitripBtripFlightOrderSearchRequest req = new OapiAlitripBtripFlightOrderSearchRequest();
OpenSearchRq obj1 = new OpenSearchRq();
obj1.setStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setApplyId(12345L);
obj1.setPage(1L);
obj1.setUserid("user1");
obj1.setPageSize(10L);
obj1.setDeptid("dept1");
obj1.setEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setCorpid("corp1");
obj1.setUpdateEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setUpdateStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setAllApply(true);
obj1.setThirdpartApplyId("123");
req.setRq(obj1);
OapiAlitripBtripFlightOrderSearchResponse rsp = client.execute(req, "74c17e625cd83b628847837c7b6ac144");
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripFlightOrderSearchRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search")

req.rq=""
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
$req = new OapiAlitripBtripFlightOrderSearchRequest;
$rq = new OpenSearchRq;
$rq->start_time="2017-05-01 00:00:00";
$rq->apply_id="12345";
$rq->page="1";
$rq->userid="user1";
$rq->page_size="10";
$rq->deptid="dept1";
$rq->end_time="2017-05-01 00:00:00";
$rq->corpid="corp1";
$rq->update_end_time="2017-05-01 00:00:00";
$rq->update_start_time="2017-05-01 00:00:00";
$rq->all_apply="true";
$rq->thirdpart_apply_id="123";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/order/search");
OapiAlitripBtripFlightOrderSearchRequest req = new OapiAlitripBtripFlightOrderSearchRequest();
OapiAlitripBtripFlightOrderSearchRequest.OpenSearchRqDomain obj1 = new OapiAlitripBtripFlightOrderSearchRequest.OpenSearchRqDomain();
obj1.StartTime = DateTime.Parse(2017-05-01 00:00:00");
obj1.ApplyId = 12345L;
obj1.Page = 1L;
obj1.Userid = "user1";
obj1.PageSize = 10L;
obj1.Deptid = "dept1";
obj1.EndTime = DateTime.Parse(2017-05-01 00:00:00");
obj1.Corpid = "corp1";
obj1.UpdateEndTime = DateTime.Parse(2017-05-01 00:00:00");
obj1.UpdateStartTime = DateTime.Parse(2017-05-01 00:00:00");
obj1.AllApply = true;
obj1.ThirdpartApplyId = "123";
req.Rq_ = obj1;
OapiAlitripBtripFlightOrderSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 成功标识。 |
| errcode | Number | 0 | 错误码。 |
| errmsg | String | 成本 | 错误信息。 |
| flight\_order\_list | Object[] | module | 机票列表。 |
| id | Number | 1234 | 机票订单id。 |
| gmt\_modified | String | 2017-05-01 00:00:00 | 更新时间。 |
| userid | String | user1 | 用户id。 |
| corp\_name | String | 阿里巴巴 | 企业名称。 |
| corpid | String | corp1 | 企业id。 |
| gmt\_create | String | 2017-05-01 00:00:00 | 创建时间。 |
| user\_name | String | 张三 | 用户名称。 |
| deptid | String | dept1 | 部门id。 |
| dept\_name | String | 淘宝 | 部门名称。 |
| apply\_id | String | 12345 | 商旅申请单id。 |
| contact\_name | String | 张三 | 联系人。 |
| dep\_city | String | 北京 | 出发城市。 |
| arr\_city | String | 上海 | 到达城市。 |
| dep\_date | String | 2017-05-01 00:00:00 | 出发日期。 |
| ret\_date | String | 2017-05-01 00:00:00 | 到达日期。 |
| trip\_type | Number | 0 | 行程类型：   - 0：单程 - 1：往返 - 2：中转 |
| passenger\_count | Number | 1 | 乘机人数量。 |
| cabin\_class | String | 舱位类型 | 舱位类型。 |
| status | Number | 1 | 订单状态：   - 0：待支付 - 1：出票中 - 2：已关闭 - 3：有改签单 - 4：有退票单 - 5：出票成功 - 6：退票申请中 - 7：改签申请中 |
| discount | String | 30.12% | 折扣。。 |
| flight\_no | String | A123456 | 航班号。 |
| passenger\_name | String | 张三,李四 | 乘机人，多个用‘,’分割。 |
| dep\_airport | String | 萧山机场 | 出发机场。 |
| arr\_airport | String | 白云机场 | 到达机场。 |
| invoice | Object | invoice | 发票信息对象。 |
| id | Number | 123 | 商旅发票id。 |
| title | String | 阿里巴巴 | 发票抬头。 |
| cost\_center | Object | costCenter | 成本中心对象。 |
| id | Number | 1234 | 商旅成本中心id。 |
| corpid | String | corp1 | 企业id。 |
| number | String | abc | 成本中心编号。 |
| name | String | 阿里巴巴 | 成本中心名称。 |
| price\_info\_list | Object[] | priceInfoList | 价目信息。 |
| price | String | 100.0 | 价格。 |
| type | Number | 1 | 资金流向：   - 1：支出 - 2：收入 |
| category | String | 机票费 | 交易类目。 |
| pay\_type | Number | 1 | 结算方式：   - 1：个人现付 - 2：企业现付 - 4：企业月结 - 8：企业预存 |
| gmt\_create | String | 2017-05-01 00:00:00 | 流水创建时间。 |
| passenger\_name | String | 张三,李四 | 乘机人，多个用‘,’分割 |
| tradeId | String | 787877878666000 | 流水单号。 |
| ticket\_no | String | abc-12138 | 改签票号。 |
| original\_ticket\_no | String | abc-123456 | 改签前的票号。 |
| changeFlightNo | String | BJ13142 | 改签航班号。 |
| discount | String | 23% | 改签折扣。 |
| startTime | String | 2021-07-11 | 改签航班起飞时间。 |
| endTime | String | 2021-07-11 | 改签航班到达时间。 |
| person\_price | String | 100.0 | 个人支付金额。 |
| insureInfo\_list | Object[] | insureInfoList | 保险信息。 |
| insure\_no | String | abcdefg | 保单号。 |
| status | Number | 1 | 状态：   - 1：已出保 - 2：已退保 |
| name | String | 张三 | 乘机人(保险人)姓名。 |
| thirdpart\_itinerary\_id | String | abfefgg | 第三方行程id。 |
| user\_affiliate\_list | Object[] | 张三,李四 | 出行人列表。 |
| userid | String | 123 | 出行人ID。 |
| user\_name | String | 张三 | 出行人名称。 |
| thirdpart\_apply\_id | String | 123 | 第三方申请单ID。 |
| btrip\_title | String | 出差 | 申请单名称。 |
| project\_id | Number | 1 | 项目id。 |
| project\_code | String | abc | 项目code。 |
| project\_title | String | abc | 项目名称。 |
| third\_part\_project\_id | String |  | 第三方项目id。 |
| page\_info | Object | module | 分页相关信息。 |
| page | Number | 1 | 当前页。。 |
| page\_size | Number | 10 | 每页大小。 |
| total\_number | Number | 100 | 总记录数。 |

### **响应体示例**

```
{
  "errcode":"0",
  "flight_order_list":{
    "gmt_create":"2017-05-01 00:00:00",
    "third_part_project_id":"",
    "arr_city":"上海",
    "corpid":"corp1",
    "user_name":"张三",
    "deptid":"dept1",
    "dep_city":"北京",
    "passenger_count":"1",
    "discount":"30.12%",
    "gmt_modified":"2017-05-01 00:00:00",
    "userid":"user1",
    "dep_date":"2017-05-01 00:00:00",
    "price_info_list":{
      "gmt_create":"2017-05-01 00:00:00",
      "discount":"23%",
      "type":"1",
      "passenger_name":"张三,李四",
      "person_price":"100.0",
      "original_ticket_no":"abc-123456",
      "price":"100.0",
      "ticket_no":"abc-12138",
      "pay_type":"1",
      "startTime":"2021-07-11",
      "endTime":"2021-07-11",
      "category":"机票费",
      "changeFlightNo":"BJ13142",
      "tradeId":"787877878666000"
    },
    "trip_type":"0",
    "flight_no":"A123456",
    "thirdpart_apply_id":"123",
    "project_id":"1",
    "apply_id":"12345",
    "id":"1234",
    "user_affiliate_list":{
      "user_name":"张三",
      "userid":"123"
    },
    "thirdpart_itinerary_id":"abfefgg",
    "cabin_class":"舱位类型",
    "contact_name":"张三",
    "arr_airport":"白云机场",
    "dept_name":"淘宝",
    "project_code":"abc",
    "project_title":"abc",
    "corp_name":"阿里巴巴",
    "passenger_name":"张三,李四",
    "dep_airport":"萧山机场",
    "btrip_title":"出差",
    "cost_center":{
      "number":"abc",
      "corpid":"corp1",
      "name":"阿里巴巴",
      "id":"1234"
    },
    "insureInfo_list":{
      "name":"张三",
      "insure_no":"abcdefg",
      "status":"1"
    },
    "ret_date":"2017-05-01 00:00:00",
    "invoice":{
      "id":"123",
      "title":"阿里巴巴"
    },
    "status":"1"
  },
  "success":"true",
  "page_info":{
    "total_number":"100",
    "page":"1",
    "page_size":"10"
  },
  "errmsg":"成本"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
