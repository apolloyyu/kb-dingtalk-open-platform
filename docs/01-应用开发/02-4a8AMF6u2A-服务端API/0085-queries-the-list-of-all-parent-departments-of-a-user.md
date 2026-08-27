---
title: "获取指定用户的所有父部门列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-list-of-all-parent-departments-of-a-user"
namespace: "development"
slug: "queries-the-list-of-all-parent-departments-of-a-user"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 部门管理 > 获取指定用户的所有父部门列表"
doc_id: "wzT2PeOB2o"
updated_at: "2026-05-27 13:09:18"
---

> Source: https://open.dingtalk.com/document/development/queries-the-list-of-all-parent-departments-of-a-user
> Path: 应用开发 / 服务端API / 通讯录管理 > 部门管理 > 获取指定用户的所有父部门列表
> Updated: 2026-05-27 13:09:18

# 获取指定用户的所有父部门列表

调用本接口，查询指定用户所属的所有父级部门，本接口不受通讯录权限范围限制。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_list-通讯录部门信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | 100 | 要查询的用户的userid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f3c2f4xxxxf65767' \
-d 'userid=100'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser");
OapiV2DepartmentListparentbyuserRequest req = new OapiV2DepartmentListparentbyuserRequest();
req.setUserid("100");
OapiV2DepartmentListparentbyuserResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentListparentbyuserRequest("https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser")

req.userid="100"
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
$req = new OapiV2DepartmentListparentbyuserRequest;
$req->setUserid("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listparentbyuser");
OapiV2DepartmentListparentbyuserRequest req = new OapiV2DepartmentListparentbyuserRequest();
req.Userid = "100";
OapiV2DepartmentListparentbyuserResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | nfe328zf67ec | 请求ID。 |
| errmsg | String | 不合法的userid | 调用失败时返回的错误信息。 |
| result | DeptListParentByUserResponse |  | 返回结果。 |
| parent\_list | DeptParentResponse[] |  | 父部门列表集合。 |
| parent\_dept\_id\_list | Number[] | [456, 123, 1] | 父部门列表。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "parent_list": [
      {
        "parent_dept_id_list": [
          37xxxx95,
          1
        ]
      }
    ]
  },
  "request_id": "nfe328zf67ec"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 需要授权 | 请确认access\_token具有操作权限 |
| 33012 | 无效的userId | 请确认userId是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后重试 |
