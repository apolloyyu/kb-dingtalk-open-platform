---
title: "获取未登录钉钉的员工列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-inactive-users-or-active-users-under-an-enterprise"
namespace: "development"
slug: "queries-the-inactive-users-or-active-users-under-an-enterprise"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 获取未登录钉钉的员工列表"
doc_id: "ybdhOGY5ms"
updated_at: "2026-06-08 09:28:37"
---

> Source: https://open.dingtalk.com/document/development/queries-the-inactive-users-or-active-users-under-an-enterprise
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 获取未登录钉钉的员工列表
> Updated: 2026-06-08 09:28:37

# 获取未登录钉钉的员工列表

调用本接口查询指定日期内未登录钉钉的企业员工列表。

## **接口调用说明**

- 每天9点后调用接口才能确保获取前一天数据。
- 调用本接口只能获取一个月内未登录钉钉的员工列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/inactive/user/v2/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_liveness\_base-企业活跃度数据访问权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| is\_active | Boolean | 是 | false | 是否活跃：   - **false**：未登录 - **true**：登录 |
| dept\_ids | String | 否 | 1,2,3 | 部门ID列表，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)获取，不传表示查询整个企业。 |
| offset | Number | 是 | 1 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |
| size | Number | 是 | 100 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。 |
| query\_date | String | 是 | 20200101 | 查询日期，日期格式为：yyyyMMdd。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/inactive/user/v2/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2146ca78-23af-4580-9335-883348ff9a54' \
-d 'dept_ids=%5C%222%2C3%2C4%5C%22' \
-d 'is_active=false' \
-d 'offset=0' \
-d 'query_date=20200101' \
-d 'size=100'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/inactive/user/v2/get");
OapiInactiveUserV2GetRequest req = new OapiInactiveUserV2GetRequest();
req.setIsActive(false);
req.setDeptIds("1,2,3");
req.setOffset(0L);
req.setSize(100L);
req.setQueryDate("20200101");
OapiInactiveUserV2GetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiInactiveUserV2GetRequest("https://oapi.dingtalk.com/topapi/inactive/user/v2/get")

req.is_active=false
req.dept_ids=""2,3,4""
req.offset=0
req.size=100
req.query_date="20200101"
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
$req = new OapiInactiveUserV2GetRequest;
$req->setIsActive("false");
$req->setDeptIds("\"2,3,4\"");
$req->setOffset("0");
$req->setSize("100");
$req->setQueryDate("20200101");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/inactive/user/v2/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/inactive/user/v2/get");
OapiInactiveUserV2GetRequest req = new OapiInactiveUserV2GetRequest();
req.IsActive = false;
req.DeptIds = "\"2,3,4\"";
req.Offset = 0L;
req.Size = 100L;
req.QueryDate = "20200101";
OapiInactiveUserV2GetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageVo |  | 返回结果。 |
| next\_cursor | Number | 1000 | 下一页的偏移量。 |
| list | String[] | ["user123","user456"] | 未登录用户列表。 |
| has\_more | Boolean | false | 是否有更多数据。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | o565d47xy9cz | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "has_more": false,
    "list": [
      "011250026469774889",
      "0260470242730556"
    ]
  },
  "request_id": "o565d47xy9cz"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | 参数非法 | 请检查必填参数是否符合要求 |
| 40069 | 无效的size | 请检查分页大小 |
| 40068 | 无效的偏移量 | 请调整偏移量 |
| 400002 | 参数格式不正确 | 请检查入参格式 |
| -1 | 系统繁忙 | 请稍后再试 |
