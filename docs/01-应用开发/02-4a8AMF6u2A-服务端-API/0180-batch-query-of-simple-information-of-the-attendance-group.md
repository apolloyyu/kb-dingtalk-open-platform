---
title: "批量获取考勤组摘要"
source_url: "https://open.dingtalk.com/document/development/batch-query-of-simple-information-of-the-attendance-group"
namespace: "development"
slug: "batch-query-of-simple-information-of-the-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 批量获取考勤组摘要"
doc_id: "ylFvE74hmU"
updated_at: "2026-05-27 13:09:50"
---

> Source: https://open.dingtalk.com/document/development/batch-query-of-simple-information-of-the-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 批量获取考勤组摘要
> Updated: 2026-05-27 13:09:50

# 批量获取考勤组摘要

调用本接口，分页获取企业内所有考勤组的摘要信息，包含考勤组名称及对应的考勤组ID。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list |
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
| cursor | Number | 否 | 222 | 分页游标，从上一次请求结果中获取，如果不传默认从第一个开始。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=6dd4xxxx94138' \
-d 'cursor=222' \
-d 'op_user_id=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list");
OapiAttendanceGroupMinimalismListRequest req = new OapiAttendanceGroupMinimalismListRequest();
req.setOpUserId("manager4220");
req.setCursor(0L);
OapiAttendanceGroupMinimalismListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupMinimalismListRequest("https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list")

req.op_user_id="dd_dd"
req.cursor=222
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
$req = new OapiAttendanceGroupMinimalismListRequest;
$req->setOpUserId("dd_dd");
$req->setCursor("222");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list");
OapiAttendanceGroupMinimalismListRequest req = new OapiAttendanceGroupMinimalismListRequest();
req.OpUserId = "dd_dd";
req.Cursor = 222L;
OapiAttendanceGroupMinimalismListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult | demo | 返回结果。 |
| has\_more | Boolean | false | 是否有更多数据。   - **true**：有 - **false**：没有 |
| cursor | Number | 685935028 | 游标位置。 |
| result | TopMinimalismGroupVo[] |  | 考勤信息。 |
| name | String | 考勤 | 考勤组名称。 |
| id | Number | 677765054 | 考勤组ID。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回的错误信息描述。 |
| request\_id | String | wv9973jntam | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "cursor": 685935028,
    "has_more": false,
    "result": [
      {
        "id": 677765054,
        "name": "周末加班"
      },
      {
        "id": 685935028,
        "name": "考勤"
      }
    ]
  },
  "success": true,
  "request_id": "wv9973jntamw"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
