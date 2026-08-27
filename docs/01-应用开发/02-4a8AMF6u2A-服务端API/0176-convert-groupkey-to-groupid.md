---
title: "groupKey转换为groupId"
source_url: "https://open.dingtalk.com/document/development/convert-groupkey-to-groupid"
namespace: "development"
slug: "convert-groupkey-to-groupid"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > groupKey转换为groupId"
doc_id: "s82TAy4EGU"
updated_at: "2026-05-27 13:09:48"
---

> Source: https://open.dingtalk.com/document/development/convert-groupkey-to-groupid
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > groupKey转换为groupId
> Updated: 2026-05-27 13:09:48

# groupKey转换为groupId

调用本接口，将考勤组的groupKey转换为groupId。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/groups/keytoid |
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
| op\_user\_id | String | 是 | user01 | 操作人的userId。 |
| group\_key | String | 是 | 02B1Exxxx | 考勤组ID，旧考勤组标识，可调用[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)接口获取group\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/groups/keytoid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=40bafxxxx9d3b06' \
-d 'group_key=0151E0xxxxA917E876' \
-d 'op_user_id=123'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/groups/keytoid");
OapiAttendanceGroupsKeytoidRequest req = new OapiAttendanceGroupsKeytoidRequest();
req.setOpUserId("user01");
req.setGroupKey("02B1Exxxx");
OapiAttendanceGroupsKeytoidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupsKeytoidRequest("https://oapi.dingtalk.com/topapi/attendance/groups/keytoid")

req.op_user_id="123"
req.group_key="0151E022xxxx917E876"
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
$req = new OapiAttendanceGroupsKeytoidRequest;
$req->setOpUserId("123");
$req->setGroupKey("0151E02xxxx17E876");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/groups/keytoid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/groups/keytoid");
OapiAttendanceGroupsKeytoidRequest req = new OapiAttendanceGroupsKeytoidRequest();
req.OpUserId = "123";
req.GroupKey = "0151E0xxxx7E876";
OapiAttendanceGroupsKeytoidResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Number | 685935028 | 考勤组ID。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 3yt2gu3zz0qi | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "result":685935028,
  "errmsg":"ok",
  "success":true,
  "request_id":"3yt2gu3zz0qi"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
