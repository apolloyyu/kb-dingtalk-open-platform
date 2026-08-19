---
title: "新增文章"
source_url: "https://open.dingtalk.com/document/development/new-article-1"
namespace: "development"
slug: "new-article-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 文章管理 > 新增文章"
doc_id: "8wQ66t8MwB"
updated_at: "2026-06-01 09:15:28"
---

> Source: https://open.dingtalk.com/document/development/new-article-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 文章管理 > 新增文章
> Updated: 2026-06-01 09:15:28

# 新增文章

调用本接口新增一篇文章。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/article/add |
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
| unionid | String | 是 | ftO2dFpz1zAiE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| article | ArticleCreateDTO | 是 |  | 文章参数对象。 |
| thumb\_media\_id | String | 否 | @lALPBbCc1XuaP\_rNAljNAlg | 图文消息的封面素材id，可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片获取mediaId。 |
| content | String | 是 | <html><body><div>123</div></body></html> | 文章内容（html格式）。 |
| title | String | 是 | 标题1 | 文章标题。 |
| uuid | String | 是 | e5836bb2-2421-49fb | 幂等参数，随机生成的UUID，防止文章重复。 |
| allow\_forward | Boolean | 否 | true | 是否允许转发：   - **true**：转发 - **false**：不转发 |
| view\_scope\_type | Number | 否 | 0 | 文章查看权限(可见范围)：   - **0**：仅企业内可见 - **1**：所有人可见 |
| digest | String | 否 | 摘要1 | 文章摘要。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/article/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=63109bxxxxd9cfd2' \
-d 'article=null' \
-d 'unionid=ftO2dFpz1zAiE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/add");
OapiMaterialArticleAddRequest req = new OapiMaterialArticleAddRequest();
ArticleCreateDTO articleCreateDTO = new ArticleCreateDTO();
articleCreateDTO.setThumbMediaId("@lALPBbCc1XuaP_rNAljNAlg");
articleCreateDTO.setContent("<html><body><div>123</div></body></html>");
articleCreateDTO.setTitle("标题1");
articleCreateDTO.setUuid("e5836bb2-2421-49fb");
articleCreateDTO.setDigest("摘要1");
req.setArticle(articleCreateDTO);
req.setUnionid("IlrIsTHaiSYXluZP61h0zxgiEiE");
OapiMaterialArticleAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialArticleAddRequest("https://oapi.dingtalk.com/topapi/material/article/add")

req.article=""
req.unionid="ftO2dFpz1zAiE"
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
$req = new OapiMaterialArticleAddRequest;
$article = new ArticleCreateDTO;
$article->thumb_media_id="dafsdfadsas";
$article->content="<html><body><div>123</div></body></html>";
$article->title="标题1";
$article->uuid="e5836bb2-2421-49fb-a9a4-c6f4ce5148f7";
$article->digest="摘要1";
$article->allow_forward="true";
$article->view_scope_type="0";
$req->setArticle($article);
$req->setUnionid("ftO2dFpz1zAiE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/article/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/add");
OapiMaterialArticleAddRequest req = new OapiMaterialArticleAddRequest();
OapiMaterialArticleAddRequest.ArticleCreateDTODomain obj1 = new OapiMaterialArticleAddRequest.ArticleCreateDTODomain();
obj1.ThumbMediaId = "dafsdfadsas";
obj1.Content = "<html><body><div>123</div></body></html>";
obj1.Title = "标题1";
obj1.Uuid = "e5836bb2-2421-49fb-a9a4-c6f4ce5148f7";
obj1.Digest = "摘要1";
obj1.AllowForward = true;
obj1.ViewScopeType = 0L;
req.Article_ = obj1;
req.Unionid = "ftO2dFpz1zAiE";
OapiMaterialArticleAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。 |
| article\_id | Number | 2044004 | 文章id。 |
| request\_id | String | 1056rst63clol | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": "1734xxxxxxe08500e",
  "request_id": "5kaikoe9uc8i"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| **错误码** | **说明** | **排查方法** |
| --- | --- | --- |
| 1002 | 参数错误 | 检查传入参数是否正确。 |
