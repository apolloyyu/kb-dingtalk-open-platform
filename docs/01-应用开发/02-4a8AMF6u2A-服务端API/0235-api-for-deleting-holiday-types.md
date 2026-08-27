---
title: "删除假期规则"
source_url: "https://open.dingtalk.com/document/development/api-for-deleting-holiday-types"
namespace: "development"
slug: "api-for-deleting-holiday-types"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 删除假期规则"
doc_id: "LUjrsRMAeh"
updated_at: "2026-05-27 17:06:26"
---

> Source: https://open.dingtalk.com/document/development/api-for-deleting-holiday-types
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 删除假期规则
> Updated: 2026-05-27 17:06:26

# 删除假期规则

调用本接口，删除指定的假期规则。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_holiday\_manage-钉钉假期管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| leave\_code | String | 是 | 03747xxxx | 假期规则唯一标识，可通过[查询假期规则列表](0238-holiday-type-query.md)接口获取leave\_code参数值。 |
| op\_userid | String | 是 | user01 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3acaxxxxa30a2' \
-d 'leave_code=037477axxxxae5e7973' \
-d 'op_userid=03085665764167'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete");
OapiAttendanceVacationTypeDeleteRequest req = new OapiAttendanceVacationTypeDeleteRequest();
req.setLeaveCode("03747xxxx");
req.setOpUserid("user01");
OapiAttendanceVacationTypeDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceVacationTypeDeleteRequest("https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete")

req.leave_code="03747xxxx7973"
req.op_userid="03085665764167"
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
$req = new OapiAttendanceVacationTypeDeleteRequest;
$req->setLeaveCode("03747xxxx7973");
$req->setOpUserid("03085665764167");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/type/delete");
OapiAttendanceVacationTypeDeleteRequest req = new OapiAttendanceVacationTypeDeleteRequest();
req.LeaveCode = "0374xxxx7973";
req.OpUserid = "03085665764167";
OapiAttendanceVacationTypeDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | LeaveTypeVo |  | 返回结果。 |
| leave\_code | String | 03747xxxx | 假期规则唯一标识。 |
| leave\_name | String | 年假 | 假期名称。 |
| leave\_view\_unit | String | day | 请假单位。   - **day**：天 - **halfDay**：半天 - **hour**：小时 |
| biz\_type | String | general\_leave | 假期类型。   - **general\_leave**：普通假期 - **lieu\_leave**：加班转调休 |
| natural\_day\_leave | Boolean | true | 是否按照自然日统计请假时长。   - **true**：按照自然日统计请假时长 - **false**：不按照自然日统计请假时长。  **[!NOTE]**  当为**false**时，用户发起请假时，会根据用户在请假时间段内的排班情况来计算请假时长。 |
| hours\_in\_per\_day | Number | 1000 | 每天折算的工作时长，百分之一。  例如：1天=10小时=1000。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| request\_id | String | xss3trk3zypq | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "biz_type": "general_leave",
    "hours_in_per_day": 1000,
    "leave_code": "03747xxxx",
    "leave_name": "年假",
    "leave_view_unit": "day",
    "natural_day_leave": true
  },
  "success": true,
  "request_id": "xss3trk3zypq"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
