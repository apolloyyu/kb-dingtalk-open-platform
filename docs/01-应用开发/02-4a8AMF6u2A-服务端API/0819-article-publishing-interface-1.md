---
title: "发布文章"
source_url: "https://open.dingtalk.com/document/development/article-publishing-interface-1"
namespace: "development"
slug: "article-publishing-interface-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 文章管理 > 发布文章"
doc_id: "MILeA9RcEe"
updated_at: "2026-06-01 09:15:43"
---

> Source: https://open.dingtalk.com/document/development/article-publishing-interface-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 文章管理 > 发布文章
> Updated: 2026-06-01 09:15:43

# 发布文章

调用本接口发布文章。

## **接口调用说明**

- 内容更新后仅保存了草稿，需要再次调用发布接口文章内容才会生效。
- 本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/article/publish |
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
| unionid | String | 是 | lO44Wvqzy7siE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| article\_id | Number | 是 | 129003 | 文章id，可以通过[查询文章列表](0817-query-the-article-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/article/publish" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c3d179xxxx802a9a25' \
-d 'article_id=129003' \
-d 'unionid=lO44Wvqzy7siE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/publish");
OapiMaterialArticlePublishRequest req = new OapiMaterialArticlePublishRequest();
req.setUnionid("lO44Wvqzy7siE");
req.setArticleId(129003L);
OapiMaterialArticlePublishResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialArticlePublishRequest("https://oapi.dingtalk.com/topapi/material/article/publish")

req.unionid="lO44Wvqzy7siE"
req.article_id=129003
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
$req = new OapiMaterialArticlePublishRequest;
$req->setUnionid("lO44Wvqzy7siE");
$req->setArticleId("129003");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/article/publish");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/publish");
OapiMaterialArticlePublishRequest req = new OapiMaterialArticlePublishRequest();
req.Unionid = "lO44Wvqzy7siE";
req.ArticleId = 129003L;
OapiMaterialArticlePublishResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| url | String | http://contentcenter.dingtalk.com?articleId=129003 | 生成文章url链接。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | sk80nnqtfjys | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "url":"http://contentcenter.dingtalk.com?articleId=129003",
  "request_id":"sk80nnqtfjys"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
