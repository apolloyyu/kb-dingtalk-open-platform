---
title: "获取用户发出的日志列表"
source_url: "https://open.dingtalk.com/document/development/query-logs-sent-by-an-employee"
namespace: "development"
slug: "query-logs-sent-by-an-employee"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 获取用户发出的日志列表"
doc_id: "3zbqKHr5Va"
updated_at: "2026-05-27 13:10:15"
---

> Source: https://open.dingtalk.com/document/development/query-logs-sent-by-an-employee
> Path: 应用开发 / 服务端 API / 日志 > 获取用户发出的日志列表
> Updated: 2026-05-27 13:10:15

# 获取用户发出的日志列表

调用本接口，获取用户发出的日志列表。

## **接口调用说明**

- 如果要获取企业某个日志模板在某段时间内的列表，传template\_name参数。
- 如果要获取某个员工某段时间段内发送的所有日志列表，传userId参数。
- 如果要获取企业下所有日志和所有人发送的日志列表，template\_name和userId参数都为空即可。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_report\_query-企业员工日志读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| start\_time | Number | 是 | 1507564800000 | 查询的日志创建的开始时间，Unix时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| end\_time | Number | 是 | 1507564800000 | 查询的日志创建的结束时间，Unix时间戳，单位毫秒。  **[!NOTE]**  start\_time参数和end\_time参数最多相隔180天。 |
| template\_name | String | 否 | 周报 | 要查询的模板名称。 |
| userid | String | 否 | user123 | 员工的userId。 |
| cursor | Number | 是 | 0 | 查询游标，初始传入0，后续从上一次的返回值中获取。 |
| size | Number | 是 | 10 | 每页数据量，最大值为20。 |
| modified\_start\_time | Number | 否 | 1507564800000 | 查询的日志修改的开始时间，Unix时间戳，单位毫秒。 |
| modified\_end\_time | Number | 否 | 1507564800000 | 查询的日志修改的结束时间，Unix时间戳，单位毫秒。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f9882xxxx66e20f' \
-d 'cursor=0' \
-d 'end_time=1507564800000' \
-d 'modified_end_time=1507564800000' \
-d 'modified_start_time=1507564800000' \
-d 'size=10' \
-d 'start_time=1507564800000' \
-d 'template_name=%E5%91%A8%E6%8A%A5' \
-d 'userid=xxxxx'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/list");
OapiReportListRequest req = new OapiReportListRequest();
req.setStartTime(1507564800000L);
req.setEndTime(1507564800000L);
req.setTemplateName("日报");
req.setUserid("user123");
req.setCursor(0L);
req.setSize(10L);
req.setModifiedStartTime(1507564800000L);
req.setModifiedEndTime(1507564800000L);
OapiReportListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportListRequest("https://oapi.dingtalk.com/topapi/report/list")

req.start_time=1507564800000
req.end_time=1507564800000
req.template_name="周报"
req.userid="xxxxx"
req.cursor=0
req.size=10
req.modified_start_time=1507564800000
req.modified_end_time=1507564800000
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
$req = new OapiReportListRequest;
$req->setStartTime("1507564800000");
$req->setEndTime("1507564800000");
$req->setTemplateName("周报");
$req->setUserid("xxxxx");
$req->setCursor("0");
$req->setSize("10");
$req->setModifiedStartTime("1507564800000");
$req->setModifiedEndTime("1507564800000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/list");
OapiReportListRequest req = new OapiReportListRequest();
req.StartTime = 1507564800000L;
req.EndTime = 1507564800000L;
req.TemplateName = "周报";
req.Userid = "xxxxx";
req.Cursor = 0L;
req.Size = 10L;
req.ModifiedStartTime = 1507564800000L;
req.ModifiedEndTime = 1507564800000L;
OapiReportListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageVo |  | 返回结果。 |
| data\_list | ReportOapiVo[] |  | 日志列表。 |
| contents | JsonObject[] |  | 日志内容。 |
| sort | String | 1 | 排序。 |
| type | String | 0 | 日志类型。 |
| value | String | 开发工作 | 用户填写的内容。  内容不能超过 1000 字符，超出的内容会被截断。 |
| key | String | 今日工作 | 模板内容。 |
| remark | String | 这是备注 | 备注。 |
| template\_name | String | 日报 | 日志模板名称。 |
| dept\_name | String | 部门1 | 部门。 |
| creator\_name | String | 张三 | 日志创建人。 |
| creator\_id | String | user123 | 日志创建人的userId。 |
| create\_time | Number | 1507564800000 | 日志创建时间。 |
| report\_id | String | xxxxxxx | 日志ID。 |
| modified\_time | Number | 1507564800000 | 日志修改时间。 |
| size | Number | 10 | 分页大小。 |
| next\_cursor | Number | 10000 | 下一游标。 |
| has\_more | Boolean | false | 是否还有下一页数据。   - **true**：有 - **false**：没有 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
    "errcode": 0,
    "errmsg":"ok",
    "result": {
        "data_list": [
            {
                "contents": [
                    {
                        "key": "今日完成工作",
                        "sort": "0",
                        "type": "1",
                        "value": "“今天已经完成的工作"
                    },
                    {
                        "key": "未完成工作",
                        "sort": "1",
                        "type": "1",
                        "value": "“未完成工作"
                    }
                ],
                "create_time": 1605680704000,
                "creator_id": "user123",
                "creator_name": "测试同学",
                "dept_name": "测试部",
                "modified_time": 1605680704000,
                "report_id": "175daxxxxxxfaa85c4",
                "template_name": "日报"
            }
        ],
        "has_more": false,
        "next_cursor": 2862455276,
        "size": 10
    },
    "request_id": "5c8q6ic6wyah"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
