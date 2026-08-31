---
title: "删除考勤组"
source_url: "https://open.dingtalk.com/document/development/delete-attendance-group"
namespace: "development"
slug: "delete-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 删除考勤组"
doc_id: "lSxG7cUdwp"
updated_at: "2026-05-27 13:09:44"
---

> Source: https://open.dingtalk.com/document/development/delete-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 删除考勤组
> Updated: 2026-05-27 13:09:44

# 删除考勤组

调用本接口，根据考勤组group\_key删除考勤组。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | 0151E02xxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0d5exxxxf31e2da' \
-d 'group_key=0151E02xxxx1A917E876' \
-d 'op_userid=123456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/delete");
OapiAttendanceGroupDeleteRequest req = new OapiAttendanceGroupDeleteRequest();
req.setOpUserid("user01");
req.setGroupKey("0151E02xxxx");
OapiAttendanceGroupDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupDeleteRequest("https://oapi.dingtalk.com/topapi/attendance/group/delete")

req.op_userid="123456"
req.group_key="0151Exxxx7E876"
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
$req = new OapiAttendanceGroupDeleteRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151Exxxx17E876");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/delete");
OapiAttendanceGroupDeleteRequest req = new OapiAttendanceGroupDeleteRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E0xxxxE876";
OapiAttendanceGroupDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | BE8C35586xxxx | 考勤组id。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 3x1mikbgn3ca | 请求ID。 |

### **响应体示例**

```
{
    "errcode": 0,
    "errmsg":"ok",
    "result": "BE8C35586xxxx",
    "success": true,
    "request_id": "3x1mikbgn3ca"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
