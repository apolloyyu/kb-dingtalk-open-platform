---
title: "获取课程参与方列表"
source_url: "https://open.dingtalk.com/document/development/get-a-list-of-course-participants"
namespace: "development"
slug: "get-a-list-of-course-participants"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课程参与方列表"
doc_id: "DTgLGCyCkG"
updated_at: "2026-06-08 09:47:46"
---

> Source: https://open.dingtalk.com/document/development/get-a-list-of-course-participants
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课程参与方列表
> Updated: 2026-06-08 09:47:46

# 获取课程参与方列表

调用本接口，可获取课程参与方信息，包括参与方角色、参与方ID、参与方类型等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/participant/list |
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
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_userid | String | 是 | manager | 当前操作人的userId。 |
| cursor | Number | 是 | 0 | 分页游标，从0开始。 |
| size | Number | 是 | 10 | 分页大小，取值1~100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/participant/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1ce7107c-4c85-4dc9-8040-a2c70ffc8906' \
-d 'course_code=GJKI49001' \
-d 'cursor=0' \
-d 'op_userid=manager' \
-d 'size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/participant/list");
OapiEduCourseParticipantListRequest req = new OapiEduCourseParticipantListRequest();
req.setCourseCode("GJKI49001");
req.setOpUserid("manager");
req.setCursor(0L);
req.setSize(10L);
OapiEduCourseParticipantListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseParticipantListRequest("https://oapi.dingtalk.com/topapi/edu/course/participant/list")

req.course_code="GJKI49001"
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
$req = new OapiEduCourseParticipantListRequest;
$req->setCourseCode("GJKI49001");
$req->setOpUserid("manager");
$req->setCursor("0");
$req->setSize("10");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/participant/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/participant/list");
OapiEduCourseParticipantListRequest req = new OapiEduCourseParticipantListRequest();
req.CourseCode = "GJKI49001";
req.OpUserid = "manager";
req.Cursor = 0L;
req.Size = 10L;
OapiEduCourseParticipantListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ListCourseParticipantResponse |  | 返回结果。 |
| has\_more | Boolean | true | 是否还有更多的数据。   - **true**：有 - **false**：没有 |
| list | CourseParticipantVO[] |  | 参与方列表。 |
| role | String | student | 参与方角色。   - **student**：学生 - **teacher**：老师 - **guardian**: 监护人 |
| participant\_id | String | user01 | 参与方ID。   - participant\_type=1时，participant\_id表示用户ID - participant\_type=2时，participant\_id表示部门ID - participant\_type=3时，participant\_id表示组织ID |
| participant\_type | String | 1 | 参与方类型。   - **1**：用户 - **2**：部门（对应家校通讯录中的班级、年级 - **3**：组织 |
| participant\_corpid | String | ding4220d8e5128d0edd | 参与方的组织的corpId。 |
| next\_cursor | Number | 10 | 表示下一次分页的游标。  如果next\_corsor为null或者has\_more为false，表示没有更多的分页数据。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 2zw2h7s074d1 | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "next_cursor": "10",
    "has_more": "true",
    "list": [
      {
        "participant_type": "1",
        "role": "student",
        "participant_corpid": "ding4220d8e5128d0edd",
        "participant_id": "user01"
      }
    ]
  },
  "errcode": "0",
  "success": "true",
  "errmsg": "ok",
  "request_id": "2zw2h7s074d1"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
