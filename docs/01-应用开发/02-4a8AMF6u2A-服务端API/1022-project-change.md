---
title: "修改项目"
source_url: "https://open.dingtalk.com/document/development/project-change"
namespace: "development"
slug: "project-change"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 项目管理 > 修改项目"
doc_id: "tRmAvxxwhp"
updated_at: "2026-06-08 09:47:11"
---

> Source: https://open.dingtalk.com/document/development/project-change
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 项目管理 > 修改项目
> Updated: 2026-06-08 09:47:11

# 修改项目

通过此接口可修改企业差旅管理系统中的项目信息，支持将第三方系统的项目变更同步至钉钉，确保多系统间数据一致性。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify |
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
| request | OpenProjectRs | 是 |  | 请求对象，包含项目修改的具体参数。 |
| corpid | String | 是 | corp\_id | 企业的corpid，标识目标企业。 |
| project\_name | String | 是 | 项目1 | 项目名称，用于展示和识别。 |
| third\_part\_id | String | 是 | p123 | 第三方项目ID。 |
| third\_part\_invoice\_id | String | 否 | i123 | 第三方发票ID。 |
| third\_part\_cost\_center\_id | String | 否 | c123 | 第三方成本中心ID。 |
| code | String | 否 | pro\_code | 项目代码。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=483a8xxxxb5592e' \
-d 'request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify");
OapiAlitripBtripProjectModifyRequest req = new OapiAlitripBtripProjectModifyRequest();
OpenProjectRs obj1 = new OpenProjectRs();
obj1.setCode("pro_code");
obj1.setCorpid("c123");
obj1.setProjectName("项目名");
obj1.setThirdPartId("po123");
obj1.setThirdPartInvoiceId("i123");
obj1.setThirdPartCostCenterId("c123");
req.setRequest(obj1);
OapiAlitripBtripProjectModifyResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripProjectModifyRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify")

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
$req = new OapiAlitripBtripProjectModifyRequest;
$request = new OpenProjectRs;
$request->code="pro_code";
$request->corpid="c123";
$request->project_name="项目名";
$request->third_part_id="po123";
$request->third_part_invoice_id="i123";
$request->third_part_cost_center_id="c123";
$req->setRequest($request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/project/modify");
OapiAlitripBtripProjectModifyRequest req = new OapiAlitripBtripProjectModifyRequest();
OapiAlitripBtripProjectModifyRequest.OpenProjectRsDomain obj1 = new OapiAlitripBtripProjectModifyRequest.OpenProjectRsDomain();
obj1.Code = "pro_code";
obj1.Corpid = "c123";
obj1.ProjectName = "项目名";
obj1.ThirdPartId = "po123";
obj1.ThirdPartInvoiceId = "i123";
obj1.ThirdPartCostCenterId = "c123";
req.Request_ = obj1;
OapiAlitripBtripProjectModifyResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 操作是否成功。 |
| module | String | true | 项目ID。 |
| errcode | Number | 123 | 返回码。 |
| errmsg | String | error stack | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "success": true,
  "request_id": "plvyfcdnb99t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
