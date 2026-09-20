---
title: "获取人员列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-home-school-user-identities"
namespace: "development"
slug: "obtains-a-list-of-home-school-user-identities"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取人员列表"
doc_id: "6Vnj3sEoiR"
updated_at: "2026-06-08 09:48:04"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-home-school-user-identities
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取人员列表
> Updated: 2026-06-08 09:48:04

# 获取人员列表

调用本接口，查看班级下的人员身份列表，一个人有可能存在多种家校身份。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/user/list |
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
| page\_size | Number | 是 | 30 | 每页大小，取值1~30。 |
| page\_no | Number | 是 | 1 | 页码，从1开始。 |
| role | String | 是 | student | 家校人员角色。   - **teacher**：老师 - **guardian**：监护人 - **student**：学生 |
| class\_id | Number | 是 | 4242006 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/user/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b791fd6f-3d90-4423-b635-a7f3149469c8' \
-d 'class_id=123435' \
-d 'page_no=1' \
-d 'page_size=30' \
-d 'role=teacher'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/list");
OapiEduUserListRequest req = new OapiEduUserListRequest();
req.setPageSize(30L);
req.setPageNo(1L);
req.setRole("student");
req.setClassId(4242006L);
OapiEduUserListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduUserListRequest("https://oapi.dingtalk.com/topapi/edu/user/list")

req.page_size=30
req.page_no=1
req.role="teacher"
req.class_id=123435
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
$req = new OapiEduUserListRequest;
$req->setPageSize("30");
$req->setPageNo("1");
$req->setRole("teacher");
$req->setClassId("123435");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/user/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/list");
OapiEduUserListRequest req = new OapiEduUserListRequest();
req.PageSize = 30L;
req.PageNo = 1L;
req.Role = "teacher";
req.ClassId = 123435L;
OapiEduUserListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| has\_more | Boolean | true | 是否还有数据。   - **true**：有 - **false**：没有 |
| details | OpenEduUserDetail[] |  | 人员身份列表。 |
| class\_id | Number | 4242006 | 班级ID。 |
| role | String | student | 家校人员角色。   - **teacher**：老师 - **guardian**：监护人 - **student**：学生 |
| feature | String |  | 不同角色的其他业务属性，可JSON反序列化。 |
| is\_adviser | String | 0 | 只在老师角色下意义。   - **1**：班主任 - **0**：非班主任 |
| student\_no | String | 3 | 学号，只有在学生角色下才有意义，**并且需确认各个班级的设置，如果没有设置，则不会返回此字段**。 |
| name | String | alan爸爸/alex爸爸 | 人员姓名。 |
| unionid | String | PiiiPyQqBxxx | 人员的unionId，无手机号的学生为""。 |
| userid | String | 15919287602721 | 人员的userId。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6i7k06ww3wy0 | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "has_more": false,
    "details": [
      {
        "userid":"10203029011219896",
        "class_id": 4242006,
        "role": "student",
        "unionid":"",
        "feature": "{\"student_no\":\"3\"}",
        "name": "杨xx"
      },
      {
        "userid":"15919287008782996632",
        "class_id": 4242006,
        "role": "student",
        "unionid":"",
        "feature": "{\"student_no\":\"1\"}",
        "name": "alan"
      },
      {
        "userid":"15919287174832996766",
        "classId": 4242006,
        "role": "student",
        "unionid":"",
        "feature": "{\"student_no\":\"2\"}",
        "name": "alex"
      }
    ]
  },
  "success": true,
  "errcode": 0,
  "errmsg":"ok",
  "request_id":"6i7k06ww3wy0"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
