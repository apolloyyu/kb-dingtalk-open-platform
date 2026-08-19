---
title: "修改申请单"
source_url: "https://open.dingtalk.com/document/development/user-modify-approval-form"
namespace: "development"
slug: "user-modify-approval-form"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 修改申请单"
doc_id: "Ze0qcrRObI"
updated_at: "2026-06-03 09:58:24"
---

> Source: https://open.dingtalk.com/document/development/user-modify-approval-form
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 修改申请单
> Updated: 2026-06-03 09:58:24

# 修改申请单

通过此接口可修改已创建的出差申请单，支持对申请人信息、行程详情、审批状态等核心字段进行更新，适用于企业差旅管理系统与钉钉审批流程的集成场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/modify |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip\_write-阿里商旅专用写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenApiNewApplyRq | 是 |  | 请求参数对象，包含完整的申请单修改信息。 |
| thirdpart\_business\_id | String | 否 | 12345 | 用户展示的外部审批单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| status | Number | 否 | 0 | 审批单状态，不传入默认为0：   - 0：审批中 - 1：同意 - 2：拒绝 |
| corpid | String | 是 | corp1 | 企业的corpid，标识目标企业身份。 |
| traveler\_list | OpenUserInfo[] | 是 |  | 出行人信息列表，用于指定本次出差的人员详情。 |
| user\_name | String | 否 | 张三 | 出行人姓名。 |
| userid | String | 是 | user1 | 申请人的userid，用于唯一标识操作用户。 |
| deptid | String | 否 | dept1 | 部门ID，若未传入则自动从用户信息中获取。  **[!IMPORTANT]**  若传递错误的部门ID（仅支持数字），可能导致后续费用无法正确归属到对应部门。 |
| user\_name | String | 否 | 张三 | 用户名称，如果要传必须传真实姓名，如果不传则会以系统当前维护userId对应的名称进行预订 |
| userid | String | 是 | user1 | 用户的userid。 |
| corp\_name | String | 否 | 阿里巴巴 | 企业名称。 |
| trip\_cause | String | 是 | 北京出差 | 出差事由。 |
| dept\_name | String | 否 | 淘宝 | 部门名称。 |
| itinerary\_list | OpenItineraryInfo[] | 是 |  | 行程列表。 |
| project\_code | String | 否 | xm1 | 项目编码。 |
| project\_title | String | 否 | 项目1 | 项目名称。 |
| arr\_date | Date | 是 | 2017-01-01 00:00:00 | 到达日期。 |
| dep\_date | Date | 是 | 2017-01-01 00:00:00 | 出发日期。 |
| invoice\_id | Number | 是 | 1234 | 发票ID。 |
| thirdpart\_cost\_center\_id | String | 否 | 12345 | 第三方成本中心ID。  该参数与**cost\_center\_id**必填一个。 |
| cost\_center\_id | Number | 否 | 123 | 商旅成本中心id。  该参数与**thirdpart\_cost\_center\_id**必填一个。 |
| arr\_city\_code | String | 否 | BJS | 到达城市编码。 |
| arr\_city | String | 是 | 北京 | 到达城市。 |
| dep\_city\_code | String | 否 | HGH | 出发城市编码。 |
| dep\_city | String | 是 | 杭州 | 出发城市。 |
| traffic\_type | Number | 是 | 0 | 交通方式：   - 0：飞机 - 1：火车, - 2：汽车, - 3：其他 |
| itinerary\_id | String | 是 | 123456 | 行程ID。 |
| trip\_way | Number | 是 | 0 | 行程类型：   - 0：单程 - 1：往返 |
| trip\_title | String | 是 | 北京出差 | 申请单标题。 |
| thirdpart\_apply\_id | String | 是 | 12345 | 外部申请单ID。 |
| trip\_day | Number | 否 | 1 | 出差天数。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/modify" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ae9655xxxx9b21a37' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/modify");
OapiAlitripBtripApprovalModifyRequest req = new OapiAlitripBtripApprovalModifyRequest();
OpenApiNewApplyRq obj1 = new OpenApiNewApplyRq();
obj1.setThirdpartBusinessId("12345");
obj1.setStatus(0L);
obj1.setCorpid("corp1");
List<OpenUserInfo> list3 = new ArrayList<OpenUserInfo>();
OpenUserInfo obj4 = new OpenUserInfo();
list3.add(obj4);
obj4.setUserName("张三");
obj4.setUserid("user1");
obj1.setTravelerList(list3);
obj1.setDeptid("dept1");
obj1.setUserName("张三");
obj1.setUserid("user1");
obj1.setCorpName("阿里巴巴");
obj1.setTripCause("北京出差");
obj1.setDeptName("淘宝");
List<OpenItineraryInfo> list6 = new ArrayList<OpenItineraryInfo>();
OpenItineraryInfo obj7 = new OpenItineraryInfo();
list6.add(obj7);
obj7.setProjectCode("xm1");
obj7.setProjectTitle("项目1");
obj7.setArrDate(StringUtils.parseDateTime("2017-01-01 00:00:00"));
obj7.setDepDate(StringUtils.parseDateTime("2017-01-01 00:00:00"));
obj7.setInvoiceId(1234L);
obj7.setThirdpartCostCenterId("12345");
obj7.setCostCenterId(123L);
obj7.setArrCityCode("BJS");
obj7.setArrCity("北京");
obj7.setDepCityCode("HGH");
obj7.setDepCity("杭州");
obj7.setTrafficType(0L);
obj7.setItineraryId("123456");
obj7.setTripWay(0L);
obj1.setItineraryList(list6);
obj1.setTripTitle("北京出差");
obj1.setThirdpartApplyId("12345");
obj1.setTripDay(1L);
req.setRq(obj1);
OapiAlitripBtripApprovalModifyResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripApprovalModifyRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/modify")

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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST, DingTalkConstant::$FORMAT_JSON);
$req = new OapiAlitripBtripApprovalModifyRequest;
$rq = new OpenApiNewApplyRq;
$rq->thirdpart_business_id = "12345";
$rq->status = 0;
$rq->corpid = "corp1";
$traveler_list = new OpenUserInfo;
$traveler_list->user_name = "张三";
$traveler_list->userid = "user1";
$rq->traveler_list = array($traveler_list);
$rq->deptid = "dept1";
$rq->user_name = "张三";
$rq->userid = "user1";
$rq->corp_name = "阿里巴巴";
$rq->trip_cause = "北京出差";
$rq->dept_name = "淘宝";
$itinerary_list = new OpenItineraryInfo;
$itinerary_list->project_code = "xm1";
$itinerary_list->project_title = "项目1";
$itinerary_list->arr_date = "2017-01-01 00:00:00";
$itinerary_list->dep_date = "2017-01-01 00:00:00";
$itinerary_list->invoice_id = 1234;
$itinerary_list->thirdpart_cost_center_id = "12345";
$itinerary_list->cost_center_id = 123;
$itinerary_list->arr_city_code = "BJS";
$itinerary_list->arr_city = "北京";
$itinerary_list->dep_city_code = "HGH";
$itinerary_list->dep_city = "杭州";
$itinerary_list->traffic_type = 0;
$itinerary_list->itinerary_id = "123456";
$itinerary_list->trip_way = 0;
$rq->itinerary_list = array($itinerary_list);
$rq->trip_title = "北京出差";
$rq->thirdpart_apply_id = "12345";
$rq->trip_day = 1;
$req->setRq($rq);
$resp = $c->execute($req, $access_token);
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/modify");
OapiAlitripBtripApprovalModifyRequest req = new OapiAlitripBtripApprovalModifyRequest();
OapiAlitripBtripApprovalModifyRequest.OpenApiNewApplyRqDomain obj1 = new OapiAlitripBtripApprovalModifyRequest.OpenApiNewApplyRqDomain();
obj1.ThirdpartBusinessId = "12345";
obj1.Status = 0L;
obj1.Corpid = "corp1";
List<OapiAlitripBtripApprovalModifyRequest.OpenUserInfoDomain> list3 = new List<OapiAlitripBtripApprovalModifyRequest.OpenUserInfoDomain>();
OapiAlitripBtripApprovalModifyRequest.OpenUserInfoDomain obj4 = new OapiAlitripBtripApprovalModifyRequest.OpenUserInfoDomain();
list3.Add(obj4);
obj4.UserName = "张三";
obj4.Userid = "user1";
obj1.TravelerList = list3;
obj1.Deptid = "dept1";
obj1.UserName = "张三";
obj1.Userid = "user1";
obj1.CorpName = "阿里巴巴";
obj1.TripCause = "北京出差";
obj1.DeptName = "淘宝";
List<OapiAlitripBtripApprovalModifyRequest.OpenItineraryInfoDomain> list6 = new List<OapiAlitripBtripApprovalModifyRequest.OpenItineraryInfoDomain>();
OapiAlitripBtripApprovalModifyRequest.OpenItineraryInfoDomain obj7 = new OapiAlitripBtripApprovalModifyRequest.OpenItineraryInfoDomain();
list6.Add(obj7);
obj7.ProjectCode = "xm1";
obj7.ProjectTitle = "项目1";
obj7.ArrDate = DateTime.Parse("2017-01-01 00:00:00");
obj7.DepDate = DateTime.Parse("2017-01-01 00:00:00");
obj7.InvoiceId = 1234L;
obj7.ThirdpartCostCenterId = "12345";
obj7.CostCenterId = 123L;
obj7.ArrCityCode = "BJS";
obj7.ArrCity = "北京";
obj7.DepCityCode = "HGH";
obj7.DepCity = "杭州";
obj7.TrafficType = 0L;
obj7.ItineraryId = "123456";
obj7.TripWay = 0L;
obj1.ItineraryList = list6;
obj1.TripTitle = "北京出差";
obj1.ThirdpartApplyId = "12345";
obj1.TripDay = 1L;
req.Rq_ = obj1;
OapiAlitripBtripApprovalModifyResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| module | OpenApiNewApplyRs | module | 结果对象。 |
| apply\_id | Number | 123 | 商旅申请单ID。 |
| thirdpart\_apply\_id | String | 12345 | 外部申请单ID。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "module":{
    "thirdpart_apply_id":"12345",
    "apply_id":"123"
  },
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
