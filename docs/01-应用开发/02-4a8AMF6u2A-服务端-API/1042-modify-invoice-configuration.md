---
title: "修改发票配置"
source_url: "https://open.dingtalk.com/document/development/modify-invoice-configuration"
namespace: "development"
slug: "modify-invoice-configuration"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 修改发票配置"
doc_id: "VoHVYWj0MA"
updated_at: "2026-06-08 09:47:25"
---

> Source: https://open.dingtalk.com/document/development/modify-invoice-configuration
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 修改发票配置
> Updated: 2026-06-08 09:47:25

# 修改发票配置

通过此接口修改阿里商旅中的发票配置信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/modify |
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
| request | OpenInvoiceModifyAndNewRq | 否 |  | 请求对象。 |
| address | String | 否 | 浙江省余杭区xxxx | 注册地址。 |
| corpid | String | 是 | dinge8a56572fxxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| bank\_name | String | 否 | xx银行 | 开户行。 |
| type | Number | 是 | 1 | 发票类型：   - **1**：增值税普通发票 - **2**：增值税专用发票 |
| title | String | 是 | 浙江xxxx有限公司 | 发票抬头。 |
| tel | String | 否 | 188xxxx0859 | 公司电话。 |
| tax\_no | String | 否 | 90300xxxx | 纳税人识别号。 |
| bank\_no | String | 否 | 512929xxxx | 银行账号。 |
| third\_part\_id | String | 是 | i123 | 第三方发票id，调用[查询可用发票列表](1041-query-available-invoices.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/modify" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e9c95axxxx6303e7f' \
-d 'request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/modify");
OapiAlitripBtripInvoiceSettingModifyRequest req = new OapiAlitripBtripInvoiceSettingModifyRequest();
OpenInvoiceModifyAndNewRq andNewRq = new OpenInvoiceModifyAndNewRq();
andNewRq.setAddress("浙江省余杭区xxxx");
andNewRq.setCorpid("dinge8a56572fxxxx");
andNewRq.setBankName("xx银行");
andNewRq.setType(1L);
andNewRq.setTitle("浙江xxxx有限公司");
andNewRq.setTel("188xxxx0859");
andNewRq.setTaxNo("90300xxxx");
andNewRq.setBankNo("512929xxxx");
andNewRq.setThirdPartId("i123");
req.setRequest(andNewRq);
OapiAlitripBtripInvoiceSettingModifyResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripInvoiceSettingModifyRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/modify")

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
$req = new OapiAlitripBtripInvoiceSettingModifyRequest;
$request = new OpenInvoiceModifyAndNewRq;
$request->address="注册地址";
$request->corpid="c123";
$request->bank_name="xx银行";
$request->type="1";
$request->title="发票抬头";
$request->tel="12312312312";
$request->tax_no="123";
$request->bank_no="123";
$request->third_part_id="i123";
$req->setRequest($request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/modify");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/modify");
OapiAlitripBtripInvoiceSettingModifyRequest req = new OapiAlitripBtripInvoiceSettingModifyRequest();
OapiAlitripBtripInvoiceSettingModifyRequest.OpenInvoiceModifyAndNewRqDomain obj1 = new OapiAlitripBtripInvoiceSettingModifyRequest.OpenInvoiceModifyAndNewRqDomain();
obj1.Address = "注册地址";
obj1.Corpid = "c123";
obj1.BankName = "xx银行";
obj1.Type = 1L;
obj1.Title = "发票抬头";
obj1.Tel = "12312312312";
obj1.TaxNo = "123";
obj1.BankNo = "123";
obj1.ThirdPartId = "i123";
req.Request_ = obj1;
OapiAlitripBtripInvoiceSettingModifyResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| module | Number | 123 | 返回值。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | zpdytmgm7fnc | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "request_id": "zpdytmgm7fnc"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
