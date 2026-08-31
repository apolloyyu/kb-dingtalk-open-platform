---
title: "获取文章详情"
source_url: "https://open.dingtalk.com/document/development/get-article"
namespace: "development"
slug: "get-article"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 文章管理 > 获取文章详情"
doc_id: "Cf0A8qUk6W"
updated_at: "2026-06-01 09:15:38"
---

> Source: https://open.dingtalk.com/document/development/get-article
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 文章管理 > 获取文章详情
> Updated: 2026-06-01 09:15:38

# 获取文章详情

调用本接口查询一篇文章的详细信息。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/article/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_materials-服务号素材管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | ftO2dFpz1zAiE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| article\_id | Number | 是 | 114001 | 文章id，可以通过[查询文章列表](0817-query-the-article-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/article/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=35b3xxxx223efa71' \
-d 'article_id=114001' \
-d 'unionid=ftO2dFpz1zAiE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/get");
OapiMaterialArticleGetRequest req = new OapiMaterialArticleGetRequest();
req.setUnionid("ftO2dFpz1zAiE");
req.setArticleId(114001L);
OapiMaterialArticleGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialArticleGetRequest("https://oapi.dingtalk.com/topapi/material/article/get")

req.unionid="ftO2dFpz1zAiE"
req.article_id=114001
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
$req = new OapiMaterialArticleGetRequest;
$req->setUnionid("ftO2dFpz1zAiE");
$req->setArticleId("114001");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/article/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/get");
OapiMaterialArticleGetRequest req = new OapiMaterialArticleGetRequest();
req.Unionid = "ftO2dFpz1zAiE";
req.ArticleId = 114001L;
OapiMaterialArticleGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| article\_id | Number | 114001 | 文章id。 |
| title | String | 标题1 | 文章标题。 |
| thumb\_media\_id | String | @lALPBbCc1XuaP\_rNAljNAlg | 封面图。 |
| publish\_status | Number | 1 | 发布状态：   - **0**：未发布 - **1**：已发布   **[!NOTE]**  文章第一次发布后，状态置为1，已发布文章支持修改，修改后此状态保持为1，每次修改文章后需要再次发布内容才会生效。 |
| publish\_time | Number | 1442027997327 | 发布时间。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| create\_time | Number | 1442027997327 | 创建时间。 |
| update\_time | Number | 1442027997327 | 更新时间。 |
| content | String | <html><div>abc</div></html> | 文章内容（html格式）。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| url | String | https://contentcenter.dingtalk.com?articleId=17001 | 文章跳转链接。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| digest | String | 摘要1 | 文章摘要。 |
| request\_id | String | 5dlbspcstarj | 请求ID。 |

### **响应体示例**

```
{
  "article_id": 114001, 
  "content": "<html><div>abc</div></html>", 
  "create_time": 1442027997327, 
  "digest": "摘要1", 
  "errcode": 0, 
  "publish_status": 1, 
  "publish_time": 1442027997327, 
  "thumb_media_id": "@lALPBbCc1XuaP_rNAljNAlg", 
  "title": "标题1", 
  "update_time": 1442027997327, 
  "url": "https://contentcenter.dingtalk.com?articleId=17001", 
  "request_id": "5dlbspcstarj"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| **错误码** | **说明** | **排查方法** |
| --- | --- | --- |
| 1100001 | 此文章已被删除 | 检查传入的article\_id是否有效。 |
