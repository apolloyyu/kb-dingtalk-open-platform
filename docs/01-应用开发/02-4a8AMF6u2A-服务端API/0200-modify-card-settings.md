---
title: "修改打卡时段设置"
source_url: "https://open.dingtalk.com/document/development/modify-card-settings"
namespace: "development"
slug: "modify-card-settings"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤班次 > 修改打卡时段设置"
doc_id: "7xGAIG6OZo"
updated_at: "2026-05-27 17:05:57"
---

> Source: https://open.dingtalk.com/document/development/modify-card-settings
> Path: 应用开发 / 服务端API / 考勤 > 考勤班次 > 修改打卡时段设置
> Updated: 2026-05-27 17:05:57

# 修改打卡时段设置

调用本接口，修改考勤班次打卡时间的设置信息。本接口目前仅支持设置卡点情况下是否打卡。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | af21axxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | user456 | 操作者的userId。 |
| punches | TopPunchVO[] | 否 |  | 卡点信息。 |
| id | Number | 是 | 123 | 卡点ID， 可通过[获取班次详情](0204-shift-query.md)接口获取id参数值。 |
| free\_check | Boolean | 是 | true | 是否无需打卡。   - **true**：开启无需打卡。 - **false**：关闭无需打卡。 |
| shift\_id | Number | 是 | 456 | 班次ID， 可通过[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口获取id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=16869xxx0e890' \
-d 'op_user_id=dd' \
-d 'punches=null' \
-d 'shift_id=456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches");
OapiAttendanceShiftUpdatepunchesRequest req = new OapiAttendanceShiftUpdatepunchesRequest();
List<TopPunchVO> punchVOS = new ArrayList<>();
TopPunchVO punchVO = new TopPunchVO();
punchVO.setFreeCheck(true);
punchVO.setId(373271823L);
req.setPunches(punchVOS);
req.setOpUserId("user456");
req.setShiftId(712550377L);
OapiAttendanceShiftUpdatepunchesResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftUpdatepunchesRequest("https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches")

req.op_user_id="dd"
req.punches=""
req.shift_id=456
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
$req = new OapiAttendanceShiftUpdatepunchesRequest;
$req->setOpUserId("dd");
$punches = new TopPunchVO;
$punches->id="123";
$punches->free_check="true";
$req->setPunches(array($punches));
$req->setShiftId("456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/updatepunches");
OapiAttendanceShiftUpdatepunchesRequest req = new OapiAttendanceShiftUpdatepunchesRequest();
req.OpUserId = "dd";
List<OapiAttendanceShiftUpdatepunchesRequest.TopPunchVODomain> list2 = new List<OapiAttendanceShiftUpdatepunchesRequest.TopPunchVODomain>();
OapiAttendanceShiftUpdatepunchesRequest.TopPunchVODomain obj3 = new OapiAttendanceShiftUpdatepunchesRequest.TopPunchVODomain();
list2.Add(obj3);
obj3.Id = 123L;
obj3.FreeCheck = true;
req.Punches_ = list2;
req.ShiftId = 456L;
OapiAttendanceShiftUpdatepunchesResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 系统错误 | 调用失败时返回的错误信息。 |
| request\_id | String | 5moh5icna65x | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "request_id": "ed67bcymo0bw"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
