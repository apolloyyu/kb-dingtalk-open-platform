---
title: "批量删除参与考勤人员"
source_url: "https://open.dingtalk.com/document/development/batch-delete-employees-under-the-attendance-group"
namespace: "development"
slug: "batch-delete-employees-under-the-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 批量删除参与考勤人员"
doc_id: "5zgraY0YEc"
updated_at: "2026-05-27 13:09:59"
---

> Source: https://open.dingtalk.com/document/development/batch-delete-employees-under-the-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 批量删除参与考勤人员
> Updated: 2026-05-27 13:09:59

# 批量删除参与考勤人员

调用本接口，批量删除指定考勤组下的考勤组成员。

## **接口调用说明**

本接口只支持删除考勤组内参与考勤的人员，不支持删除参与考勤的部门。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/users/remove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b153xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | 0151E0223B1xxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |
| user\_id\_list | String[] | 是 | user01,user02 | 用户列表，每次调用最多传100个userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/users/remove" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=49ceexxxx4c192' \
-d 'group_key=0151E022xxxx917E876' \
-d 'op_userid=123456' \
-d 'user_id_list=123456%2C123457'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/remove");
OapiAttendanceGroupUsersRemoveRequest req = new OapiAttendanceGroupUsersRemoveRequest();
req.setOpUserid("user01");
req.setGroupKey("0151E0223B1xxxx");
req.setUserIdList("user01,user02");
OapiAttendanceGroupUsersRemoveResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupUsersRemoveRequest("https://oapi.dingtalk.com/topapi/attendance/group/users/remove")

req.op_userid="123456"
req.group_key="0151E022xxxx17E876"
req.user_id_list="123456,123457"
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
$req = new OapiAttendanceGroupUsersRemoveRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151E0xxxx7E876");
$req->setUserIdList("123456,123457");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/users/remove");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/remove");
OapiAttendanceGroupUsersRemoveRequest req = new OapiAttendanceGroupUsersRemoveRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E0xxxx17E876";
req.UserIdList = "123456,123457";
OapiAttendanceGroupUsersRemoveResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| error\_info\_list | ErrorInfo[] |  | 错误列表。 |
| failure\_list | String[] |  | 失败列表。 |
| msg | String | business fault | 错误描述。 |
| code | String | 1000 | 错误码。 |
| success\_list | String[] |  | 成功列表。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 47qflcctatn2 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "success_list": [
      "user01",
      "user02"
    ]
  },
  "success": true,
  "request_id": "47qflcctatn2"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
