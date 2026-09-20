---
title: "获取用户日志未读数"
source_url: "https://open.dingtalk.com/document/development/querying-the-employee-s-log-is-not-reading"
namespace: "development"
slug: "querying-the-employee-s-log-is-not-reading"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 获取用户日志未读数"
doc_id: "9ZE3KRgQ3Q"
updated_at: "2026-05-27 13:10:22"
---

> Source: https://open.dingtalk.com/document/development/querying-the-employee-s-log-is-not-reading
> Path: 应用开发 / 服务端 API / 日志 > 获取用户日志未读数
> Updated: 2026-05-27 13:10:22

# 获取用户日志未读数

调用本接口，获取员工有多少数量的日志（一个月内）是未读状态。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/getunreadcount |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_report\_query-企业员工日志读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user123 | 要获取的员工userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/getunreadcount" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8f8xxxxd14f4' \
-d 'userid=123456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/getunreadcount");
OapiReportGetunreadcountRequest req = new OapiReportGetunreadcountRequest();
req.setUserid("123456");
OapiReportGetunreadcountResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportGetunreadcountRequest("https://oapi.dingtalk.com/topapi/report/getunreadcount")

req.userid="123456"
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
$req = new OapiReportGetunreadcountRequest;
$req->setUserid("123456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/getunreadcount");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/getunreadcount");
OapiReportGetunreadcountRequest req = new OapiReportGetunreadcountRequest();
req.Userid = "123456";
OapiReportGetunreadcountResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| count | Number | 2 | 员工日志未读数。 |
| request\_id | String | wp9ie6b3d8pg | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回的错误信息。 |

### **响应体示例**

```
{
    "count": 2,
    "errcode": 0,
    "errmsg": "ok",
    "request_id": "iwctsa0311jj"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
