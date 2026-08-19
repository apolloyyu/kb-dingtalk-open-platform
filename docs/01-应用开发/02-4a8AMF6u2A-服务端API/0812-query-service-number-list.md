---
title: "查询服务号列表"
source_url: "https://open.dingtalk.com/document/development/query-service-number-list"
namespace: "development"
slug: "query-service-number-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 服务号管理 > 查询服务号列表"
doc_id: "OlclFCqIGY"
updated_at: "2026-06-01 09:15:32"
---

> Source: https://open.dingtalk.com/document/development/query-service-number-list
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 服务号管理 > 查询服务号列表
> Updated: 2026-06-01 09:15:32

# 查询服务号列表

调用本接口查询当前组织的服务号列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/serviceaccount/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_manage-服务号管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| pageStart | Number | 否 | 1 | 页码，从1开始。 |
| pageSize | Number | 否 | 5 | 每页条数。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/serviceaccount/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=6782xxxxf1c84' \
-d 'pageSize=5' \
-d 'pageStart=1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/list");
OapiServiceaccountListRequest req = new OapiServiceaccountListRequest();
req.setPageStart(1L);
req.setPageSize(5L);
OapiServiceaccountListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceaccountListRequest("https://oapi.dingtalk.com/topapi/serviceaccount/list")

req.pageStart=1
req.pageSize=5
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
$req = new OapiServiceaccountListRequest;
$req->setPageStart("1");
$req->setPageSize("5");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/serviceaccount/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/list");
OapiServiceaccountListRequest req = new OapiServiceaccountListRequest();
req.PageStart = 1L;
req.PageSize = 5L;
OapiServiceaccountListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | zrrqyia71zl9 | 请求ID。 |
| errmsg | String | ok | 返回码。 |
| errcode | Number | 0 | 返回码描述。 |
| total\_count | Number | 20 | 总记录数。 |
| item\_count | Number | 5 | 当前记录数。 |
| items | PublisherDTO[] |  | 服务号列表。 |
| desc | String | 我是钉三多 | 机器人主页中的服务号功能简介。 |
| preview\_media\_id | String | @lALPBbCc1XuaP\_rNAljNAlg | 机器人主页中，消息预览图片的mediaId。 |
| brief | String | 互动服务窗 | 机器人管理列表中的简介。 |
| avatar\_media\_id | String | @lALPBbCc1XuaP\_rNAljNAlg | 头像图片mediaId。 |
| name | String | 服务号001 | 服务号名称。 |
| status | String | normal | 状态：   - **normal**：正常 - **disabled**：停用 |
| unionid | String | jYdrJoCmTo0iE | 服务号的unionid。 |

### **响应体示例**

```
{
  "errcode":0,
  "item_count":5,
  "total_count":20,
  "request_id":"zrrqyia71zl9",
  "items":{
    "brief":"互动服务窗",
    "unionid":"jYdrJoCmTo0iE",
    "preview_media_id":"@lALPBbCc1XuaP_rNAljNAlg",
    "name":"服务号001",
    "desc":"我是钉三多",
    "avatar_media_id":"@lALPBbCc1XuaP_rNAljNAlg",
    "status":"normal"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
