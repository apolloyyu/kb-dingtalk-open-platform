---
title: "回放课程"
source_url: "https://open.dingtalk.com/document/development/replay-course"
namespace: "development"
slug: "replay-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 回放课程"
doc_id: "dba4H6LRyI"
updated_at: "2026-06-08 09:47:52"
---

> Source: https://open.dingtalk.com/document/development/replay-course
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 回放课程
> Updated: 2026-06-08 09:47:52

# 回放课程

调用本接口，可获取课程回放链接，用于进行在线课堂授课的内容回放。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/replay |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_read-钉钉教育在线课堂数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| course\_code | String | 是 | nRFRa5001 | 需要回放的课程编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_user\_id | String | 是 | manager7078 | 操作用户的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/replay" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c81bb012-14a0-4946-a282-129fe96c53ae' \
-d 'course_code=nRFRa5001' \
-d 'op_user_id=manager7078'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/replay");
OapiEduCourseReplayRequest req = new OapiEduCourseReplayRequest();
req.setCourseCode("nRFRa5001");
req.setOpUserId("manager7078");
OapiEduCourseReplayResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseReplayRequest("https://oapi.dingtalk.com/topapi/edu/course/replay")

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
$req = new OapiEduCourseReplayRequest;
$req->setCourseCode("nRFRa5001");
$req->setOpUserId("manager7078");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/replay");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/replay");
OapiEduCourseReplayRequest req = new OapiEduCourseReplayRequest();
req.CourseCode = "nRFRa5001";
req.OpUserId = "manager7078";
OapiEduCourseReplayResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ReplayCourseResponse |  | 返回结果。 |
| replayable | Boolean | true | 是否可回放。   - **true**：可以回放 - **false**：不能回放 |
| replay\_urls | String[] | ["https://h5.dingtalk.com/live/video\_lesson.htm?feedId=xxxx&mcnId=xxxx&feedProperty=1&itemId=xxxx&dd\_nav\_bgcolor=FF2C2D2F#/live"] | 回放url列表。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result": {
    "replayable": true,
    "replay_urls": [
      "https://h5.dingtalk.com/live/video_lesson.htm?feedId=xxxx&mcnId=xxxx&feedProperty=1&itemId=xxxx&dd_nav_bgcolor=FF2C2D2F#/live"
    ]
  },
  "errcode": 0,
  "success": true,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
