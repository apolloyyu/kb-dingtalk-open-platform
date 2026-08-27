---
title: "groupId转换为groupKey"
source_url: "https://open.dingtalk.com/document/development/groupid-to-groupkey"
namespace: "development"
slug: "groupid-to-groupkey"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > groupId转换为groupKey"
doc_id: "uqXy4szXgc"
updated_at: "2026-05-27 13:09:49"
---

> Source: https://open.dingtalk.com/document/development/groupid-to-groupkey
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > groupId转换为groupKey
> Updated: 2026-05-27 13:09:49

# groupId转换为groupKey

调用本接口，将考勤组的groupId转换为groupKey。groupKey为考群组新版字段的标识，部分考勤组需要使用groupKey为参数，如果当前仅有考勤组groupId字段，可调用本接口获取groupKey。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/groups/idtokey |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 否 | user01 | 操作人的userId。 |
| group\_id | Number | 是 | 1586536 | 考勤组ID，可调用[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)接口获取group\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/groups/idtokey" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ea55fdxxxx64242a' \
-d 'group_id=12' \
-d 'op_user_id=123'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/groups/idtokey");
OapiAttendanceGroupsIdtokeyRequest req = new OapiAttendanceGroupsIdtokeyRequest();
req.setOpUserId("user01");
req.setGroupId(1586536L);
OapiAttendanceGroupsIdtokeyResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupsIdtokeyRequest("https://oapi.dingtalk.com/topapi/attendance/groups/idtokey")

req.op_user_id="123"
req.group_id=12
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
$req = new OapiAttendanceGroupsIdtokeyRequest;
$req->setOpUserId("123");
$req->setGroupId("12");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/groups/idtokey");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/groups/idtokey");
OapiAttendanceGroupsIdtokeyRequest req = new OapiAttendanceGroupsIdtokeyRequest();
req.OpUserId = "123";
req.GroupId = 12L;
OapiAttendanceGroupsIdtokeyResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | 0151E0223B1xxxx | 考勤组ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 3yt2gu3zz0qi | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "result":0151E0223B1xxxx,
  "errmsg":"ok",
  "request_id":"3yt2gu3zz0qi"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
