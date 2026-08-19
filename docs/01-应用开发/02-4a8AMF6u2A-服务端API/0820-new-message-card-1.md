---
title: "新增图文卡片"
source_url: "https://open.dingtalk.com/document/development/new-message-card-1"
namespace: "development"
slug: "new-message-card-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 图文卡片管理 > 新增图文卡片"
doc_id: "zFrsUpiT4s"
updated_at: "2026-06-03 09:48:37"
---

> Source: https://open.dingtalk.com/document/development/new-message-card-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 图文卡片管理 > 新增图文卡片
> Updated: 2026-06-03 09:48:37

# 新增图文卡片

调用本接口新增图文卡片。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/news/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_materials-服务号素材管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| articles | ArticleDTO[] | 是 |  | 文章列表。 |
| article\_id | Number | 是 | 10012 | 文章id，可以通过[查询文章列表](0817-query-the-article-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/news/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b67exxxx88247b1' \
-d 'articles=null' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/add");
OapiMaterialNewsAddRequest req = new OapiMaterialNewsAddRequest();
List<ArticleDTO> articleDTOs = new ArrayList<ArticleDTO>();
ArticleDTO articleDTO = new ArticleDTO();
articleDTOs.add(articleDTO);
articleDTO.setArticleId(10012L);
req.setArticles(articleDTOs);
req.setUnionid("jYdrJoCmTo0iE");
OapiMaterialNewsAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialNewsAddRequest("https://oapi.dingtalk.com/topapi/material/news/add")

req.articles="[10012]"
req.unionid="jYdrJoCmTo0iE"
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
$req = new OapiMaterialNewsAddRequest;
$articles = new ArticleDTO;
$req->setArticles(array($articles));
$req->setUnionid("jYdrJoCmTo0iE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/news/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/add");
OapiMaterialNewsAddRequest req = new OapiMaterialNewsAddRequest();
List<ArticleDTO> articleDTOs = new List<ArticleDTO>();
ArticleDTO articleDTO = new ArticleDTO();
articleDTO.ArticleId = 10012L;
articleDTOs.Add(articleDTO);
req.Articles = articleDTOs;
req.Unionid = "jYdrJoCmTo0iE";
OapiMaterialNewsAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| media\_id | String | cardDHndhMAowusiE | 卡片素材id。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | gwyoxs1xoh68 | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"gwyoxs1xoh68",
  "media_id":"cardDHndhMAowusiE"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
