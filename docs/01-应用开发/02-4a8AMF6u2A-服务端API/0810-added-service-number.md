---
title: "新增服务号"
source_url: "https://open.dingtalk.com/document/development/added-service-number"
namespace: "development"
slug: "added-service-number"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 服务号管理 > 新增服务号"
doc_id: "SWPNiJm7Rv"
updated_at: "2026-06-01 09:15:34"
---

> Source: https://open.dingtalk.com/document/development/added-service-number
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 服务号管理 > 新增服务号
> Updated: 2026-06-01 09:15:34

# 新增服务号

本接口用于新增一个服务号。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/serviceaccount/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_manage-服务号管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | 创建服务号 | 服务号名称。 |
| avatar\_media\_id | String | 是 | @lALPBbCc1XuaP\_rNAljNAlg | 头像图片mediaId，可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片获取mediaId。 |
| brief | String | 否 | 互动服务窗 | 机器人管理列表中的简介。 |
| desc | String | 是 | 我是描述 | 机器人主页中的服务号功能简介，最多200个字符。 |
| preview\_media\_id | String | 是 | @lALPBbCc1XuaP\_rNAljNAlg | 机器人主页中，消息预览图片的mediaId，可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片获取mediaId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/serviceaccount/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=2da92dxxxxd1e358' \
-d 'avatar_media_id=%40lALxxxxNAlg' \
-d 'brief=%E4%BA%92%E5%8A%A8%E6%9C%8D%E5%8A%A1%E7%AA%97' \
-d 'desc=%E6%88%91%E6%98%AF%E9%92%89%E4%B8%89%E5%A4%9A' \
-d 'name=%E9%92%89%E4%B8%89%E5%A4%9A' \
-d 'preview_media_id=%40lALPBbCc1XuaP_rNAljNAlg'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/add");
OapiServiceaccountAddRequest req = new OapiServiceaccountAddRequest();
req.setName("创建服务号");
req.setAvatarMediaId("@lALPBbCc1XuaP_rNAljNAlg");
req.setBrief("互动服务窗");
req.setDesc("我是描述");
req.setPreviewMediaId("@lALPBbCc1XuaP_rNAljNAlg");
OapiServiceaccountAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceaccountAddRequest("https://oapi.dingtalk.com/topapi/serviceaccount/add")

req.name="钉三多"
req.avatar_media_id="@lALPBbCc1XuaP_rNAljNAlg"
req.brief="互动服务窗"
req.desc="我是钉三多"
req.preview_media_id="@lALPBbCc1XuaP_rNAljNAlg"
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
$req = new OapiServiceaccountAddRequest;
$req->setName("钉三多");
$req->setAvatarMediaId("@lALPBbCc1XuaP_rNAljNAlg");
$req->setBrief("互动服务窗");
$req->setDesc("我是钉三多");
$req->setPreviewMediaId("@lALPBbCc1XuaP_rNAljNAlg");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/serviceaccount/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/add");
OapiServiceaccountAddRequest req = new OapiServiceaccountAddRequest();
req.Name = "钉三多";
req.AvatarMediaId = "@lALPBbCc1XuaP_rNAljNAlg";
req.Brief = "互动服务窗";
req.Desc = "我是钉三多";
req.PreviewMediaId = "@lALPBbCc1XuaP_rNAljNAlg";
OapiServiceaccountAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| unionid | String | ybTmcbTAgyMiE | 服务号的unionid。 |
| request\_id | String | vsb12w88ebu1 | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "unionid":"ybTmcbTAgyMiE",
  "request_id":"vsb12w88ebu1"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码 | 说明 | 排查方法 |
| --- | --- | --- |
| 800001 | 请勿创建重复名称的服务号 | 修改服务号名称。 |
| 800004 | 可创建服务号数量达到上限 | 最多允许创建40个。 |
