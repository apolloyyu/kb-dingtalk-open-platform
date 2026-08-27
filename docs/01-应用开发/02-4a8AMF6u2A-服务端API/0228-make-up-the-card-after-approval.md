---
title: "通知补卡通过"
source_url: "https://open.dingtalk.com/document/development/make-up-the-card-after-approval"
namespace: "development"
slug: "make-up-the-card-after-approval"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 假勤审批 > 通知补卡通过"
doc_id: "DCX51D9HBf"
updated_at: "2026-05-27 17:06:22"
---

> Source: https://open.dingtalk.com/document/development/make-up-the-card-after-approval
> Path: 应用开发 / 服务端API / 考勤 > 假勤审批 > 通知补卡通过
> Updated: 2026-05-27 17:06:22

# 通知补卡通过

调用本接口，通知考勤补卡通过。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/approve/check |
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
| userid | String | 是 | manager4220 | 员工的userId。 |
| work\_date | String | 是 | 2019-08-15 | 要补卡的时间，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取的work\_date值。 |
| punch\_id | Number | 是 | 176877195378 | 要补的排班ID，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取的shift\_id值。 |
| punch\_check\_time | String | 是 | 2019-08-15 08:00 | 排班的打卡时间，可通过[批量查询人员排班信息](0206-query-batch-scheduling-information.md)接口获取的plan\_check\_time值。 |
| user\_check\_time | String | 是 | 2019-08-15 07:59 | 用户打卡时间。 |
| approve\_id | String | 是 | aasdv13124 | 审批单ID，自定义值。 |
| jump\_url | String | 是 | https://open.dingtalk.com/ | 审批单跳转地址。 |
| tag\_name | String | 是 | 补卡 | 审批单名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/create?access_token=YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "create_report_param": {
   
    }
  }'
```

Java

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/approve/check" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1eddxxxxca1a1' \
-d 'approve_id=aasdv13124' \
-d 'jump_url=https%3A%2F%2Fxxx.xxx' \
-d 'punch_check_time=2019-08-15+08%3A00' \
-d 'punch_id=12345' \
-d 'tag_name=%E8%A1%A5%E5%8D%A1' \
-d 'user_check_time=2019-08-15+07%3A59' \
-d 'userid=dd_dd' \
-d 'work_date=2019-08-15'
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceApproveCheckRequest("https://oapi.dingtalk.com/topapi/attendance/approve/check")

req.userid="dd_dd"
req.work_date="2019-08-15"
req.punch_id=12345
req.punch_check_time="2019-08-15 08:00"
req.user_check_time="2019-08-15 07:59"
req.approve_id="aasdv13124"
req.jump_url="https://xxx.xxx"
req.tag_name="补卡"
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
$req = new OapiAttendanceApproveCheckRequest;
$req->setUserid("dd_dd");
$req->setWorkDate("2019-08-15");
$req->setPunchId("12345");
$req->setPunchCheckTime("2019-08-15 08:00");
$req->setUserCheckTime("2019-08-15 07:59");
$req->setApproveId("aasdv13124");
$req->setJumpUrl("https://xxx.xxx");
$req->setTagName("补卡");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/approve/check");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/check");
OapiAttendanceApproveCheckRequest req = new OapiAttendanceApproveCheckRequest();
req.Userid = "dd_dd";
req.WorkDate = "2019-08-15";
req.PunchId = 12345L;
req.PunchCheckTime = "2019-08-15 08:00";
req.UserCheckTime = "2019-08-15 07:59";
req.ApproveId = "aasdv13124";
req.JumpUrl = "https://xxx.xxx";
req.TagName = "补卡";
OapiAttendanceApproveCheckResponse rsp = client.Execute(req, access_token);
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
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
