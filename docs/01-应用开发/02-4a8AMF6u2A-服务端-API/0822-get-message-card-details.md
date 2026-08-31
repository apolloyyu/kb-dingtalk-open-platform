---
title: "获取图文卡片详情"
source_url: "https://open.dingtalk.com/document/development/get-message-card-details"
namespace: "development"
slug: "get-message-card-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 图文卡片管理 > 获取图文卡片详情"
doc_id: "SbIAE4gd1J"
updated_at: "2026-06-01 09:15:48"
---

> Source: https://open.dingtalk.com/document/development/get-message-card-details
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 图文卡片管理 > 获取图文卡片详情
> Updated: 2026-06-01 09:15:48

# 获取图文卡片详情

调用本接口获取图文卡片详情。

## **接口调用说明**

本接口在互动服务窗内暂无对应产品功能。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/material/news/get |
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
| media\_id | String | 是 | P16mHftLYX8iE | 图文卡片素材id，可以通过[查询图文卡片列表](0824-query-message-card-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/material/news/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=485ebbxxxxe1cf3618' \
-d 'media_id=P16mHftLYX8iE' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/get");
OapiMaterialNewsGetRequest req = new OapiMaterialNewsGetRequest();
req.setUnionid("jYdrJoCmTo0iE");
req.setMediaId("P16mHftLYX8iE");
OapiMaterialNewsGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMaterialNewsGetRequest("https://oapi.dingtalk.com/topapi/material/news/get")

req.unionid="jYdrJoCmTo0iE"
req.media_id="P16mHftLYX8iE"
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
$req = new OapiMaterialNewsGetRequest;
$req->setUnionid("jYdrJoCmTo0iE");
$req->setMediaId("P16mHftLYX8iE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/material/news/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/material/news/get");
OapiMaterialNewsGetRequest req = new OapiMaterialNewsGetRequest();
req.Unionid = "jYdrJoCmTo0iE";
req.MediaId = "P16mHftLYX8iE";
OapiMaterialNewsGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | ezsx3d8hrgzx | 请求ID。 |
| media\_id | String | mvFiiRhuwt5IiE | 卡片素材id。 |
| update\_time | Number | 1560137792000 | 图文卡片更新时间。 |
| articles | ArticleDTO[] |  | 文章列表。 |
| article\_id | Number | 114002 | 文章id。 |
| title | String | 新的标题 | 文章标题。 |
| content | String | <p>第一个段落</p> | 文章内容。 |
| thumb\_media\_id | String | @lALPBbCc1XuaP\_rNAljNAlg | 封面图片的素材id。 |
| publish\_status | Number | 1 | 发布状态：   - **0**：未发布 - **1**：已发布   **[!NOTE]**  文章第一次发布后，状态为1，已发布文章支持修改，修改后此状态保持为1，每次修改文章后需要再次发布内容才会生效。 |
| publish\_time | Number | 1560137792000 | 发布时间。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| user\_view\_count | Number | 1 | 已读用户数。 |
| total\_view\_count | Number | 12 | 阅读次数。 |
| create\_time | Number | 1560137792000 | 文章创建时间。 |
| update\_time | Number | 1560137792000 | 文章更新时间。 |
| url | String | https://content.dingtalk.com/article?articleId=1234 | 文章链接。  **[!NOTE]**  文章成功发布之后才有返回值。 |
| digest | String | 关于这篇文章... | 文章摘要。 |

### **响应体示例**

```
{
  "errcode": 0,
  "update_time": 1560137792000,
  "request_id": "ezsx3d8hrgzx",
  "media_id": "mvFiiRhuwt5IiE",
  "articles": [
    {
      "article_id": 114002,
      "update_time": 1560137792000,
      "thumb_media_id": "@lALPBbCc1XuaP_rNAljNAlg",
      "create_time": 1560137792000,
      "publish_time": 1560137792000,
      "digest": "关于这篇文章...",
      "user_view_count": 1,
      "title": "新的标题",
      "total_view_count": 12,
      "content": "<p>第一个段落</p>",
      "publish_status": 1,
      "url": "https://content.dingtalk.com/article?articleId=1234"
    }
  ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
