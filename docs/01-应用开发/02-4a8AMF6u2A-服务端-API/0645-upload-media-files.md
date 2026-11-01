---
title: "上传媒体文件"
source_url: "https://open.dingtalk.com/document/development/upload-media-files"
namespace: "development"
slug: "upload-media-files"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 媒体文件 > 上传媒体文件"
doc_id: "dGelMr4jOQ"
updated_at: "2026-06-01 09:15:23"
---

> Source: https://open.dingtalk.com/document/development/upload-media-files
> Path: 应用开发 / 服务端 API / 文档/文件 > 媒体文件 > 上传媒体文件
> Updated: 2026-06-01 09:15:23

# 上传媒体文件

调用本接口，上传图片、语音媒体资源文件以及普通文件，接口返回媒体资源标识media\_id。

## **接口调用说明**

调用本接口，上传媒体文件后，可获取媒体资源标识media\_id。关于media\_id：

- 使用multipart/form-data POST上传文件， 文件标识名为media。
- media\_id是可复用的，同一个media\_id多次使用。
- media\_id对应的资源文件，仅能在钉钉客户端内使用。
- 媒体文件使用的空间是钉钉提供给组织的特定存储空间，调用本功能接口上传文件，不占用钉钉组织的钉盘空间。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/media/upload |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| type | String | 是 | image | 媒体文件类型：   - **image**：图片，图片最大20MB。支持上传jpg、gif、png、bmp格式。 - **voice**：语音，语音文件最大2MB。支持上传amr、mp3、wav格式。 - **video**：视频，视频最大20MB。支持上传mp4格式。 - **file**：普通文件，最大20MB。支持上传doc、docx、xls、xlsx、ppt、pptx、zip、pdf、rar格式。   **[!IMPORTANT]**  如果使用C#调用该接口出现**40004**（不合法的媒体文件类型）错误，需将参数**type**加在请求的URL后面。 |
| media | FileItem | 是 | C:/Users/Desktop/222.png | 要上传的媒体文件。  form-data中媒体文件标识，有filename、filelength、content-type等信息。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/media/upload" \
-H 'Content-Type:multipart/form-data;charset=utf-8' \
-F 'access_token=4c813ba0-2363-4927-9de0-376b0e6853a2' \
-F 'type=image' \
-F 'media=@"C:/Users/Desktop/222.png"'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/media/upload");
OapiMediaUploadRequest req = new OapiMediaUploadRequest();
req.setType("image");
// 要上传的媒体文件
FileItem item = new FileItem("C:/Users/Desktop/222.png");
req.setMedia(item);
OapiMediaUploadResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMediaUploadRequest("https://oapi.dingtalk.com/media/upload")

req.type="image"
req.media=dingtalk.api.FileItem('abc.jpg',open('abc.jpg','rb'))
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
$req = new OapiMediaUploadRequest;
$req->setType("image");

$req->setMedia("C:/Users/Desktop/222.png");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/media/upload");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/media/upload");
OapiMediaUploadRequest req = new OapiMediaUploadRequest();
req.Type = "image";
req.Media = new FileItem("C:/Users/Desktop/222.png");
OapiMediaUploadResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| type | String | file | 媒体文件类型：   - **image**：图片 - **voice**：语音 - **file**：普通文件 - **video**：视频 |
| media\_id | String | @#lAzPDgCwPn1mJiDOQoLpxxxx | 媒体文件上传后获取的唯一标识。 |
| created\_at | Number | 1599556098964 | 媒体文件上传时间戳。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "media_id": "$iAEKAqNwbmcDBgTNAk",
  "created_at": 1605863153573,
  "type": "image"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
