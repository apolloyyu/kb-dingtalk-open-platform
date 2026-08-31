---
title: "获取申请单详情"
source_url: "https://open.dingtalk.com/document/development/obtains-the-detailed-data-of-a-single-request"
namespace: "development"
slug: "obtains-the-detailed-data-of-a-single-request"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 获取申请单详情"
doc_id: "CFvqggDQos"
updated_at: "2026-06-03 09:58:28"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-detailed-data-of-a-single-request
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 获取申请单详情
> Updated: 2026-06-03 09:58:28

# 获取申请单详情

调用本接口可获取单个阿里商旅审批单的详细信息，包括申请人、出行人、行程、审批人等完整数据。适用于企业内部差旅审批系统中查询单个申请单详情的场景，常用于审批流展示、费用报销关联等环节。

## 接口调用说明

该接口主要用于企业差旅管理系统中，当需要展示某一条审批申请的完整信息时使用。例如在审批流程页面中加载申请单详情、财务报销系统中关联历史出差记录、或数据分析平台中提取结构化差旅数据等业务流程。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get |
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
| rq | OpenSearchRq | 是 |  | 请求对象，包含用于查询申请单的标识信息。 |
| thirdpart\_apply\_id | String | 否 | abcdef | 外部审批单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| apply\_id | Number | 否 | 123 | 阿里商旅审批单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| apply\_show\_id | String | 否 | 2017651 | 阿里商旅审批单展示ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| corpid | String | 是 | corp1 | 企业的corpid，用于标识所属企业。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=00140xxxxadbf85b' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get");
OapiAlitripBtripApplyGetRequest req = new OapiAlitripBtripApplyGetRequest();
OpenSearchRq obj1 = new OpenSearchRq();
obj1.setThirdpartApplyId("abcdef");
obj1.setApplyId(123L);
obj1.setApplyShowId("201710111505000464651");
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripApplyGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripApplyGetRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get")

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
$req = new OapiAlitripBtripApplyGetRequest;
$rq = new OpenSearchRq;
$rq->thirdpart_apply_id="abcdef";
$rq->apply_id="123";
$rq->apply_show_id="201710111505000464651";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/apply/get");
OapiAlitripBtripApplyGetRequest req = new OapiAlitripBtripApplyGetRequest();
OapiAlitripBtripApplyGetRequest.OpenSearchRqDomain obj1 = new OapiAlitripBtripApplyGetRequest.OpenSearchRqDomain();
obj1.ThirdpartApplyId = "abcdef";
obj1.ApplyId = 123L;
obj1.ApplyShowId = "201710111505000464651";
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripApplyGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| module | OpenApplyRs |  | 审批单对象。 |
| id | Number | 12345 | 商旅审批单ID。 |
| apply\_show\_id | String | 201710111505000464651 | 商旅审批展示ID。 |
| gmt\_create | Date | 2017-05-01 00:00:00 | 创建时间。 |
| gmt\_modified | Date | 2017-05-01 00:00:00 | 更新时间。 |
| thirdpart\_id | String | 8a5043a0-539xxxx | 第三方审批单ID。  如果非第三方审批单则为空。 |
| corpid | String | ding3cb4e74a88d5a55xxxx | 企业的corpid。 |
| corp\_name | String | 阿里巴巴 | 企业名称。 |
| userid | String | user1 | 用户的userid。 |
| user\_name | String | 张三 | 用户姓名。 |
| deptid | String | dept1 | 部门ID。 |
| trip\_day | Number | 1 | 出差天数。 |
| dept\_name | String | 淘宝 | 部门名称。 |
| trip\_cause | String | 北京出差 | 出差事由。 |
| trip\_title | String | 北京出差 | 审批单标题。 |
| status | Number | 1 | 申请单状态：   - 0：申请 - 1：同意 - 2：拒绝 - 3：转交 - 4：取消 - 5：修改已同意 - 6：撤销已同意 - 7：修改审批中 - 8：已同意(修改被拒绝) - 9：撤销审批中 - 10：已同意(撤销被拒绝) - 11：已同意(修改被取消) - 12：已同意(撤销被取消) |
| status\_desc | String | 同意 | 审批单状态描述。 |
| itinerary\_list | OpenItineraryInfo[] |  | 行程列表。 |
| trip\_way | Number | 1 | 行程方式：   - 0：单程 - 1：往返 |
| itinerary\_id | String | 7901607 | 行程ID。 |
| traffic\_type | Number | 0 | 交通方式：   - 0：飞机 - 1：火车 - 2：汽车 - 3：其他 |
| dep\_city | String | 杭州 | 出发城市。 |
| arr\_city | String | 北京 | 到达城市。 |
| dep\_date | Date | 2017-05-01 00:00:00 | 出发时间。 |
| cost\_center\_name | String | 阿里巴巴 | 成本中心。 |
| arr\_date | Date | 2017-05-01 00:00:00 | 到达时间。 |
| invoice\_name | String | 阿里巴巴 | 发票抬头。 |
| project\_title | String | 项目1 | 项目名称。 |
| project\_code | String | xm1 | 项目编号 |
| traveler\_list | OpenUserInfo[] |  | 出行人列表。 |
| userid | String | user1 | 出行人的userid。 |
| user\_name | String | 张三 | 出行人姓名。 |
| approver\_list | OpenApproverInfo[] |  | 审批人列表。 |
| order | Number | 1 | 审批人顺序。 |
| userid | String | user1 | 审批人的userid。 |
| user\_name | String | 张三 | 审批人姓名。 |
| status | Number | 1 | 审批状态：   - 0：审批中 - 1：已同意 - 2：已拒绝 - 3：已转交 - 4：已取消 - 5：已终止 - 6：发起审批 - 7：评论 |
| status\_desc | String | 同意 | 审批状态描述。 |
| note | String | 同意 | 审批意见。 |
| operate\_time | Date | 2017-05-01 00:00:00 | 操作时间。 |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
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
      "project_title":"项目1",
      "project_code":"xm1",
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
