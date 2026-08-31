---
title: "查询图文卡片列表"
source_url: "https://open.dingtalk.com/document/development/query-message-card-list"
namespace: "development"
slug: "query-message-card-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 图文卡片管理 > 查询图文卡片列表"
doc_id: "vdcr73XsRE"
updated_at: "2026-06-01 09:15:35"
---

> Source: https://open.dingtalk.com/document/development/query-message-card-list
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 图文卡片管理 > 查询图文卡片列表
> Updated: 2026-06-01 09:15:35

# 查询图文卡片列表

调用本接口查询图文卡片列表。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/news/list |
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
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| page\_start | Number | 否 | 1 | 页码，从1开始。 |
| page\_size | Number | 否 | 5 | 每页条数。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/news/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e8641xxxxb3a89' \
-d 'page_size=5' \
-d 'page_start=1' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/list");
OapiMaterialNewsListRequest req = new OapiMaterialNewsListRequest();
req.setUnionid("jYdrJoCmTo0iE");
req.setPageStart(1L);
req.setPageSize(5L);
OapiMaterialNewsListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialNewsListRequest("https://oapi.dingtalk.com/topapi/material/news/list")

req.unionid="jYdrJoCmTo0iE"
req.page_start=1
req.page_size=5
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
$req = new OapiMaterialNewsListRequest;
$req->setUnionid("jYdrJoCmTo0iE");
$req->setPageStart("1");
$req->setPageSize("5");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/news/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/list");
OapiMaterialNewsListRequest req = new OapiMaterialNewsListRequest();
req.Unionid = "jYdrJoCmTo0iE";
req.PageStart = 1L;
req.PageSize = 5L;
OapiMaterialNewsListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | z6srrynclfdc | 请求ID。 |
| total\_count | Number | 1 | 总记录数。 |
| item\_count | Number | 1 | 当前返回记录数。 |
| items | NewsCardDTO[] |  | 卡片列表。 |
| articles | ArticleDTO[] |  | 文章列表。 |
| article\_id | Number | 120001 | 文章id。 |
| title | String | 健康小提醒 | 文章标题。 |
| thumb\_media\_id | String | dsa8d87y7c8d8c | 封面图片的素材id。 |
| publish\_status | Number | 1 | 发布状态：   - **0**：未发布 - **1**：已发布   **[!NOTE]**  文章第一次发布后，状态置为1，已发布文章支持修改，修改后此状态保持为1，每次修改文章后需要再次发布内容才会生效。 |
| publish\_time | Number | 1442027997327 | 发布时间。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| user\_view\_count | Number | 1 | 已读用户数。 |
| total\_view\_count | Number | 12 | 阅读次数。 |
| create\_time | Number | 1442027997327 | 创建时间。 |
| update\_time | Number | 1442027997327 | 修改时间。 |
| url | String | https://content.dingtalk.com/article?articleId=1234 | 文章链接。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| content | String | article\_backup\_raw\_content\_xxxx | 文章内容。 |
| digest | String | 关于这篇文章... | 文章摘要。 |
| update\_time | Number | 1442027997327 | 图文卡片更新时间。 |
| media\_id | String | dsa8d87y7c8d8c | 图文卡片的素材id。 |

### **响应体示例**

```
{
  "errcode": 0, 
  "item_count": 1, 
  "items": [
    {
      "articles": [
        {
          "article_id": 120001, 
          "content": "article_backup_raw_content_1953005", 
          "create_time": 1442027997327, 
          "digest": "关于这篇文章...", 
          "publish_status": 1, 
          "publish_time": 1442027997327, 
          "thumb_media_id": "dsa8d87y7c8d8c", 
          "title": "健康小提醒", 
          "total_view_count": 12, 
          "update_time": 1442027997327, 
          "url": "https://content.dingtalk.com/article?articleId=1234", 
          "user_view_count": 1
        }
      ], 
      "media_id": "dsa8d87y7c8d8c", 
      "update_time": 1442027997327
    }
  ], 
  "total_count": 1, 
  "request_id": "z6srrynclfdc"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
