---
title: "添加老师"
source_url: "https://open.dingtalk.com/document/development/add-teacher"
namespace: "development"
slug: "add-teacher"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 添加老师"
doc_id: "6O7sQFOURA"
updated_at: "2026-06-08 09:48:17"
---

> Source: https://open.dingtalk.com/document/development/add-teacher
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 添加老师
> Updated: 2026-06-08 09:48:17

# 添加老师

调用本接口，在指定班级下新增老师信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/teacher/create |
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
| biz\_id | String | 否 | biz\_id | 业务ID，自定义值，每次调用该参数保持唯一。 |
| adviser | Number | 是 | 1 | 是否为班主任。   - **0**：非班主任 - **1**：班主任 |
| userid | String | 是 | 129039503 | 老师的userId。 |
| operator | String | 是 | user01 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/teacher/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=686df454-e85c-4a3d-9725-d1764e4ef9f8' \
-d 'adviser=1' \
-d 'biz_id=1234' \
-d 'class_id=1234' \
-d 'operator=12345' \
-d 'userid=123345'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/teacher/create");
OapiEduTeacherCreateRequest req = new OapiEduTeacherCreateRequest();
req.setAdviser(1L);
req.setBizId("biz_id");
req.setClassId(4240018L);
req.setOperator("user01");
req.setUserid("129039503");
OapiEduTeacherCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduTeacherCreateRequest("https://oapi.dingtalk.com/topapi/edu/teacher/create")

req.class_id=1234
req.biz_id="1234"
req.adviser=1
req.userid="123345"
req.operator="12345"
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
$req = new OapiEduTeacherCreateRequest;
$req->setClassId("1234");
$req->setBizId("1234");
$req->setAdviser("1");
$req->setUserid("123345");
$req->setOperator("12345");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/teacher/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/teacher/create");
OapiEduTeacherCreateRequest req = new OapiEduTeacherCreateRequest();
req.ClassId = 1234L;
req.BizId = "1234";
req.Adviser = 1L;
req.Userid = "123345";
req.Operator = "12345";
OapiEduTeacherCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenEduUserCreateResponse |  | 调用结果。 |
| biz\_id | String | biz\_id | 业务ID。 |
| userid | String | 129039503 | 老师的userId。 |
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
