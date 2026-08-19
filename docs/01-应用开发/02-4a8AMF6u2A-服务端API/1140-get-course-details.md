---
title: "获取课程详情"
source_url: "https://open.dingtalk.com/document/development/get-course-details"
namespace: "development"
slug: "get-course-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课程详情"
doc_id: "NAmPfmdfv4"
updated_at: "2026-06-08 09:47:42"
---

> Source: https://open.dingtalk.com/document/development/get-course-details
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课程详情
> Updated: 2026-06-08 09:47:42

# 获取课程详情

调用本接口，获取课程详情，包括课程介绍、课程名称、课程编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_read-钉钉教育在线课堂数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_userid | String | 是 | manager1 | 当前操作人的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=554529ea-2574-445e-833b-bf240e4f4ecf' \
-d 'course_code=GJKI49001' \
-d 'op_userid=manager1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/get");
OapiEduCourseGetRequest req = new OapiEduCourseGetRequest();
req.setCourseCode("GJKI49001");
req.setOpUserid("manager1");
OapiEduCourseGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseGetRequest("https://oapi.dingtalk.com/topapi/edu/course/get")

req.course_code="GJKI49001"
req.op_userid="manager1"
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
$req = new OapiEduCourseGetRequest;
$req->setCourseCode("GJKI49001");
$req->setOpUserid("manager1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/get");
OapiEduCourseGetRequest req = new OapiEduCourseGetRequest();
req.CourseCode = "GJKI49001";
req.OpUserid = "manager1";
OapiEduCourseGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Course |  | 返回结果。 |
| introduce | String | 数字管理师 | 课程介绍。 |
| name | String | 数字化管理 | 课程名称。 |
| code | String | GJKI49001 | 课程编码。 |
| teacher\_corpid | String | ding4220d8e5128dxxxx | 老师的组织corpId。 |
| teacher\_userid | String | teacher1 | 老师的userId。 |
| start\_time | Number | 1596506100000 | 课程开始时间，Unix毫秒时间戳。 |
| end\_time | Number | 1596506200000 | 课程结束时间，Unix毫秒时间戳。 |
| biz\_key | String | uk\_1 | 业务唯一键，用于保证课程的唯一性，防止重复创建。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | f033gckmia | 请求ID。 |

### **响应体示例**

```
{
  "result":{
    "biz_key":"uk_1",
    "start_time":1596506100000,
    "code":"GJKI49001",
    "introduce":"课程介绍",
    "name":"课程名称",
    "end_time":1596506200000,
    "teacher_userid":"teacher1",
    "teacher_corpid":"ding4220d8e5128d0edd"
  },
  "errcode":0,
  "success":true,
  "errmsg":"ok",
  "request_id":"p6raxtjlj007"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
