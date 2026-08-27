---
title: "获取学科实例列表"
source_url: "https://open.dingtalk.com/document/development/get-the-list-of-subject-examples"
namespace: "development"
slug: "get-the-list-of-subject-examples"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学科实例列表"
doc_id: "3r1xPEDFzo"
updated_at: "2026-06-08 09:47:37"
---

> Source: https://open.dingtalk.com/document/development/get-the-list-of-subject-examples
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学科实例列表
> Updated: 2026-06-08 09:47:37

# 获取学科实例列表

调用本接口，可获取学科实例列表，包括学科编码、学科名称、学段编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/subject/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_maindata\_read-钉钉教育元数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cursor | Number | 是 | 0 | 游标，从0开始。 |
| data\_order\_type | Number | 否 | 0 | 排序依赖字段类型。 |
| size | Number | 是 | 100 | 每页数据条数。 |
| sort\_type | Number | 否 | 1 | 排序规则。   - **0**：升序 - **1**：降序 |
| operator\_userid | String | 是 | user4551 | 用户的userId。 |
| subject\_code\_list | String | 否 | [\"cn\_p\_shuxue\",\"cn\_p\_yuwen\"] | 学科编码列表，调用[获取学科元数据列表](1134-dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject.md)接口获取subject\_code参数值。 |
| period\_code | String | 是 | primary\_school | 学段编码，调用[获取学段元数据列表](1128-dingtalk-the-main-data-of-the-education-ecosystem-to-query.md)接口获取period\_code参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/subject/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c8e975e7-bd6e-47c9-8061-0cae27655836' \
-d 'cursor=0' \
-d 'data_order_type=0' \
-d 'operator_userid=user4551' \
-d 'period_code=primary_school' \
-d 'size=100' \
-d 'sort_type=1' \
-d 'subject_code_list=%22cn_p_shuxue%22%2C%22cn_p_yuwen%22'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/list");
OapiEduSubjectListRequest req = new OapiEduSubjectListRequest();
req.setCursor(0L);
req.setDataOrderType(0L);
req.setSize(100L);
req.setSortType(1L);
req.setOperatorUserid("user4551");
req.setSubjectCodeList("[\"cn_p_shuxue\",\"cn_p_yuwen\"]");
req.setPeriodCode("primary_school");
OapiEduSubjectListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduSubjectListRequest("https://oapi.dingtalk.com/topapi/edu/subject/list")

req.cursor=0
req.data_order_type=0
req.size=100
req.sort_type=1
req.operator_userid="user4551"
req.subject_code_list="["cn_p_shuxue","cn_p_yuwen"]"
req.period_code="primary_school"
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
$req = new OapiEduSubjectListRequest;
$req->setCursor("0");
$req->setDataOrderType("0");
$req->setSize("100");
$req->setSortType("1");
$req->setOperatorUserid("user4551");
$req->setSubjectCodeList("[\"cn_p_shuxue\",\"cn_p_yuwen\"]");
$req->setPeriodCode("primary_school");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/subject/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/list");
OapiEduSubjectListRequest req = new OapiEduSubjectListRequest();
req.Cursor = 0L;
req.DataOrderType = 0L;
req.Size = 100L;
req.SortType = 1L;
req.OperatorUserid = "user4551";
req.SubjectCodeList = ""cn_p_shuxue","cn_p_yuwen"";
req.PeriodCode = "primary_school";
OapiEduSubjectListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageQueryResponse |  | 数据对象。 |
| next\_cursor | Number | 100 | 下一页游标。 |
| has\_more | Boolean | false | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| list | SubjectInstanceDTO[] |  | 学科实例列表。 |
| subject\_code | String | 12 | 学科编码。 |
| subject\_name | String | 数学 | 学科名称。 |
| period\_code | String | primary\_school | 学段编码。 |
| total\_count | Number | 1 | 总数据条数。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "next_cursor": 100,
    "total_count": 1,
    "has_more": false,
    "list": [
      {
        "subject_code": "12",
        "period_code": "primary_school",
        "subject_name": "数学"
      }
    ]
  },
  "success": true,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
