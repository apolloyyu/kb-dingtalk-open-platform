---
title: "获取部门用户详情"
source_url: "https://open.dingtalk.com/document/development/queries-department-user-details"
namespace: "development"
slug: "queries-department-user-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 行业通讯录 > 获取部门用户详情"
doc_id: "U9g1h8mzi0"
updated_at: "2026-05-27 13:09:39"
---

> Source: https://open.dingtalk.com/document/development/queries-department-user-details
> Path: 应用开发 / 服务端API / 通讯录管理 > 行业通讯录 > 获取部门用户详情
> Updated: 2026-05-27 13:09:39

# 获取部门用户详情

调用本接口，获取部门用户详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/industry/user/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_industry\_info\_read-行业通讯录信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 1 | 部门ID，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |
| userid | String | 是 | user01 | 员工userId，可调用[获取部门下人员列表](0130-obtains-the-list-of-people-under-a-department.md)接口获取userid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/industry/user/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=65c6a6xxxxc44' \
-d 'dept_id=12345' \
-d 'userid=12222'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/user/get");
OapiIndustryUserGetRequest req = new OapiIndustryUserGetRequest();
req.setDeptId(1L);
req.setUserid("user01");
OapiIndustryUserGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiIndustryUserGetRequest("https://oapi.dingtalk.com/topapi/industry/user/get")

req.dept_id=12345
req.userid="12222"
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
$req = new OapiIndustryUserGetRequest;
$req->setDeptId("12345");
$req->setUserid("12222");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/industry/user/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/user/get");
OapiIndustryUserGetRequest req = new OapiIndustryUserGetRequest();
req.DeptId = 12345L;
req.Userid = "12222";
OapiIndustryUserGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenIndustryEmp |  | 员工信息。 |
| roles | OpenRole[] |  | 人员角色列表。 |
| name | String | 村民 | 角色名称。 |
| id | Number | 155785 | 角色ID。 |
| name | String | 张xx | 员工姓名。 |
| feature | String | {\"relate\_type\":\"父子\",\"address\":\"地球村\"} | 不同角色的其他业务属性。可JSON反序列化。 |
| unionid | String | gliizBUjUxxxx | 用户在当前钉钉开放平台账号范围内的唯一标识。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 7afehfo9w76t | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "roles": [
      {
        "id": 149507744,
        "name": "村民"
      },
      {
        "id": 149507745,
        "name": "学生"
      },
      {
        "id": 149507746,
        "name": "主管理员"
      }
    ],
    "name": "张xx",
    "unionid": "gliizBUjUxxxx",
    "feature": "{\"relate_type\":\"父子\",\"address\":\"地球村\"}"
  },
  "errcode": 0,
  "errmsg": "ok",
  "request_id": "7afehfo9w76t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400043 | 无效的orgId | 请确认access\_token是否正确 |
| 40009 | 无效的dept\_id | 请确认dept\_id是否正确 |
| 33012 | 无效的userid | 请确认员工id是否为空 |
| 400001 | 系统错误 | 请稍后重试 |
