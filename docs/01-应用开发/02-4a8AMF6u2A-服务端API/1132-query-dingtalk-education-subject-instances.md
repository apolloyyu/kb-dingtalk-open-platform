---
title: "获取学科实例详情"
source_url: "https://open.dingtalk.com/document/development/query-dingtalk-education-subject-instances"
namespace: "development"
slug: "query-dingtalk-education-subject-instances"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学科实例详情"
doc_id: "X2oMw3wfnN"
updated_at: "2026-06-08 09:47:36"
---

> Source: https://open.dingtalk.com/document/development/query-dingtalk-education-subject-instances
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学科实例详情
> Updated: 2026-06-08 09:47:36

# 获取学科实例详情

调用本接口，可获取学科实例详情，包括学科名称、学科编码、学段编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/subject/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_maindata\_read-钉钉教育元数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| operator\_userid | String | 是 | user001231 | 用户的userId。 |
| subject\_code | String | 否 | cn\_p\_shuxue | 学科编码，调用[获取学科元数据列表](1134-dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject.md)接口获取subject\_code参数值。 |
| period\_code | String | 是 | primary\_school | 学段编码，调用[获取学段元数据列表](1128-dingtalk-the-main-data-of-the-education-ecosystem-to-query.md)接口获取period\_code参数值。 |
| subject\_name | String | 否 | 数学 | 学科名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/subject/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a82526f5-8b97-42b8-b9c7-30d9eb3f09a4' \
-d 'operator_userid=user001231' \
-d 'period_code=primary_school' \
-d 'subject_code=cn_p_shuxue' \
-d 'subject_name=%E6%95%B0%E5%AD%A6'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/get");
OapiEduSubjectGetRequest req = new OapiEduSubjectGetRequest();
req.setOperatorUserid("user001231");
req.setSubjectCode("cn_p_shuxue");
req.setPeriodCode("primary_school");
req.setSubjectName("数学");
OapiEduSubjectGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduSubjectGetRequest("https://oapi.dingtalk.com/topapi/edu/subject/get")

req.operator_userid="user001231"
req.subject_code="cn_p_shuxue"
req.period_code="primary_school"
req.subject_name="数学"
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
$req = new OapiEduSubjectGetRequest;
$req->setOperatorUserid("user001231");
$req->setSubjectCode("cn_p_shuxue");
$req->setPeriodCode("primary_school");
$req->setSubjectName("数学");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/subject/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/get");
OapiEduSubjectGetRequest req = new OapiEduSubjectGetRequest();
req.OperatorUserid = "user001231";
req.SubjectCode = "cn_p_shuxue";
req.PeriodCode = "primary_school";
req.SubjectName = "数学";
OapiEduSubjectGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 请求是否调用成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | SubjectInstanceDTO |  | 学科实例对象。 |
| subject\_code | String | cn\_p\_shuxue | 学科编码。 |
| period\_code | String | primary\_school | 学段编码。 |
| subject\_name | String | 数学 | 学科名称。 |

### **响应体示例**

```
{
  "errcode":0,
  "result":{
    "subject_code":"cn_p_shuxue",
    "period_code":"primary_school",
    "subject_name":"数学"
  },
  "success":true,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
