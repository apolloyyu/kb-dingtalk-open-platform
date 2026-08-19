---
title: "添加课程参与方"
source_url: "https://open.dingtalk.com/document/development/add-course-participants"
namespace: "development"
slug: "add-course-participants"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 添加课程参与方"
doc_id: "zqz1EeJy8s"
updated_at: "2026-06-08 09:47:44"
---

> Source: https://open.dingtalk.com/document/development/add-course-participants
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 添加课程参与方
> Updated: 2026-06-08 09:47:44

# 添加课程参与方

调用本接口，可添加课程参与方。参与方角色包括学生、监护人和老师。

## **接口调用说明**

授课老师只支持通过[创建课程](1137-create-course.md)和[修改课程](1138-modify-course.md)接口进行添加和修改。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/participant/add |
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
| op\_userid | String | 是 | manager1 | 当前操作者的userId。 |
| participant\_corpid | String | 是 | ding4220d8e5128d0edd | 参与方的组织cropId。CorpId  **[!IMPORTANT]**  **必须和当前组织相同或者存在关联关系。**  第三方企业应用请参考[关联关系](0152-associated-organizations-overview.md)。 |
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| participant\_type | Number | 是 |  | 参与方类型。   - **1**：用户，可添加的人数上限为1000。 - **2**：部门，可添加的部门数上限为100，对应家校通讯录中的班级、年级。 - **3**：组织，可添加的组织数上限为5。 |
| participant\_id | String | 是 | user01 | 参与方ID。   - participant\_type=1时，participant\_id为用户的userid - participant\_type=2时，participant\_id为部门ID - participant\_type=3时，participant\_id为组织的corpid |
| role | String | 是 | student | 参与方角色。   - **student**：学生 - **guardian**: 监护人 - **teacher**：老师  **[!IMPORTANT]**  授课老师只支持通过[创建课程](1137-create-course.md)和[修改课程](1138-modify-course.md)接口进行添加和修改。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/participant/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=bdd273ff-c9f4-41f3-bf88-aebc5745527b' \
-d 'course_code=GJKI49001' \
-d 'op_userid=manager1' \
-d 'participant_corpid=ding4220d8e5128d0edd' \
-d 'participant_id=user01' \
-d 'role=student'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/participant/add");
OapiEduCourseParticipantAddRequest req = new OapiEduCourseParticipantAddRequest();
req.setOpUserid("manager1");
req.setParticipantCorpid("ding4220d8e5128d0edd");
req.setCourseCode("GJKI49001");
req.setParticipantId("user01");
req.setRole("student");
req.setParticipantType(1L);
OapiEduCourseParticipantAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseParticipantAddRequest("https://oapi.dingtalk.com/topapi/edu/course/participant/add")

req.op_userid="manager1"
req.participant_corpid="ding4220d8e5128d0edd"
req.course_code="GJKI49001"
req.participant_id="user01"
req.role="student"
req.participant_type=1
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
$req = new OapiEduCourseParticipantAddRequest;
$req->setOpUserid("manager1");
$req->setParticipantCorpid("ding4220d8e5128d0edd");
$req->setCourseCode("GJKI49001");
$req->setParticipantId("user01");
$req->setRole("student");
$req->setParticipantType("1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/participant/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/participant/add");
OapiEduCourseParticipantAddRequest req = new OapiEduCourseParticipantAddRequest();
req.OpUserid = "manager1";
req.ParticipantCorpid = "ding4220d8e5128d0edd";
req.CourseCode = "GJKI49001";
req.ParticipantId = "user01";
req.Role = "student";
req.ParticipantType = 1L;
OapiEduCourseParticipantAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | hex6wxpxz9ld | 请求ID。 |
| result | Boolean | true | 添加是否成功。   - **true**：成功 - **false**：失败 |
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
  "request_id": "2zw2h7s074d1"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
