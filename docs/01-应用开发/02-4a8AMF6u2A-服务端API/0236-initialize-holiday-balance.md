---
title: "初始化假期余额"
source_url: "https://open.dingtalk.com/document/development/initialize-holiday-balance"
namespace: "development"
slug: "initialize-holiday-balance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 初始化假期余额"
doc_id: "7oXpa5mZAH"
updated_at: "2026-05-27 17:06:27"
---

> Source: https://open.dingtalk.com/document/development/initialize-holiday-balance
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 初始化假期余额
> Updated: 2026-05-27 17:06:27

# 初始化假期余额

调用本接口，实现对某个员工多个普通假期余额进行初始化的操作。

## **接口调用说明**

调休假期类型无需调用初始化接口，调休假期类型是加班时长自动转为调休假期时长。创建假期规则有2种方式，通过调用接口创建、通过钉钉官方应用考勤产品创建：

| 创建假期规则方式 | 调用本接口是否支持更新假期类型 |
| --- | --- |
| 调用[添加假期规则](0233-add-holiday-rules.md)接口创建的假期类型。 | 支持 |
| 企业管理后台考勤应用创建的假期类型。   - 考勤应用系统默认创建。 - 通过考勤应用后台创建 。 | 不支持 |

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init |
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
| op\_userid | String | 是 | manager1 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |
| leave\_quotas | LeaveQuotas | 是 |  | 待初始化的假期余额记录。 |
| userid | String | 是 | zhangsan | 员工的userId。 |
| end\_time | Number | 是 | 1653851001000 | 额度有效期结束时间，毫秒级时间戳。 |
| start\_time | Number | 是 | 1553851001000 | 额度有效期开始时间，毫秒级时间戳。 |
| leave\_code | String | 是 | f84a282xxxx | 假期类型唯一标识。  **[!NOTE]**   - 支持初始化调用[添加假期规则](0233-add-holiday-rules.md)接口添加的假期类型。 - 不支持初始化企业自带的假期。 |
| reason | String | 否 | 管理员导入 | 操作原因。 |
| quota\_num\_per\_day | Number | 否 | 100 | 以天计算的额度总数。  **[!NOTE]**  假期类型按天计算时，该值不为空且按百分之一天折算。  例如：1000=10天。 |
| quota\_num\_per\_hour | Number | 否 | 100 | 以小时计算的额度总数。  **[!NOTE]**  假期类型按小时，计算该值不为空且按百分之一小时折算。  例如：1000=10小时。 |
| quota\_cycle | String | 否 | 2019 | 额度所对应的周期。  **[!NOTE]**  格式必须满足“yyyy”。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d82be2bxxxx023' \
-d 'leave_quotas=null' \
-d 'op_userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init");
OapiAttendanceVacationQuotaInitRequest req = new OapiAttendanceVacationQuotaInitRequest();
req.setOpUserid("zhangsan");
List<LeaveQuotas> list = new ArrayList<LeaveQuotas>();
LeaveQuotas leaveQuotas = new LeaveQuotas();
list.add(leaveQuotas);
leaveQuotas.setUserid("user1");
leaveQuotas.setEndTime(1653851001000L);
leaveQuotas.setStartTime(1553851001000L);
leaveQuotas.setLeaveCode("f84a2829-xxxx0653");
leaveQuotas.setReason("管理员导入");
leaveQuotas.setQuotaNumPerDay(100L);
leaveQuotas.setQuotaNumPerHour(100L);
leaveQuotas.setQuotaCycle("2019");
req.setLeaveQuotas(list);
OapiAttendanceVacationQuotaInitResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceVacationQuotaInitRequest("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init")

req.op_userid="zhangsan"
req.leave_quotas=""
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
$req = new OapiAttendanceVacationQuotaInitRequest;
$req->setOpUserid("zhangsan");
$leave_quotas = new LeaveQuotas;
$leave_quotas->userid="zhangsan";
$leave_quotas->end_time="1653851001000";
$leave_quotas->start_time="1553851001000";
$leave_quotas->leave_code="f84a2829-d245-4312-9ff2-0653e5b3abb2";
$leave_quotas->reason="管理员导入";
$leave_quotas->quota_num_per_day="100";
$leave_quotas->quota_num_per_hour="100";
$leave_quotas->quota_cycle="2019";
$req->setLeaveQuotas(array($leave_quotas));
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/init");
OapiAttendanceVacationQuotaInitRequest req = new OapiAttendanceVacationQuotaInitRequest();
req.OpUserid = "zhangsan";
List<OapiAttendanceVacationQuotaInitRequest.LeaveQuotasDomain> list2 = new List<OapiAttendanceVacationQuotaInitRequest.LeaveQuotasDomain>();
OapiAttendanceVacationQuotaInitRequest.LeaveQuotasDomain obj3 = new OapiAttendanceVacationQuotaInitRequest.LeaveQuotasDomain();
list2.Add(obj3);
obj3.Userid = "zhangsan";
obj3.EndTime = 1653851001000L;
obj3.StartTime = 1553851001000L;
obj3.LeaveCode = "f84a2829-d245-4312-9ff2-0653e5b3abb2";
obj3.Reason = "管理员导入";
obj3.QuotaNumPerDay = 100L;
obj3.QuotaNumPerHour = 100L;
obj3.QuotaCycle = "2019";
req.LeaveQuotas_ = list2;
OapiAttendanceVacationQuotaInitResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result[] |  | 返回结果。 |
| reason | String | 按天计算的额度不能为空 | 失败原因。 |
| quota | Quota |  | 失败记录。 |
| leave\_code | String | f84a2829-xxxx0653 | 假期类型唯一标识。 |
| userid | String | user1 | 员工的userId。 |
| quota\_cycle | String | 2019 | 额度所对应的周期。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 调用失败时返回的错误信息。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| request\_id | String | zq4aec1jton8 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": [
    {
      "quota": {
        "leave_code": "f84a2829-xxxx0653",
        "userid": "10203029011219896"
      },
      "reason": "按天计算的额度不能为空"
    }
  ],
  "success": true,
  "request_id": "zq4aec1jton8"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
