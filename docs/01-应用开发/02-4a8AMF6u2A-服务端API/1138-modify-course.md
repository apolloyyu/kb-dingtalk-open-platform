---
title: "修改课程"
source_url: "https://open.dingtalk.com/document/development/modify-course"
namespace: "development"
slug: "modify-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 修改课程"
doc_id: "p0azO2ae6O"
updated_at: "2026-06-08 09:47:40"
---

> Source: https://open.dingtalk.com/document/development/modify-course
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 修改课程
> Updated: 2026-06-08 09:47:40

# 修改课程

调用本接口，修改课程信息，包括课程的开始时间、结束时间等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_write-钉钉教育在线课堂数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| teacher\_corpid | String | 否 | ding4220d8e5128d0edd | 老师的组织的corpId。CorpId |
| teacher\_userid | String | 否 | teacher1 | 老师的userId。 |
| introduce | String | 是 | 课程介绍 | 课程介绍。 |
| name | String | 是 | 课程名称 | 课程名称。 |
| start\_time | Number | 否 | 1596506100000 | 课程的开始时间，Unix毫秒时间戳。 |
| end\_time | Number | 否 | 1596506200000 | 课程的结束时间，Unix毫秒时间戳。 |
| op\_userid | String | 是 | manager1 | 当前用户的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7a54050b-f7d5-4039-b32b-cf5fa37e598f' \
-d 'course_code=GJKI49001' \
-d 'end_time=1596506200000' \
-d 'introduce=%E8%AF%BE%E7%A8%8B%E4%BB%8B%E7%BB%8D' \
-d 'name=%E8%AF%BE%E7%A8%8B%E5%90%8D%E7%A7%B0' \
-d 'op_userid=manager1' \
-d 'start_time=1596506100000' \
-d 'teacher_corpid=ding4220d8e5128d0edd' \
-d 'teacher_userid=teacher1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/update");
OapiEduCourseUpdateRequest req = new OapiEduCourseUpdateRequest();
req.setCourseCode("GJKI49001");
req.setTeacherCorpid("ding4220d8e5128d0edd");
req.setTeacherUserid("teacher1");
req.setIntroduce("课程介绍");
req.setName("课程名称");
req.setStartTime(1596506100000L);
req.setEndTime(1596506200000L);
req.setOpUserid("manager1");
OapiEduCourseUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseUpdateRequest("https://oapi.dingtalk.com/topapi/edu/course/update")

req.course_code="GJKI49001"
req.teacher_corpid="ding4220d8e5128d0edd"
req.teacher_userid="teacher1"
req.introduce="课程介绍"
req.name="课程名称"
req.start_time=1596506100000
req.end_time=1596506200000
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
$req = new OapiEduCourseUpdateRequest;
$req->setCourseCode("GJKI49001");
$req->setTeacherCorpid("ding4220d8e5128d0edd");
$req->setTeacherUserid("teacher1");
$req->setIntroduce("课程介绍");
$req->setName("课程名称");
$req->setStartTime("1596506100000");
$req->setEndTime("1596506200000");
$req->setOpUserid("manager1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/update");
OapiEduCourseUpdateRequest req = new OapiEduCourseUpdateRequest();
req.CourseCode = "GJKI49001";
req.TeacherCorpid = "ding4220d8e5128d0edd";
req.TeacherUserid = "teacher1";
req.Introduce = "课程介绍";
req.Name = "课程名称";
req.StartTime = 1596506100000L;
req.EndTime = 1596506200000L;
req.OpUserid = "manager1";
OapiEduCourseUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | hex6wxpxz9ld | 请求ID。 |
| result | Boolean | true | 修改是否成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": true,
  "success": true,
  "request_id": "hex6wxpxz9ld"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
