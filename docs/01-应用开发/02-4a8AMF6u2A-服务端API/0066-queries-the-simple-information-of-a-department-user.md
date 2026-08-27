---
title: "获取部门用户基础信息"
source_url: "https://open.dingtalk.com/document/development/queries-the-simple-information-of-a-department-user"
namespace: "development"
slug: "queries-the-simple-information-of-a-department-user"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 获取部门用户基础信息"
doc_id: "zaIhIgvYFm"
updated_at: "2026-06-08 09:28:33"
---

> Source: https://open.dingtalk.com/document/development/queries-the-simple-information-of-a-department-user
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 获取部门用户基础信息
> Updated: 2026-06-08 09:28:33

# 获取部门用户基础信息

调用本接口获取指定部门的用户基础信息。

## **接口调用说明**

- 本接口只支持获取员工的userId和name两个字段信息，如需获取部门下员工详情信息，请参考[获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md)。
- 本接口只支持获取当前部门内的员工基础信息，子部门内员工信息获取不到。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/user/listsimple |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_member-通讯录部门成员读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 10 | 部门ID，如果是根部门，该参数传1，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)获取dept\_id参数值。 |
| cursor | Number | 是 | 0 | 分页查询的游标，最开始传0，后续传返回参数中的next\_cursor值。 |
| size | Number | 是 | 10 | 分页长度，最大值100。 |
| order\_field | String | 否 | modify\_desc | 部门成员的排序规则。默认值，**custom。**   - **entry\_asc**：代表按照进入部门的时间升序。 - **entry\_desc**：代表按照进入部门的时间降序。 - **modify\_asc**：代表按照部门信息修改时间升序。 - **modify\_desc**：代表按照部门信息修改时间降序。 - **custom**：代表用户定义(未定义时按照拼音)排序。 |
| contain\_access\_limit | Boolean | 否 | false | 是否返回访问受限的员工。   - **true**：是 - **false**：否 |
| language | String | 否 | zh\_CN | 通讯录语言，取值。   - **zh\_CN**：中文（默认值）。 - **en\_US**：英文。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/user/listsimple" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c1f2d110-4e7c-4536-a340-06652613e0c1' \
-d 'contain_access_limit=false' \
-d 'cursor=0' \
-d 'dept_id=10' \
-d 'language=zh_CN' \
-d 'order_field=modify_desc' \
-d 'size=10'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listsimple");
OapiUserListsimpleRequest req = new OapiUserListsimpleRequest();
req.setDeptId(10L);
req.setCursor(0L);
req.setSize(10L);
req.setOrderField("modify_desc");
req.setContainAccessLimit(false);
req.setLanguage("zh_CN");
OapiUserListsimpleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserListsimpleRequest("https://oapi.dingtalk.com/topapi/user/listsimple")

req.dept_id=10
req.cursor=0
req.size=10
req.order_field="modify_desc"
req.contain_access_limit=false
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
$req = new OapiUserListsimpleRequest;
$req->setDeptId("10");
$req->setCursor("0");
$req->setSize("10");
$req->setOrderField("modify_desc");
$req->setContainAccessLimit("false");
$req->setLanguage("zh_CN");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/user/listsimple");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/listsimple");
OapiUserListsimpleRequest req = new OapiUserListsimpleRequest();
req.DeptId = 10L;
req.Cursor = 0L;
req.Size = 10L;
req.OrderField = "modify_desc";
req.ContainAccessLimit = false;
req.Language = "zh_CN";
OapiUserListsimpleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4f9md9obopn2 | 请求ID。 |
| errcode | Number | 0 | 返回码，0代表成功。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageResult |  | 返回结果。 |
| has\_more | Boolean | true | 是否还有更多的数据。   - **true**：是 - **false**：否 |
| next\_cursor | Number | 10 | 下一次分页的游标，如果has\_more为false，表示没有更多的分页数据。 |
| list | ListUserSimpleResponse[] |  | 用户信息列表。 |
| userid | String | zxxxxx | 用户的userid。 |
| name | String | 张三 | 用户姓名。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "has_more": false,
    "list": [
      {
        "name": "测试用户2",
        "userid": "user100"
      },
      {
        "name": "李思",
        "userid": "user1"
      }
    ]
  },
  "request_id": "x4p6arvi0fzj"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | 无效的参数 | 请确认参数按上述要求填写 |
| 60003 | 未找到对应部门 | 请确认部门id是否正确 |
| 40069 | 无效的size | 请调整分页的大小 |
| 40068 | 无效的偏移量 | 请调整偏移量 |
| -1 | 系统繁忙 | 请稍后再试 |
