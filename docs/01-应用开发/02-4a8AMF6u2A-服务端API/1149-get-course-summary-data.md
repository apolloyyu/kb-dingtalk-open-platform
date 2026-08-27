---
title: "获取课堂概要数据"
source_url: "https://open.dingtalk.com/document/development/get-course-summary-data"
namespace: "development"
slug: "get-course-summary-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课堂概要数据"
doc_id: "fKxD2K6Cpe"
updated_at: "2026-07-20 09:21:45"
---

> Source: https://open.dingtalk.com/document/development/get-course-summary-data
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课堂概要数据
> Updated: 2026-07-20 09:21:45

# 获取课堂概要数据

调用本接口，获取课堂概要数据，包括数据类别编码、课堂数据、课堂编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/summadata/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_read-钉钉教育在线课堂数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cursor | Number | 是 | 0 | 分页游标，从0开始。 |
| size | Number | 是 | 10 | 分页大小。 |
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_userid | String | 是 | manager | 当前操作人的userId。 |
| category\_codes | String[] | 是 | BASIC\_INFO,RAISE\_HAND | 数据类别编码数组，可参考[数据类别](1136-teaching-data-overview.md#section-2mx-hrp-6et)介绍。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/summadata/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2bf1eb4xxxx0b21eb' \
-d 'category_codes=BASIC_INFO%2CRAISE_HAND' \
-d 'course_code=GJKI49001' \
-d 'cursor=0' \
-d 'op_userid=manager' \
-d 'size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/summadata/list");
OapiEduCourseSummadataListRequest req = new OapiEduCourseSummadataListRequest();
req.setCursor(0L);
req.setSize(10L);
req.setCourseCode("GJKI49001");
req.setOpUserid("manager");
req.setCategoryCodes("BASIC_INFO");
OapiEduCourseSummadataListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseSummadataListRequest("https://oapi.dingtalk.com/topapi/edu/course/summadata/list")

req.cursor=0
req.size=10
req.course_code="GJKI49001"
req.op_userid="manager"
req.category_codes="BASIC_INFO,RAISE_HAND"
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
$req = new OapiEduCourseSummadataListRequest;
$req->setCursor("0");
$req->setSize("10");
$req->setCourseCode("GJKI49001");
$req->setOpUserid("manager");
$req->setCategoryCodes("BASIC_INFO,RAISE_HAND");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/summadata/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/summadata/list");
OapiEduCourseSummadataListRequest req = new OapiEduCourseSummadataListRequest();
req.Cursor = 0L;
req.Size = 10L;
req.CourseCode = "GJKI49001";
req.OpUserid = "manager";
req.CategoryCodes = "BASIC_INFO,RAISE_HAND";
OapiEduCourseSummadataListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageQueryResponse |  | 返回结果。 |
| next\_cursor | Number | 0 | 表示下一次分页的游标。  如果next\_corsor为null或者has\_more为false，表示没有更多的分页数据。 |
| has\_more | Boolean | true | 表示是否还有更多的数据。   - **true**：有 - **false**：没有 |
| list | CourseSummaryDataDTO[] |  | 课堂数据。 |
| category\_code | String | BASIC\_INFO | 数据类别编码，可参考[数据类别](1136-teaching-data-overview.md#section-2mx-hrp-6et)介绍。 |
| category\_biz\_key | String | 1\_6d20b8xxxx | 数据类别业务唯一键。 |
| data | Json | {"classroomMemberCount":2,"classroomEndTime":1600696867000,"classroomStartTime":1600696128000,"classroomMessageCount":2} | 课堂数据。   - **key**：数据因子编码 - **value**： 对应的数据 |
| course\_code | String | GJKI49001 | 课堂编码。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 2zw2h7s074d1 | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "next_cursor": 0,
    "has_more": true,
    "list": [
      {
        "category_biz_key": "1_6d20b8axxxx37b4b4",
        "data": "{\"classroomMemberCount\":2,\"classroomEndTime\":1600696867000,\"classroomStartTime\":1600696128000,\"classroomMessageCount\":2}",
        "course_code": "GJKI49001",
        "category_code": "BASIC_INFO"
      }
    ]
  },
  "errcode": 0,
  "success": true,
  "errmsg": "ok",
  "request_id": "2zw2h7s074d1"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
