---
title: "获取企业商旅酒店订单数据"
source_url: "https://open.dingtalk.com/document/development/enterprises-obtain-order-data-for-business-hotels"
namespace: "development"
slug: "enterprises-obtain-order-data-for-business-hotels"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取企业商旅酒店订单数据"
doc_id: "5NAxVFnddu"
updated_at: "2026-06-08 09:47:16"
---

> Source: https://open.dingtalk.com/document/development/enterprises-obtain-order-data-for-business-hotels
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 订单管理 > 获取企业商旅酒店订单数据
> Updated: 2026-06-08 09:47:16

# 获取企业商旅酒店订单数据

通过此接口获取企业商旅中的酒店订单数据，支持按时间、部门、用户、审批单等条件进行查询，适用于企业差旅管理系统中对酒店预订记录的统计分析、财务对账和报销处理等场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search |
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
| rq | OpenSearchRq | 是 |  | 请求对象，封装查询条件。 |
| start\_time | Date | 否 | 2017-05-01 00:00:00 | 查询起始时间，格式为`yyyy-MM-dd HH:mm:ss`。 |
| apply\_id | Number | 否 | 12345 | 商旅审批单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| page | Number | 否 | 1 | 分页页码，从第1页开始。 |
| userid | String | 否 | user1 | 用户的userid，表示要查询的员工身份标识。 |
| page\_size | Number | 否 | 10 | 每页数量，默认10，最大50 |
| deptid | String | 否 | dept1 | 部门ID。 |
| end\_time | Date | 否 | 2017-05-01 00:00:00 | 查询结束时间，格式为`yyyy-MM-dd HH:mm:ss`。 |
| corpid | String | 是 | corp1 | 企业的corpid，用于唯一标识目标企业。 |
| update\_end\_time | Date | 否 | 2017-05-01 00:00:00 | 更新开始时间。 |
| update\_start\_time | Date | 否 | 2017-05-01 00:00:00 | 更新结束时间。 |
| all\_apply | Boolean | 否 | true | **false**：搜索未报销订单。 |
| thirdpart\_apply\_id | String | 否 | 123 | 第三方申请单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=559ae2xxxx835b082' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search");
OapiAlitripBtripHotelOrderSearchRequest req = new OapiAlitripBtripHotelOrderSearchRequest();
OpenSearchRq openSearchRq = new OpenSearchRq();
openSearchRq.setStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
openSearchRq.setApplyId(12345L);
openSearchRq.setPage(1L);
openSearchRq.setUserid("user1");
openSearchRq.setPageSize(10L);
openSearchRq.setDeptid("dept1");
openSearchRq.setEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
openSearchRq.setCorpid("corp1");
openSearchRq.setUpdateEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
openSearchRq.setUpdateStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
openSearchRq.setAllApply(true);
openSearchRq.setThirdpartApplyId("123");
req.setRq(openSearchRq);
OapiAlitripBtripHotelOrderSearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripHotelOrderSearchRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search")

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
$req = new OapiAlitripBtripHotelOrderSearchRequest;
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
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/hotel/order/search");
OapiAlitripBtripHotelOrderSearchRequest req = new OapiAlitripBtripHotelOrderSearchRequest();
OapiAlitripBtripHotelOrderSearchRequest.OpenSearchRqDomain obj1 = new OapiAlitripBtripHotelOrderSearchRequest.OpenSearchRqDomain();
obj1.StartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.ApplyId = 12345L;
obj1.Page = 1L;
obj1.Userid = "user1";
obj1.PageSize = 10L;
obj1.Deptid = "dept1";
obj1.EndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.Corpid = "corp1";
obj1.UpdateEndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.UpdateStartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.AllApply = true;
obj1.ThirdpartApplyId = "123";
req.Rq_ = obj1;
OapiAlitripBtripHotelOrderSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| module | OpenHotelOrderRs[] |  | 酒店订单列表。 |
| id | Number | 237410191384229703 | 订单ID。 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 创建时间。 |
| gmt\_modified | Date | 2017-05-01 00:00:00 | 更新时间。 |
| corpid | String | ding3cb4e74axxxx | 企业的corpid。 |
| corp\_name | String | 阿里巴巴 | 企业名称。 |
| userid | String | user1 | 用户的userid。 |
| user\_name | String | 张三 | 用户名称。 |
| deptid | String | dept1 | 部门ID。 |
| dept\_name | String | 淘宝 | 部门名称。 |
| apply\_id | Number | 8530697 | 商旅申请单ID。 |
| contact\_name | String | 李四 | 联系人姓名。 |
| city | String | 北京 | 酒店所在城市。 |
| hotel\_name | String | 未来酒店 | 酒店名称。 |
| check\_in | Date | 2017-05-01 00:00:00 | 入住时间。 |
| check\_out | Date | 2017-05-01 00:00:00 | 离店时间。 |
| room\_type | String | 标间 | 房型。 |
| room\_num | Number | 1 | 房间数。 |
| night | Number | 4 | 总共住几晚。 |
| guest | String | 张三,李四 | 入住顾客，多个用','分割。 |
| order\_type\_desc | String | 信用住 | 订单类型描述。 |
| order\_status\_desc | String | 预订成功 | 订单状态描述。 |
| cost\_center | OpenCostCenterDo |  | 成本中心对象。 |
| id | Number | 231573 | 商旅成本中心ID。 |
| corpid | String | corp1 | 企业的corpid。 |
| number | String | 12345 | 成本中心编号。 |
| name | String | 测试成本中心 | 成本中心名称。 |
| invoice | OpenInvoiceDo |  | 发票对象。 |
| id | Number | 143614 | 商旅发票ID。 |
| title | String | 阿里巴巴 | 发票抬头。 |
| price\_info\_list | OpenPriceInfo[] |  | 价目详情列表。 |
| price | String | 100.0 | 价格。 |
| type | Number | 1 | 资金流向：   - **1**：支出 - **2**：收入 |
| category | String | 酒店费用 | 交易类型。 |
| pay\_type | Number | 1 | 结算方式：   - **1**：个人现付 - **2**：企业现付 - **4**：企业月结 - **8**：企业预存 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 流水创建时间。 |
| passenger\_name | String | 张三,李四 | 入住人信息，多个用‘,’分割。 |
| thirdpart\_itinerary\_id | String | abcdef | 第三方行程ID。 |
| order\_status | Number | 1 | 订单状态：   - **1**：等待确认 - **2**：等待付款 - **3**：预订成功 - **4**：申请退款 - **5**：退款成功 - **6**：已关闭 - **7**：结账成功 - **8**：支付成功 |
| order\_type | Number | 1 | 订单类型：   - **1**：预付 - **5**：面付 - **6**：信用住 |
| user\_affiliate\_list | OpenUserAffiliateDo[] |  | 入住人列表。 |
| userid | String | 123 | 入住人姓名。 |
| user\_name | String | 张三 | 入住人名称。 |
| thirdpart\_apply\_id | String | 123 | 第三方申请单ID。 |
| btrip\_title | String | 出差 | 申请单名称。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "module":{
    "gmt_create":"2017-05-01 00:00:00",
    "corpid":"corp1",
    "city":"北京",
    "user_name":"张三",
    "deptid":"dept1",
    "gmt_modified":"2017-05-01 00:00:00",
    "userid":"user1",
    "price_info_list":{
      "gmt_create":"2017-05-01 00:00:00",
      "price":"100.0",
      "pay_type":"1",
      "type":"1",
      "category":"酒店费用",
      "passenger_name":"张三,李四"
    },
    "check_out":"2017-05-01 00:00:00",
    "order_status":"1",
    "room_num":"1",
    "thirdpart_apply_id":"123",
    "apply_id":"123",
    "id":"12345",
    "order_type":"1",
    "user_affiliate_list":{
      "user_name":"张三",
      "userid":"123"
    },
    "thirdpart_itinerary_id":"abcdef",
    "contact_name":"李四",
    "check_in":"2017-05-01 00:00:00",
    "night":"4",
    "dept_name":"淘宝",
    "corp_name":"阿里巴巴",
    "hotel_name":"未来酒店",
    "btrip_title":"出差",
    "order_type_desc":"信用住",
    "cost_center":{
      "number":"abc",
      "corpid":"corp1",
      "name":"测试成本中心",
      "id":"123"
    },
    "guest":"张三,李四",
    "invoice":{
      "id":"123",
      "title":"阿里巴巴"
    },
    "order_status_desc":"预订成功",
    "room_type":"标间"
  },
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
