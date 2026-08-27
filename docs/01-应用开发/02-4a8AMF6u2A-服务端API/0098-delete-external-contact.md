---
title: "删除外部联系人"
source_url: "https://open.dingtalk.com/document/development/delete-external-contact"
namespace: "development"
slug: "delete-external-contact"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 外部联系人 > 删除外部联系人"
doc_id: "hD9G5lxqmw"
updated_at: "2026-05-27 13:09:31"
---

> Source: https://open.dingtalk.com/document/development/delete-external-contact
> Path: 应用开发 / 服务端API / 通讯录管理 > 外部联系人 > 删除外部联系人
> Updated: 2026-05-27 13:09:31

# 删除外部联系人

调用本接口，删除企业外部联系人。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/extcontact/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_ext\_write-企业外部联系人写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| user\_id | String | 是 | 0125xxxx0251487 | 要删除的外部联系人的userId，可以调用[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口获取userid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/extcontact/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=22c945xxxx509f1' \
-d 'user_id=0125xxxx0251487'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/delete");
OapiExtcontactDeleteRequest req = new OapiExtcontactDeleteRequest();
req.setUserId("0125xxxx0251487");
OapiExtcontactDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiExtcontactDeleteRequest("https://oapi.dingtalk.com/topapi/extcontact/delete")

req.user_id="0125xxxx0251487"
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
$req = new OapiExtcontactDeleteRequest;
$req->setUserId("0125xxxx0251487");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/extcontact/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/delete");
OapiExtcontactDeleteRequest req = new OapiExtcontactDeleteRequest();
req.UserId = "0125xxxx0251487";
OapiExtcontactDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 439eqp31da45 | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id": "439eqp31da45"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33009 | 无效的tokenGrantType | 请检查access\_token是否正确 |
| 33012 | 无效的userId | 请检查userId是否正确 |
| 43007 | 需要操作权限 | 请检查access\_token是否具有操作权限 |
| 400001 | 系统错误 | 请稍后再试 |
