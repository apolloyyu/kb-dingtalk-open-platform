---
title: "查询假期余额"
source_url: "https://open.dingtalk.com/document/development/query-holiday-balance"
namespace: "development"
slug: "query-holiday-balance"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 假期管理 > 查询假期余额"
doc_id: "mn4VTVc7SB"
updated_at: "2026-05-27 17:06:30"
---

> Source: https://open.dingtalk.com/document/development/query-holiday-balance
> Path: 应用开发 / 服务端 API / 考勤 > 假期管理 > 查询假期余额
> Updated: 2026-05-27 17:06:30

# 查询假期余额

调用本接口，根据企业或员工分页获取假期余额信息，每次返回50条数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_holiday\_readonly-钉钉假期读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| leave\_code | String | 是 | f84a2xxxx | 假期类型唯一标识，可通过[查询假期规则列表](0238-holiday-type-query.md)接口获取leave\_code参数值。 |
| op\_userid | String | 是 | user01 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |
| userids | String | 是 | user02,user03 | 待查询的员工ID列表。 |
| offset | Number | 是 | 0 | 分页偏移，从0开始的非负整数。 |
| size | Number | 是 | 10 | 分页偏移，最大50。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=48acxxxx0dbdbee' \
-d 'leave_code=f84a2829-d245-4312-9ff2-0653e5b3abb2' \
-d 'offset=0' \
-d 'op_userid=zhangsan' \
-d 'size=10' \
-d 'userids=zhangsan%2Clisi'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list");
OapiAttendanceVacationQuotaListRequest req = new OapiAttendanceVacationQuotaListRequest();
req.setLeaveCode("f84a2xxxx");
req.setOpUserid("user01");
req.setUserids("user02,user03");
req.setOffset(0L);
req.setSize(10L);
OapiAttendanceVacationQuotaListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceVacationQuotaListRequest("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list")

req.leave_code="f84a2829-d245-4312-9ff2-0653e5b3abb2"
req.op_userid="zhangsan"
req.userids="zhangsan,lisi"
req.offset=0
req.size=10
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
$req = new OapiAttendanceVacationQuotaListRequest;
$req->setLeaveCode("f84a2829-d245-4312-9ff2-0653e5b3abb2");
$req->setOpUserid("zhangsan");
$req->setUserids("zhangsan,lisi");
$req->setOffset("0");
$req->setSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/list");
OapiAttendanceVacationQuotaListRequest req = new OapiAttendanceVacationQuotaListRequest();
req.LeaveCode = "f84a2829-d245-4312-9ff2-0653e5b3abb2";
req.OpUserid = "zhangsan";
req.Userids = "zhangsan,lisi";
req.Offset = 0L;
req.Size = 10L;
OapiAttendanceVacationQuotaListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OapiLeaveQuotaUserListVo |  | 返回结果。 |
| has\_more | Boolean | false | 是否存在更多记录。   - **true**：存在 - **false**：不存在 |
| leave\_quotas | Leavequotas[] |  | 假期余额列表。 |
| userid | String | user01 | 员工的userId。 |
| leave\_code | String | f84a2xxxx | 假期类型唯一标识。 |
| quota\_cycle | String | 2019 | 额度所对应的周期。 |
| quota\_id | String | f8abb2xxxx | 配额的唯一标记。 |
| start\_time | Number | 1653851001000 | 假期有效期开始时间，毫秒级时间戳。 |
| end\_time | Number | 1753851001000 | 额度有效期结束时间，毫秒级时间戳。 |
| quota\_num\_per\_hour | Number | 1000 | 以小时计算的额度总数。  **[!NOTE]**  假期类型按小时，计算该值不为空且按百分之一小时折算。  例如：1000=10小时。 |
| quota\_num\_per\_day | Number | 1000 | 以天计算的额度总数。  **[!NOTE]**  假期类型按天计算时，该值不为空且按百分之一天折算。  例如：1000=10天。 |
| used\_num\_per\_day | Number | 100 | 以天计算的使用额度。  **[!NOTE]**  假期类型按天计算时，该值不为空且按百分之一天折算。  例如：100=1天。 |
| used\_num\_per\_hour | Number | 1000 | 以小时计算的使用额度。  **[!NOTE]**  假期类型按小时计算时，该值不为空且按百分之一小时折算。  例如：1000=10小时。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "has_more": false,
    "leave_quotas": [
      {
        "end_time": 1753851001000,
        "leave_code": "f84a2xxxx",
        "quota_cycle": "2019",
        "quota_id": "f8abb2xxxx",
        "quota_num_per_day": 1000,
        "start_time": 1653851001000,
        "used_num_per_day": 100,
        "quota_num_per_hour": 1000,
        "userid": "user01",
        "used_num_per_hour": 1000
      }
    ]
  },
  "success": true,
  "request_id": "exz4w88xfo7n"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
