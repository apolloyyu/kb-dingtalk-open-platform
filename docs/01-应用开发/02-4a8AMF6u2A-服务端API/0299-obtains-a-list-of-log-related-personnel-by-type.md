---
title: "获取日志相关人员列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-log-related-personnel-by-type"
namespace: "development"
slug: "obtains-a-list-of-log-related-personnel-by-type"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日志 > 获取日志相关人员列表"
doc_id: "dJjHTEmagy"
updated_at: "2026-05-27 13:10:18"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-log-related-personnel-by-type
> Path: 应用开发 / 服务端API / 日志 > 获取日志相关人员列表
> Updated: 2026-05-27 13:10:18

# 获取日志相关人员列表

调用本接口，查询日志已读人员列表、评论人员列表或点赞人员列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/statistics/listbytype |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_report\_statistics-钉钉日志统计数据读权限permission-qyapi\_report\_query-企业员工日志读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| report\_id | String | 是 | 17469xxx | 日志ID，可通过[获取用户发送日志的概要信息](0298-view-log-summary-data.md)或[获取用户发出的日志列表](0297-query-logs-sent-by-an-employee.md)接口获取report\_id参数值。 |
| type | Number | 是 | 0 | 查询类型：   - **0**：已读人员列表 - **1**：评论人员列表 - **2**：点赞人员列表 |
| offset | Number | 否 | 0 | 分页查询的游标，最开始传0，后续传返回参数中的next\_cursor值，默认值为0。 |
| size | Number | 否 | 100 | 分页参数，每页大小，最多传100，默认值为100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/statistics/listbytype" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3ff7cb1c-c513-4259-8d8f-6fde2603a15c' \
-d 'offset=0' \
-d 'report_id=abc' \
-d 'size=100' \
-d 'type=0'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/statistics/listbytype");
OapiReportStatisticsListbytypeRequest req = new OapiReportStatisticsListbytypeRequest();
req.setReportId("17469xxx");
req.setType(0L);
req.setOffset(0L);
req.setSize(100L);
OapiReportStatisticsListbytypeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportStatisticsListbytypeRequest("https://oapi.dingtalk.com/topapi/report/statistics/listbytype")

req.report_id="abc"
req.type=0
req.offset=0
req.size=100
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
$req = new OapiReportStatisticsListbytypeRequest;
$req->setReportId("abc");
$req->setType("0");
$req->setOffset("0");
$req->setSize("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/statistics/listbytype");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/statistics/listbytype");
OapiReportStatisticsListbytypeRequest req = new OapiReportStatisticsListbytypeRequest();
req.ReportId = "abc";
req.Type = 0L;
req.Offset = 0L;
req.Size = 100L;
OapiReportStatisticsListbytypeResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | p0gvgqih0nfv | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| result | ReportPageVo |  | 返回结果。 |
| next\_cursor | Number | 100 | 下一次分页调用的offset值，当返回结果里没有next\_cursor时，表示分页结束。 |
| has\_more | Boolean | true | 是否还有下一页数据。   - **true**：有 - **false**：没有 |
| userid\_list | String[] | ["user123","user456"] | userId列表。 |

### **响应体示例**

```
{
    "errcode": 0,
    "result": {
        "has_more": false,
        "userid_list": [
            "user123",
            "user456"
        ]
    },
    "success": true,
    "request_id": "8g4lsa49kfzq"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
