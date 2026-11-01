---
title: "删除学科实例"
source_url: "https://open.dingtalk.com/document/development/delete-dingtalk-education-disciplines"
namespace: "development"
slug: "delete-dingtalk-education-disciplines"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 通用基础 > 删除学科实例"
doc_id: "NKRzLVX7YD"
updated_at: "2026-06-08 09:47:34"
---

> Source: https://open.dingtalk.com/document/development/delete-dingtalk-education-disciplines
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 通用基础 > 删除学科实例
> Updated: 2026-06-08 09:47:34

# 删除学科实例

调用本接口，可根据period\_code、subject\_code等参数删除学科实例。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/subject/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_maindata\_write-钉钉教育元数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| operator\_userid | String | 是 | user7550 | 操作人的userId。 |
| period\_code | String | 是 | primary\_school | 学段编码，调用[获取学段元数据列表](1128-dingtalk-the-main-data-of-the-education-ecosystem-to-query.md)接口获取period\_code参数值。 |
| subject\_name | String | 是 | 数学 | 学科名称。 |
| subject\_code | String | 是 | cn\_p\_shuxue | 学科编码，调用[获取学科元数据列表](1134-dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject.md)接口获取subject\_code参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/subject/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=394601fc-c903-4d8b-8132-60705da00828' \
-d 'operator_userid=user7550' \
-d 'period_code=primary_school' \
-d 'subject_code=cn_p_shuxue' \
-d 'subject_name=%E6%95%B0%E5%AD%A6'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/delete");
OapiEduSubjectDeleteRequest req = new OapiEduSubjectDeleteRequest();
req.setOperatorUserid("user7550");
req.setPeriodCode("primary_school");
req.setSubjectName("数学");
req.setSubjectCode("cn_p_shuxue");
OapiEduSubjectDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduSubjectDeleteRequest("https://oapi.dingtalk.com/topapi/edu/subject/delete")

req.operator_userid="user7550"
req.period_code="primary_school"
req.subject_name="数学"
req.subject_code="cn_p_shuxue"
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
$req = new OapiEduSubjectDeleteRequest;
$req->setOperatorUserid("user7550");
$req->setPeriodCode("primary_school");
$req->setSubjectName("数学");
$req->setSubjectCode("cn_p_shuxue");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/subject/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/delete");
OapiEduSubjectDeleteRequest req = new OapiEduSubjectDeleteRequest();
req.OperatorUserid = "user7550";
req.PeriodCode = "primary_school";
req.SubjectName = "数学";
req.SubjectCode = "cn_p_shuxue";
OapiEduSubjectDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 操作是否成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result":true,
  "errcode":0,
  "success":true,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
