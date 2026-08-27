---
title: "获取在职员工列表"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-query-the-list-of-on-the-job-employees-of-the"
namespace: "development"
slug: "intelligent-personnel-query-the-list-of-on-the-job-employees-of-the"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工管理 > 获取在职员工列表"
doc_id: "JMTsjnyDeR"
updated_at: "2026-06-23 10:40:26"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-query-the-list-of-on-the-job-employees-of-the
> Path: 应用开发 / 服务端API / 智能人事 > 员工管理 > 获取在职员工列表
> Updated: 2026-06-23 10:40:26

# 获取在职员工列表

调用本接口，查询企业在职员工userid列表。

## **接口调用说明**

- 该接口只能获取企业开通“智能人事”应用之后的员工信息，获取不到开通之前的员工信息。
- 针对家校企业、关联组织， 本接口不保证和智能人事产品上数据一致， 请直接使用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)获取企业内员工。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| status\_list | String | 是 | 2,3,5,-1 | 在职员工状态筛选，可以查询多个状态。不同状态之间使用英文逗号分隔。   - **2**：试用期 - **3**：正式 - **5**：待离职 - **-1**：无状态 |
| offset | Number | 是 | 0 | 分页游标，从0开始。根据返回结果里的next\_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next\_cursor的值。 |
| size | Number | 是 | 50 | 分页大小，最大50。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9f9e21xxxxcea97bd' \
-d 'offset=0' \
-d 'size=50' \
-d 'status_list=2%2C3%2C5%2C-1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob");
OapiSmartworkHrmEmployeeQueryonjobRequest req = new OapiSmartworkHrmEmployeeQueryonjobRequest();
req.setStatusList("2,3,5,-1");
req.setOffset(0L);
req.setSize(50L);
OapiSmartworkHrmEmployeeQueryonjobResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartworkHrmEmployeeQueryonjobRequest("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob")

req.status_list="[2,3,5,-1]"
req.offset=0
req.size=50
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
$req = new OapiSmartworkHrmEmployeeQueryonjobRequest;
$req->setStatusList("[2,3,5,-1]");
$req->setOffset("0");
$req->setSize("50");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/queryonjob");
OapiSmartworkHrmEmployeeQueryonjobRequest req = new OapiSmartworkHrmEmployeeQueryonjobRequest();
req.StatusList = "2,3,5,-1";
req.Offset = 0L;
req.Size = 50L;
OapiSmartworkHrmEmployeeQueryonjobResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult |  | 返回结果。 |
| data\_list | String | ["user123"] | 查询到的员工userid。 |
| next\_cursor | Number | 0 | 下一次分页调用的offset值，当返回结果里没有next\_cursor时，表示分页结束。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | false | 是否调用成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | u2nu5vpoq6p | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "data_list": [
      "user123"
    ],
    "next_cursor": 0,
  },
  "success": true,
  "request_id": "u2nu5vpoq6p4"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
