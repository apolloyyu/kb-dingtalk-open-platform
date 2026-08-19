---
title: "商旅成本中心转换为外部成本中心"
source_url: "https://open.dingtalk.com/document/development/business-travel-cost-center-converted-to-external-cost-center"
namespace: "development"
slug: "business-travel-cost-center-converted-to-external-cost-center"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 商旅成本中心转换为外部成本中心"
doc_id: "jaCvtitwut"
updated_at: "2026-06-08 09:47:09"
---

> Source: https://open.dingtalk.com/document/development/business-travel-cost-center-converted-to-external-cost-center
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 商旅成本中心转换为外部成本中心
> Updated: 2026-06-08 09:47:09

# 商旅成本中心转换为外部成本中心

通过此接口，可将阿里商旅中的成本中心信息转换为外部系统可用的成本中心标识，便于企业实现商旅费用与外部财务系统的映射和统一管理。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip\_write-阿里商旅专用写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenCostCenterTransferRq | 是 |  | 请求对象。 |
| thirdpart\_id | String | 是 | abcefg | 第三方成本中心id。 |
| cost\_center\_id | Number | 是 | 12345 | 商旅成本中心id。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=797cd57exxxx2a210955' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer");
OapiAlitripBtripCostCenterTransferRequest req = new OapiAlitripBtripCostCenterTransferRequest();
OpenCostCenterTransferRq obj1 = new OpenCostCenterTransferRq();
obj1.setThirdpartId("abcefg");
obj1.setCostCenterId(12345L);
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripCostCenterTransferResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripCostCenterTransferRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer")

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
$req = new OapiAlitripBtripCostCenterTransferRequest;
$rq = new OpenCostCenterTransferRq;
$rq->thirdpart_id="abcefg";
$rq->cost_center_id="12345";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/transfer");
OapiAlitripBtripCostCenterTransferRequest req = new OapiAlitripBtripCostCenterTransferRequest();
OapiAlitripBtripCostCenterTransferRequest.OpenCostCenterTransferRqDomain obj1 = new OapiAlitripBtripCostCenterTransferRequest.OpenCostCenterTransferRqDomain();
obj1.ThirdpartId = "abcefg";
obj1.CostCenterId = 12345L;
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripCostCenterTransferResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 错误码。 |
| errmsg | String | 成功 | 错误码描述。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
