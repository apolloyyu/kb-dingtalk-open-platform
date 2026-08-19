---
title: "获取待入职员工列表"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-query-the-list-of-employees-to-be-hired"
namespace: "development"
slug: "intelligent-personnel-query-the-list-of-employees-to-be-hired"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工管理 > 获取待入职员工列表"
doc_id: "N630gTLAuC"
updated_at: "2026-05-29 09:13:54"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-query-the-list-of-employees-to-be-hired
> Path: 应用开发 / 服务端API / 智能人事 > 员工管理 > 获取待入职员工列表
> Updated: 2026-05-29 09:13:54

# 获取待入职员工列表

调用本接口，查询企业待入职员工userid列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| offset | Number | 是 | 0 | 分页游标，从0开始。根据返回结果里的next\_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next\_cursor的值。 |
| size | Number | 是 | 50 | 分页大小，最大50。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=682ebxxxxdec8a' \
-d 'offset=0' \
-d 'size=50'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry");
OapiSmartworkHrmEmployeeQuerypreentryRequest req = new OapiSmartworkHrmEmployeeQuerypreentryRequest();
req.setOffset(0L);
req.setSize(50L);
OapiSmartworkHrmEmployeeQuerypreentryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartworkHrmEmployeeQuerypreentryRequest("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry")

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
$req = new OapiSmartworkHrmEmployeeQuerypreentryRequest;
$req->setOffset("0");
$req->setSize("50");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/querypreentry");
OapiSmartworkHrmEmployeeQuerypreentryRequest req = new OapiSmartworkHrmEmployeeQuerypreentryRequest();
req.Offset = 0L;
req.Size = 50L;
OapiSmartworkHrmEmployeeQuerypreentryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult |  | 返回结果。 |
| next\_cursor | Number | 10 | 下一次分页调用的offset值，当返回结果里没有nextCursor时，表示分页结束。 |
| data\_list | String[] | ["11","22"] | 查询到的待入职员工userid。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | false | 是否调用成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 64jz549xdj6q | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "data_list": [
      "15994884216176833",
      "15996141263318674"
    ],
    "next_cursor": 10,
  },
  "success": true,
  "request_id": "72hy5js8p7dh"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
