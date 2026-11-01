---
title: "删除课程"
source_url: "https://open.dingtalk.com/document/development/delete-course"
namespace: "development"
slug: "delete-course"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 删除课程"
doc_id: "fzJfty5DI8"
updated_at: "2026-06-08 09:47:41"
---

> Source: https://open.dingtalk.com/document/development/delete-course
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 删除课程
> Updated: 2026-06-08 09:47:41

# 删除课程

调用本接口，可根据course\_code参数删除课程。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_write-钉钉教育在线课堂数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_userid | String | 是 | manager1 | 当前操作人的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=5a59c491-87e0-4df4-bf3c-4600d2b51b87' \
-d 'course_code=GJKI49001' \
-d 'op_userid=manager1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/delete");
OapiEduCourseDeleteRequest req = new OapiEduCourseDeleteRequest();
req.setCourseCode("GJKI49001");
req.setOpUserid("manager1");
OapiEduCourseDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseDeleteRequest("https://oapi.dingtalk.com/topapi/edu/course/delete")

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
$req = new OapiEduCourseDeleteRequest;
$req->setCourseCode("GJKI49001");
$req->setOpUserid("manager1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/delete");
OapiEduCourseDeleteRequest req = new OapiEduCourseDeleteRequest();
req.CourseCode = "GJKI49001";
req.OpUserid = "manager1";
OapiEduCourseDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | hex6wxpxz9ld | 请求ID。 |
| result | Boolean | true | 删除是否成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result":true,
  "errcode":0,
  "success":true,
  "errmsg":"ok",
  "request_id": "hex6wxpxz9ld"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
