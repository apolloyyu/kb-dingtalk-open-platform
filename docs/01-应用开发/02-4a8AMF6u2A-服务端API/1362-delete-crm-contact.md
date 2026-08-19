---
title: "删除联系人数据"
source_url: "https://open.dingtalk.com/document/development/delete-crm-contact"
namespace: "development"
slug: "delete-crm-contact"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 联系人管理 > 删除联系人数据"
doc_id: "gFKsciuxFk"
updated_at: "2026-06-08 09:53:28"
---

> Source: https://open.dingtalk.com/document/development/delete-crm-contact
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 联系人管理 > 删除联系人数据
> Updated: 2026-06-08 09:53:28

# 删除联系人数据

调用本接口，删除当前组织CRM指定联系人。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_write-CRM主数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| operator\_userid | String | 是 | user01 | 操作人用户userId。 |
| data\_id | String | 是 | INST\_XX | 联系人实例ID，通过[根据指定条件查询联系人数据](1365-api-getcontacts.md)接口获取instance\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=bb3d98a7-592d-4f92-a0b8-7d705b4fc2cd' \
-d 'operator_userid=123456778' \
-d 'data_id=INST_XX'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete");
OapiCrmObjectdataContactDeleteRequest req = new OapiCrmObjectdataContactDeleteRequest();
req.setOperatorUserid("user01");
req.setDataId("INST_XX");
OapiCrmObjectdataContactDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectdataContactDeleteRequest("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete")

req.operator_userid="userid_xxx"
req.data_id="INST_XX"
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
$req = new OapiCrmObjectdataContactDeleteRequest;
$req->setOperatorUserid("userid_xxx");
$req->setDataId("INST_XX");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete");
OapiCrmObjectdataContactDeleteRequest req = new OapiCrmObjectdataContactDeleteRequest();
req.OperatorUserid = "user01";
req.DataId = "INST_XX";
OapiCrmObjectdataContactDeleteResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataDeleteDto |  | 删除结果。 |
| instance\_id | String | iNST\_XX | 删除的联系人实例ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "instance_id": "iNST_XX"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
