---
title: "更新文章"
source_url: "https://open.dingtalk.com/document/development/save-article-details-1"
namespace: "development"
slug: "save-article-details-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 文章管理 > 更新文章"
doc_id: "TvEUrHzWKC"
updated_at: "2026-06-01 09:15:45"
---

> Source: https://open.dingtalk.com/document/development/save-article-details-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 文章管理 > 更新文章
> Updated: 2026-06-01 09:15:45

# 更新文章

调用本接口更新指定文章。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/article/update |
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
| unionid | String | 是 | lO44Wvqzy7siE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| article | ArticleCreateDTO | 是 |  | 文章参数对象。 |
| thumb\_media\_id | String | 否 | @lALPBbCc1XuaP\_rNAljNAlg | 图文消息的封面图片素材id，可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片获取mediaId。 |
| content | String | 是 | <div>123</div> | 文章内容（html格式）。 |
| title | String | 是 | 修改后标题 | 文章标题。 |
| article\_id | Number | 是 | 129003 | 文章id，可以通过[查询文章列表](0817-query-the-article-list.md)接口获取。 |
| digest | String | 否 | 摘要1 | 文章摘要。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/article/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7c2a9xxxx0850c6' \
-d 'article=null' \
-d 'unionid=lO44Wvqzy7siE'
```

Java

```
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/update");
  OapiMaterialArticleUpdateRequest req = new OapiMaterialArticleUpdateRequest();
  ArticleCreateDTO createDTO = new ArticleCreateDTO();
  createDTO.setThumbMediaId("图片");
  createDTO.setContent("<div>123</div>");
  createDTO.setTitle("修改后标题");
  createDTO.setArticleId(129003L);
  createDTO.setDigest("摘要1");
  req.setArticle(createDTO);
  req.setUnionid("lO44Wvqzy7siE");
  OapiMaterialArticleUpdateResponse rsp = client.execute(req, access_token);
  System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialArticleUpdateRequest("https://oapi.dingtalk.com/topapi/material/article/update")

req.article=""
req.unionid="lO44Wvqzy7siE"
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
$req = new OapiMaterialArticleUpdateRequest;
$article = new ArticleCreateDTO;
$article->thumb_media_id="图片";
$article->content="<div>123</div>";
$article->title="修改后标题";
$article->article_id="129003";
$article->digest="摘要1";
$req->setArticle($article);
$req->setUnionid("lO44Wvqzy7siE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/article/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/update");
OapiMaterialArticleUpdateRequest req = new OapiMaterialArticleUpdateRequest();
OapiMaterialArticleUpdateRequest.ArticleCreateDTODomain obj1 = new OapiMaterialArticleUpdateRequest.ArticleCreateDTODomain();
obj1.ThumbMediaId = "图片";
obj1.Content = "<div>123</div>";
obj1.Title = "修改后标题";
obj1.ArticleId = 129003L;
obj1.Digest = "摘要1";
req.Article_ = obj1;
req.Unionid = "lO44Wvqzy7siE";
OapiMaterialArticleUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 4ieov7rmxctz | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"4ieov7rmxctz"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
