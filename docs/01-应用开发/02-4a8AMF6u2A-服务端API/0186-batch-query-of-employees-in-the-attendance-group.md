---
title: "查询参与考勤人员列表"
source_url: "https://open.dingtalk.com/document/development/batch-query-of-employees-in-the-attendance-group"
namespace: "development"
slug: "batch-query-of-employees-in-the-attendance-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 查询参与考勤人员列表"
doc_id: "Cq9F8lSUPe"
updated_at: "2026-05-27 13:10:00"
---

> Source: https://open.dingtalk.com/document/development/batch-query-of-employees-in-the-attendance-group
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 查询参与考勤人员列表
> Updated: 2026-05-27 13:10:00

# 查询参与考勤人员列表

调用本接口，根据考勤组的groupKey查询指定考勤组内参与考勤人员的员工列表。如果参与考勤人员设置了部门，接口无法获取到部门ID的信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/users/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b1534xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| size | Number | 否 | 50 | 分页大小。 |
| cursor | String | 是 | 10 | 上一批次最后一个userid，传null、空值表示从头开始查。 |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | CEDDFFxxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/users/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d2ee6exxxx9266c' \
-d 'cursor=%5C%22%5C%22' \
-d 'group_key=0151Exxxx17E876' \
-d 'op_userid=123456' \
-d 'size=50'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/query");
OapiAttendanceGroupUsersQueryRequest req = new OapiAttendanceGroupUsersQueryRequest();
req.setSize(50L);
req.setCursor("10");
req.setOpUserid("user01");
req.setGroupKey("CEDDFFxxxx");
OapiAttendanceGroupUsersQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupUsersQueryRequest("https://oapi.dingtalk.com/topapi/attendance/group/users/query")

req.size=50
req.cursor="\"\""
req.op_userid="123456"
req.group_key="0151E0xxxx17E876"
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
$req = new OapiAttendanceGroupUsersQueryRequest;
$req->setSize("50");
$req->setCursor("\"\"");
$req->setOpUserid("123456");
$req->setGroupKey("0151E02xxxx7E876");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/users/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/query");
OapiAttendanceGroupUsersQueryRequest req = new OapiAttendanceGroupUsersQueryRequest();
req.Size = 50L;
req.Cursor = "\"\"";
req.OpUserid = "123456";
req.GroupKey = "0151E0xxxxE876";
OapiAttendanceGroupUsersQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | ntxswpdprw5d | 请求ID。 |
| result | DingOpenResult |  | 返回结果。 |
| result | Result |  | 查询结果。 |
| user\_list | String[] | user01 | 用户列表。 |
| has\_more | String | false | 是否还有更多。   - **true**：有 - **false**：没有 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |

### **响应体示例**

```
{
  "result": {
    "errcode": 0,
    "errmsg":"ok",
    "result": {
      "has_more": "false",
      "user_list": [
        "user01"
      ]
    },
    "success": true
  },
  "request_id": "ntxswpdprw5d"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
