---
title: "查询服务号详情"
source_url: "https://open.dingtalk.com/document/development/inquire-about-service-number-details"
namespace: "development"
slug: "inquire-about-service-number-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 服务号管理 > 查询服务号详情"
doc_id: "y4xC0Wsk6g"
updated_at: "2026-06-01 09:15:29"
---

> Source: https://open.dingtalk.com/document/development/inquire-about-service-number-details
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 服务号管理 > 查询服务号详情
> Updated: 2026-06-01 09:15:29

# 查询服务号详情

调用本接口根据服务号的unionid查询服务号详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/serviceaccount/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_manage-服务号管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/serviceaccount/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=fe8a45xxxxd67406e0' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/get");
OapiServiceaccountGetRequest req = new OapiServiceaccountGetRequest();
req.setUnionid("jYdrJoCmTo0i");
OapiServiceaccountGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceaccountGetRequest("https://oapi.dingtalk.com/topapi/serviceaccount/get")

req.unionid="jYdrJoCmTo0iE"
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
$req = new OapiServiceaccountGetRequest;
$req->setUnionid("jYdrJoCmTo0iE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/serviceaccount/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/get");
OapiServiceaccountGetRequest req = new OapiServiceaccountGetRequest();
req.Unionid = "jYdrJoCmTo0iE";
OapiServiceaccountGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 5o3jwi6ppmo | 请求ID。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| service\_account | ServiceAccountDTO |  | 服务号详情。 |
| status | String | normal | 状态：   - **normal**：正常 - **disabled**：删除 |
| unionid | String | jYdrJoCmTo0i | 服务号的unionid。 |
| name | String | 服务号001 | 服务号名称。 |
| brief | String | 互动服务窗 | 机器人管理列表中的简介，最多60个字符。 |
| desc | String | 我是钉三多 | 机器人主页中的服务号功能简介，最多200个字符。 |
| avatar\_media\_id | String | @lALPBbCc1XuaP\_rNAljNAlg | 头像图片mediaId。 |
| operator\_user\_id\_list | String[] | ["staffId1","staffId2"] | 运营人员列表。 |
| black\_user\_id\_list | String[] | ["staffId1","staffId2"] | 黑名单人员列表。 |
| allow\_send\_to\_all | Boolean | true | 是否全员发送。 |
| allow\_send\_user\_id\_list | String[] | ["staffId1","staffId2"] | 可发送用户列表。 |
| allow\_send\_dept\_id\_list | Number[] | [123,456] | 可发送部门id列表。 |

### **响应体示例**

```
{
  "errcode":0,
  "service_account":{
    "brief":"互动服务窗",
    "unionid":"jYdrJoCmTo0i",
    "preview_media_id":"@lALPBbCc1XuaP_rNAljNAlg",
    "name":"服务号001",
    "status":"normal",
    "desc":"我是钉三多",
    "avatar_media_id":"@lALPBbCc1XuaP_rNAljNAlg"
  },
  "request_id":"5o3jwi6ppmo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
