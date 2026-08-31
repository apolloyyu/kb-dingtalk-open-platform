---
title: "配置发票适用人群"
source_url: "https://open.dingtalk.com/document/development/configure-invoice-users"
namespace: "development"
slug: "configure-invoice-users"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 配置发票适用人群"
doc_id: "tQ8untiyvO"
updated_at: "2026-06-08 09:47:22"
---

> Source: https://open.dingtalk.com/document/development/configure-invoice-users
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 配置发票适用人群
> Updated: 2026-06-08 09:47:22

# 配置发票适用人群

通过此接口配置发票的适用人群，支持按员工ID批量设置可报销人员范围或指定全部员工适用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | OpenInvoiceRuleRq | 是 |  | 请求对象。 |
| corpid | String | 是 | dinge8a56572fxxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| entities | Entity[] | 否 |  | 人员列表。 |
| name | String | 是 | 张xx | 人员名称。 |
| id | String | 是 | user01 | 人员id。 |
| type | Number | 是 | 1 | **1**：员工 |
| all\_employe | Boolean | 是 | false | 是否适用所有员工。   - **true**：是 - **false**：否 |
| third\_part\_id | String | 是 | i123 | 第三方发票id，调用[查询可用发票列表](1041-query-available-invoices.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ca621c97-82f9-4e1e-991a-900356c2cb85' \
-d 'request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule");
OapiAlitripBtripInvoiceSettingRuleRequest req = new OapiAlitripBtripInvoiceSettingRuleRequest();
OpenInvoiceRuleRq invoiceRuleRq = new OpenInvoiceRuleRq();
invoiceRuleRq.setCorpid("dinge8a56572fxxxx");
List<Entity> entities = new ArrayList<Entity>();
Entity entity = new Entity();
entities.add(entity);
entity.setName("张xx");
entity.setId("user01");
entity.setType(1L);
invoiceRuleRq.setEntities(entities);
invoiceRuleRq.setAllEmploye(false);
invoiceRuleRq.setThirdPartId("i123");
req.setRequest(invoiceRuleRq);
OapiAlitripBtripInvoiceSettingRuleResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripInvoiceSettingRuleRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule")

req.request=""
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
$req = new OapiAlitripBtripInvoiceSettingRuleRequest;
$request = new OpenInvoiceRuleRq;
$request->corpid="123";
$entities = new Entity;
$entities->name="张三";
$entities->id="123";
$entities->type="1";
$request->entities = array($entities);
$request->all_employe="false";
$request->third_part_id="i123";
$req->setRequest($request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/rule");
OapiAlitripBtripInvoiceSettingRuleRequest req = new OapiAlitripBtripInvoiceSettingRuleRequest();
OapiAlitripBtripInvoiceSettingRuleRequest.OpenInvoiceRuleRqDomain obj1 = new OapiAlitripBtripInvoiceSettingRuleRequest.OpenInvoiceRuleRqDomain();
obj1.Corpid = "123";
List<OapiAlitripBtripInvoiceSettingRuleRequest.EntityDomain> list3 = new List<OapiAlitripBtripInvoiceSettingRuleRequest.EntityDomain>();
OapiAlitripBtripInvoiceSettingRuleRequest.EntityDomain obj4 = new OapiAlitripBtripInvoiceSettingRuleRequest.EntityDomain();
list3.Add(obj4);
obj4.Name = "张三";
obj4.Id = "123";
obj4.Type = 1L;
obj1.Entities= list3;
obj1.AllEmploye = false;
obj1.ThirdPartId = "i123";
req.Request_ = obj1;
OapiAlitripBtripInvoiceSettingRuleResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| module | OpenInvoiceRuleRS | {} | 返回值。 |
| add\_num | Number | 1 | 新增适用人群数。当配置的发票适用人群列表大于当前适用人群数时，返回该参数。 |
| remove\_num | Number | 0 | 删除适用人群数。当配置的发票适用人群列表少于当前的适用人群数时，返回该参数。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | psevtfwak32n | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "module": {
    "add_num": 1,
    "remove_num": 0
  },
  "success": true,
  "request_id": "psevtfwak32n"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
