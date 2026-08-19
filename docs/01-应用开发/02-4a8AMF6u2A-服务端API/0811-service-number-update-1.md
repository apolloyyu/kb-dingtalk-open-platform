---
title: "更新服务号"
source_url: "https://open.dingtalk.com/document/development/service-number-update-1"
namespace: "development"
slug: "service-number-update-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 服务号管理 > 更新服务号"
doc_id: "53EYecQMY3"
updated_at: "2026-06-01 09:15:30"
---

> Source: https://open.dingtalk.com/document/development/service-number-update-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 服务号管理 > 更新服务号
> Updated: 2026-06-01 09:15:30

# 更新服务号

本接口用于更新指定服务号的相关信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/serviceaccount/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_manage-服务号管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | vfdiPCiSeSXdoiE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| name | String | 否 | 钉三多 | 服务号名称。 |
| avatar\_media\_id | String | 否 | @lALPBbCc1XuaP\_rNAljNAlg | 头像图片mediaId，可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片获取mediaId。 |
| brief | String | 否 | 互动服务窗 | 机器人管理列表中的简介，最多60个字符。 |
| desc | String | 否 | 我是钉三多 | 机器人主页中的服务号功能简介，最多200个字符。 |
| preview\_media\_id | String | 否 | @lALPBbCc1XuaP\_rNAljNAlg | 机器人主页中，消息预览图片的mediaId，可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片获取mediaId。 |
| status | String | 否 | normal | 状态：   - **normal**：正常 - **disabled**：删除   **[!IMPORTANT]**  当status设置为disabled时，就代表永久的删除当前服务号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/serviceaccount/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=976c4xxxx5f618' \
-d 'avatar_media_id=%40lALPBbCc1XuaP_rNAljNAlg' \
-d 'brief=%E4%BA%92%E5%8A%A8%E6%9C%8D%E5%8A%A1%E7%AA%97' \
-d 'desc=%E6%88%91%E6%98%AF%E9%92%89%E4%B8%89%E5%A4%9A' \
-d 'name=%E9%92%89%E4%B8%89%E5%A4%9A' \
-d 'preview_media_id=%40lALPBbCc1XuaP_rNAljNAlg' \
-d 'status=normal' \
-d 'unionid=vfdiPCiSeSXdoiE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/update");
OapiServiceaccountUpdateRequest req = new OapiServiceaccountUpdateRequest();
req.setName("钉三多");
req.setAvatarMediaId("@lALPBbCc1XuaP_rNAljNAlg");
req.setBrief("互动服务窗");
req.setDesc("我是钉三多");
req.setPreviewMediaId("@lALPBbCc1XuaP_rNAljNAlg");
req.setUnionid("vfdiPCiSeSXdoiE");
req.setStatus("normal");
OapiServiceaccountUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceaccountUpdateRequest("https://oapi.dingtalk.com/topapi/serviceaccount/update")

req.name="钉三多"
req.avatar_media_id="@lALPBbCc1XuaP_rNAljNAlg"
req.brief="互动服务窗"
req.desc="我是钉三多"
req.preview_media_id="@lALPBbCc1XuaP_rNAljNAlg"
req.unionid="vfdiPCiSeSXdoiE"
req.status="normal"
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
$req = new OapiServiceaccountUpdateRequest;
$req->setName("钉三多");
$req->setAvatarMediaId("@lALPBbCc1XuaP_rNAljNAlg");
$req->setBrief("互动服务窗");
$req->setDesc("我是钉三多");
$req->setPreviewMediaId("@lALPBbCc1XuaP_rNAljNAlg");
$req->setUnionid("vfdiPCiSeSXdoiE");
$req->setStatus("normal");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/serviceaccount/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/update");
OapiServiceaccountUpdateRequest req = new OapiServiceaccountUpdateRequest();
req.Name = "钉三多";
req.AvatarMediaId = "@lALPBbCc1XuaP_rNAljNAlg";
req.Brief = "互动服务窗";
req.Desc = "我是钉三多";
req.PreviewMediaId = "@lALPBbCc1XuaP_rNAljNAlg";
req.Unionid = "vfdiPCiSeSXdoiE";
req.Status = "normal";
OapiServiceaccountUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 5lbow5aebhbi | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"5lbow5aebhbi"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
