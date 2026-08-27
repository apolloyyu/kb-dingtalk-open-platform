---
title: "获取花名册字段组详情"
source_url: "https://open.dingtalk.com/document/development/get-roster-field-group-details"
namespace: "development"
slug: "get-roster-field-group-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 花名册 > 获取花名册字段组详情"
doc_id: "LRMqlxxksZ"
updated_at: "2026-05-29 09:13:53"
---

> Source: https://open.dingtalk.com/document/development/get-roster-field-group-details
> Path: 应用开发 / 服务端API / 智能人事 > 花名册 > 获取花名册字段组详情
> Updated: 2026-05-29 09:13:53

# 获取花名册字段组详情

调用本接口，查询花名册的员工档案信息中有权限的字段列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agentid | Number | 是 | 868810166 | 应用AgentId，可在钉钉开发者后台的应用详情页获取。  iShot2022-10-21_14 |

### **请求示例**

curl

```
curl -i 'https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist' \
  -X 'POST' \
  -H 'Content-Type: application/json' \
  -H 'x-acs-dingtalk-access-token: 3a559bdf93xxxx69e80' \
  -d '{"agentid":23470561}'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist");
OapiSmartworkHrmEmployeeFieldGrouplistRequest req = new OapiSmartworkHrmEmployeeFieldGrouplistRequest();
req.setAgentid(23470561L);
OapiSmartworkHrmEmployeeFieldGrouplistResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartworkHrmEmployeeFieldGrouplistRequest("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist")

req.agentid=23470561
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
$req = new OapiSmartworkHrmEmployeeFieldGrouplistRequest;
$req->setAgentid("23470561");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/field/grouplist");
OapiSmartworkHrmEmployeeFieldGrouplistRequest req = new OapiSmartworkHrmEmployeeFieldGrouplistRequest();
req.Agentid = 23470561L;
OapiSmartworkHrmEmployeeFieldGrouplistResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | halydt5ckqpe | 请求ID。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 10001 | 返回码。 |
| success | Boolean | true | 是否成功标记。   - **true**：成功 - **false**：失败 |
| result | GroupMetaInfo[] |  | 返回结果。 |
| group\_id | String | sys | 字段组ID。 |
| has\_detail | Boolean | false | 是否支持明细。   - **true**：支持 - **false**：不支持 |
| field\_list | FieldMetaInfo[] |  | 组里面的字段集合。 |
| field\_type | String | DDDateField | 字段类型。   - **DDSelectField**：选项类型 - **TextField**：文本类型 - **DDDateField**：日期类型 - **DDDateWithLongField**：长日期类型 - **DDPhotoField**：图片类型 |
| field\_name | String | 身份证(人像面) | 字段描述。 |
| field\_code | String | sys00-mainDept | 字段code。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": [
    {
      "field_list": [
        {
          "field_code": "sys-authRealName",
          "field_name": "实人认证",
          "field_type": "NONE"
        }
      ],
      "group_id": "sys",
      "has_detail": false
    },
    {
      "field_list": [
        {
          "field_code": "sys08-forntIDcard",
          "field_name": "身份证(人像面)",
          "field_type": "DDPhotoField"
        },
        {
          "field_code": "sys08-rearIDcard",
          "field_name": "身份证(国徽面)",
          "field_type": "DDPhotoField"
        },
        {
          "field_code": "sys08-academicCertificate",
          "field_name": "学历证书",
          "field_type": "DDPhotoField"
        },
        {
          "field_code": "sys08-diplomaCertificate",
          "field_name": "学位证书",
          "field_type": "DDPhotoField"
        },
        {
          "field_code": "sys08-releaseLetter",
          "field_name": "前公司离职证明",
          "field_type": "DDPhotoField"
        },
        {
          "field_code": "sys08-personalPhoto",
          "field_name": "员工照片",
          "field_type": "DDPhotoField"
        }
      ],
      "group_id": "sys08",
      "has_detail": false
    }
  ],
  "success": true,
  "request_id": "halydt5ckqpe"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
