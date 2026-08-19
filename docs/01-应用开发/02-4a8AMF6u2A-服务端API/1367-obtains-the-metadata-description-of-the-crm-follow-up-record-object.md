---
title: "获取跟进记录对象的元数据"
source_url: "https://open.dingtalk.com/document/development/obtains-the-metadata-description-of-the-crm-follow-up-record-object"
namespace: "development"
slug: "obtains-the-metadata-description-of-the-crm-follow-up-record-object"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 跟进记录 > 获取跟进记录对象的元数据"
doc_id: "60x57Qo7ip"
updated_at: "2026-06-08 09:53:24"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-metadata-description-of-the-crm-follow-up-record-object
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 跟进记录 > 获取跟进记录对象的元数据
> Updated: 2026-06-08 09:53:24

# 获取跟进记录对象的元数据

调用本接口，读取钉钉CRM跟进记录对象的元数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-CRM主数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7dad1a09-ffcb-4263-bdb1-d3b7dd55f749'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe");
OapiCrmObjectmetaFollowrecordDescribeRequest req = new OapiCrmObjectmetaFollowrecordDescribeRequest();
OapiCrmObjectmetaFollowrecordDescribeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectmetaFollowrecordDescribeRequest("https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe")

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
$req = new OapiCrmObjectmetaFollowrecordDescribeRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe");
OapiCrmObjectmetaFollowrecordDescribeRequest req = new OapiCrmObjectmetaFollowrecordDescribeRequest();
OapiCrmObjectmetaFollowrecordDescribeResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DObject |  | 返回结果。 |
| name | String | crm\_customer | 对象名称。 |
| customized | Boolean | false | 是否自定义对象。   - **true**：是 - **false**：不是 |
| fields | Fields[] |  | 字段列表。 |
| name | String | customer\_name | 字段名称。 |
| customized | Boolean | false | 是否自定义字段。   - **true**：是 - **false**：不是 |
| label | String | 客户名称 | 字段展示名。 |
| type | String | Text | 字段类型。 |
| nillable | Boolean | false | 是否可空。   - **true**：可为空 - **false**：不能为空 |
| format | String | yyyy-MM-dd | 日期格式。 |
| unit | String | 天 | 日期单位/金额单位。 |
| select\_options | SelectOptions[] | selectOptions | 选项列表。 |
| key | String | option\_1 | 选项key。 |
| value | String | 选项1 | 选项名。 |
| quote | Boolean | true | 是否引用关联。   - **true**：引用 - **false**：不引用 |
| reference\_to | String | crm\_contact | 关联对象名称。 |
| reference\_fields | ReferenceFields[] |  | 引用的关联对象的字段列表。 |
| label | String | 联系人名称 | 引用的关联对象字段显示名。 |
| type | String | Text | 引用的关联对象字段类型。 |
| nillable | Boolean | false | 引用的关联对象字段是否可空。   - **true**：可为空 - **false**：不能为空 |
| format | String | yyyy-MM-dd | 引用的关联对象字段格式。 |
| unit | String | 天 | 引用的关联对象字段单位。 |
| select\_options | SelectOptions[] |  | 引用的关联对象的字段选项列表。 |
| key | String | option\_2 | 引用的关联对象的字段选项key。 |
| value | String | 选项2 | 引用的关联对象的字段选项值。 |
| name | String | crm\_customer\_name | 引用的关联对象的字段名称。 |
| roll\_up\_summary\_fields | RollUpSummaryFields[] |  | 对MasterDetail类型有效：roll-up summary字段列表。 |
| name | String | Money-XDADDF | 需要汇总的明细内字段名。 |
| aggregator | String | SUM | 汇总方法。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "code": "PROC-6AA993FE-261C-4601-BD4B-256D2A8FEC49",
    "customized": false,
    "fields": [
      {
        "customized": false,
        "label": "客户",
        "name": "follow_record_related_customer",
        "nillable": false,
        "quote": true,
        "reference_fields": [
          {
            "label": "客户名称",
            "name": "customer_name",
            "nillable": false,
            "type": "Text"
          }
        ],
        "reference_to": "crm_customer",
        "type": "Lookup"
      },
      {
        "customized": false,
        "label": "联系人",
        "name": "follow_record_related_contact",
        "nillable": true,
        "quote": true,
        "reference_fields": [
          {
            "label": "姓名",
            "name": "contact_name",
            "nillable": false,
            "type": "Text"
          }
        ],
        "reference_to": "crm_contact",
        "type": "Lookup"
      },
      {
        "customized": true,
        "label": "拜访方式",
        "name": "DDSelectField-K2U5UJAC",
        "nillable": false,
        "select_options": [
          {
            "key": "option_K2U5VJBL",
            "value": "当面拜访"
          },
          {
            "key": "option_K2U5VJBM",
            "value": "电话拜访"
          },
          {
            "key": "option_K2U5VJBN",
            "value": "网络拜访"
          },
          {
            "key": "option_K2U5VJBO",
            "value": "其他"
          }
        ],
        "type": "Select"
      },
      {
        "customized": true,
        "label": "拜访内容",
        "name": "TextareaField-K2U5UJAF",
        "nillable": false,
        "type": "Textarea"
      }
    ],
    "name": "crm_follow_record",
    "status": "PUBLISHED"
  },
  "request_id": "15r94vowuzawz"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
