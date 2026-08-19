---
title: "获取学段元数据列表"
source_url: "https://open.dingtalk.com/document/development/dingtalk-the-main-data-of-the-education-ecosystem-to-query"
namespace: "development"
slug: "dingtalk-the-main-data-of-the-education-ecosystem-to-query"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学段元数据列表"
doc_id: "P5awHAWaae"
updated_at: "2026-06-08 09:47:30"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-the-main-data-of-the-education-ecosystem-to-query
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 通用基础 > 获取学段元数据列表
> Updated: 2026-06-08 09:47:30

# 获取学段元数据列表

调用本接口，可获取学段元数据列表，包括学段ID、层级、区域编码、学段编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/period/metadata/list |
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
| cursor | Number | 是 | 0 | 分页游标，从0开始。 |
| size | Number | 是 | 100 | 每页数据条数。 |
| data\_order\_type | Number | 否 | 1 | 排序依赖字段类型。   - **1**：根据修改时间 - **2**：根据主键id - **3**：根据指定的排序字段 |
| sort\_type | Number | 否 | 0 | 排序规则。   - **0**：升序 - **1**：降序 |
| area\_code | String | 是 | CN | 地区编码。   - **CN**：中国编码 |
| level | Number | 否 | 1 | 层级。 |
| parent\_id | Number | 否 | 1 | 父ID，调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为period时的dept\_id参数值。 |
| operator\_userid | String | 是 | user01121 | 用户的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/period/metadata/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=72b411e9-52d7-412b-a848-7969dfb70adc' \
-d 'area_code=CN' \
-d 'cursor=0' \
-d 'data_order_type=1' \
-d 'level=1' \
-d 'operator_userid=user01121' \
-d 'parent_id=1' \
-d 'size=100' \
-d 'sort_type=0'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/period/metadata/list");
OapiEduPeriodMetadataListRequest req = new OapiEduPeriodMetadataListRequest();
req.setCursor(0L);
req.setSize(100L);
req.setDataOrderType(1L);
req.setSortType(0L);
req.setAreaCode("CN");
req.setLevel(1L);
req.setParentId(1L);
req.setOperatorUserid("user01121");
OapiEduPeriodMetadataListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduPeriodMetadataListRequest("https://oapi.dingtalk.com/topapi/edu/period/metadata/list")

req.cursor=0
req.size=100
req.data_order_type=1
req.sort_type=0
req.area_code="CN"
req.level=1
req.parent_id=1
req.operator_userid="user01121"
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
$req = new OapiEduPeriodMetadataListRequest;
$req->setCursor("0");
$req->setSize("100");
$req->setDataOrderType("1");
$req->setSortType("0");
$req->setAreaCode("CN");
$req->setLevel("1");
$req->setParentId("1");
$req->setOperatorUserid("user01121");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/period/metadata/list");
```

C#

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/period/metadata/list");
OapiEduPeriodMetadataListRequest req = new OapiEduPeriodMetadataListRequest();
req.Cursor = 0L;
req.Size = 100L;
req.DataOrderType = 1L;
req.SortType = 0L;
req.AreaCode = "CN";
req.Level = 1L;
req.ParentId = 1L;
req.OperatorUserid = "user01121";
OapiEduPeriodMetadataListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageQueryResponse |  | 返回数据。 |
| next\_cursor | Number | 100 | 下一页游标。 |
| has\_more | Boolean | false | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| list | PeriodMetadataDTO[] |  | 学段元数据列表。 |
| id | Number | 3 | 学段ID。 |
| level | Number | 2 | 层级。 |
| parent\_id | Number | 1 | 父ID。 |
| area\_code | String | CN | 区域编码。 |
| period\_code | String | primary\_school | 学段编码。 |
| period\_name | String | 小学 | 学段名称。 |
| total\_count | Number | 1 | 总数据条数。 |

### **响应体示例**

```
{
  "errcode": "0",
  "result": {
    "next_cursor": 100,
    "total_count": 15,
    "has_more": "false",
    "list": [
      {
        "area_code": "CN",
        "id": 5,
        "level": 2,
        "parent_id": 1,
        "period_code": "kindergarten_1",
        "period_name": "小班"
      }
    ]
  },
  "success": "true",
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
