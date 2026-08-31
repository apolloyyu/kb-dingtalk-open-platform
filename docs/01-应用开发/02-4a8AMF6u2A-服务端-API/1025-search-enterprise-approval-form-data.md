---
title: "获取申请单列表"
source_url: "https://open.dingtalk.com/document/development/search-enterprise-approval-form-data"
namespace: "development"
slug: "search-enterprise-approval-form-data"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 获取申请单列表"
doc_id: "1tvEFFj5Xa"
updated_at: "2026-06-08 09:47:13"
---

> Source: https://open.dingtalk.com/document/development/search-enterprise-approval-form-data
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 获取申请单列表
> Updated: 2026-06-08 09:47:13

# 获取申请单列表

调用本接口按照企业corpid和用户userid维度，获取申请单包括审批状态、时间等数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenSearchRq | 是 |  | 请求对象。 |
| gmt\_modified | Date | 否 | 2017-05-01 00:00:00 | 更新时间大于等于此时间的审批单。 |
| page\_size | Number | 否 | 10 | 每页返回数量，默认10，最多50。 |
| end\_time | Date | 否 | 2017-05-01 00:00:00 | 结束时间。 |
| start\_time | Date | 否 | 2017-05-01 00:00:00 | 开始时间。 |
| page | Number | 否 | 1 | 页数，从1开始。 |
| userid | String | 否 | user1 | 提交审批单的用户的userid。 |
| deptid | String | 否 | dept1 | 部门ID。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |
| all\_apply | Boolean | 否 | true | 是否包括未报销的申请：   - **false**: 未报销的申请单 |
| only\_shang\_lv\_apply | Boolean | 否 | false | 是否仅包括商旅申请单：   - **true**：商旅申请单 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=70bdcafxxxx778' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search");
OapiAlitripBtripApplySearchRequest req = new OapiAlitripBtripApplySearchRequest();
OpenSearchRq obj1 = new OpenSearchRq();
obj1.setGmtModified(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setPageSize(10L);
obj1.setEndTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setStartTime(StringUtils.parseDateTime("2017-05-01 00:00:00"));
obj1.setPage(1L);
obj1.setUserid("user1");
obj1.setDeptid("dept1");
obj1.setCorpid("corp1");
obj1.setAllApply(true);
obj1.setOnlyShangLvApply(false);
req.setRq(obj1);
OapiAlitripBtripApplySearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripApplySearchRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search")

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
$req = new OapiAlitripBtripApplySearchRequest;
$rq = new OpenSearchRq;
$rq->gmt_modified="2017-05-01 00:00:00";
$rq->page_size="10";
$rq->end_time="2017-05-01 00:00:00";
$rq->start_time="2017-05-01 00:00:00";
$rq->page="1";
$rq->userid="user1";
$rq->deptid="dept1";
$rq->corpid="corp1";
$rq->all_apply="true";
$rq->only_shang_lv_apply="false";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/search");
OapiAlitripBtripApplySearchRequest req = new OapiAlitripBtripApplySearchRequest();
OapiAlitripBtripApplySearchRequest.OpenSearchRqDomain obj1 = new OapiAlitripBtripApplySearchRequest.OpenSearchRqDomain();
obj1.GmtModified = DateTime.Parse("2017-05-01 00:00:00");
obj1.PageSize = 10L;
obj1.EndTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.StartTime = DateTime.Parse("2017-05-01 00:00:00");
obj1.Page = 1L;
obj1.Userid = "user1";
obj1.Deptid = "dept1";
obj1.Corpid = "corp1";
obj1.AllApply = true;
obj1.OnlyShangLvApply = false;
req.Rq_ = obj1;
OapiAlitripBtripApplySearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| module | OpenApplyRs[] |  | 审批单列表。 |
| id | Number | 7438532 | 商旅审批单ID。 |
| apply\_show\_id | String | 201710111505000464651 | 商旅审批展示ID。 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 创建时间。 |
| gmt\_modified | Date | 2017-05-01 00:00:00 | 更新时间。 |
| thirdpart\_id | String | 81bb785b-4ee2xxxx | 第三方审批单ID。  如果非第三方审批单则为空。 |
| corpid | String | corp1 | 企业的corpid。 |
| userid | String | user1 | 用户的userid。 |
| deptid | String | dept1 | 用户的部门ID。 |
| corp\_name | String | 阿里巴巴 | 企业名称。 |
| user\_name | String | 张三 | 用户名称。 |
| dept\_name | String | 钉钉 | 部门名称。 |
| trip\_day | Number | 1 | 出差天数。 |
| trip\_cause | String | 项目沟通 | 出差事由。 |
| trip\_title | String | 北京出差 | 申请单标题。 |
| status | Number | 1 | 申请单状态：   - 0：申请 - 1：同意 - 2：拒绝 - 3：转交 - 4：取消 - 5：修改已同意 - 6：撤销已同意 - 7：修改审批中 - 8：已同意(修改被拒绝) - 9：撤销审批中 - 10：已同意(撤销被拒绝) - 11：已同意(修改被取消) - 12：已同意(撤销被取消) |
| status\_desc | String | 同意 | 审批单状态描述。 |
| itinerary\_list | OpenItineraryInfo[] |  | 行程列表。 |
| trip\_way | Number | 1 | 行程方式：   - 0：单程 - 1：往返 |
| itinerary\_id | String | 8947547 | 行程ID。 |
| traffic\_type | Number | 0 | 交通方式：   - 0：飞机 - 1：火车 - 2：汽车 - 3：其他 |
| dep\_city | String | 杭州 | 出发城市。 |
| arr\_city | String | 北京 | 到达城市。 |
| cost\_center\_name | String | 阿里巴巴 | 成本中心。 |
| invoice\_name | String | 阿里巴巴 | 发票抬头。 |
| dep\_date | Date | 2017-05-01 00:00:00 | 出发日期。 |
| arr\_date | Date | 2017-05-01 00:00:00 | 到达日期。 |
| project\_code | String | xm1 | 项目代码。 |
| project\_title | String | 项目1 | 项目名称。 |
| traveler\_list | OpenUserInfo[] |  | 出行人列表。 |
| userid | String | user1 | 出行人userid。 |
| user\_name | String | 张三 | 出行人姓名。 |
| approver\_list | OpenApproverInfo[] |  | 审批人列表。 |
| order | Number | 1 | 审批人顺序。 |
| user\_name | String | 张三 | 审批人姓名。 |
| userid | String | user1 | 审批人userid。 |
| status | Number | 1 | 审批状态：   - 0：审批中 - 1：已同意 - 2：已拒绝 - 3：已转交 - 4：已取消 - 5：已终止 - 6：发起审批 - 7：评论 |
| status\_desc | String | 同意 | 审批状态描述。 |
| note | String | 同意 | 审批意见。 |
| operate\_time | Date | 2017-05-01 00:00:00 | 操作时间。 |
| flow\_code | String | abc123 | 流程编码。 |
| errmsg | String | 成功 | 返回码。 |
| errcode | Number | 0 | 返回码描述。 |
| success | Boolean | true | 操作是否成功。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "module":{
    "gmt_create":"2017-05-01 00:00:00",
    "apply_show_id":"201710111505000464651",
    "corpid":"corp1",
    "status_desc":"同意",
    "user_name":"张三",
    "deptid":"dept1",
    "dept_name":"淘宝",
    "gmt_modified":"2017-05-01 00:00:00",
    "corp_name":"阿里巴巴",
    "userid":"user1",
    "flow_code":"abc123",
    "trip_day":"1",
    "traveler_list":{
      "user_name":"张三",
      "userid":"user1"
    },
    "thirdpart_id":"abc",
    "trip_title":"北京出差",
    "itinerary_list":{
      "arr_city":"北京",
      "arr_date":"2017-05-01 00:00:00",
      "trip_way":"1",
      "itinerary_id":"abcdefg",
      "traffic_type":"0",
      "dep_city":"杭州",
      "project_code":"xm1",
      "project_title":"项目1",
      "cost_center_name":"阿里巴巴",
      "dep_date":"2017-05-01 00:00:00",
      "invoice_name":"阿里巴巴"
    },
    "approver_list":{
      "note":"同意",
      "status_desc":"同意",
      "user_name":"张三",
      "userid":"user1",
      "order":"1",
      "status":"1",
      "operate_time":"2017-05-01 00:00:00"
    },
    "id":"12345",
    "trip_cause":"北京出差",
    "status":"1"
  },
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
