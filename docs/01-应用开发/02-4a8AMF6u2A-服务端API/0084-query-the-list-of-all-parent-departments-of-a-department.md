---
title: "获取指定部门的所有父部门列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-all-parent-departments-of-a-department"
namespace: "development"
slug: "query-the-list-of-all-parent-departments-of-a-department"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 部门管理 > 获取指定部门的所有父部门列表"
doc_id: "TxAyw4150J"
updated_at: "2026-05-27 13:09:17"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-all-parent-departments-of-a-department
> Path: 应用开发 / 服务端API / 通讯录管理 > 部门管理 > 获取指定部门的所有父部门列表
> Updated: 2026-05-27 13:09:17

# 获取指定部门的所有父部门列表

调用本接口，获取指定部门的所有父部门ID列表。该接口不受通讯录权限范围限制

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/listparentbydept |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_list-通讯录部门信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 42xxxx36 | 要查询的部门ID，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/listparentbydept" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a456xxxx13da5' \
-d 'dept_id=100'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listparentbydept");
OapiV2DepartmentListparentbydeptRequest req = new OapiV2DepartmentListparentbydeptRequest();
req.setDeptId(100L);
OapiV2DepartmentListparentbydeptResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentListparentbydeptRequest("https://oapi.dingtalk.com/topapi/v2/department/listparentbydept")

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
$req = new OapiV2DepartmentListparentbydeptRequest;
$req->setDeptId("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/department/listparentbydept");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listparentbydept");
OapiV2DepartmentListparentbydeptRequest req = new OapiV2DepartmentListparentbydeptRequest();
req.DeptId = 100L;
OapiV2DepartmentListparentbydeptResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 10u9dj0853fwe | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 不合法的部门id | 调用失败时返回的错误信息。 |
| result | DeptListParentByDeptIdResponse |  | 父部门ID列表。 |
| parent\_id\_list | Number[] | [789, 456, 123, 1] | 该部门的所有父部门ID列表。  **[!NOTE]**  获取的list元素第一个是当前部门ID，最后一个是父部门ID，从左至右部门层级递增。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "parent_id_list": [
      42xxxx36,
      1
    ]
  },
  "request_id": "ov7bc964j9pe"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 需要授权 | 请确认access\_token具有操作权限 |
| 60003 | 未找到对应部门 | 请确认dept\_id是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后再试 |
