---
title: "删除项目"
source_url: "https://open.dingtalk.com/document/development/delete-a-project"
namespace: "development"
slug: "delete-a-project"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 项目管理 > 删除项目"
doc_id: "40ISRKF62x"
updated_at: "2026-06-08 09:47:12"
---

> Source: https://open.dingtalk.com/document/development/delete-a-project
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 项目管理 > 删除项目
> Updated: 2026-06-08 09:47:12

# 删除项目

通过此接口可删除由第三方系统同步至钉钉商旅的企业项目。该操作将移除指定的项目数据，适用于企业内部项目管理系统与钉钉商旅集成场景中清理无效或已结束项目的业务需求。

## 接口调用说明

本接口主要用于企业差旅管理系统的项目生命周期管理流程中。当企业在外部系统中关闭或删除某个项目时，可通过调用此接口同步清除钉钉商旅平台中的对应项目信息，确保数据一致性。

调用前需确保：

- 已完成企业身份认证并开通阿里商旅服务；
- 当前项目未关联正在进行的出差申请或报销单据；
- 调用应用已获得“阿里商旅专用权限点”授权。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/project/delete |
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
| corpid | String | 是 | dingabxxxx | 企业的corpid，用于标识目标企业。 |
| third\_part\_id | String | 是 | pro\_id123 | 第三方项目ID。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/project/delete" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7cf400xxxx1a9cb5' \
-d 'corpid=c123' \
-d 'third_part_id=pro_id123'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/project/delete");
OapiAlitripBtripProjectDeleteRequest req = new OapiAlitripBtripProjectDeleteRequest();
req.setCorpid("c123");
req.setThirdPartId("pro_id123");
OapiAlitripBtripProjectDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripProjectDeleteRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/project/delete")

req.corpid="c123"
req.third_part_id="pro_id123"
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
$req = new OapiAlitripBtripProjectDeleteRequest;
$req->setCorpid("c123");
$req->setThirdPartId("pro_id123");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/project/delete");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/project/delete");
OapiAlitripBtripProjectDeleteRequest req = new OapiAlitripBtripProjectDeleteRequest();
req.Corpid = "c123";
req.ThirdPartId = "pro_id123";
OapiAlitripBtripProjectDeleteResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 123 | 返回码。 |
| success | Boolean | true | 操作是否成功。 |
| module | Boolean | true | 操作结果。 |
| errmsg | String | error stack | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "module": true,
  "success": true,
  "request_id": "7jtvxpf5impr"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
