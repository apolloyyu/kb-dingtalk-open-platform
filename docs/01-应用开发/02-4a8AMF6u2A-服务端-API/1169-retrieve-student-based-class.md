---
title: "获取学生ID列表"
source_url: "https://open.dingtalk.com/document/development/retrieve-student-based-class"
namespace: "development"
slug: "retrieve-student-based-class"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取学生ID列表"
doc_id: "ZpuODnXH6P"
updated_at: "2026-06-08 09:48:18"
---

> Source: https://open.dingtalk.com/document/development/retrieve-student-based-class
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取学生ID列表
> Updated: 2026-06-08 09:48:18

# 获取学生ID列表

调用本接口，根据班级ID和教师ID获取学生的ID列表，包括班级ID、学生ID等信息。接口会校验教师是否已授权第三方企业应用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/class/studentid/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_homework\_read-钉钉教育学生信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该API的应用凭证，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| class\_id | Number | 是 | 26347 | 班级ID，调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| app\_id | Number | 是 | 13708001 | 应用ID，可在[开发者后台](https://open-dev.dingtalk.com/#/)的**应用信息**页面查看。image |
| userid | String | 是 | tea123 | 教师userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/class/studentid/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=662381ab-dc29-4762-8791-cd6713ed8752' \
-d 'app_id=321' \
-d 'class_id=123' \
-d 'userid=12321'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/class/studentid/get");
OapiEduClassStudentidGetRequest req = new OapiEduClassStudentidGetRequest();
req.setClassId(26347L);
req.setAppId(13708001L);
req.setUserid("tea123");
OapiEduClassStudentidGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduClassStudentidGetRequest("https://oapi.dingtalk.com/topapi/edu/class/studentid/get")

req.class_id=123
req.app_id=321
req.userid="12321"
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
$req = new OapiEduClassStudentidGetRequest;
$req->setClassId("123");
$req->setAppId("321");
$req->setUserid("12321");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/class/studentid/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/class/studentid/get");
OapiEduClassStudentidGetRequest req = new OapiEduClassStudentidGetRequest();
req.ClassId = 123L;
req.AppId = 321L;
req.Userid = "12321";
OapiEduClassStudentidGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenEduSelectStudentIdResponse |  | 返回结果。 |
| class\_id | Number | 26347 | 班级ID。 |
| student\_ids | String[] | ["student1","student2"] | 学生ID列表。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "class_id": 26347,
    "student_ids": [
      "student1",
      "student2"
    ]
  },
  "success": true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
