---
title: "获取企业信息"
source_url: "https://open.dingtalk.com/document/development/obtain-enterprise-information"
namespace: "development"
slug: "obtain-enterprise-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 行业通讯录 > 获取企业信息"
doc_id: "Mo5bBl8LQG"
updated_at: "2026-05-27 13:09:40"
---

> Source: https://open.dingtalk.com/document/development/obtain-enterprise-information
> Path: 应用开发 / 服务端API / 通讯录管理 > 行业通讯录 > 获取企业信息
> Updated: 2026-05-27 13:09:40

# 获取企业信息

调用本接口，获取行业通讯录的企业信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/industry/organization/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_industry\_info\_read-行业通讯录信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/industry/organization/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=69a3xxxxxee570'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/organization/get");
OapiIndustryOrganizationGetRequest req = new OapiIndustryOrganizationGetRequest();
OapiIndustryOrganizationGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiIndustryOrganizationGetRequest("https://oapi.dingtalk.com/topapi/industry/organization/get")

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
$req = new OapiIndustryOrganizationGetRequest;
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/industry/organization/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/organization/get");
OapiIndustryOrganizationGetRequest req = new OapiIndustryOrganizationGetRequest();
OapiIndustryOrganizationGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenIndustryOrgInfo |  | 企业信息。 |
| region\_location | String | 中国\_浙江省\_杭州市\_余杭区 | 具体的企业区域位置信息，下划线划分省市区。例如：中国\_浙江省\_杭州市\_余杭区 |
| region\_id | String | 990102 | 企业所在区域id。  **[!NOTE]**  **110101** 针对行政区，国家统一标准，可以自行处理。例如**11**开头北京市，**0101**东城区类似。 |
| region\_type | String | COUNTY | 企业所在区域类型，目前有以下五种：   - **PROVINCE**：省份 - **CITY**：城市 - **COUNTRY**：县区 - **TOWN**：乡镇 - **VILLAGE**：村 |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 7afehfo9w76t | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "region_type": "COUNTY",
    "region_id": "990102",
    "region_location": "中国_浙江省_杭州市_余杭区"
  },
  "errcode": 0,
  "errmsg": "ok",
  "request_id": "7afehfo9w76t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400043 | 无效的orgId | 请确认access\_token是否正确 |
| 400001 | 系统错误 | 请稍后重试 |
