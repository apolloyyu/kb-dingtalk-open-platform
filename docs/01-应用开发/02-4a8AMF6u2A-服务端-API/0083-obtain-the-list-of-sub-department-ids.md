---
title: "获取子部门ID列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-list-of-sub-department-ids"
namespace: "development"
slug: "obtain-the-list-of-sub-department-ids"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 部门管理 > 获取子部门ID列表"
doc_id: "6cYJXFzVai"
updated_at: "2026-05-27 13:09:16"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-list-of-sub-department-ids
> Path: 应用开发 / 服务端 API / 通讯录管理 > 部门管理 > 获取子部门ID列表
> Updated: 2026-05-27 13:09:16

# 获取子部门ID列表

调用本接口，获取企业部门下的所有直属子部门列表。

## **接口调用说明**

- 本接口不受授权范围限制。
- 本接口只支持获取下一级所有部门ID列表。

例如，调用本接口获取根部门的子部门ID列表，获取的结果是[123,666]，部门1和部门2下的子部门是获取不到的。

![子部门ID列表](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4585197361/p358767.png)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/listsubid |
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
| dept\_id | Number | 是 | 1 | 父部门ID，根部门传1，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/listsubid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0dcxxxx108dcd028' \
-d 'dept_id=100'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsubid");
OapiV2DepartmentListsubidRequest req = new OapiV2DepartmentListsubidRequest();
req.setDeptId(100L);
OapiV2DepartmentListsubidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentListsubidRequest("https://oapi.dingtalk.com/topapi/v2/department/listsubid")

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
$req = new OapiV2DepartmentListsubidRequest;
$req->setDeptId("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/department/listsubid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsubid");
OapiV2DepartmentListsubidRequest req = new OapiV2DepartmentListsubidRequest();
req.DeptId = 100L;
OapiV2DepartmentListsubidResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 48vhxdnwhve6 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 不合法的部门id | 调用错误时返回的错误信息。 |
| result | DeptListSubIdResponse |  | 返回结果。 |
| dept\_id\_list | Number[] | [2,3,4,5] | 子部门列表。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "dept_id_list": [
      379xxxx95,
      411xxxx76,
      399xxxx96,
      400xxxx83,
      404xxxx47
    ]
  },
  "request_id": "169dfniaazqb4"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 60003 | 未找到对应部门 | 请确认dept\_id是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后重试 |
