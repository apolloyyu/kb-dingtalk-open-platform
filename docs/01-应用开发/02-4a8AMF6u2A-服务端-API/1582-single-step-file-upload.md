---
title: "单步文件上传"
source_url: "https://open.dingtalk.com/document/development/single-step-file-upload"
namespace: "development"
slug: "single-step-file-upload"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 单步文件上传"
doc_id: "nFdXQWfy5d"
updated_at: "2026-08-25 09:38:38"
---

> Source: https://open.dingtalk.com/document/development/single-step-file-upload
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 单步文件上传
> Updated: 2026-08-25 09:38:38

# 单步文件上传

调用本接口上传文件到钉盘。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，已接入用户不受影响。

钉盘提供接口将文件上传至存储服务器。上传方式为以下两种：

- 分块上传

  分块上传支持将文件分片上传，并由commit步骤完成数据提交，可实现较大文件的上传，最多支持8M \* 10000。
- 单步上传。

  单步上传流程较简单，使用标准 http multipart 上传，文件大小不得超过8M。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 请保证自己的机器有足够的出口带宽，否则可能导致上传异常缓慢。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/file/upload/single`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| file\_size | Number | 是 | 58927664 | 文件大小，单位byte。  **[!NOTE]**  文件大小不得超过8M。 |
| agent\_id | String | 是 | 868810166 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| file | FileItem | 是 | C:/Users/Desktop/222.txt | 文件内容。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| media\_id | String | #iAEHAqRmaWxlA6 | 文件的唯一标识media\_id。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/file/upload/single?access_token=ACCESS_TOKEN&agent_id=AGENT_ID&file_size=FILE_SIZE
```

**请求示例（JAVA SDK）**

```
OapiFileUploadSingleRequest request = new OapiFileUploadSingleRequest();
request.setFileSize(45L);
request.setAgentId("83642");
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/file/upload/single?"+ WebUtils.buildQuery(request.getTextParams(),"utf-8"));
// 必须重新new一个请求
request = new OapiFileUploadSingleRequest();
request.setFile(new FileItem("C:/Users/Desktop/222.txt"));
OapiFileUploadSingleResponse response = client.execute(request,access_token);
System.out.println(response.getBody());
```

**请求示例（curl）**

```
curl --location --request POST 'https://oapi.dingtalk.com/file/upload/single?agent_id=AGENTID&file_size=FILESIZE&access_token=ACCESSTOKEN' \
--form 'file=@"C:/Users/Desktop/222.txt"'
```

**请求示例（PHPCurl）**

```
<?php

$curl = curl_init();

curl_setopt_array($curl, array(

  CURLOPT_URL => 'https://oapi.dingtalk.com/file/upload/single?agent_id=AGENTID&file_size=FILESIZE&access_token=ACCESSTOKEN',

  CURLOPT_RETURNTRANSFER => true,

  CURLOPT_ENCODING => '',

  CURLOPT_MAXREDIRS => 10,

  CURLOPT_TIMEOUT => 0,

  CURLOPT_FOLLOWLOCATION => true,

  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

  CURLOPT_CUSTOMREQUEST => 'POST',

  CURLOPT_POSTFIELDS => array('file'=> new CURLFILE('C:/Users/Desktop/222.txt')),

));

$response = curl_exec($curl);

curl_close($curl);

echo $response;
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "media_id": "#iAEHAqRmaWxlA6h5dW5kaXNrMATOCxdnqwXNBsYGzQVPB85fV3gDCM0BlA"
}
```
