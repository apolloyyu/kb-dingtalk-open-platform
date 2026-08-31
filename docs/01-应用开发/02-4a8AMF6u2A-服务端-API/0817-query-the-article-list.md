---
title: "查询文章列表"
source_url: "https://open.dingtalk.com/document/development/query-the-article-list"
namespace: "development"
slug: "query-the-article-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 文章管理 > 查询文章列表"
doc_id: "8Vqt8rPDem"
updated_at: "2026-06-01 09:15:41"
---

> Source: https://open.dingtalk.com/document/development/query-the-article-list
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 文章管理 > 查询文章列表
> Updated: 2026-06-01 09:15:41

# 查询文章列表

调用本接口查询文章列表。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/article/list |
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
| page\_size | Number | 是 | 5 | 每页条数。 |
| page\_start | Number | 是 | 1 | 页码。 |
| publishStatus | Number | 否 | 1 | 文章发布状态：   - **0**：未发布 - **1**：已发布 |
| status | Number | 否 | 0 | 文章状态：   - **0**：正常 - **1**：删除 - **-1**：返回所有(正常、删除)状态 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/article/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d5f36f03-c5c0-4c2f-8165-a971c5ed6350' \
-d 'page_size=5' \
-d 'page_start=1' \
-d 'publishStatus=1' \
-d 'status=0' \
-d 'unionid=lO44Wvqzy7siE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/list");
OapiMaterialArticleListRequest req = new OapiMaterialArticleListRequest();
req.setUnionid("lO44Wvqzy7siE");
req.setPageSize(5L);
req.setPageStart(1L);
OapiMaterialArticleListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialArticleListRequest("https://oapi.dingtalk.com/topapi/material/article/list")

req.unionid="lO44Wvqzy7siE"
req.page_size=5
req.page_start=1
req.publishStatus=1
req.status=0
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
$req = new OapiMaterialArticleListRequest;
$req->setUnionid("lO44Wvqzy7siE");
$req->setPageSize("5");
$req->setPageStart("1");
$req->setPublishStatus("1");
$req->setStatus("0");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/article/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/article/list");
OapiMaterialArticleListRequest req = new OapiMaterialArticleListRequest();
req.Unionid = "lO44Wvqzy7siE";
req.PageSize = 5L;
req.PageStart = 1L;
req.PublishStatus = 1L;
req.Status = 0L;
OapiMaterialArticleListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| items | ArticleDTO[] |  | 文章列表。 |
| article\_id | Number | 129003 | 文章id。 |
| title | String | 标题1 | 标题。 |
| thumb\_media\_id | String | @lALPBbCc1XuaP\_rNAljNAlg | 封面图。 |
| publish\_status | Number | 1 | 发布状态：   - **0**：未发布 - **1**：已发布   **[!NOTE]**  文章第一次发布后，状态置为1，已发布文章支持修改，修改后此状态保持为1，每次修改文章后需要再次发布内容才会生效。 |
| publish\_time | Number | 1442027997327 | 发布时间。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| create\_time | Number | 1442027997327 | 创建时间。 |
| update\_time | Number | 1442027997327 | 更新时间。 |
| content | String | article\_backup\_raw\_content\_xxxx | 文章内容。 |
| url | String | https://dingtalk.com?articleId=17001 | 文章跳转链接。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| digest | String | 摘要1 | 文章摘要。 |
| total\_count | Number | 100 | 文章总数。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| item\_count | Number | 5 | 本页条数。 |
| request\_id | String | 8g4j3xpjuuly | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "item_count": 5,
  "total_count": 100,
  "request_id": "8g4j3xpjuuly",
  "items": [
    {
      "article_id": 129003,
      "update_time": 1442027997327,
      "thumb_media_id": "@lALPBbCc1XuaP_rNAljNAlg",
      "create_time": 1442027997327,
      "publish_time": 1442027997327,
      "digest": "摘要1",
      "title": "标题1",
      "publish_status": 1,
      "content": "article_backup_raw_content_xxxx",
      "url": "https://contentcenter.dingtalk.com?articleId=17001"
    }
  ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
