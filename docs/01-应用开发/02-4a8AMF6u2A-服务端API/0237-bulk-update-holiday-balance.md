---
title: "批量更新假期余额"
source_url: "https://open.dingtalk.com/document/development/bulk-update-holiday-balance"
namespace: "development"
slug: "bulk-update-holiday-balance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假期管理 > 批量更新假期余额"
doc_id: "65O7C3gNZP"
updated_at: "2026-05-27 17:06:28"
---

> Source: https://open.dingtalk.com/document/development/bulk-update-holiday-balance
> Path: 应用开发 / 服务端API / 考勤 > 假期管理 > 批量更新假期余额
> Updated: 2026-05-27 17:06:28

# 批量更新假期余额

调用本接口，批量更新假期总余额信息。

## **接口调用说明**

本接口更新假期余额的效果是在假期原有的余额基础上进行加减，并不会影响员工已经消耗的假期额度。

例如，如下图所示的流程说明：

1. 调用[添加假期规则](0233-add-holiday-rules.md)接口创建普通假期，再调用[初始化假期余额](0236-initialize-holiday-balance.md)接口初始化余额是8天。
2. 调用本接口更新张三的假期余额，接口参数**quota\_num\_per\_day**值传的是900，调用结果产生的记录是在原有的余额基础上添加了一天。
3. 张三在钉钉上发起了该请假类型的请假审批单，请假2天，记录产生扣除2天的记录。
4. 调用本接口更新张三的假期余额，接口参数**quota\_num\_per\_day**值传的是1000，调用结果产生的记录是添加了一天，最终余额为8天。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1095238471/p961133.png)

创建假期规则有2种方式，通过调用接口创建、通过钉钉官方应用考勤产品创建：

| 创建假期规则方式 | 调用本接口是否支持更新假期类型 |
| --- | --- |
| 调用[添加假期规则](0233-add-holiday-rules.md)接口创建的假期类型。 | 支持 |
| 企业管理后台考勤应用创建的假期类型。   - 考勤应用系统默认创建。 - 通过考勤应用后台创建 。 | 不支持 |

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/vacation/quota/update |
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
| op\_userid | String | 是 | user01 | 当前企业内拥有**OA审批**应用权限的管理员的userId。 |
| leave\_quotas | LeaveQuotas[] | 是 |  | 待更新的假期余额记录。 |
| userid | String | 是 | user1 | 员工的userId。 |
| end\_time | Number | 否 | 1753851001000 | 额度有效期结束时间，毫秒级时间戳。 |
| start\_time | Number | 否 | 1653851001000 | 额度有效期开始时间，毫秒级时间戳。 |
| leave\_code | String | 是 | f84a2dxxxx | 自定义添加的假期类型。  **[!NOTE]**  此类型必须是通过[添加假期规则](0233-add-holiday-rules.md)接口创建的假期类型。 |
| reason | String | 否 | 管理员导入 | 操作原因。 |
| quota\_num\_per\_day | Number | 否 | 100 | 以天计算的额度总数。  **[!NOTE]**  假期类型按天计算时，该值不为空且按百分之一天折算。  例如：1000=10天。 |
| quota\_num\_per\_hour | Number | 否 | 100 | 以小时计算的额度总数。  **[!NOTE]**  假期类型按小时，计算该值不为空且按百分之一小时折算。  例如：1000=10小时。 |
| quota\_cycle | String | 否 | 2019 | 额度所对应的周期，格式必须是"yyyy"，例如"2021"。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/vacation/quota/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9e10xxxx4ba535' \
-d 'leave_quotas=null' \
-d 'op_userid=zhangsan'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/update");
OapiAttendanceVacationQuotaUpdateRequest req = new OapiAttendanceVacationQuotaUpdateRequest();
List<LeaveQuotas> list = new ArrayList<LeaveQuotas>();
LeaveQuotas leaveQuotas = new LeaveQuotas();
list.add(leaveQuotas);
leaveQuotas.setUserid("user1");
leaveQuotas.setEndTime(1753851001000L);
leaveQuotas.setStartTime(1653851001000L);
leaveQuotas.setLeaveCode("f84a2dxxxx");
leaveQuotas.setReason("管理员导入");
leaveQuotas.setQuotaNumPerDay(100L);
leaveQuotas.setQuotaNumPerHour(100L);
leaveQuotas.setQuotaCycle("2019");
req.setLeaveQuotas(list.toString());
req.setOpUserid("manager1");
OapiAttendanceVacationQuotaUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceVacationQuotaUpdateRequest("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/update")

req.leave_quotas=""
req.op_userid="zhangsan"
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
$req = new OapiAttendanceVacationQuotaUpdateRequest;
$leave_quotas = new LeaveQuotas;
$leave_quotas->userid="zhangsan";
$leave_quotas->end_time="1753851001000";
$leave_quotas->start_time="1653851001000";
$leave_quotas->leave_code="f84a2829-d245-4312-9ff2-0653e5b3abb2";
$leave_quotas->reason="管理员导入";
$leave_quotas->quota_num_per_day="100";
$leave_quotas->quota_num_per_hour="100";
$leave_quotas->quota_cycle="2019";
$req->setLeaveQuotas(array($leave_quotas));
$req->setOpUserid("zhangsan");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/vacation/quota/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/vacation/quota/update");
OapiAttendanceVacationQuotaUpdateRequest req = new OapiAttendanceVacationQuotaUpdateRequest();
List<OapiAttendanceVacationQuotaUpdateRequest.LeaveQuotasDomain> list2 = new List<OapiAttendanceVacationQuotaUpdateRequest.LeaveQuotasDomain>();
OapiAttendanceVacationQuotaUpdateRequest.LeaveQuotasDomain obj3 = new OapiAttendanceVacationQuotaUpdateRequest.LeaveQuotasDomain();
list2.Add(obj3);
obj3.Userid = "zhangsan";
obj3.EndTime = 1753851001000L;
obj3.StartTime = 1653851001000L;
obj3.LeaveCode = "f84a2829-d245-4312-9ff2-0653e5b3abb2";
obj3.Reason = "管理员导入";
obj3.QuotaNumPerDay = 100L;
obj3.QuotaNumPerHour = 100L;
obj3.QuotaCycle = "2019";
req.LeaveQuotas_ = list2;
req.OpUserid = "zhangsan";
OapiAttendanceVacationQuotaUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result[] |  | 返回结果。 |
| reason | String | 假期类型不存在 | 失败原因。 |
| quota | Quota |  | 失败记录。 |
| leave\_code | String | f84a2dxxxx | 假期类型唯一标识。 |
| userid | String | user1 | 员工的userId。 |
| quota\_cycle | String | 2019 | 额度所对应的周期。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否正确访问。   - **true**：是 - **false**：不是 |
| request\_id | String | 6fnd2l2tnodd | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "quota": {
        "leave_code": "f84a2dxxxx",
        "quota_cycle": "2019",
        "userid": "user1"
      },
      "reason": "假期类型不存在"
    }
  ],
  "success": true,
  "request_id": "6fnd2l2tnodd"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
