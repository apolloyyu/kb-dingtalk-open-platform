---
title: "查询假期规则列表"
source_url: "https://open.dingtalk.com/document/development/holiday-type-query"
namespace: "development"
slug: "holiday-type-query"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 查询假期规则列表"
doc_id: "AtQqhMJV9C"
updated_at: "2026-05-27 17:06:29"
---

> Source: https://open.dingtalk.com/document/development/holiday-type-query
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 查询假期规则列表
> Updated: 2026-05-27 17:06:29

# 查询假期规则列表

调用本接口，查询企业内的假期规则列表，包括假期名称、请假单位等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/vacation/type/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_holiday\_readonly-钉钉假期读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 是 | user01 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |
| vacation\_source | String | 否 | all | 假期来源。取值：   - **"all"**：获取的是所有假期类型 - **""**：获取的是调用添加假期规则接口新建的假期。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/vacation/type/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=43aexxxxd897cd9' \
-d 'op_userid=03085665764167' \
-d 'vacation_source=all'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/type/list");
OapiAttendanceVacationTypeListRequest req = new OapiAttendanceVacationTypeListRequest();
req.setOpUserid("user01");
req.setVacationSource("all");
OapiAttendanceVacationTypeListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceVacationTypeListRequest("https://oapi.dingtalk.com/topapi/attendance/vacation/type/list")

req.op_userid="03085665764167"
req.vacation_source="all"
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
$req = new OapiAttendanceVacationTypeListRequest;
$req->setOpUserid("03085665764167");
$req->setVacationSource("all");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/vacation/type/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/type/list");
OapiAttendanceVacationTypeListRequest req = new OapiAttendanceVacationTypeListRequest();
req.OpUserid = "03085665764167";
req.VacationSource = "all";
OapiAttendanceVacationTypeListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 3k4z2hq8pv2x | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| result | Result[] |  | 返回结果。 |
| leave\_code | String | 037477sdfsxxxx | 假期规则唯一标识。 |
| leave\_name | String | 年假 | 假期名称。 |
| leave\_view\_unit | String | day | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| leave\_certificate | LeaveCertificateVo |  | 请假证明。 |
| leave\_certificate.unit | String | hour | 请假证明单位。   - **hour**：小时 - **day**：天 |
| leave\_certificate.duration | Number | 1 | 超过多长时间需提供请假证明。 |
| leave\_certificate.enable | Boolean | false | 是否开启请假证明。   - **true**：开启 - **false**：未开启 |
| leave\_certificate.prompt\_information | String | 请假信息 | 请假提示文案。 |
| submit\_time\_rule | SubmitTimeRuleVo |  | 限时提交规则。 |
| submit\_time\_rule.time\_value | Number | 18 | 限制值。   - 当timeUnit为**day**时，有效值范围是0至30天； - timeUnit为**hour**时，有效值范围是0至24小时。 |
| submit\_time\_rule.time\_unit | String | hour | 时间单位。   - **day**：天 - **hour**：小时 |
| submit\_time\_rule.time\_type | String | before | 限制类型。   - **before**：提前 - **after**：补交 |
| submit\_time\_rule.enable\_time\_limit | Boolean | false | 是否开启限时提交功能。   - **true**：开启 - **false**：不开启 |
| biz\_type | String | general\_leave | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| natural\_day\_leave | String | true | 是否按照自然日统计请假时长。   - **true**：按照自然日统计请假时长 - **false**：不按照自然日统计请假时长  **[!NOTE]**  当为**false**时，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。 |
| validity\_type | String | absolute\_time | 有效类型。   - **absolute\_time**：绝对时间 - **relative\_time**：相对时间 |
| validity\_value | String | 12-31 | 延长日期。   - 当validity\_type为**absolute\_time**该值不为空且满足“yy-mm”格式。 - 当validity\_type为**relative\_time**该值为大于1的整数。 |
| hours\_in\_per\_day | Number | 1000 | 每天折算的工作时长，百分之一。  例如：1天=10小时=1000。 |
| source | String | inner | 假期来源。   - **external**：开放接口自定义的 - **inner**：oa后台新建的 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "biz_type": "general_leave",
      "hours_in_per_day": 1000,
      "leave_code": "037477sdfsxxxx",
      "leave_name": "年假",
      "leave_view_unit": "day",
      "leave_certificate": {
        "unit": "hour",
        "duration": "1",
        "enable": false,
        "prompt_information": "请假信息"
      },
      "submit_time_rule": {
        "time_value": 18,
        "time_unit": "day",
        "time_type": "before",
        "enable_time_limit": false
      },
      "validity_type": "absolute_time",
      "natural_day_leave": "true",
      "validity_value": "12-31",
      "source": "external"
    }
  ],
  "success": true,
  "request_id": "3k4z2hq8pv2x"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
