---
title: "加入课程"
source_url: "https://open.dingtalk.com/document/development/join-course"
namespace: "development"
slug: "join-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 加入课程"
doc_id: "7StToH2AKb"
updated_at: "2026-06-08 09:47:48"
---

> Source: https://open.dingtalk.com/document/development/join-course
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 加入课程
> Updated: 2026-06-08 09:47:48

# 加入课程

调用本接口，加入课程。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/join |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_write-钉钉教育在线课堂数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| course\_code | String | 是 | nRFRa5001 | 需要加入的课程编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_user\_id | String | 是 | manager7078 | 当前操作用户的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/join" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=559409ed-a415-4886-a465-6675e2638e41' \
-d 'course_code=nRFRa5001' \
-d 'op_user_id=manager7078'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/join");
OapiEduCourseJoinRequest req = new OapiEduCourseJoinRequest();
req.setCourseCode("nRFRa5001");
req.setOpUserId("manager7078");
OapiEduCourseJoinResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseJoinRequest("https://oapi.dingtalk.com/topapi/edu/course/join")

req.course_code="nRFRa5001"
req.op_user_id="manager7078"
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
$req = new OapiEduCourseJoinRequest;
$req->setCourseCode("nRFRa5001");
$req->setOpUserId("manager7078");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/join");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/join");
OapiEduCourseJoinRequest req = new OapiEduCourseJoinRequest();
req.CourseCode = "nRFRa5001";
req.OpUserId = "manager7078";
OapiEduCourseJoinResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | JoinCourseResponse |  | 返回结果。 |
| join\_url | String | https://h5.dingtalk.com/live/video\_lesson.htm?feedId=5xxxx | 加入课程的链接。 |
| joinable | Boolean | true | 是否可加入。   - **true**：可以加入 - **false**：不能加入 |
| success | Boolean | true | 操作是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 2zw2h7s074d | 请求ID。 |

### **响应体示例**

```
{
  "result":{
    "join_url":"https://h5.dingtalk.com/live/video_lesson.htm?feedId=d5ff4f29-01bf-441b-a384-81b9d532b6b9&mcnId=1709073120201407324&feedProperty=1&itemId=d5ff4f29-01bf-441b-a384-81b9d532b6b9&dd_nav_bgcolor=FF2C2D2F#/live",
    "joinable":true
  },
  "errcode":0,
  "success":true,
  "errmsg":"ok",
  "request_id": "2zw2h7s074d1"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
