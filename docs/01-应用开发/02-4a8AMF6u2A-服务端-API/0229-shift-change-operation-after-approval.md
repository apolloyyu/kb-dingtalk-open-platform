---
title: "通知换班通过"
source_url: "https://open.dingtalk.com/document/development/shift-change-operation-after-approval"
namespace: "development"
slug: "shift-change-operation-after-approval"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 假勤审批 > 通知换班通过"
doc_id: "95Fb8pWqlm"
updated_at: "2026-05-27 17:06:23"
---

> Source: https://open.dingtalk.com/document/development/shift-change-operation-after-approval
> Path: 应用开发 / 服务端 API / 考勤 > 假勤审批 > 通知换班通过
> Updated: 2026-05-27 17:06:23

# 通知换班通过

通过本接口，换班审批通过后，通知考勤执行换班动作，可以和自己换班，也可以和别人换班。

## **接口调用说明**

换班约束条件如下：

- 换班双方必须都在排班制考勤组。
- 换班日期和还班日期双方必须都要有排班或排休。
- 换完班后的打卡时间不能有冲突。例如1号的排班是8：00-22：00，2号的排班是10：00-次日9：00，假如1号和2号换班。换完班后1号的排班是10：00-次日9：00，2号的排班是8：00-22：00，此时1号的打卡时间范围内包含了2号上班时间，这种情况称之为打卡时间冲突。
- 换班不支持撤销。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager123 | 发起人的userId。 |
| switch\_date | String | 是 | 2019-09-08 | 申请换班日期，当天必须有排班或排休。 |
| reback\_date | String | 是 | 2019-09-09 | 还班日期，当天必须有排班或排休。  **[!NOTE]**  如果申请换班人和被换班人是同一个人，那么必须要有还班日期。 |
| apply\_userid | String | 是 | manager123 | 申请换班人的userId，仅支持排班制考勤组用户。 |
| target\_userid | String | 是 | user123 | 被换班人的userId，仅支持排班制考勤组用户。 |
| approve\_id | String | 是 | 2376620852 | 审批单ID，自定义参数值。 |
| apply\_shift\_id | Number | 是 | 1234566 | 申请人换班日期当天的班次ID，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取shift\_id参数值。 |
| target\_shift\_id | Number | 是 | 1234566 | 被换班人换班日期当天的班次ID，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取shift\_id参数值。 |
| reback\_apply\_shift\_id | Number | 是 | 1234566 | 申请人还班日期当天的班次ID，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取shift\_id参数值。 |
| reback\_target\_shift\_id | Number | 是 | 1234566 | 被换班人还班日期当天的班次ID，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取shift\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=82683xxxxc28be8' \
-d 'apply_shift_id=123' \
-d 'apply_userid=dd_dd' \
-d 'approve_id=asdasdjashd' \
-d 'reback_apply_shift_id=789' \
-d 'reback_date=2019-09-09' \
-d 'reback_target_shift_id=897' \
-d 'switch_date=2019-09-08' \
-d 'target_shift_id=456' \
-d 'target_userid=aa_aa' \
-d 'userid=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch");
OapiAttendanceApproveScheduleSwitchRequest req = new OapiAttendanceApproveScheduleSwitchRequest();
req.setUserid("dd_dd");
req.setSwitchDate("2019-09-08");
req.setRebackDate("2019-09-09");
req.setApplyUserid("dd_dd");
req.setTargetUserid("aa_aa");
req.setApplyShiftId(123L);
req.setTargetShiftId(456L);
req.setRebackApplyShiftId(789L);
req.setRebackTargetShiftId(897L);
req.setApproveId("asdasdjashd");
OapiAttendanceApproveScheduleSwitchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceApproveScheduleSwitchRequest("https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch")

req.userid="dd_dd"
req.switch_date="2019-09-08"
req.reback_date="2019-09-09"
req.apply_userid="dd_dd"
req.target_userid="aa_aa"
req.apply_shift_id=123
req.target_shift_id=456
req.reback_apply_shift_id=789
req.reback_target_shift_id=897
req.approve_id="asdasdjashd"
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
$req = new OapiAttendanceApproveScheduleSwitchRequest;
$req->setUserid("dd_dd");
$req->setSwitchDate("2019-09-08");
$req->setRebackDate("2019-09-09");
$req->setApplyUserid("dd_dd");
$req->setTargetUserid("aa_aa");
$req->setApplyShiftId("123");
$req->setTargetShiftId("456");
$req->setRebackApplyShiftId("789");
$req->setRebackTargetShiftId("897");
$req->setApproveId("asdasdjashd");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/schedule/switch");
OapiAttendanceApproveScheduleSwitchRequest req = new OapiAttendanceApproveScheduleSwitchRequest();
req.Userid = "dd_dd";
req.SwitchDate = "2019-09-08";
req.RebackDate = "2019-09-09";
req.ApplyUserid = "dd_dd";
req.TargetUserid = "aa_aa";
req.ApplyShiftId = 123L;
req.TargetShiftId = 456L;
req.RebackApplyShiftId = 789L;
req.RebackTargetShiftId = 897L;
req.ApproveId = "asdasdjashd";
OapiAttendanceApproveScheduleSwitchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
        "errcode":0,
        "errmsg":"872995737"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
