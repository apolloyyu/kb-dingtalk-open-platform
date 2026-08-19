---
title: "创建课程"
source_url: "https://open.dingtalk.com/document/development/create-course"
namespace: "development"
slug: "create-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 创建课程"
doc_id: "t8fUZGI2i4"
updated_at: "2026-06-08 09:47:39"
---

> Source: https://open.dingtalk.com/document/development/create-course
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 创建课程
> Updated: 2026-06-08 09:47:39

# 创建课程

调用本接口，可创建课程并获取课程唯一编码。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/create |
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
| op\_userid | String | 是 | manager1 | 当前用户的userId。 |
| teacher\_corpid | String | 是 | ding4220xxxx | 老师的组织的corpId。CorpId |
| teacher\_userid | String | 是 | teacher1 | 老师的userId。 |
| introduce | String | 是 | 数字管理师 | 课程介绍。 |
| biz\_key | String | 是 | uk\_1 | 业务唯一键，用于保证课程的唯一性，防止重复创建。 |
| name | String | 是 | 数字化管理 | 课程名称。 |
| start\_time | Number | 否 | 1596506100000 | 课程的开始时间，Unix毫秒时间戳。 |
| end\_time | Number | 否 | 1596506200000 | 课程的结束时间，Unix毫秒时间戳。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=807d43dc-67e8-4be9-b522-3fecae91fa89' \
-d 'biz_key=uk_1' \
-d 'end_time=1596506200000' \
-d 'introduce=%E6%88%91%E6%98%AF%E8%AF%BE%E7%A8%8B%E4%BB%8B%E7%BB%8D' \
-d 'name=%E6%88%91%E6%98%AF%E8%AF%BE%E7%A8%8B%E5%90%8D%E7%A7%B0' \
-d 'op_userid=manager1' \
-d 'start_time=1596506100000' \
-d 'teacher_corpid=ding4220d8e5128d0edd' \
-d 'teacher_userid=teacher1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/create");
OapiEduCourseCreateRequest req = new OapiEduCourseCreateRequest();
req.setOpUserid("manager1");
req.setTeacherCorpid("ding4220d8e5128d0edd");
req.setTeacherUserid("teacher1");
req.setIntroduce("我是课程介绍");
req.setBizKey("uk_1");
req.setName("我是课程名称");
req.setStartTime(1596506100000L);
req.setEndTime(1596506200000L);
OapiEduCourseCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseCreateRequest("https://oapi.dingtalk.com/topapi/edu/course/create")

req.op_userid="manager1"
req.teacher_corpid="ding4220d8e5128d0edd"
req.teacher_userid="teacher1"
req.introduce="我是课程介绍"
req.biz_key="uk_1"
req.name="我是课程名称"
req.start_time=1596506100000
req.end_time=1596506200000
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
$req = new OapiEduCourseCreateRequest;
$req->setOpUserid("manager1");
$req->setTeacherCorpid("ding4220d8e5128d0edd");
$req->setTeacherUserid("teacher1");
$req->setIntroduce("我是课程介绍");
$req->setBizKey("uk_1");
$req->setName("我是课程名称");
$req->setStartTime("1596506100000");
$req->setEndTime("1596506200000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/create");
OapiEduCourseCreateRequest req = new OapiEduCourseCreateRequest();
req.OpUserid = "manager1";
req.TeacherCorpid = "ding4220d8e5128d0edd";
req.TeacherUserid = "teacher1";
req.Introduce = "我是课程介绍";
req.BizKey = "uk_1";
req.Name = "我是课程名称";
req.StartTime = 1596506100000L;
req.EndTime = 1596506200000L;
OapiEduCourseCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| course\_code | String | FBnCv218004 | 课程唯一编码。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | f033gckmia | 请求ID。 |

### **响应体示例**

```
{
  "course_code": "FBnCv218004",
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "request_id": "f033gf5ckmia"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
