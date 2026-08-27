---
title: "开始课程"
source_url: "https://open.dingtalk.com/document/development/start-course"
namespace: "development"
slug: "start-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 开始课程"
doc_id: "Z73Iybm8US"
updated_at: "2026-06-08 09:47:50"
---

> Source: https://open.dingtalk.com/document/development/start-course
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 开始课程
> Updated: 2026-06-08 09:47:50

# 开始课程

调用本接口，开始课程。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/start |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_write-钉钉教育在线课堂数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | be3xxxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| course\_code | String | 是 | nRFRa5001 | 需要开始的课程编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| op\_user\_id | String | 是 | manager7078 | 操作用户的userId。 |
| start\_option | StartOption | 否 |  | 开始课程的可选属性设定。 |
| b\_allow\_join\_in\_advance | Boolean | 否 | true | 是否允许提前进入课堂。   - **true**：表明生成的课堂可以允许学生最多提前30分钟进入 - **false**（默认）：不允许学生提前进入课堂，只有老师发起后才可进入。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/start" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=68afc032-047a-435d-bd19-1556296ad5fc' \
-d 'course_code=nRFRa5001' \
-d 'op_user_id=manager7078' \
-d 'start_option=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/start");
OapiEduCourseStartRequest req = new OapiEduCourseStartRequest();
req.setCourseCode("nRFRa5001");
req.setOpUserId("manager7078");
OapiEduCourseStartRequest.StartOption obj1 = new OapiEduCourseStartRequest.StartOption();
obj1.setbAllowJoinInAdvance(true);
req.setStartOption(obj1);
OapiEduCourseStartResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseStartRequest("https://oapi.dingtalk.com/topapi/edu/course/start")

req.course_code="nRFRa5001"
req.op_user_id="manager7078"
req.start_option=""
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
$req = new OapiEduCourseStartRequest;
$req->setCourseCode("nRFRa5001");
$req->setOpUserId("manager7078");
$start_option = new StartOption;
$start_option->b_allow_join_in_advance="true";
$req->setStartOption($start_option);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/start");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/start");
OapiEduCourseStartRequest req = new OapiEduCourseStartRequest();
req.CourseCode = "nRFRa5001";
req.OpUserId = "manager7078";
OapiEduCourseStartRequest.StartOptionDomain obj1 = new OapiEduCourseStartRequest.StartOptionDomain();
obj1.BAllowJoinInAdvance = true;
req.StartOption_ = obj1;
OapiEduCourseStartResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | StartCourseResponse |  | 返回结果。 |
| target\_type | Number | 2 | 交互目标类型。   - **2**：使用在线课堂 |
| target\_id | String | d5ff4f29-9d53xxxxx | 课堂的ID。  当target\_type为2时，target\_id表示在线课堂的ID。 |
| is\_reuse | Boolean | true | 是否重用已有的课堂。   - **true**：重用 - **false**：不重用 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result": {
    "is_reuse": true,
    "target_type": 2,
    "target_id": "d5ff4f29-01bf-441b-a384-81b9d532b6b9"
  },
  "errcode": 0,
  "success": true,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
