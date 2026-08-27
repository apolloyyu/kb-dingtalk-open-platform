---
title: "删除公告"
source_url: "https://open.dingtalk.com/document/development/delete-announcements-based-on-the-announcement-id"
namespace: "development"
slug: "delete-announcements-based-on-the-announcement-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 删除公告"
doc_id: "jkWUFTslgi"
updated_at: "2026-05-27 17:06:32"
---

> Source: https://open.dingtalk.com/document/development/delete-announcements-based-on-the-announcement-id
> Path: 应用开发 / 服务端API / 公告 > 删除公告
> Updated: 2026-05-27 17:06:32

# 删除公告

调用本接口，根据公告ID删除公告。

## **接口调用说明**

本接口只有以下身份可以删除公告：

- 主管理员
- 公告子管理员并且是待删除公告的创建者

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/blackboard/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_manage-钉钉公告管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| blackboard\_id | String | 是 | 098uyg65ffytr43 | 公告ID，可以通过[获取公告ID列表](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口获取result参数值。 |
| operation\_userid | String | 是 | manager01 | 操作人userId，必须是公告管理员。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/blackboard/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8eb1exxxx448a2' \
-d 'blackboard_id=098uyg65ffytr43' \
-d 'operation_userid=manager01'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/delete");
OapiBlackboardDeleteRequest req = new OapiBlackboardDeleteRequest();
req.setBlackboardId("098uyg65ffytr43");
req.setOperationUserid("manager01");
OapiBlackboardDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiBlackboardDeleteRequest("https://oapi.dingtalk.com/topapi/blackboard/delete")

req.blackboard_id="098uyg65ffytr43"
req.operation_userid="manager01"
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
$req = new OapiBlackboardDeleteRequest;
$req->setBlackboardId("098uyg65ffytr43");
$req->setOperationUserid("manager01");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/blackboard/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/delete");
OapiBlackboardDeleteRequest req = new OapiBlackboardDeleteRequest();
req.BlackboardId = "098uyg65ffytr43";
req.OperationUserid = "manager01";
OapiBlackboardDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 是否删除成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 本次调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 请求失败返回错误信息。 |
| errmsg | String | ok | 返回码描述 |
| request\_id | String | roz884n3k7rf | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": true,
  "success": true,
  "request_id": "xf13p2lvv200"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
