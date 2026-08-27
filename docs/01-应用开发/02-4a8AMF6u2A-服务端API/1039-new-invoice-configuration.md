---
title: "新增发票配置"
source_url: "https://open.dingtalk.com/document/development/new-invoice-configuration"
namespace: "development"
slug: "new-invoice-configuration"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 新增发票配置"
doc_id: "mbnLh3HVLF"
updated_at: "2026-06-08 09:47:21"
---

> Source: https://open.dingtalk.com/document/development/new-invoice-configuration
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 新增发票配置
> Updated: 2026-06-08 09:47:21

# 新增发票配置

通过此接口新增企业发票配置信息，支持增值税普通发票和专用发票的设置。适用于企业差旅报销、财务管理系统中统一维护发票信息的场景。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add |
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
| rq | OpenInvoiceModifyAndNewRq | 是 |  | 发票信息请求对象，包含完整的发票配置内容。 |
| corpid | String | 是 | dinge8a56572fxxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| type | Number | 是 | 1 | 发票类型：   - **1**：增值税普通发票 - **2**：增值税专用发票 |
| title | String | 是 | 浙江xxxx有限公司 | 发票抬头。 |
| tax\_no | String | 是 | 90300xxxx | 纳税人识别号。 |
| bank\_name | String | 否 | xx银行 | 开户行。 |
| address | String | 否 | 浙江省余杭区xxxx | 注册地址。 |
| tel | String | 否 | 188xxxx0859 | 公司电话。 |
| bank\_no | String | 否 | 512929xxxx | 银行账号。 |
| third\_part\_id | String | 是 | i123 | 第三方发票id。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c0ac6xxxx1feb75df' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add");
OapiAlitripBtripInvoiceSettingAddRequest req = new OapiAlitripBtripInvoiceSettingAddRequest();
OpenInvoiceModifyAndNewRq modifyAndNewRq = new OpenInvoiceModifyAndNewRq();
modifyAndNewRq.setCorpid("dinge8a56572fxxxx");
modifyAndNewRq.setType(1L);
modifyAndNewRq.setTitle("浙江xxxx有限公司");
modifyAndNewRq.setTaxNo("90300xxxx");
modifyAndNewRq.setBankName("xx银行");
modifyAndNewRq.setAddress("浙江省余杭区xxxx");
modifyAndNewRq.setTel("188xxxx0859");
modifyAndNewRq.setBankNo("512929xxxx");
modifyAndNewRq.setThirdPartId("i123");
req.setRq(modifyAndNewRq);
OapiAlitripBtripInvoiceSettingAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripInvoiceSettingAddRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add")

req.rq=""
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
$req = new OapiAlitripBtripInvoiceSettingAddRequest;
$rq = new OpenInvoiceModifyAndNewRq;
$rq->corpid="123";
$rq->type="1";
$rq->title="发票抬头";
$rq->tax_no="123";
$rq->bank_name="XX银行";
$rq->address="xxx";
$rq->tel="123123123";
$rq->bank_no="123";
$rq->third_part_id="i123";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/add");
OapiAlitripBtripInvoiceSettingAddRequest req = new OapiAlitripBtripInvoiceSettingAddRequest();
OapiAlitripBtripInvoiceSettingAddRequest.OpenInvoiceModifyAndNewRqDomain obj1 = new OapiAlitripBtripInvoiceSettingAddRequest.OpenInvoiceModifyAndNewRqDomain();
obj1.Corpid = "123";
obj1.Type = 1L;
obj1.Title = "发票抬头";
obj1.TaxNo = "123";
obj1.BankName = "XX银行";
obj1.Address = "xxx";
obj1.Tel = "123123123";
obj1.BankNo = "123";
obj1.ThirdPartId = "i123";
req.Rq_ = obj1;
OapiAlitripBtripInvoiceSettingAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| module | Number | 340290 | 结果值。 |
| request\_id | String | 3y4cwh3v6ex7 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "module": 340290,
  "success": true,
  "request_id": "3y4cwh3v6ex7"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
