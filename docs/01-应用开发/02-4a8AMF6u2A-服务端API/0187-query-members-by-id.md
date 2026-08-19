---
title: "校验用户是否在当前考勤组"
source_url: "https://open.dingtalk.com/document/development/query-members-by-id"
namespace: "development"
slug: "query-members-by-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 校验用户是否在当前考勤组"
doc_id: "MyNp8zEiqp"
updated_at: "2026-05-27 13:10:02"
---

> Source: https://open.dingtalk.com/document/development/query-members-by-id
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 校验用户是否在当前考勤组
> Updated: 2026-05-27 13:10:02

# 校验用户是否在当前考勤组

调用本接口，校验某个部门或者员工是否属于某个考勤组。

## **接口调用说明**

- 如果需要校验的是员工列表，本接口返回的是在该考勤组的员工userId。
- 如果需要校验的是部门列表，本接口返回在是在该考勤组的部门Id，不会返回该部门下的员工userId列表。

例如，考勤组设置了参与考勤人员设置了**测试部门**、员工**张三**，测试部门下有员工李某。分别校验不同的部门或人员，接口返回示例如下：

- 校验李某的userId，本接口不会返回李某的userId值。
- 校验张三的userId，本接口会返回张三的userId值。
- 校验测试部门Id，本接口会返回测试部门的部门Id值。
- 校验张三、李某是否在考勤组，接口会返回张三的userId值。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_user\_id | String | 是 | dd\_dd | 操作人userId。 |
| group\_id | Number | 是 | 98562 | 考勤组ID。  **[!NOTE]**  如果你使用的是旧考勤组标识即group\_key，可以调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口将group\_key转换为group\_id。 |
| member\_ids | String | 是 | user123,user456 | 成员ID，可以是userId或者deptId，多个ID之间使用英文逗号分割，每次调用最多支持传20个元素值。 |
| member\_type | Number | 是 | 0 | 成员类型：   - **0**：员工 - **1**：部门 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9bacfaxxxx71260' \
-d 'group_id=1234' \
-d 'member_ids=dd_dd' \
-d 'member_type=0' \
-d 'op_user_id=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids");
OapiAttendanceGroupMemberListbyidsRequest req = new OapiAttendanceGroupMemberListbyidsRequest();
req.setOpUserId("user123");
req.setMemberIds("user123,user456");
req.setMemberType(0L);
req.setGroupId(68593L);
OapiAttendanceGroupMemberListbyidsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupMemberListbyidsRequest("https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids")

req.op_user_id="dd_dd"
req.member_ids="dd_dd"
req.member_type=0
req.group_id=1234
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
$req = new OapiAttendanceGroupMemberListbyidsRequest;
$req->setOpUserId("dd_dd");
$req->setMemberIds("dd_dd");
$req->setMemberType("0");
$req->setGroupId("1234");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids");
OapiAttendanceGroupMemberListbyidsRequest req = new OapiAttendanceGroupMemberListbyidsRequest();
req.OpUserId = "dd_dd";
req.MemberIds = "dd_dd";
req.MemberType = 0L;
req.GroupId = 1234L;
OapiAttendanceGroupMemberListbyidsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | z81tif88lkot | 请求ID。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| result | String[] | ["user123","user456"] | 属于该考勤组的成员ID，可以是userId或者deptId。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    "user123",
    "user456"
  ],
  "success": true,
  "request_id": "4nvsqf4ij2xq"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
