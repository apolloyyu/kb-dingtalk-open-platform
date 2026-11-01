---
title: "获取人员详情"
source_url: "https://open.dingtalk.com/document/development/obtain-the-identity-details-of-home-school-personnel"
namespace: "development"
slug: "obtain-the-identity-details-of-home-school-personnel"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取人员详情"
doc_id: "XTiNQ6nR4x"
updated_at: "2026-06-08 09:48:06"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-identity-details-of-home-school-personnel
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取人员详情
> Updated: 2026-06-08 09:48:06

# 获取人员详情

调用本接口，查看班级下的人员详细信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/user/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_addresslist\_edu\_read-【敏感】钉钉教育家校通讯录读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| class\_id | Number | 是 | 389206748 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| role | String | 是 | student | 家校人员角色。   - **teacher**：老师 - **guardian**：监护人 - **student**：学生 |
| userid | String | 是 | 1020302901 | 人员userId，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取userid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/user/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8f5bb744-44d3-4a65-841c-56cfe3c7f352' \
-d 'class_id=12345' \
-d 'role=teacher' \
-d 'userid=1233345'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/get");
OapiEduUserGetRequest req = new OapiEduUserGetRequest();
req.setClassId(4240006L);
req.setRole("student");
req.setUserid("manager9707");
OapiEduUserGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduUserGetRequest("https://oapi.dingtalk.com/topapi/edu/user/get")

req.class_id=12345
req.role="teacher"
req.userid="1233345"
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
$req = new OapiEduUserGetRequest;
$req->setClassId("12345");
$req->setRole("teacher");
$req->setUserid("1233345");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/user/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/get");
OapiEduUserGetRequest req = new OapiEduUserGetRequest();
req.ClassId = 12345L;
req.Role = "teacher";
req.Userid = "1233345";
OapiEduUserGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| details | Detail[] |  | 人员身份详情。 |
| class\_id | Number | 4240006 | 班级ID。 |
| role | String | student | 家校人员角色。   - **teacher**: 老师 - **guardian**: 监护人 - **student**: 学生 |
| feature | String | {\"student\_no\":\"9144\"} | 不同角色的其他业务属性，可JSON反序列化。 |
| is\_adviser | String | 0 | 只在老师角色下意义。   - **1**：班主任 - **0**：表示非班主任 |
| student\_no | String | 0 | 学号，只有在学生角色下才有意义。 |
| name | String | 杨xx | 人员姓名。 |
| unionid | String | PiiiPyQqBxxx | 人员的unionId，无手机号的学生为""。 |
| userid | String | manager9707 | 人员userId。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 用户不存在 | 调用失败时返回的错误描述。 |
| request\_id | String | 6gx4s57dsfds | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "details": [{
      "class_id": 4240006,
      "feature": "{\"student_no\":\"3\"}",
      "name": "杨xx",
      "role": "student",
      "unionid": "vFzK5bMU9OsEIGOf3WKwWgiEiE",
      "userid": "manager9707"
    }]
  },
  "success": true,
  "request_id": "sq3vg8kdeqvg"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
