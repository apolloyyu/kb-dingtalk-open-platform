---
title: "获取员工人数"
source_url: "https://open.dingtalk.com/document/development/user-management-acquires-number-employees"
namespace: "development"
slug: "user-management-acquires-number-employees"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 获取员工人数"
doc_id: "Nl8Xx4wCcQ"
updated_at: "2026-06-08 09:28:36"
---

> Source: https://open.dingtalk.com/document/development/user-management-acquires-number-employees
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 获取员工人数
> Updated: 2026-06-08 09:28:36

# 获取员工人数

调用本接口获取员工人数。

## **接口调用说明**

本接口不受通讯录权限范围限制。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/user/count |
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
| only\_active | Boolean | 是 | false | 是否包含未激活钉钉人数：   - **false**：包含未激活钉钉的人员数量。 - **true**：只包含激活钉钉的人员数量。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/user/count" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7a1bee78-57cb-4a05-9316-0341b1ca303f' \
-d 'only_active=false'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/count");
OapiUserCountRequest req = new OapiUserCountRequest();
req.setOnlyActive(false);
OapiUserCountResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUserCountRequest("https://oapi.dingtalk.com/topapi/user/count")

req.only_active=false
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
$req = new OapiUserCountRequest;
$req->setOnlyActive("false");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/user/count");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/user/count");
OapiUserCountRequest req = new OapiUserCountRequest();
req.OnlyActive = false;
OapiUserCountResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | o38h5bztjouc | 请求ID。 |
| errcode | Number | 0 | 状态码，0表示调用成功。 |
| errmsg | String | 不合法的access\_token | 调用失败时返回错误信息。 |
| result | CountUserResponse |  | 返回结果。 |
| count | Number | 4 | 员工数量。 |

### **响应体示例**

```
{
    "errcode": 0,
    "errmsg":"ok",
    "result": {
        "count": 4
    },
    "request_id": "40k5v0mgbzyh"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | 参数为空 | 请确认必填参数填写完整 |
| 40035 | 不合法的参数 | 请确认参数符合上述文档要求 |
| -1 | 系统繁忙 | 请稍后再试 |
