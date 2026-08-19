---
title: "批量删除地点"
source_url: "https://open.dingtalk.com/document/development/delete-position-in-batches-under-the-attendance-group"
namespace: "development"
slug: "delete-position-in-batches-under-the-attendance-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 批量删除地点"
doc_id: "n0cB2cKWhx"
updated_at: "2026-05-27 13:10:10"
---

> Source: https://open.dingtalk.com/document/development/delete-position-in-batches-under-the-attendance-group
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 批量删除地点
> Updated: 2026-05-27 13:10:10

# 批量删除地点

调用本接口，在指定考勤组下批量删除position。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/positions/remove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b1534xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | CEDDFxxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |
| position\_key\_list | String | 是 | C384Fxxxx | 要删除position的key列表，可通过[批量查询地点](0193-batch-query-position-under-attendance-group.md)接口获取，每次最多支持删除100个地点信息。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/positions/remove" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=25961xxxx7912f13' \
-d 'group_key=0151E022xxxx72A1A917E876' \
-d 'op_userid=123456' \
-d 'position_key_list=%22123%22%2C%22123%22'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/positions/remove");
OapiAttendanceGroupPositionsRemoveRequest req = new OapiAttendanceGroupPositionsRemoveRequest();
req.setOpUserid("user01");
req.setGroupKey("CEDDFxxxx");
req.setPositionKeyList("C384Fxxxx");
OapiAttendanceGroupPositionsRemoveResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupPositionsRemoveRequest("https://oapi.dingtalk.com/topapi/attendance/group/positions/remove")

req.op_userid="123456"
req.group_key="0151E02xxxx17E876"
req.position_key_list="["123","123"]"
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
$req = new OapiAttendanceGroupPositionsRemoveRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151E02xxxx17E876");
$req->setPositionKeyList("[\"123\",\"123\"]");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/positions/remove");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/positions/remove");
OapiAttendanceGroupPositionsRemoveRequest req = new OapiAttendanceGroupPositionsRemoveRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E0xxxx17E876";
req.PositionKeyList = ""123","123"";
OapiAttendanceGroupPositionsRemoveResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| success\_list | String[] | ["C384Fxxxx"] | 成功列表。 |
| error\_info\_list | ErrorInfo[] |  | 错误列表。 |
| failure\_list | String[] | ["C384Fxxxx"] | 失败列表。 |
| msg | String | business fault | 错误描述。 |
| code | String | 1000 | 错误码。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 1493be6v5yefm | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "error_info_list": [
      {
        "code": "1000",
        "failure_list": [
          "C384Fxxxx"
        ],
        "msg": "business fault"
      }
    ],
    "success_list": [
      "C384Fxxxx"
    ]
  },
  "success": true,
  "request_id": "1493be6v5yefm"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
