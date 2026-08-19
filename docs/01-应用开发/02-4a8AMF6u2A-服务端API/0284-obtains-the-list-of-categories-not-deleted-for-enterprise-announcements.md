---
title: "获取公告分类列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-list-of-categories-not-deleted-for-enterprise-announcements"
namespace: "development"
slug: "obtains-the-list-of-categories-not-deleted-for-enterprise-announcements"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 获取公告分类列表"
doc_id: "WIp5wUmkUZ"
updated_at: "2026-05-29 09:13:33"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-list-of-categories-not-deleted-for-enterprise-announcements
> Path: 应用开发 / 服务端API / 公告 > 获取公告分类列表
> Updated: 2026-05-29 09:13:33

# 获取公告分类列表

调用本接口，获取未删除的公告分类列表，如果公告类别已被删除，则无法获取，同时本接口可返回**正式公告、节假日公告**的类别信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/blackboard/category/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_read-读取钉钉公告微应用数据的权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| operation\_userid | String | 是 | manager01 | 操作人userId，必须是公告管理员。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/blackboard/category/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b0f8f4xxxx3daa8' \
-d 'operation_userid=manager01'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/category/list");
OapiBlackboardCategoryListRequest req = new OapiBlackboardCategoryListRequest();
req.setOperationUserid("manager01");
OapiBlackboardCategoryListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiBlackboardCategoryListRequest("https://oapi.dingtalk.com/topapi/blackboard/category/list")

req.operation_userid="manager01"
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
$req = new OapiBlackboardCategoryListRequest;
$req->setOperationUserid("manager01");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/blackboard/category/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/category/list");
OapiBlackboardCategoryListRequest req = new OapiBlackboardCategoryListRequest();
req.OperationUserid = "manager01";
OapiBlackboardCategoryListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | BlackboardCategoryVo[] |  | 返回结果。 |
| id | String | 89uuhygybj | 分类ID。 |
| name | String | 日签 | 分类名。 |
| success | Boolean | true | 本次调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | ie9aarwu1m1t | 请求ID。 |

### **响应体示例**

```
{
  "result":[
    {
      "name":"正式公告",
      "id":d6305870xxxxfec993c"
    },
    {
      "name":"节假日公告",
      "id":"8a8cfxxxx5b8a"
    }
  ],
  "errcode":0,
  "success":true,
  "request_id":"ie9aarwu1m1t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
