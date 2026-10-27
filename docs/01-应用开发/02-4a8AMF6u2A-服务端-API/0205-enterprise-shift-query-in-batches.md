---
title: "获取班次摘要信息"
source_url: "https://open.dingtalk.com/document/development/enterprise-shift-query-in-batches"
namespace: "development"
slug: "enterprise-shift-query-in-batches"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤班次 > 获取班次摘要信息"
doc_id: "TyJPQsLM4X"
updated_at: "2026-05-27 17:06:01"
---

> Source: https://open.dingtalk.com/document/development/enterprise-shift-query-in-batches
> Path: 应用开发 / 服务端 API / 考勤 > 考勤班次 > 获取班次摘要信息
> Updated: 2026-05-27 17:06:01

# 获取班次摘要信息

调用本接口，查询所有的班次信息。在钉钉考勤应用中，班次是一类具有相同的打卡时间、休息时间等规则的组合，企业可根据实际业务设置多个班次。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/shift/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | manager4220 | 操作人userId。 |
| cursor | Number | 否 | 0 | 游标ID，起始值为0。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/shift/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e47ef3ff-ff01-4da7-8aa8-53bc0ad47be3' \
-d 'cursor=1234' \
-d 'op_user_id=dd_test'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/list");
OapiAttendanceShiftListRequest req = new OapiAttendanceShiftListRequest();
req.setOpUserId("dd_test");
req.setCursor(0L);
OapiAttendanceShiftListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceShiftListRequest("https://oapi.dingtalk.com/topapi/attendance/shift/list")

req.op_user_id="dd_test"
req.cursor=1234
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
$req = new OapiAttendanceShiftListRequest;
$req->setOpUserId("dd_test");
$req->setCursor("1234");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/shift/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/list");
OapiAttendanceShiftListRequest req = new OapiAttendanceShiftListRequest();
req.OpUserId = "dd_test";
req.Cursor = 1234L;
OapiAttendanceShiftListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult |  | 查询结果。 |
| has\_more | Boolean | false | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| cursor | Number | 678215070 | 下一页的游标位置。 |
| result | TopMinimalismShiftVo[] |  | 班次信息。  每页返回200条，大于200条将分页返回。 |
| name | String | A | 班次名称。 |
| id | Number | 677995086 | 班次ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 1079sd06ne6zy | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "cursor": 678215070,
    "has_more": false,
    "result": [
      {
        "id": 677995086,
        "name": "A"
      },
      {
        "id": 678215070,
        "name": "B"
      }
    ]
  },
  "success": true,
  "request_id": "1079sd06ne6zy"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
