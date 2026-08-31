---
title: "获取外部联系人标签列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-external-contact-tags"
namespace: "development"
slug: "obtains-a-list-of-external-contact-tags"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 外部联系人 > 获取外部联系人标签列表"
doc_id: "WE3hb5Uryb"
updated_at: "2026-05-27 13:09:34"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-external-contact-tags
> Path: 应用开发 / 服务端 API / 通讯录管理 > 外部联系人 > 获取外部联系人标签列表
> Updated: 2026-05-27 13:09:34

# 获取外部联系人标签列表

调用本接口，获取企业外部联系人的标签。企业使用此接口可获取企业外部联系人标签列表，例如这个外部联系人是公司的客户，那么标签可能就是客户。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ext\_read-企业外部联系人读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| size | Number | 否 | 20 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。 |
| offset | Number | 否 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e6eaxxxxa401' \
-d 'offset=0' \
-d 'size=20'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups");
OapiExtcontactListlabelgroupsRequest req = new OapiExtcontactListlabelgroupsRequest();
req.setSize(20L);
req.setOffset(0L);
OapiExtcontactListlabelgroupsResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiExtcontactListlabelgroupsRequest("https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups")

req.size=20
req.offset=0
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
$req = new OapiExtcontactListlabelgroupsRequest;
$req->setSize("20");
$req->setOffset("0");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/listlabelgroups");
OapiExtcontactListlabelgroupsRequest req = new OapiExtcontactListlabelgroupsRequest();
req.Size = 20L;
req.Offset = 0L;
OapiExtcontactListlabelgroupsResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| results | OpenLabelGroup[] |  | 查询结果。 |
| name | String | 类型 | 标签组名字。 |
| color | Number | -15220075 | 标签组颜色。 |
| labels | OpenLabel[] |  | 标签列表。 |
| name | String | 客户 | 标签名称。 |
| id | Number | 1026002 | 标签ID。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 8n3mksu5hqzy | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "results":[
    {
      "color":-15220075,
      "name":"类型",
      "labels":[
        {
          "name":"客户",
          "id":1561077310
        },
        {
          "name":"渠道商",
          "id":1561077311
        },
        {
          "name":"供应商",
          "id":1561077312
        },
        {
          "name":"合作伙伴",
          "id":1561077313
        },
        {
          "name":"面试人员",
          "id":1561077314
        },
        {
          "name":"其他类型",
          "id":1561077315
        }
      ]
    },
    {
      "color":-11687445,
      "name":"级别",
      "labels":[
        {
          "name":"一般",
          "id":1561077317
        },
        {
          "name":"重要",
          "id":1561077318
        },
        {
          "name":"核心",
          "id":1561077319
        }
      ]
    },
    {
      "color":-543394,
      "name":"状态",
      "labels":[
        {
          "name":"潜在",
          "id":1561077321
        },
        {
          "name":"意向",
          "id":1561077322
        },
        {
          "name":"洽谈",
          "id":1561077323
        },
        {
          "name":"成交",
          "id":1561077324
        },
        {
          "name":"流失",
          "id":1561077325
        }
                        ]
                },
                {
                        "color":-543394,
                        "name":"人事招聘状态",
                        "labels":[
                                {
                                        "name":"待邀约",
                                        "id":1561077327
                                },
                                {
                                        "name":"待面试",
                                        "id":1561077328
                                },
                                {
                                        "name":"初试",
                                        "id":1561077329
                                },
                                {
                                        "name":"复试",
                                        "id":1561077330
                                },
                                {
                                        "name":"入职",
                                        "id":1561077331
                                }
                        ]
                }
        ],
        "request_id":"51jof1jt5f4t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33009 | 无效的tokenGrantType | 请检查access\_token是否正确 |
| 400043 | 无效的orgId | 请检查access\_token是否正确 |
| 41101 | 无效的size | 请检查分页大小是否合法 |
| 40068 | 无效的偏移量 | 请调整偏移量 |
| -1 | 系统繁忙 | 请稍后再试 |
