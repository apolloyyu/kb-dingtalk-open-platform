---
title: "获取部门列表"
source_url: "https://open.dingtalk.com/document/development/user-management-acquires-the-list-departments"
namespace: "development"
slug: "user-management-acquires-the-list-departments"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 部门管理 > 获取部门列表"
doc_id: "Qy7R57slfX"
updated_at: "2026-05-27 13:09:15"
---

> Source: https://open.dingtalk.com/document/development/user-management-acquires-the-list-departments
> Path: 应用开发 / 服务端 API / 通讯录管理 > 部门管理 > 获取部门列表
> Updated: 2026-05-27 13:09:15

# 获取部门列表

调用本接口，获取下一级部门基础信息。本接口只支持获取当前部门的下一级部门基础信息，不支持获取当前部门下所有层级子部门。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/listsub |
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
| dept\_id | Number | 否 | 1 | 父部门ID，可调用[获取部门列表](#)接口获取dept\_id参数值。 |
| language | String | 否 | zh\_CN | 通讯录语言：   - **zh\_CN**（默认）：中文 - **en\_US**：英文 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/listsub" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=6846xxxx0cc781' \
-d 'dept_id=100' \
-d 'language=zh_CN'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsub");
OapiV2DepartmentListsubRequest req = new OapiV2DepartmentListsubRequest();
req.setDeptId(1L);
req.setLanguage("zh_CN");
OapiV2DepartmentListsubResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentListsubRequest("https://oapi.dingtalk.com/topapi/v2/department/listsub")

req.dept_id=100
req.language="zh_CN"
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
$req = new OapiV2DepartmentListsubRequest;
$req->setDeptId("100");
$req->setLanguage("zh_CN");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/department/listsub");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/listsub");
OapiV2DepartmentListsubRequest req = new OapiV2DepartmentListsubRequest();
req.DeptId = 100L;
req.Language = "zh_CN";
OapiV2DepartmentListsubResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5um7ykyaalsj | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 不合法的access\_token | 调用失败时返回的错误信息。 |
| result | DeptBaseResponse[] |  | 部门列表。 |
| dept\_id | Number | 100 | 部门ID。 |
| name | String | HR | 部门名称。 |
| parent\_id | Number | 50 | 父部门ID。 |
| create\_dept\_group | Boolean | true | 是否同步创建一个关联此部门的企业群：   - **true**：创建 - **false**：不创建 |
| auto\_add\_user | Boolean | false | 部门群已经创建后，有新人加入部门是否会自动加入该群：   - **true**：会自动入群 - **false**：不会 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": [
    {
      "auto_add_user": true,
      "create_dept_group": true,
      "dept_id": 37xxxx95,
      "name": "市场部",
      "parent_id": 1
    },
    {
      "auto_add_user": true,
      "create_dept_group": true,
      "dept_id": 399xxxx96,
      "name": "财务部",
      "parent_id": 1
    }
  ],
  "request_id": "5um7ykyaalsj"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 60003 | 未找到对应部门 | 请确认dept\_id是否正确 |
| 400002 | 无效的参数 | 请确认参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后再试 |
