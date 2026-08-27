---
title: "获取月对账结算数据"
source_url: "https://open.dingtalk.com/document/development/obtain-monthly-reconciliation-settlement-data"
namespace: "development"
slug: "obtain-monthly-reconciliation-settlement-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 账单管理 > 获取月对账结算数据"
doc_id: "6jBgMapT03"
updated_at: "2026-06-08 09:47:28"
---

> Source: https://open.dingtalk.com/document/development/obtain-monthly-reconciliation-settlement-data
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 账单管理 > 获取月对账结算数据
> Updated: 2026-06-08 09:47:28

# 获取月对账结算数据

本接口用于获取企业月度对账结算数据的下载地址，适用于财务对账场景，支持企业内部应用和第三方企业应用调用。获取到的下载链接可用于自动化下载月度差旅费用明细，便于企业进行财务结算、成本分析与报表生成。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get |
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
| request | OpenAccountRq | 是 |  | 请求对象。 |
| bill\_month | String | 否 | 202004 | 对账单月份，不传取最新对账单。 |
| corpid | String | 是 | dinge8a56572xxxx | 企业的corpid，可登录[开发者后台](https://open-dev.dingtalk.com/)查看。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a177b8xxxxe0e32d1' \
-d 'request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get");
OapiAlitripBtripMonthbillUrlGetRequest req = new OapiAlitripBtripMonthbillUrlGetRequest();
OpenAccountRq accountRq = new OpenAccountRq();
accountRq.setBillMonth("202004");
accountRq.setCorpid("dinge8a56572xxxx");
req.setRequest(accountRq);
OapiAlitripBtripMonthbillUrlGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripMonthbillUrlGetRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get")

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
$req = new OapiAlitripBtripMonthbillUrlGetRequest;
$request = new OpenAccountRq;
$request->bill_month="202004";
$request->corpid="dingsdsdsfsdf";
$req->setRequest($request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/monthbill/url/get");
OapiAlitripBtripMonthbillUrlGetRequest req = new OapiAlitripBtripMonthbillUrlGetRequest();
OapiAlitripBtripMonthbillUrlGetRequest.OpenAccountRqDomain obj1 = new OapiAlitripBtripMonthbillUrlGetRequest.OpenAccountRqDomain();
obj1.BillMonth = "202004";
obj1.Corpid = "dingsdsdsfsdf";
req.Request_ = obj1;
OapiAlitripBtripMonthbillUrlGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 成功标识。 |
| module | OpenAccountRs[] | module | 返回对象。 |
| start\_date | String | 2020-04-01 | 账期开始时间。 |
| end\_date | String | 2020-04-30 | 账期结束时间。 |
| url | String | http://hangzhou.com/xxxx | json数据下载链接，通过HttpClient 获取，并以GBK格式解析，链接有效期为五分钟。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| request\_id | String | 4cmx63u8ue76 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "module": [
    {
      "end_date": "2020-05-24",
      "start_date": "2020-04-25",
      "url": "http://hangzhou.com/xxxx"
    }
  ],
  "success": true,
  "request_id": "4cmx63u8ue76"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
