---
title: "批量新增参与考勤人员"
source_url: "https://open.dingtalk.com/document/development/batch-add-employees-under-the-attendance-group"
namespace: "development"
slug: "batch-add-employees-under-the-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 批量新增参与考勤人员"
doc_id: "zmq1jvTrym"
updated_at: "2026-05-27 13:09:53"
---

> Source: https://open.dingtalk.com/document/development/batch-add-employees-under-the-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 批量新增参与考勤人员
> Updated: 2026-05-27 13:09:53

# 批量新增参与考勤人员

调用本接口根据考勤组groupKey，批量新增参与考勤人员到指定考勤组。该接口只支持添加员工，不支持添加部门。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/users/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b1534xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人userid。 |
| group\_key | String | 是 | CEDDxxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |
| user\_id\_list | String[] | 是 | user02,user03 | 用户列表，最大值100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/users/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e0f3d9xxxxa9b71' \
-d 'group_key=0151E0xxxx917E876' \
-d 'op_userid=123456' \
-d 'user_id_list=123456%2C123457'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/add");
OapiAttendanceGroupUsersAddRequest req = new OapiAttendanceGroupUsersAddRequest();
req.setOpUserid("user01");
req.setGroupKey("CEDDxxxx");
req.setUserIdList("user02,user03");
OapiAttendanceGroupUsersAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupUsersAddRequest("https://oapi.dingtalk.com/topapi/attendance/group/users/add")

req.op_userid="123456"
req.group_key="0151E02xxxx7E876"
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
$req = new OapiAttendanceGroupUsersAddRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151E0xxxx7E876");
$req->setUserIdList("123456,123457");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/users/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/add");
OapiAttendanceGroupUsersAddRequest req = new OapiAttendanceGroupUsersAddRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E02xxxx917E876";
req.UserIdList = "123456,123457";
OapiAttendanceGroupUsersAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| error\_info\_list | ErrorInfo[] |  | 错误列表。 |
| failure\_list | String[] |  | 失败列表。 |
| msg | String | business fault | 错误信息。 |
| code | String | 1000 | 错误码。 |
| success\_list | String[] |  | 成功列表。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | w8iju9gfb236 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "success_list": [
      "user456",
      "manager4220"
    ]
  },
  "success": true,
  "request_id": "w8iju9gfb236"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
