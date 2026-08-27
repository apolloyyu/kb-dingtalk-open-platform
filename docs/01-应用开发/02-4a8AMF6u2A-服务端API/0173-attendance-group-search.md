---
title: "搜索考勤组摘要"
source_url: "https://open.dingtalk.com/document/development/attendance-group-search"
namespace: "development"
slug: "attendance-group-search"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 搜索考勤组摘要"
doc_id: "cyLGiHXrgu"
updated_at: "2026-05-27 13:09:45"
---

> Source: https://open.dingtalk.com/document/development/attendance-group-search
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 搜索考勤组摘要
> Updated: 2026-05-27 13:09:45

# 搜索考勤组摘要

调用本接口根据考勤组名称模糊搜索，获取考勤组摘要信息，包含考勤组名称、考勤组ID。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/search |
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
| op\_user\_id | String | 是 | manager123 | 操作人userId。 |
| group\_name | String | 是 | 考勤 | 考勤组名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d7689axxxx70e7a' \
-d 'group_name=%Exxxx%BA%97' \
-d 'op_user_id=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/search");
OapiAttendanceGroupSearchRequest req = new OapiAttendanceGroupSearchRequest();
req.setOpUserId("manager123");
req.setGroupName("考勤");
OapiAttendanceGroupSearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupSearchRequest("https://oapi.dingtalk.com/topapi/attendance/group/search")

req.op_user_id="dd_dd"
req.group_name="西溪门店"
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
$req = new OapiAttendanceGroupSearchRequest;
$req->setOpUserId("dd_dd");
$req->setGroupName("西溪门店");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/search");
OapiAttendanceGroupSearchRequest req = new OapiAttendanceGroupSearchRequest();
req.OpUserId = "dd_dd";
req.GroupName = "西溪门店";
OapiAttendanceGroupSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | TopMinimalismGroupVO[] |  | 查询结果。 |
| name | String | 考勤 | 考勤组名称。 |
| id | Number | 685935028 | 考勤组ID。 |
| success | Boolean | true | 是否查询成功。   - **true**：修改 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 750mu3wy9fu | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": [
    {
      "id": 685935028,
      "name": "考勤"
    }
  ],
  "success": true,
  "request_id": "750muu3wy9fu"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
