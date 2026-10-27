---
title: "获取学科元数据列表"
source_url: "https://open.dingtalk.com/document/development/dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject"
namespace: "development"
slug: "dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学科元数据列表"
doc_id: "vrRdbbW11f"
updated_at: "2026-06-08 09:47:38"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学科元数据列表
> Updated: 2026-06-08 09:47:38

# 获取学科元数据列表

调用本接口，可获取学科元数据列表，包括学科元数据ID、区域编码、学段编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/subject/metadata/list |
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
| cursor | Number | 是 | 0 | 分页游标，从0开始。 |
| level | Number | 否 | 2 | 层级。 |
| operator\_userid | String | 是 | user0012 | 用户的userId。 |
| parent\_id | Number | 否 | 11 | 父ID，调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为period时的dept\_id参数值。 |
| period\_code | String | 是 | primary\_school | 学段编码，调用[获取学科元数据列表](#)接口获取period\_code参数值。 |
| data\_order\_type | Number | 否 | 0 | 排序依赖字段类型。 |
| area\_code | String | 是 | CN | 地区编码。 |
| size | Number | 是 | 100 | 每页数据条数。 |
| sort\_type | Number | 否 | 1 | 排序方式。   - **0**：正序 - **1**：倒序 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/subject/metadata/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f59c873a-3ed1-470b-9d25-fdc4219cdf4f' \
-d 'area_code=CN' \
-d 'cursor=0' \
-d 'data_order_type=0' \
-d 'level=2' \
-d 'operator_userid=user0012' \
-d 'parent_id=11' \
-d 'period_code=primary_school' \
-d 'size=100' \
-d 'sort_type=1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/metadata/list");
OapiEduSubjectMetadataListRequest req = new OapiEduSubjectMetadataListRequest();
req.setCursor(0L);
req.setLevel(2L);
req.setOperatorUserid("user0012");
req.setParentId(11L);
req.setPeriodCode("primary_school");
req.setDataOrderType(0L);
req.setAreaCode("CN");
req.setSize(2L);
req.setSortType(1L);
OapiEduSubjectMetadataListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduSubjectMetadataListRequest("https://oapi.dingtalk.com/topapi/edu/subject/metadata/list")

req.cursor=0
req.level=2
req.operator_userid="user0012"
req.parent_id=11
req.period_code="primary_school"
req.data_order_type=0
req.area_code="CN"
req.size=100
req.sort_type=1
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
$req = new OapiEduSubjectMetadataListRequest;
$req->setCursor("0");
$req->setLevel("2");
$req->setOperatorUserid("user0012");
$req->setParentId("11");
$req->setPeriodCode("primary_school");
$req->setDataOrderType("0");
$req->setAreaCode("CN");
$req->setSize("100");
$req->setSortType("1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/subject/metadata/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/subject/metadata/list");
OapiEduSubjectMetadataListRequest req = new OapiEduSubjectMetadataListRequest();
req.Cursor = 0L;
req.Level = 2L;
req.OperatorUserid = "user0012";
req.ParentId = 11L;
req.PeriodCode = "primary_school";
req.DataOrderType = 0L;
req.AreaCode = "CN";
req.Size = 100L;
req.SortType = 1L;
OapiEduSubjectMetadataListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageQueryResponse |  | 返回结果。 |
| next\_cursor | Number | 100 | 下一页游标。 |
| has\_more | Boolean | false | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| list | SubjectMetadataDTO[] |  | 学科元数据列表。 |
| id | Number | 13 | 学科元数据ID。 |
| area\_code | String | CN | 区域编码。 |
| period\_code | String | primary\_school | 学段编码。 |
| parent\_id | Number | 1 | 父ID。 |
| level | Number | 2 | 层级。 |
| subject\_name | String | 语文 | 学科名称。 |
| subject\_code | String | cn\_p\_yuwen | 学科编码。 |
| total\_count | Number | 1 | 总数据条数。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "has_more": false,
    "list": [
      {
        "area_code": "CN",
        "id": 13,
        "level": 2,
        "parent_id": 1,
        "period_code": "primary_school",
        "subject_code": "cn_p_yuwen",
        "subject_name": "语文"
      }
    ],
    "next_cursor": 2,
    "total_count": 16
  },
  "success": true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
