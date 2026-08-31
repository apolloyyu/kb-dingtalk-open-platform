---
title: "获取部门用户userid列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-department-userids"
namespace: "development"
slug: "query-the-list-of-department-userids"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 获取部门用户userid列表"
doc_id: "3oMeAnvUVQ"
updated_at: "2026-06-08 09:28:34"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-department-userids
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 获取部门用户userid列表
> Updated: 2026-06-08 09:28:34

# 获取部门用户userid列表

调用本接口获取指定部门的userid列表。

## **接口调用说明**

- 本接口不受通讯录权限范围限制。
- **目前暂不支持一次性获取企业下所有员工userid值**，如果开发者希望获取企业下所有员工userid值，可以通过以下方法：

  - 调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口，通过逐级遍历，获取该企业下在授权范围内的所有部门ID。
  - 调用本文档接口，分别获取每一个部门下的员工userid。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/user/listid |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_member-成员信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 100 | 部门deptId，可通过调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)获取部门deptId。  **[!NOTE]**  如果是根部门，该参数传1。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/user/listid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=03987655-598f-4f7a-8fc3-aaf257c47c27' \
-d 'dept_id=100'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listid");
OapiUserListidRequest req = new OapiUserListidRequest();
req.setDeptId(100L);
OapiUserListidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserListidRequest("https://oapi.dingtalk.com/topapi/user/listid")

req.dept_id=100
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
$req = new OapiUserListidRequest;
$req->setDeptId("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/user/listid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listid");
OapiUserListidRequest req = new OapiUserListidRequest();
req.DeptId = 100L;
OapiUserListidResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4f9kasjdhop | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | ListUserByDeptResponse |  | 返回结果。 |
| userid\_list | String[] | ["zxxxx","lixxxi"] | 指定部门的userid列表。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "userid_list": [
      "usxxx",
      "manager4xxx",
      "10203029011xxxx",
      "usexxx"
    ]
  },
  "request_id": "3naksldjh0dk"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 60003 | 未找到部门 | 请确认dept\_id是否正确 |
| 400002 | 无效的参数 | 请确认参数是否合法 |
| -1 | 系统繁忙 | 请稍后重试 |
