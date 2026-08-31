---
title: "获取考勤组详情"
source_url: "https://open.dingtalk.com/document/development/query-a-single-attendance-group"
namespace: "development"
slug: "query-a-single-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 获取考勤组详情"
doc_id: "jN14RqfFQy"
updated_at: "2026-05-27 13:09:46"
---

> Source: https://open.dingtalk.com/document/development/query-a-single-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 获取考勤组详情
> Updated: 2026-05-27 13:09:46

# 获取考勤组详情

调用本接口根据考勤组ID获取考勤组详情，例如考勤组名称、考勤组主负责人和考勤类型等信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/query |
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
| op\_user\_id | String | 是 | user123 | 操作人userId。 |
| group\_id | Number | 是 | 685935028 | 考勤组ID，可调用[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)接口获取group\_id参数值。  **[!NOTE]**  如果是旧考勤组标识即group\_key，可调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将group\_key转换为group\_id。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=65671xxxx92ddf0' \
-d 'group_id=23456' \
-d 'op_user_id=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/query");
OapiAttendanceGroupQueryRequest req = new OapiAttendanceGroupQueryRequest();
req.setOpUserId("dd_dd");
req.setGroupId(23456L);
OapiAttendanceGroupQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupQueryRequest("https://oapi.dingtalk.com/topapi/attendance/group/query")

req.op_user_id="dd_dd"
req.group_id=23456
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
$req = new OapiAttendanceGroupQueryRequest;
$req->setOpUserId("dd_dd");
$req->setGroupId("23456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/query");
OapiAttendanceGroupQueryRequest req = new OapiAttendanceGroupQueryRequest();
req.OpUserId = "dd_dd";
req.GroupId = 23456L;
OapiAttendanceGroupQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopSimpleGroupVO |  | 返回结果。 |
| name | String | 考勤 | 考勤组名称。 |
| shift\_ids | Number[] | [677995086] | 排班ID。 |
| id | Number | 685935028 | 考勤组ID。 |
| wifis | String[] | ["test-inc"] | wifi名称。 |
| address\_list | String[] | ["西溪湿地"] | 考勤地址。 |
| work\_day\_list | Number[] | [0,1,2,3] | 工作日。 |
| member\_count | Number | 39 | 人员人数。 |
| type | String | TURN | 考勤组类型。   - **FIXED：**代表固定班制考勤组 - **TURN：**代表排班制考勤组 - **NONE：**代表自由工时考勤组 |
| url | String | https://attend.dingtalk.com/xxxx | 跳转链接。 |
| manager\_list | String | user456 | 考勤组管理员。 |
| owner\_user\_id | String | user01 | 考勤组主负责人的userId。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 72hycvnsyykp | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "address_list": [
      "西溪湿地"
    ],
    "id": 685935028,
    "manager_list": "[user456]",
    "member_count": 1,
    "name": "考勤",
    "owner_user_id": "user01",
    "shift_ids": [
      677995086
    ],
    "type": "TURN",
    "url": "https://attend.dingtalk.com/xxxx",
    "wifis": [
      "test-inc"
    ],
    "work_day_list": [
      0,
      677995086,
      677995086,
      677995086,
      677995086,
      678215070,
      0
    ]
  },
  "success": true,
  "request_id": "lps4czm0g3qu"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
