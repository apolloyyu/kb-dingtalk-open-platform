---
title: "获取日志评论详情"
source_url: "https://open.dingtalk.com/document/development/queries-log-comment-details"
namespace: "development"
slug: "queries-log-comment-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日志 > 获取日志评论详情"
doc_id: "JlGn67zcTw"
updated_at: "2026-05-27 13:10:21"
---

> Source: https://open.dingtalk.com/document/development/queries-log-comment-details
> Path: 应用开发 / 服务端API / 日志 > 获取日志评论详情
> Updated: 2026-05-27 13:10:21

# 获取日志评论详情

调用本接口，可获取评论的详情信息，包括评论人userId、评论内容和评论时间等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/comment/list |
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
| report\_id | String | 是 | 174xxxx | 日志ID，可通过[获取用户发送日志的概要信息](0298-view-log-summary-data.md)或[获取用户发出的日志列表](0297-query-logs-sent-by-an-employee.md)接口获取report\_id参数值。 |
| offset | Number | 否 | 0 | 分页查询的游标，最开始传0，后续传返回参数中的next\_cursor值，默认值为0。 |
| size | Number | 否 | 20 | 分页参数，每页大小，最多传20，默认值为20。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/comment/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2b8c6xxxx80cd51b' \
-d 'offset=0' \
-d 'report_id=abc' \
-d 'size=20'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/comment/list");
OapiReportCommentListRequest req = new OapiReportCommentListRequest();
req.setReportId("174xxxx");
req.setOffset(0L);
req.setSize(20L);
OapiReportCommentListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportCommentListRequest("https://oapi.dingtalk.com/topapi/report/comment/list")

req.report_id="abc"
req.offset=0
req.size=20
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
$req = new OapiReportCommentListRequest;
$req->setReportId("abc");
$req->setOffset("0");
$req->setSize("20");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/comment/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/comment/list");
OapiReportCommentListRequest req = new OapiReportCommentListRequest();
req.ReportId = "abc";
req.Offset = 0L;
req.Size = 20L;
OapiReportCommentListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ReportPageVo |  | 返回结果。 |
| comments | ReportCommentVo[] |  | 日志评论详情。 |
| create\_time | Date | 2020-09-08 00:26:37 | 评论时间。 |
| content | String | 不错 | 评论内容。 |
| userid | String | user456 | 评论人ID。 |
| has\_more | Boolean | true | 是否还有下一页。   - **true**：有 - **false**：没有 |
| next\_cursor | Number | 20 | 下一次分页调用的offset值，当返回结果里没有next\_cursor时，表示分页结束。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 5kngbdmfdrle | 请求ID。 |
| success | Boolean | true | 调用结果。   - **true**：成功 - **false**：失败 |

### **响应体示例**

```
{
    "errcode": 0,
    "result": {
        "comments": [
            {
                "content": "不错",
                "create_time": "2020-09-08 00:26:37",
                "userid": "user456"
            }
        ],
        "has_more": false
    },
    "success": true,
    "request_id": "5kngbdmfdrle"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
