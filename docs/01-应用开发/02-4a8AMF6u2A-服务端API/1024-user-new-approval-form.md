---
title: "新建审批单"
source_url: "https://open.dingtalk.com/document/development/user-new-approval-form"
namespace: "development"
slug: "user-new-approval-form"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 新建审批单"
doc_id: "OrUS6JJnap"
updated_at: "2026-06-03 09:58:26"
---

> Source: https://open.dingtalk.com/document/development/user-new-approval-form
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 新建审批单
> Updated: 2026-06-03 09:58:26

# 新建审批单

通过此接口创建新的审批单，适用于企业商旅场景下的出差申请流程自动化。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/new |
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
| rq | OpenApiNewApplyRq | 是 |  | 请求对象，封装完整的审批单创建参数。 |
| trip\_day | Number | 否 | 1 | 出差天数。 |
| thirdpart\_apply\_id | String | 是 | 1a7e15f82fxxxx | 外部申请单id。 |
| trip\_title | String | 是 | 北京出差 | 申请单标题。 |
| itinerary\_list | OpenItineraryInfo[] | 是 |  | 行程列表。 |
| trip\_way | Number | 是 | 0 | 行程类型：   - **0**：单程 - **1**：往返 |
| itinerary\_id | String | 是 | 59363496 | 用户自定义行程ID。 |
| traffic\_type | Number | 是 | 0 | 交通方式：   - **0**：飞机 - **1**：火车 - **2**：汽车 - **3**：其他 |
| dep\_city | String | 是 | 杭州 | 出发城市。 |
| dep\_city\_code | String | 否 | HGH | 出发城市编码。 |
| arr\_city | String | 是 | 北京 | 到达城市。 |
| arr\_city\_code | String | 否 | BJS | 到达城市编码。 |
| cost\_center\_id | Number | 是 | 3454232 | 商旅成本中心id，可通过[查询成本中心](1017-query-cost-center.md)接口获取。  **[!NOTE]**  若不填则第三方成本中心id必填。 |
| thirdpart\_cost\_center\_id | String | 否 | 3454232 | 第三方成本中心id，可通过[查询成本中心](1017-query-cost-center.md)接口获取。  **[!NOTE]**  若不填则商旅成本中心id必填。 |
| invoice\_id | Number | 是 | 3891xxxx | 发票id，可调用[查询可用发票列表](1041-query-available-invoices.md)接口获取。 |
| dep\_date | Date | 是 | 2017-01-01 00:00:00 | 出发日期。 |
| arr\_date | Date | 是 | 2017-01-01 00:00:00 | 到达日期。 |
| project\_title | String | 否 | 项目1 | 项目名称。 |
| project\_code | String | 否 | xm1 | 项目编号。 |
| dept\_name | String | 否 | 淘宝 | 部门名称。 |
| trip\_cause | String | 是 | 北京出差 | 出差事由。 |
| corp\_name | String | 否 | 阿里巴巴 | 企业名称。 |
| userid | String | 是 | user1 | 用户的userid。 |
| user\_name | String | 否 | 张xx | 用户名称。  **[!NOTE]**  如果要传必须传真实姓名，如果不传则会以系统当前维护userId对应的名称进行预订。 |
| deptid | String | 否 | 1864154 | 部门id。  **[!NOTE]**  如果不传，会根据user相关信息去获取对应的部门信息，如果传的是错误的部门信息，后面无法做部门的费用归属。 |
| traveler\_list | OpenUserInfo[] | 是 |  | 出行人列表。 |
| userid | String | 是 | user1 | 出行人的userid。 |
| user\_name | String | 否 | 张xx | 出行人姓名。 |
| corpid | String | 是 | ding14xxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| status | Number | 否 | 0 | 审批单状态。   - **0**（默认）：审批中 - **1**：同意 - **2**：拒绝 |
| thirdpart\_business\_id | String | 否 | 34234521 | 用户展示的外部审批单id信息。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/new" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3fa56fxxxx968d68f' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/new");
OapiAlitripBtripApprovalNewRequest req = new OapiAlitripBtripApprovalNewRequest();
OpenApiNewApplyRq apiNewApplyRq = new OpenApiNewApplyRq();
apiNewApplyRq.setTripDay(1L);
apiNewApplyRq.setThirdpartApplyId("12345");
apiNewApplyRq.setTripTitle("北京出差");
List<OpenItineraryInfo> itineraryInfos = new ArrayList<OpenItineraryInfo>();
OpenItineraryInfo itineraryInfo = new OpenItineraryInfo();
itineraryInfos.add(itineraryInfo);
itineraryInfo.setTripWay(0L);
itineraryInfo.setItineraryId("59363496");
itineraryInfo.setTrafficType(0L);
itineraryInfo.setDepCity("杭州");
itineraryInfo.setDepCityCode("HGH");
itineraryInfo.setArrCity("北京");
itineraryInfo.setArrCityCode("BJS");
itineraryInfo.setCostCenterId(123L);
itineraryInfo.setThirdpartCostCenterId("12345");
itineraryInfo.setInvoiceId(3891xxxxL);
itineraryInfo.setDepDate(StringUtils.parseDateTime("2017-01-01 00:00:00"));
itineraryInfo.setArrDate(StringUtils.parseDateTime("2017-01-01 00:00:00"));
itineraryInfo.setProjectTitle("项目1");
itineraryInfo.setProjectCode("xm1");
apiNewApplyRq.setItineraryList(itineraryInfos);
apiNewApplyRq.setDeptName("淘宝");
apiNewApplyRq.setTripCause("北京出差");
apiNewApplyRq.setCorpName("阿里巴巴");
apiNewApplyRq.setUserid("user1");
apiNewApplyRq.setUserName("张xx");
apiNewApplyRq.setDeptid("1864154");
List<OpenUserInfo> openUserInfos = new ArrayList<OpenUserInfo>();
OpenUserInfo openUserInfo = new OpenUserInfo();
openUserInfos.add(openUserInfo);
openUserInfo.setUserid("user1");
openUserInfo.setUserName("张xx");
apiNewApplyRq.setTravelerList(openUserInfos);
apiNewApplyRq.setCorpid("ding14xxxx");
apiNewApplyRq.setStatus(0L);
apiNewApplyRq.setThirdpartBusinessId("12345");
req.setRq(apiNewApplyRq);
OapiAlitripBtripApprovalNewResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripApprovalNewRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/new")

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
$req = new OapiAlitripBtripApprovalNewRequest;
$rq = new OpenApiNewApplyRq;
$rq->trip_day = 1;
$rq->thirdpart_apply_id = "12345";
$rq->trip_title = "北京出差";
$itinerary_list = new OpenItineraryInfo;
$itinerary_list->trip_way = 0;
$itinerary_list->itinerary_id = "59363496";
$itinerary_list->traffic_type = 0;
$itinerary_list->dep_city = "杭州";
$itinerary_list->dep_city_code = "HGH";
$itinerary_list->arr_city = "北京";
$itinerary_list->arr_city_code = "BJS";
$itinerary_list->cost_center_id = 123;
$itinerary_list->thirdpart_cost_center_id = "12345";
$itinerary_list->invoice_id = 3891xxxx;
$itinerary_list->dep_date = "2017-01-01 00:00:00";
$itinerary_list->arr_date = "2017-01-01 00:00:00";
$itinerary_list->project_title = "项目1";
$itinerary_list->project_code = "xm1";
$rq->itinerary_list = array($itinerary_list);
$rq->dept_name = "淘宝";
$rq->trip_cause = "北京出差";
$rq->corp_name = "阿里巴巴";
$rq->userid = "user1";
$rq->user_name = "张xx";
$rq->deptid = "1864154";
$traveler_list = new OpenUserInfo;
$traveler_list->userid = "user1";
$traveler_list->user_name = "张xx";
$rq->traveler_list = array($traveler_list);
$rq->corpid = "ding14xxxx";
$rq->status = 0;
$rq->thirdpart_business_id = "12345";
$req->setRq($rq);
$resp = $c->execute($req, $access_token);
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/new");
OapiAlitripBtripApprovalNewRequest req = new OapiAlitripBtripApprovalNewRequest();

OapiAlitripBtripApprovalNewRequest.OpenApiNewApplyRqDomain obj1 = new OapiAlitripBtripApprovalNewRequest.OpenApiNewApplyRqDomain();
obj1.TripDay = 1L;
obj1.ThirdpartApplyId = "12345";
obj1.TripTitle = "北京出差";
List<OapiAlitripBtripApprovalNewRequest.OpenItineraryInfoDomain> list3 = new List<OapiAlitripBtripApprovalNewRequest.OpenItineraryInfoDomain>();
OapiAlitripBtripApprovalNewRequest.OpenItineraryInfoDomain obj4 = new OapiAlitripBtripApprovalNewRequest.OpenItineraryInfoDomain();
list3.Add(obj4);
obj4.TripWay = 0L;
obj4.ItineraryId = "59363496";
obj4.TrafficType = 0L;
obj4.DepCity = "杭州";
obj4.DepCityCode = "HGH";
obj4.ArrCity = "北京";
obj4.ArrCityCode = "BJS";
obj4.CostCenterId = 123L;
obj4.ThirdpartCostCenterId = "12345";
obj4.InvoiceId = 3891xxxxL;
obj4.DepDate = DateTime.Parse("2017-01-01 00:00:00");
obj4.ArrDate = DateTime.Parse("2017-01-01 00:00:00");
obj4.ProjectTitle = "项目1";
obj4.ProjectCode = "xm1";
obj1.ItineraryList = list3;
obj1.DeptName = "淘宝";
obj1.TripCause = "北京出差";
obj1.CorpName = "阿里巴巴";
obj1.Userid = "user1";
obj1.UserName = "张xx";
obj1.Deptid = "1864154";
List<OapiAlitripBtripApprovalNewRequest.OpenUserInfoDomain> list6 = new List<OapiAlitripBtripApprovalNewRequest.OpenUserInfoDomain>();
OapiAlitripBtripApprovalNewRequest.OpenUserInfoDomain obj7 = new OapiAlitripBtripApprovalNewRequest.OpenUserInfoDomain();
list6.Add(obj7);
obj7.Userid = "user1";
obj7.UserName = "张xx";
obj1.TravelerList = list6;
obj1.Corpid = "ding14xxxx";
obj1.Status = 0L;
obj1.ThirdpartBusinessId = "12345";
req.Rq_ = obj1;
OapiAlitripBtripApprovalNewResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| module | OpenApiNewApplyRs | module | 结果对象。 |
| thirdpart\_apply\_id | String | 1a7e15f82fxxxx | 外部申请单id。 |
| apply\_id | Number | 59363496 | 商旅申请单id。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 成功标识。 |
| request\_id | String | 5tl2ldoxw115 | 请求ID。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "module":{
    "thirdpart_apply_id":"12345",
    "apply_id":59363496
  },
  "request_id": "5tl2ldoxw115"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
