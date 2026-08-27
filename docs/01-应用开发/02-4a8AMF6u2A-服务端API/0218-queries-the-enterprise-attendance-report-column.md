---
title: "获取考勤报表列定义"
source_url: "https://open.dingtalk.com/document/development/queries-the-enterprise-attendance-report-column"
namespace: "development"
slug: "queries-the-enterprise-attendance-report-column"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤统计 > 获取考勤报表列定义"
doc_id: "2vxROY8oRL"
updated_at: "2026-05-27 17:06:18"
---

> Source: https://open.dingtalk.com/document/development/queries-the-enterprise-attendance-report-column
> Path: 应用开发 / 服务端API / 考勤 > 考勤统计 > 获取考勤报表列定义
> Updated: 2026-05-27 17:06:18

# 获取考勤报表列定义

调用本接口，据列的ID查询考勤智能报表中该列的统计数据，企业可以自主选择需要哪些列值来参与薪酬的计算。

## **接口调用说明**

- 如果是获取假期相关字段信息，不返回ID。如果希望获取假期相关信息，请调用[获取报表假期数据](0217-obtains-the-holiday-data-from-the-smart-attendance-report.md)接口。
- 确保已开启了智能统计功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/getattcolumns |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/getattcolumns" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1aae6dxxxx7bf36'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getattcolumns");
OapiAttendanceGetattcolumnsRequest req = new OapiAttendanceGetattcolumnsRequest();
OapiAttendanceGetattcolumnsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGetattcolumnsRequest("https://oapi.dingtalk.com/topapi/attendance/getattcolumns")

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
$req = new OapiAttendanceGetattcolumnsRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/getattcolumns");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getattcolumns");
OapiAttendanceGetattcolumnsRequest req = new OapiAttendanceGetattcolumnsRequest();
OapiAttendanceGetattcolumnsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | emhw3318cdhv | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| result | AttColumnsForTopVo |  | 查询结果。 |
| columns | ColumnForTopVo[] |  | 报表列信息。 |
| id | Number | 123 | 报表列ID。 |
| type | Number | 0 | 报表列类型。 |
| name | String | 工时 | 报表列名。 |
| alias | String | 3\_on\_duty\_user\_check\_result | 列报表。 |
| status | Number | 0 | 报表列的状态。 |
| sub\_type | Number | 0 | 子类型。 |
| expression\_id | Number | 129334038 | 废弃字段，勿用此字段处理业务。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "columns": [
      {
        "alias": "should_attendance_days",
        "expression_id": 129334038,
        "id": 129339038,
        "name": "应出勤天数",
        "status": 0,
        "sub_type": 0,
        "type": 0
      },
      {
        "alias": "making_up_lack_times",
        "expression_id": 129334039,
        "id": 129339039,
        "name": "补卡次数",
        "status": 0,
        "sub_type": 0,
        "type": 0
      }
    ]
  },
  "request_id": "10stq4mcre2wu"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
