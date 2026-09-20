---
title: "新建成本中心"
source_url: "https://open.dingtalk.com/document/development/new-cost-center"
namespace: "development"
slug: "new-cost-center"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 新建成本中心"
doc_id: "39Us16y6UI"
updated_at: "2026-06-08 09:47:04"
---

> Source: https://open.dingtalk.com/document/development/new-cost-center
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 新建成本中心
> Updated: 2026-06-08 09:47:04

# 新建成本中心

通过此接口创建新的成本中心，适用于已开通阿里商旅服务且需要在钉钉生态中集成差旅管理能力的企业或ISV服务商，

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/new |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip\_write-阿里商旅专用写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenCostCenterSaveRq | 是 |  | 请求对象，封装新建成本中心所需的所有参数。 |
| alipay\_no | String | 否 | a@alipay.com | 绑定支付宝账号。 |
| title | String | 是 | 阿里商旅 | 成本中心名称。 |
| scope | Number | 是 | 1 | 适用范围：   - **1**：全员 - **2**：部分人员 |
| thirdpart\_id | String | 是 | cost1 | 第三方成本中心ID。 |
| number | String | 否 | 12345 | 第三方成本中心编号。 |
| corpid | String | 是 | corp1 | 企业的corpid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/new" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=4bfc5fxxxxafdb0d' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/new");
OapiAlitripBtripCostCenterNewRequest req = new OapiAlitripBtripCostCenterNewRequest();
OpenCostCenterSaveRq obj1 = new OpenCostCenterSaveRq();
obj1.setAlipayNo("a@alipay.com");
obj1.setTitle("阿里商旅");
obj1.setScope(1L);
obj1.setThirdpartId("cost1");
obj1.setNumber("12345");
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripCostCenterNewResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripCostCenterNewRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/new")

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
$req = new OapiAlitripBtripCostCenterNewRequest;
$rq = new OpenCostCenterSaveRq;
$rq->alipay_no="a@alipay.com";
$rq->title="阿里商旅";
$rq->scope="1";
$rq->thirdpart_id="cost1";
$rq->number="12345";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/new");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/new");
OapiAlitripBtripCostCenterNewRequest req = new OapiAlitripBtripCostCenterNewRequest();
OapiAlitripBtripCostCenterNewRequest.OpenCostCenterSaveRqDomain obj1 = new OapiAlitripBtripCostCenterNewRequest.OpenCostCenterSaveRqDomain();
obj1.AlipayNo = "a@alipay.com";
obj1.Title = "阿里商旅";
obj1.Scope = 1L;
obj1.ThirdpartId = "cost1";
obj1.Number = "12345";
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripCostCenterNewResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenCostCenterSaveRs |  | 操作结果。 |
| id | Number | 1234 | 商旅横版中心ID。 |
| success | Boolean | true | 成功标识。 |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "result":{
    "id":"1234"
  },
  "errcode":0,
  "success":true,
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
