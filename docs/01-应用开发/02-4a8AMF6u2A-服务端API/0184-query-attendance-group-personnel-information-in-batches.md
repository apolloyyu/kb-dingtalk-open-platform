---
title: "获取参与考勤人员的userid"
source_url: "https://open.dingtalk.com/document/development/query-attendance-group-personnel-information-in-batches"
namespace: "development"
slug: "query-attendance-group-personnel-information-in-batches"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 获取参与考勤人员的userid"
doc_id: "Z0UrHecADb"
updated_at: "2026-05-27 13:09:57"
---

> Source: https://open.dingtalk.com/document/development/query-attendance-group-personnel-information-in-batches
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 获取参与考勤人员的userid
> Updated: 2026-05-27 13:09:57

# 获取参与考勤人员的userid

调用本接口，分页获取某个考勤组下的所有员工的userId。

## **接口调用说明**

如果参与考勤人员设置了部门，接口返回部门下的员工的userId，不返回部门ID。

例如，参与考勤人员设置了**测试部门**、员工**张三**，测试部门下有一个员工**李四**。调用本接口可以获取到如下信息：

- 测试部门（包括子部门）下的员工的userId，即李四的userId
- 员工张三的员工userId

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cursor | Number | 否 | 0 | 游标值，表示从第几个开始，不传默认从第一个开始。 |
| op\_user\_id | String | 是 | user123 | 操作人userId。 |
| group\_id | Number | 是 | 98562 | 考勤组ID。  **[!NOTE]**  如果你使用的是旧考勤组标识即group\_key，可以调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将group\_key转换为group\_id。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e6e94xxxxeb7b3' \
-d 'cursor=9828' \
-d 'group_id=98562' \
-d 'op_user_id=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list");
OapiAttendanceGroupMemberusersListRequest req = new OapiAttendanceGroupMemberusersListRequest();
req.setCursor(0L);
req.setOpUserId("user123");
req.setGroupId(98562L);
OapiAttendanceGroupMemberusersListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupMemberusersListRequest("https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list")

req.cursor=9828
req.op_user_id="dd_dd"
req.group_id=98562
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
$req = new OapiAttendanceGroupMemberusersListRequest;
$req->setCursor("9828");
$req->setOpUserId("dd_dd");
$req->setGroupId("98562");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list");
OapiAttendanceGroupMemberusersListRequest req = new OapiAttendanceGroupMemberusersListRequest();
req.Cursor = 9828L;
req.OpUserId = "dd_dd";
req.GroupId = 98562L;
OapiAttendanceGroupMemberusersListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 3pgsafymemlr | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| result | PageResult |  | 人员列表。 |
| has\_more | Boolean | false | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| cursor | Number | 1387570559 | 分页获取下一次请求的起始位置。 |
| result | String[] | ["user123","user456"] | 考勤组人员userId列表。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "cursor": 1387570559,
    "has_more": false,
    "result": [
      "user123",
      "user456"
    ]
  },
  "success": true,
  "request_id": "146drwo74wiss"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
