---
title: "获取用户发送日志的概要信息"
source_url: "https://open.dingtalk.com/document/development/view-log-summary-data"
namespace: "development"
slug: "view-log-summary-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日志 > 获取用户发送日志的概要信息"
doc_id: "gN5jHZYcc7"
updated_at: "2026-05-27 13:10:16"
---

> Source: https://open.dingtalk.com/document/development/view-log-summary-data
> Path: 应用开发 / 服务端API / 日志 > 获取用户发送日志的概要信息
> Updated: 2026-05-27 13:10:16

# 获取用户发送日志的概要信息

调用本接口，根据员工userId或者日志模板名称，分页获取员工在一段时间范围内发送的日志概要信息，包括日志创建人，日志ID和日志模板名称。

## **接口调用说明**

> **[!NOTE]**
>
> 如果需要获取发起的日志详情信息，请调用[获取用户发出的日志列表](0297-query-logs-sent-by-an-employee.md)接口。

- 如果要获取企业某个日志模板在某段时间内发送的日志概要信息，传template\_name参数。
- 如果要获取某个员工某段时间段内发送日志的概要信息，传userId参数。
- 如果要获取企业下所有日志和所有人发送的日志概要信息，template\_name和userId参数都为空即可。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/simplelist |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_report\_statistics-钉钉日志统计数据读权限permission-qyapi\_report\_query-企业员工日志读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| start\_time | Number | 是 | 1507564800000 | 查询起始时间，Unix时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| end\_time | Number | 是 | 1507564800000 | 查询截止时间，Unix时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| template\_name | String | 否 | 周报 | 要查询的模板名称。 |
| userid | String | 否 | user123 | 员工的userId。 |
| cursor | Number | 是 | 0 | 查询游标，初始传入0，后续从上一次的返回值中获取。 |
| size | Number | 是 | 10 | 每页数据量，最大为20。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/simplelist" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7ba7xxxxc925' \
-d 'cursor=0' \
-d 'end_time=1507564800000' \
-d 'size=10' \
-d 'start_time=1507564800000' \
-d 'template_name=%E5%91%A8%E6%8A%A5' \
-d 'userid=xxxxx'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/simplelist");
OapiReportSimplelistRequest req = new OapiReportSimplelistRequest();
req.setStartTime(1507564800000L);
req.setEndTime(1507564800000L);
req.setTemplateName("周报");
req.setUserid("xxxxx");
req.setCursor(0L);
req.setSize(10L);
OapiReportSimplelistResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportSimplelistRequest("https://oapi.dingtalk.com/topapi/report/simplelist")

req.start_time=1507564800000
req.end_time=1507564800000
req.template_name="周报"
req.userid="xxxxx"
req.cursor=0
req.size=10
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
$req = new OapiReportSimplelistRequest;
$req->setStartTime("1507564800000");
$req->setEndTime("1507564800000");
$req->setTemplateName("周报");
$req->setUserid("xxxxx");
$req->setCursor("0");
$req->setSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/simplelist");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/simplelist");
OapiReportSimplelistRequest req = new OapiReportSimplelistRequest();
req.StartTime = 1507564800000L;
req.EndTime = 1507564800000L;
req.TemplateName = "周报";
req.Userid = "xxxxx";
req.Cursor = 0L;
req.Size = 10L;
OapiReportSimplelistResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageVo |  | 返回结果。 |
| data\_list | ReportOapiVo[] |  | 日志列表。 |
| remark | String | 日报 | 备注。 |
| template\_name | String | 日报 | 日志模板名。 |
| dept\_name | String | 市场部 | 部门。 |
| creator\_name | String | 杨xx | 日志创建人。 |
| creator\_id | String | manager4220 | 日志创建人userId。 |
| create\_time | Number | 1507564800000 | 日志创建时间。 |
| report\_id | String | 1746xxxx | 日志ID。 |
| size | Number | 10 | 分页大小。 |
| next\_cursor | Number | 10000 | 下一页的游标，当返回结果里没有next\_cursor时，表示分页结束。 |
| has\_more | Boolean | false | 是否还有下一页数据。   - **true**：有 - **false**：没有 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 3qwbhu6edlcz | 请求ID。 |

### **响应体示例**

```
{
    "errcode": 0,
    "result": {
        "data_list": [
            {
                "create_time": 1599495985000,
                "creator_id": "user123",
                "creator_name": "测试用户",
                "dept_name": "开放平台,市场部",
                "remark": "",
                "report_id": "174696xxxxxxxdab6fe",
                "template_name": "日报"
            }
        ],
        "has_more": false,
        "next_cursor": 2664853010,
        "size": 10
    },
    "request_id": "3qwbhu6edlcz"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
