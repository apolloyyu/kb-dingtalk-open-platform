---
title: "获取部门下人员列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-list-of-people-under-a-department"
namespace: "development"
slug: "obtains-the-list-of-people-under-a-department"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 行业通讯录 > 获取部门下人员列表"
doc_id: "4DewEwGcyR"
updated_at: "2026-05-27 13:09:38"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-list-of-people-under-a-department
> Path: 应用开发 / 服务端API / 通讯录管理 > 行业通讯录 > 获取部门下人员列表
> Updated: 2026-05-27 13:09:38

# 获取部门下人员列表

调用本接口，获取行业通讯录下某个部门的人员列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/industry/user/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_industry\_info\_read-行业通讯录信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 1 | 部门id，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |
| role | String | 否 | Village | 行业相关，不同行业角色不一样。例如：   - 针对家校    - **teacher**: 老师   - **guardian**: 监护人   - **student**: 学生 - 针对农村    - **GroupManager**: 组长   - **HeadOfHouseHold**: 户主   - **HouseAdmin**: 家庭管理员   - **Villager**：村民   - **Leaseholder**：租客 |
| cursor | Number | 否 | 1 | 分页查询的游标。 |
| size | Number | 是 | 10 | 分页查询的大小，最大值1000。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/industry/user/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b4658384-7dfb-4d14-b7aa-a5ee6825895c' \
-d 'cursor=1000' \
-d 'dept_id=123456' \
-d 'role=village' \
-d 'size=1000'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/user/list");
OapiIndustryUserListRequest req = new OapiIndustryUserListRequest();
req.setDeptId(1L);
req.setSize(10L);
req.setCursor(1L);
OapiIndustryUserListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiIndustryUserListRequest("https://oapi.dingtalk.com/topapi/industry/user/list")

req.dept_id=123456
req.role="village"
req.cursor=1000
req.size=1000
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
$req = new OapiIndustryUserListRequest;
$req->setDeptId("123456");
$req->setRole("village");
$req->setCursor("1000");
$req->setSize("1000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/industry/user/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/user/list");
OapiIndustryUserListRequest req = new OapiIndustryUserListRequest();
req.DeptId = 123456L;
req.Role = "village";
req.Cursor = 1000L;
req.Size = 1000L;
OapiIndustryUserListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ResultWrapper |  | 人员列表信息。 |
| has\_more | Boolean | false | 是否还有更多数据。 |
| next\_cursor | Number | 1 | 分页查询的游标。 |
| details | OpenIndustryEmp[] |  | 员工列表。 |
| feature | String | "{}" | 不同角色的其他业务属性。可JSON反序列化。 |
| roles | OpenRole[] |  | 人员角色列表。 |
| name | String | 村民 | 角色名称。 |
| id | Number | 149507744 | 角色ID。 |
| name | String | 张xx | 员工姓名。 |
| userid | String | user01 | 员工的userId。 |
| unionid | String | gliizBUjUxxxx | 用户在当前钉钉开放平台账号范围内的唯一标识。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 请求是否成功。 |
| request\_id | String | 7afehfo9w76t | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "has_more": false,
    "details": [
      {
        "userid": "user02",
        "unionid": "gliizBUjUxxxx",
        "roles": [],
        "feature": "{}",
        "name": "张xx"
      },
      {
        "userid": "user01",
        "dept_id": 4242006,
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
        "feature": "{}",
        "name": "李xx"
      }
    ]
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
| 40009 | 无效的部门id | 请检查dept\_id是否正确 |
| 40069 | 无效的size | 请检查size是否合法 |
| 400002 | 无效的参数 | 请校验参数是否按要求输入 |
| -1 | 系统繁忙 | 请稍后再试 |
