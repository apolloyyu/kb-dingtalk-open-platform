---
title: "获取企业已经加入的或申请加入中的上下游组织的信息"
source_url: "https://open.dingtalk.com/document/development/obtains-information-about-the-workspaces-that-the-enterprise-has-joined"
namespace: "development"
slug: "obtains-information-about-the-workspaces-that-the-enterprise-has-joined"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 获取企业已经加入的或申请加入中的上下游组织的信息"
doc_id: "OaHOvj9aMF"
updated_at: "2026-05-26 09:00:59"
---

> Source: https://open.dingtalk.com/document/development/obtains-information-about-the-workspaces-that-the-enterprise-has-joined
> Path: 应用开发 / 服务端API / 通讯录管理 > 上下游组织（原合作空间） > 获取企业已经加入的或申请加入中的上下游组织的信息
> Updated: 2026-05-26 09:00:59

# 获取企业已经加入的或申请加入中的上下游组织的信息

调用本接口获取企业已经加入的上下游组织信息或获取企业已经加入的上下游组织信息。上下游组织是基于普通组织底层构建的业务类型，通讯录相关API都可以使用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/union/cooperate/joined/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_related\_org\_read-钉钉通讯录关联组织读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be31xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| status | Number | 是 | 0 | 要查询的空间状态：   - **0**：申请中 - **1**：已成功加入 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/union/cooperate/info/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9fc0ce4xxxxa103041' \
-d 'status=0'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/union/cooperate/info/list");
OapiUnionCooperateInfoListRequest req = new OapiUnionCooperateInfoListRequest();
req.setStatus(0L);
OapiUnionCooperateInfoListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUnionCooperateInfoListRequest("https://oapi.dingtalk.com/topapi/union/cooperate/info/list")

req.status=0
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
$req = new OapiUnionCooperateInfoListRequest;
$req->setStatus("0");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/union/cooperate/info/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/union/cooperate/info/list");
OapiUnionCooperateInfoListRequest req = new OapiUnionCooperateInfoListRequest();
req.Status = 0L;
OapiUnionCooperateInfoListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenCooperateOrgVo[] |  | 空间信息。 |
| belong\_org\_name | String | 测试空间归属企业 | 空间归属企业名称。 |
| belong\_corp\_id | String | "belongtest" | 空间归属企业corpId。 |
| org\_name | String | "测试空间" | 空间名称。 |
| corp\_id | String | "test" | 查询空间的corpId。 |
| success | Boolean | true | 是否调用成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result":{
    "belong_corp_id":"\"belongtest\"",
    "belong_org_name":"测试空间归属企业",
    "org_name":"\"测试空间\"",
    "corp_id":"\"test\""
  },
  "errcode":0,
  "success":"true",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
