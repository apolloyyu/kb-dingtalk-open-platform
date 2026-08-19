---
title: "查询可用发票列表"
source_url: "https://open.dingtalk.com/document/development/query-available-invoices"
namespace: "development"
slug: "query-available-invoices"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 查询可用发票列表"
doc_id: "QJyh969G8z"
updated_at: "2026-06-08 09:47:23"
---

> Source: https://open.dingtalk.com/document/development/query-available-invoices
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 发票管理 > 查询可用发票列表
> Updated: 2026-06-08 09:47:23

# 查询可用发票列表

调用本接口可查询企业用户可用的发票列表，适用于员工报销、商旅预订等场景中核验可使用发票信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenInvoiceRq | 是 |  | 请求对象。 |
| title | String | 否 | 发票1 | 发票抬头名称。 |
| userid | String | 是 | user1 | 用户的userid。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d9870xxxxd8e0327de' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search");
OapiAlitripBtripInvoiceSearchRequest req = new OapiAlitripBtripInvoiceSearchRequest();
OpenInvoiceRq obj1 = new OpenInvoiceRq();
obj1.setTitle("发票1");
obj1.setUserid("user1");
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripInvoiceSearchResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripInvoiceSearchRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search")

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
$req = new OapiAlitripBtripInvoiceSearchRequest;
$rq = new OpenInvoiceRq;
$rq->title="发票1";
$rq->userid="user1";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/invoice/search");
OapiAlitripBtripInvoiceSearchRequest req = new OapiAlitripBtripInvoiceSearchRequest();
OapiAlitripBtripInvoiceSearchRequest.OpenInvoiceRqDomain obj1 = new OapiAlitripBtripInvoiceSearchRequest.OpenInvoiceRqDomain();
obj1.Title = "发票1";
obj1.Userid = "user1";
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripInvoiceSearchResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| invoice | OpenInvoiceDo[] | module | 发票列表。 |
| id | Number | 123 | 商旅发票id。 |
| title | String | 阿里巴巴 | 发票抬头。 |
| success | Boolean | true | 操作是否成功。 |
| errmsg | String | 成功 | 返回信息。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode":0,
  "success":"true",
  "errmsg":"成功",
  "invoice":{
    "id":"123",
    "title":"阿里巴巴"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
