---
title: "删除图文卡片"
source_url: "https://open.dingtalk.com/document/development/delete-message-card"
namespace: "development"
slug: "delete-message-card"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 图文卡片管理 > 删除图文卡片"
doc_id: "M5uZVh9xTk"
updated_at: "2026-06-01 09:15:44"
---

> Source: https://open.dingtalk.com/document/development/delete-message-card
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 图文卡片管理 > 删除图文卡片
> Updated: 2026-06-01 09:15:44

# 删除图文卡片

调用本接口删除指定的图文卡片素材。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/news/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_materials-服务号素材管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| media\_id | String | 是 | P16mHftLYX8iE | 图文卡片素材id，可以通过[查询图文卡片列表](0824-query-message-card-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/news/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b67exxxx88247b1' \
-d 'media_id=P16mHftLYX8iE' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/delete");
OapiMaterialNewsDeleteRequest req = new OapiMaterialNewsDeleteRequest();
req.setUnionid("jYdrJoCmTo0iE");
req.setMediaId("P16mHftLYX8iE");
OapiMaterialNewsDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialNewsDeleteRequest("https://oapi.dingtalk.com/topapi/material/news/delete")

req.unionid="jYdrJoCmTo0iE"
req.media_id="P16mHftLYX8iE"
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
$req = new OapiMaterialNewsDeleteRequest;
$req->setUnionid("jYdrJoCmTo0iE");
$req->setMediaId("P16mHftLYX8iE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/news/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/delete");
OapiMaterialNewsDeleteRequest req = new OapiMaterialNewsDeleteRequest();
req.Unionid = "jYdrJoCmTo0iE";
req.MediaId = "P16mHftLYX8iE";
OapiMaterialNewsDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | zfzyu42bh20z | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"zfzyu42bh20z"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
