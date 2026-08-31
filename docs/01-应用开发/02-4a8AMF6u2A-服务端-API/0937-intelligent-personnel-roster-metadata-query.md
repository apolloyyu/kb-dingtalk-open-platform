---
title: "获取花名册元数据"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-roster-metadata-query"
namespace: "development"
slug: "intelligent-personnel-roster-metadata-query"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 花名册 > 获取花名册元数据"
doc_id: "EwuPaibBpi"
updated_at: "2026-05-29 09:13:55"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-roster-metadata-query
> Path: 应用开发 / 服务端 API / 智能人事 > 花名册 > 获取花名册元数据
> Updated: 2026-05-29 09:13:55

# 获取花名册元数据

调用本接口，获取员工花名册的元数据，包括花名册分组、字段等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agentid | Number | 是 | 123456 | 应用的AgentID。   - 企业内部应用，可在[开发者后台](https://open-dev.dingtalk.com/#/corpeapp)的应用详情页获取应用ID。image - 第三方企业应用，通过[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取agentid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e0fa0fxxxxe870327' \
-d 'agentid=123456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get");
OapiSmartworkHrmRosterMetaGetRequest req = new OapiSmartworkHrmRosterMetaGetRequest();
req.setAgentid(123456L);
OapiSmartworkHrmRosterMetaGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartworkHrmRosterMetaGetRequest("https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get")

req.agentid=123456
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
$req = new OapiSmartworkHrmRosterMetaGetRequest;
$req->setAgentid("123456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/roster/meta/get");
OapiSmartworkHrmRosterMetaGetRequest req = new OapiSmartworkHrmRosterMetaGetRequest();
req.Agentid = 123456L;
OapiSmartworkHrmRosterMetaGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | GroupMetaInfo[] |  | 返回结果，花名册分组定义。 |
| group\_name | String | 自定义分组 | 分组名称。 |
| group\_id | String | custom654xxx | 分组标识。 |
| field\_meta\_info\_list | FieldMetaInfo[] |  | 花名册分组内字段定义。 |
| field\_name | String | 自定义字段 | 字段名称。 |
| field\_code | String | 494c20ee-4aa1-4465-ae8c-a25e406219eb | 字段标识。 |
| derived | Boolean | false | 是否衍生字段，例如司龄、年龄等系统计算的字段。   - **true**：衍生字段 - **false**：不衍生字段 |
| detail | Boolean | false | 分组是否支持明细。   - **true**：支持 - **false**：不支持 |
| success | Boolean | true | 服务调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 8badquf9r90f | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": [
    {
      "detail": false,
      "field_meta_info_list": [
        {
          "derived": false,
          "field_code": "sys-authRealName",
          "field_name": "实人认证"
        }
      ],
      "group_id": "sys",
      "group_name": "系统信息"
    },
    {
      "detail": false,
      "field_meta_info_list": [
        {
          "derived": false,
          "field_code": "sys04-bankAccountNo",
          "field_name": "银行卡号"
        },
        {
          "derived": false,
          "field_code": "sys04-accountBank",
          "field_name": "开户行"
        }
      ],
      "group_id": "sys04",
      "group_name": "银行卡信息"
    },
    {
      "detail": true,
      "field_meta_info_list": [
        {
          "derived": false,
          "field_code": "sys07-familyMemberName",
          "field_name": "姓名(家人)"
        },
        {
          "derived": false,
          "field_code": "sys07-familyMemberRelation",
          "field_name": "关系(家人)"
        }
      ],
      "group_id": "sys07",
      "group_name": "家庭信息"
    }
  ],
  "success": true,
  "request_id": "zrdnl3s9qa1b"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
