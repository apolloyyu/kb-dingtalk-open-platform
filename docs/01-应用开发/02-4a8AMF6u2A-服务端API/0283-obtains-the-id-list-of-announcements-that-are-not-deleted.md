---
title: "获取公告ID列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-id-list-of-announcements-that-are-not-deleted"
namespace: "development"
slug: "obtains-the-id-list-of-announcements-that-are-not-deleted"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 获取公告ID列表"
doc_id: "GkWSfb6sjX"
updated_at: "2026-05-29 09:13:32"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-id-list-of-announcements-that-are-not-deleted
> Path: 应用开发 / 服务端API / 公告 > 获取公告ID列表
> Updated: 2026-05-29 09:13:32

# 获取公告ID列表

调用本接口，获取企业某公告分类下所有未删除公告的ID列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/blackboard/listids |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_read-读取钉钉公告微应用数据的权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| query\_request | OapiBlackboardQueryVo | 是 |  | 请求对象。 |
| operation\_userid | String | 是 | manager4220 | 操作人userId，必须是公告管理员。 |
| page\_size | Number | 是 | 10 | 分页大小，从1开始不超过30，且必须为正整数。 |
| start\_time | Date | 否 | 2019-10-07 10:10:10 | 开始时间。   - 如果只传**start\_time**，**start\_time**距当前时间不能超过180天。 - 如果传**start\_time**和**end\_time**，时间间隔不能超过180天。 - 如果不传**start\_time**和**end\_time**，默认获取近一个月内的公告信息。 |
| end\_time | Date | 否 | 2019-11-07 10:10:10 | 结束时间。   - 如果只传**start\_time**，**start\_time**距当前时间不能超过180天。 - 如果传**start\_time**和**end\_time**，时间间隔不能超过180天。 - 如果不传**start\_time**和**end\_time**，默认获取近一个月内的公告信息。 |
| page | Number | 是 | 1 | 页码，从1开始且必须为正整数。 |
| category\_id | String | 否 | 9i9u7y7g6t65 | 分类ID，可以通过[获取公告分类列表](0284-obtains-the-list-of-categories-not-deleted-for-enterprise-announcements.md)接口获取id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/blackboard/listids" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0acdxxxx23a6e843' \
-d 'query_request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/listids");
OapiBlackboardListidsRequest req = new OapiBlackboardListidsRequest();
OapiBlackboardQueryVo queryVoObj= new OapiBlackboardQueryVo();
queryVoObj.setOperationUserid("manager4220");
queryVoObj.setPageSize(10L);
queryVoObj.setStartTime(StringUtils.parseDateTime("2019-10-07 10:10:10"));
queryVoObj.setEndTime(StringUtils.parseDateTime("2019-11-07 10:10:10"));
queryVoObj.setPage(1L);
queryVoObj.setCategoryId("9i9u7y7g6t65");
req.setQueryRequest(queryVoObj);
OapiBlackboardListidsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiBlackboardListidsRequest("https://oapi.dingtalk.com/topapi/blackboard/listids")

req.query_request=""
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
$req = new OapiBlackboardListidsRequest;
$query_request = new OapiBlackboardQueryVo;
$query_request->operation_userid="manager01";
$query_request->page_size="10";
$query_request->start_time="2019-10-07 10:10:10";
$query_request->end_time="2019-11-07 10:10:10";
$query_request->page="1";
$query_request->category_id="9i9u7y7g6t65";
$req->setQueryRequest($query_request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/blackboard/listids");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/listids");
OapiBlackboardListidsRequest req = new OapiBlackboardListidsRequest();
OapiBlackboardListidsRequest.OapiBlackboardQueryVoDomain obj1 = new OapiBlackboardListidsRequest.OapiBlackboardQueryVoDomain();
obj1.OperationUserid = "manager01";
obj1.PageSize = 10L;
obj1.StartTime = DateTime.Parse(2019-10-07 10:10:10");
obj1.EndTime = DateTime.Parse(2019-11-07 10:10:10");
obj1.Page = 1L;
obj1.CategoryId = "9i9u7y7g6t65";
req.QueryRequest_ = obj1;
OapiBlackboardListidsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String[] | ["72b4f87d27e815f6fecxxxx"] | 公告ID列表。 |
| success | Boolean | true | 本次调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | pxxm7ylvmppr | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": [
    "72b4f87d27e815f6fecxxxx"
  ],
  "success": true,
  "request_id": "pxxm7ylvmppr"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
