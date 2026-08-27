---
title: "删除发票信息"
source_url: "https://open.dingtalk.com/document/development/delete-invoice-information"
namespace: "development"
slug: "delete-invoice-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 删除发票信息"
doc_id: "rGk7BDRkLN"
updated_at: "2026-06-08 09:47:27"
---

> Source: https://open.dingtalk.com/document/development/delete-invoice-information
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 删除发票信息
> Updated: 2026-06-08 09:47:27

# 删除发票信息

调用本接口可删除指定的发票信息。

## 接口调用说明

适用于企业在阿里商旅平台中管理用户提交的发票信息时，需要删除已失效或重复录入的发票记录。常用于与[查询可用发票列表](1041-query-available-invoices.md)接口配合使用，在前端展示发票列表后，用户选择删除某条发票时触发此接口。

> **[!NOTE]**
>
> 调用前需通过[查询可用发票列表](1041-query-available-invoices.md)接口获取第三方发票ID（`third_part_id`），确保传入有效的发票标识。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete |
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
| request | OpenInvoiceDeleteRq | 否 |  | 请求对象，包含企业标识和待删除的发票信息。 |
| corpid | String | 是 | dinge8a56572fxxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |
| third\_part\_id | String | 是 | i123 | 第三方发票id，调用[查询可用发票列表](1041-query-available-invoices.md#undefined)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0f849520-6f6d-4da2-aa36-77e76d87240c' \
-d 'request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete");
OapiAlitripBtripInvoiceSettingDeleteRequest req = new OapiAlitripBtripInvoiceSettingDeleteRequest();
OpenInvoiceDeleteRq deleteRq = new OpenInvoiceDeleteRq();
deleteRq.setCorpid("corp123");
deleteRq.setThirdPartId("i123");
req.setRequest(deleteRq);
OapiAlitripBtripInvoiceSettingDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripInvoiceSettingDeleteRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete")

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
$req = new OapiAlitripBtripInvoiceSettingDeleteRequest;
$request = new OpenInvoiceDeleteRq;
$request->corpid="corp123";
$request->third_part_id="i123";
$req->setRequest($request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/setting/delete");
OapiAlitripBtripInvoiceSettingDeleteRequest req = new OapiAlitripBtripInvoiceSettingDeleteRequest();
OapiAlitripBtripInvoiceSettingDeleteRequest.OpenInvoiceDeleteRqDomain obj1 = new OapiAlitripBtripInvoiceSettingDeleteRequest.OpenInvoiceDeleteRqDomain();
obj1.Corpid = "corp123";
obj1.ThirdPartId = "i123";
req.Request_ = obj1;
OapiAlitripBtripInvoiceSettingDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| module | Boolean | true | 返回值。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 3ohtyuoasihv | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true
  ,
  "module":true,
  "request_id": "3ohtyuoasihv"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
