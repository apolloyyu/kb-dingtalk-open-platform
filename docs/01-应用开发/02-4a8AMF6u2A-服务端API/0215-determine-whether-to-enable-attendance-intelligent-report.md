---
title: "查询是否启用智能统计报表"
source_url: "https://open.dingtalk.com/document/development/determine-whether-to-enable-attendance-intelligent-report"
namespace: "development"
slug: "determine-whether-to-enable-attendance-intelligent-report"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤统计 > 查询是否启用智能统计报表"
doc_id: "7i62hcupfY"
updated_at: "2026-05-27 17:06:15"
---

> Source: https://open.dingtalk.com/document/development/determine-whether-to-enable-attendance-intelligent-report
> Path: 应用开发 / 服务端API / 考勤 > 考勤统计 > 查询是否启用智能统计报表
> Updated: 2026-05-27 17:06:15

# 查询是否启用智能统计报表

调用本接口，判断企业是否已开启考勤智能报表，如果企业未启用智能报表，无法调用统计报表其他的接口。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/isopensmartreport |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/isopensmartreport" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b74b3xxxx0bb7c'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/isopensmartreport");
OapiAttendanceIsopensmartreportRequest req = new OapiAttendanceIsopensmartreportRequest();
OapiAttendanceIsopensmartreportResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceIsopensmartreportRequest("https://oapi.dingtalk.com/topapi/attendance/isopensmartreport")

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
$req = new OapiAttendanceIsopensmartreportRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/isopensmartreport");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/isopensmartreport");
OapiAttendanceIsopensmartreportRequest req = new OapiAttendanceIsopensmartreportRequest();
OapiAttendanceIsopensmartreportResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | IsOpenSmartReportForTopVo |  | 返回结果。 |
| smart\_report | Boolean | true | 是否开启了智能统计报表：   - **true**：开启 - **false**：未开启 |
| request\_id | String | 6f9h5mh9a94i | 请求ID。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "smart_report": true
  },
  "request_id": "6f9h5mh9a94i"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
