---
title: "获取自定义对象的元数据"
source_url: "https://open.dingtalk.com/document/development/get-metadata-description-of-crm-custom-object"
namespace: "development"
slug: "get-metadata-description-of-crm-custom-object"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 自定义对象 > 获取自定义对象的元数据"
doc_id: "CfRvdjOlwD"
updated_at: "2026-06-08 09:53:19"
---

> Source: https://open.dingtalk.com/document/development/get-metadata-description-of-crm-custom-object
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 自定义对象 > 获取自定义对象的元数据
> Updated: 2026-06-08 09:53:19

# 获取自定义对象的元数据

调用本接口读取钉钉CRM自定义对象（用户自己创建的表单，不包含客户、联系人和跟进记录）的元数据描述。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectmeta/describe |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_customdata\_read-CRM自定义对象数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | PROC-EF1xxxx | 自定义表单code，进入表单编辑页面，最下方可查看。iShot2022-11-01 20 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectmeta/describe" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7dad1a09-ffcb-4263-bdb1-d3b7dd55f749' \
-d 'name=PROC-EF1xxxx'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/describe");
OapiCrmObjectmetaDescribeRequest req = new OapiCrmObjectmetaDescribeRequest();
req.setName("PROC-EF1xxxx");
OapiCrmObjectmetaDescribeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectmetaDescribeRequest("https://oapi.dingtalk.com/topapi/crm/objectmeta/describe")

req.name="PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9"
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
$req = new OapiCrmObjectmetaDescribeRequest;
$req->setName("PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectmeta/describe");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/describe");
OapiCrmObjectmetaDescribeRequest req = new OapiCrmObjectmetaDescribeRequest();
req.Name = "PROC-EF1xxxx";

OapiCrmObjectmetaDescribeResponse rsp = client.Execute(req, accessToken);
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
| select\_options | SelectOptions[] |  | 选项列表。 |
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
| select\_options | SelectOptions[] | SelectOptions | 引用的关联对象的字段选项列表。 |
| key | String | option\_2 | 引用的关联对象的字段选项key。 |
| value | String | 选项2 | 引用的关联对象的字段选项值。 |
| name | String | crm\_customer | 引用的关联对象的字段名称。 |
| roll\_up\_summary\_fields | RollUpSummaryFields[] |  | 对MasterDetail类型有效：roll-up summary字段列表。 |
| name | String | Money-XDADDF | 需要汇总的明细内字段名。 |
| aggregator | String | SUM | 汇总方法。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 调用失败时返回的错误信息。 |

### **响应体示例**

```
{
  "result": {
    "customized": false,
    "name": "crm_customer",
    "fields": [
      {
        "reference_fields": [
          {
            "unit": "天",
            "select_options": [
              {
                "value": "选项2",
                "key": "option_2"
              }
            ],
            "format": "yyyy-MM-dd",
            "name": "crm_customer",
            "label": "联系人名称",
            "type": "Text",
            "nillable": false
          }
        ],
        "unit": "天",
        "customized": false,
        "quote": true,
        "reference_to": "crm_contact",
        "select_options": [
          {
            "value": "选项1",
            "key": "option_1"
          }
        ],
        "roll_up_summary_fields": [
          {
            "aggregator": "SUM",
            "name": "Money-XDADDF"
          }
        ],
        "name": "customer_name",
        "format": "yyyy-MM-dd",
        "label": "客户名称",
        "type": "Text",
        "nillable": false
      }
    ]
  },
  "errcode": 0,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
