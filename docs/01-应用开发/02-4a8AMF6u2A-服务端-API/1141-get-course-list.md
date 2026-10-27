---
title: "获取课程列表"
source_url: "https://open.dingtalk.com/document/development/get-course-list"
namespace: "development"
slug: "get-course-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课程列表"
doc_id: "kWRgWNC12G"
updated_at: "2026-06-08 09:47:43"
---

> Source: https://open.dingtalk.com/document/development/get-course-list
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课程列表
> Updated: 2026-06-08 09:47:43

# 获取课程列表

调用本接口，可获取课程列表，包括课程介绍、课程名称、课程编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/list |
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
| op\_userid | String | 是 | manager | 当前操作人的userId。 |
| cursor | Number | 是 | 0 | 分页游标，从0开始。 |
| size | Number | 是 | 10 | 分页大小，取值1~100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=32ee7ad4-53d7-447e-a6f6-3433d7d0fdd9' \
-d 'cursor=0' \
-d 'op_userid=manager' \
-d 'size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/list");
OapiEduCourseListRequest req = new OapiEduCourseListRequest();
req.setOpUserid("manager");
req.setCursor(0L);
req.setSize(10L);
OapiEduCourseListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseListRequest("https://oapi.dingtalk.com/topapi/edu/course/list")

req.op_userid="manager"
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
$req = new OapiEduCourseListRequest;
$req->setOpUserid("manager");
$req->setCursor("0");
$req->setSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/list");
OapiEduCourseListRequest req = new OapiEduCourseListRequest();
req.OpUserid = "manager";
req.Cursor = 0L;
req.Size = 10L;
OapiEduCourseListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | f033gckmia | 请求ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | ListCourseResponse |  | 返回结果。 |
| has\_more | Boolean | ture | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| list | CourseVO[] |  | 课程列表。 |
| biz\_key | String | uk\_1 | 业务唯一键，用于保证课程的唯一性，防止重复创建。 |
| teacher\_userid | String | manager4220 | 老师的userId。 |
| teacher\_corpid | String | ding4220d8e5128d0edd | 老的的组织的corpId。 |
| end\_time | Number | 1596506200000 | 结束时间，Unix毫秒时间戳。 |
| start\_time | Number | 1596506100000 | 开始时间，Unix毫秒时间戳。 |
| introduce | String | 课程介绍 | 课程介绍。 |
| name | String | 课程名称 | 课程名称。 |
| code | String | 12312 | 课程编码。 |
| next\_cursor | Number | FBnCv218004 | 表示下一次分页的游标。  如果next\_corsor为null或者has\_more为false，表示没有更多的分页数据。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "has_more": false,
    "list": [
      {
        "biz_key": "uk_1",
        "code": "FBnCv218004",
        "end_time": 1602675300000,
        "introduce": "数字化管理师",
        "name": "数字化管理",
        "start_time": 1602675000000,
        "teacher_corpid": "ding99b58ff12396b07d24f2f5cc6abecbxxxx",
        "teacher_userid": "manager1102"
      }
    ],
    "next_cursor": 10
  },
  "success": true,
  "request_id": "nqvwptnc4c7n"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
