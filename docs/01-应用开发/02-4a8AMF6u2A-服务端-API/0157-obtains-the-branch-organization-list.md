---
title: "获取分支组织列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-branch-organization-list"
namespace: "development"
slug: "obtains-the-branch-organization-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 上下级组织（原关联组织） > 获取分支组织列表"
doc_id: "prdTrIBhMi"
updated_at: "2026-05-26 09:01:01"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-branch-organization-list
> Path: 应用开发 / 服务端 API / 通讯录管理 > 上下级组织（原关联组织） > 获取分支组织列表
> Updated: 2026-05-26 09:01:01

# 获取分支组织列表

调用本接口获取分支组织列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/org/union/branch/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_related\_org\_read-钉钉通讯录关联组织读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/org/union/branch/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1406xxxxd418bf'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/org/union/branch/get");
OapiOrgUnionBranchGetRequest req = new OapiOrgUnionBranchGetRequest();
OapiOrgUnionBranchGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiOrgUnionBranchGetRequest("https://oapi.dingtalk.com/topapi/org/union/branch/get")

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
$req = new OapiOrgUnionBranchGetRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/org/union/branch/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/org/union/branch/get");
OapiOrgUnionBranchGetRequest req = new OapiOrgUnionBranchGetRequest();
OapiOrgUnionBranchGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenOrgUnion[] |  | 返回接口。 |
| union\_org\_name | String | 胜利小学 | 分支组织名称。 |
| union\_corpid | String | dingofuewlxxxx | 分支组织的corpid。 |
| success | Boolean | true | 是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 不合法的access\_token | 返回码描述。 |
| request\_id | String | 1gixtornci30 | 请求ID。 |

### **响应体示例**

```
{
  "result":{
    "union_corpid":"dingofuewlxxxx",
    "union_org_name":"胜利小学"
  },
  "errcode":0,
  "success":"true",
  "request_id":"1gixtornci30"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400043 | 无效的orgId | 请检查access\_token是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
