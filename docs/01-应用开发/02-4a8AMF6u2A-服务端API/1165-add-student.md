---
title: "添加学生"
source_url: "https://open.dingtalk.com/document/development/add-student"
namespace: "development"
slug: "add-student"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 添加学生"
doc_id: "V5A72iWaw3"
updated_at: "2026-06-08 09:48:14"
---

> Source: https://open.dingtalk.com/document/development/add-student
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 添加学生
> Updated: 2026-06-08 09:48:14

# 添加学生

调用本接口，在指定的班级下新增学生信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/student/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-钉钉教育家校通讯录写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| class\_id | Number | 是 | 4240018 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| name | String | 是 | 阳xx | 学生姓名。 |
| biz\_id | String | 否 | biz\_id | 业务的唯一ID，自定义值，每次调用保持唯一。 |
| student\_no | String | 否 | no12 | 学生学号，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取student\_no参数值。 |
| operator | String | 是 | user01 | 钉钉企业管理员的userId。 |
| mobile | String | 否 | 152xxxxxxxx | 学生手机号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/student/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=73e195fa-7e0d-413a-a5be-45f8966ac434' \
-d 'biz_id=1234' \
-d 'class_id=12345' \
-d 'mobile=13812345678' \
-d 'name=%E5%BC%A0%E4%B8%89' \
-d 'operator=123456' \
-d 'student_no=1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/student/create");
OapiEduStudentCreateRequest req = new OapiEduStudentCreateRequest();
req.setBizId("biz_id");
req.setClassId(4240018L);
req.setName("阳xx");
req.setOperator("user01");
req.setStudentNo("no12");
req.setMobile("152xxxxxxxx")
OapiEduStudentCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduStudentCreateRequest("https://oapi.dingtalk.com/topapi/edu/student/create")

req.class_id=12345
req.name="张三"
req.biz_id="1234"
req.student_no="1"
req.operator="123456"
req.mobile="13812345678"
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
$req = new OapiEduStudentCreateRequest;
$req->setClassId("12345");
$req->setName("张三");
$req->setBizId("1234");
$req->setStudentNo("1");
$req->setOperator("123456");
$req->setMobile("13812345678");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/student/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/student/create");
OapiEduStudentCreateRequest req = new OapiEduStudentCreateRequest();
req.ClassId = 12345L;
req.Name = "张三";
req.BizId = "1234";
req.StudentNo = "1";
req.Operator = "123456";
req.Mobile = "13812345678";
OapiEduStudentCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 调用结果。 |
| biz\_id | String | biz\_id | 业务的唯一ID。 |
| userid | String | manager01 | 学生的userId。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 5bsof0hsgtds | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "biz_id": "biz_id",
    "userid": "manager01"
  },
  "success": true,
  "request_id": "5bsof0hsgtds"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
