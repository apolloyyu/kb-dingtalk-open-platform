---
title: "获取日志接收人员列表"
source_url: "https://open.dingtalk.com/document/development/queries-log-sharing-personnel"
namespace: "development"
slug: "queries-log-sharing-personnel"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日志 > 获取日志接收人员列表"
doc_id: "haid495lC3"
updated_at: "2026-05-27 13:10:19"
---

> Source: https://open.dingtalk.com/document/development/queries-log-sharing-personnel
> Path: 应用开发 / 服务端API / 日志 > 获取日志接收人员列表
> Updated: 2026-05-27 13:10:19

# 获取日志接收人员列表

调用本接口，可获取日志接收人员列表。日志接收范围如果包含群，本接口将会获取到该群内的成员userId值。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/receiver/list |
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
| report\_id | String | 是 | 174xxxx | 日志ID，可通过[获取用户发送日志的概要信息](0298-view-log-summary-data.md)或[获取用户发出的日志列表](0297-query-logs-sent-by-an-employee.md)接口获取report\_id参数值。 |
| offset | Number | 否 | 0 | 分页查询的游标，最开始传0，后续传返回参数中next\_cursor的值，默认值为0。 |
| size | Number | 否 | 100 | 分页参数，每页大小，最多传100，默认值为100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/create?access_token=YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "create_report_param": {
      "contents": [
        {
          "sort": 0,
          "type": 1,
          "content_type": "markdown",
          "content": "### 今日完成工作\n1. 完成项目需求分析\n2. 编写技术方案文档",
          "key": "今日完成工作"
        },
        {
          "sort": 1,
          "type": 1,
          "content_type": "markdown",
          "content": "### 明日计划\n1. 开始编码实现\n2. 进行单元测试",
          "key": "明日计划"
        }
      ],
      "template_id": "12345abcde",
      "to_userids": ["user123", "user456"],
      "to_chat": true,
      "to_cids": ["cid123"],
      "dd_from": "report",
      "userid": "user123"
    }
  }'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/receiver/list");
OapiReportReceiverListRequest req = new OapiReportReceiverListRequest();
req.setReportId("174xxxx");
req.setOffset(0L);
req.setSize(100L);
OapiReportReceiverListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiReportCreateRequest("https://oapi.dingtalk.com/topapi/report/create")

req.create_report_param=""
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
$req = new OapiReportCreateRequest;
$create_report_param = new OapiCreateReportParam;
$contents = new OapiReportContentVo;
$contents->sort="0";
$contents->type="1";
$contents->content_type="markdown";
$contents->content="### 序号1";
$contents->key="字段1";
$create_report_param->contents = array($contents);
$create_report_param->to_userids="[\"123\",\"456\"]";
$create_report_param->template_id="12345abcde";
$create_report_param->to_chat="true";
$create_report_param->dd_from="report";
$create_report_param->userid="12345";
$create_report_param->to_cids="[\"123\",\"456\"]";
$req->setCreateReportParam($create_report_param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/create");
OapiReportCreateRequest req = new OapiReportCreateRequest();
OapiReportCreateRequest.OapiCreateReportParamDomain obj1 = new OapiReportCreateRequest.OapiCreateReportParamDomain();
List<OapiReportCreateRequest.OapiReportContentVoDomain> list3 = new List<OapiReportCreateRequest.OapiReportContentVoDomain>();
OapiReportCreateRequest.OapiReportContentVoDomain obj4 = new OapiReportCreateRequest.OapiReportContentVoDomain();
list3.Add(obj4);
obj4.Sort = 0L;
obj4.Type = 1L;
obj4.ContentType = "markdown";
obj4.Content = "### 序号1";
obj4.Key = "字段1";
obj1.Contents= list3;
obj1.ToUserids = ""123","456"";
obj1.TemplateId = "12345abcde";
obj1.ToChat = true;
obj1.DdFrom = "report";
obj1.Userid = "12345";
obj1.ToCids = ""123","456"";
req.CreateReportParam_ = obj1;
OapiReportCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ReportPageVo |  | 返回结果。 |
| has\_more | Boolean | true | 是否还有下一页数据。   - **true**：有 - **false**：没有 |
| next\_cursor | Number | 100 | 下一次分页调用的offset值，当返回结果里没有next\_cursor时，表示分页结束。 |
| userid\_list | String[] | ["user123","user456"] | 日志接收人userId列表。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | p0gvgqih0nfv | 请求ID。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |

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
    "request_id": "7aen3idk2fqh"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
