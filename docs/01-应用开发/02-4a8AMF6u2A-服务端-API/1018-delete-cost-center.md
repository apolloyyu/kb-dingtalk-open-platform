---
title: "删除成本中心"
source_url: "https://open.dingtalk.com/document/development/delete-cost-center"
namespace: "development"
slug: "delete-cost-center"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 删除成本中心"
doc_id: "RfT6ww2Pr8"
updated_at: "2026-06-08 09:47:06"
---

> Source: https://open.dingtalk.com/document/development/delete-cost-center
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 维护成本中心和发票抬头 > 删除成本中心
> Updated: 2026-06-08 09:47:06

# 删除成本中心

通过本接口可删除指定的成本中心。删除后该成本中心将不可恢复，请确保无正在进行的费用报销或其他业务关联后再执行操作。

## 接口调用说明

适用于企业财务系统对接中清理已废弃的成本中心，需配合第三方成本中心ID（thirdpart\_id）或企业内部corpid进行精准删除。典型场景包括：组织架构调整后的成本中心合并、员工离职后关联成本中心清理、测试数据清除等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete |
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
| rq | OpenCostCenterDeleteRq | 是 |  | 请求对象，封装删除所需参数。 |
| thirdpart\_id | String | 否 | cost1 | 第三方成本中心id。 |
| corpid | String | 否 | corp1 | 企业的corpid，用于定位目标企业。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e6d28exxxxdf476' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete");
OapiAlitripBtripCostCenterDeleteRequest req = new OapiAlitripBtripCostCenterDeleteRequest();
OpenCostCenterDeleteRq obj1 = new OpenCostCenterDeleteRq();
obj1.setThirdpartId("cost1");
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripCostCenterDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripCostCenterDeleteRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete")

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
$req = new OapiAlitripBtripCostCenterDeleteRequest;
$rq = new OpenCostCenterDeleteRq;
$rq->thirdpart_id="cost1";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/cost/center/delete");
OapiAlitripBtripCostCenterDeleteRequest req = new OapiAlitripBtripCostCenterDeleteRequest();
OapiAlitripBtripCostCenterDeleteRequest.OpenCostCenterDeleteRqDomain obj1 = new OapiAlitripBtripCostCenterDeleteRequest.OpenCostCenterDeleteRqDomain();
obj1.ThirdpartId = "cost1";
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripCostCenterDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 调用是否成功。 |

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
