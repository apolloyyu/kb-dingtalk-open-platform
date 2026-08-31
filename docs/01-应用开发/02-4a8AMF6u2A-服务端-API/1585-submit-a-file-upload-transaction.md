---
title: "提交文件上传事务"
source_url: "https://open.dingtalk.com/document/development/submit-a-file-upload-transaction"
namespace: "development"
slug: "submit-a-file-upload-transaction"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 提交文件上传事务"
doc_id: "LXuY7KVGGN"
updated_at: "2026-08-25 09:38:41"
---

> Source: https://open.dingtalk.com/document/development/submit-a-file-upload-transaction
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 提交文件上传事务
> Updated: 2026-08-25 09:38:41

# 提交文件上传事务

本接口为文件分块上传最后一步，提交本次分块上传事务，默认情况下，系统会删除超过 24 小时没有提交的分块文件上传事务。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件上传信息](0674-obtain-file-upload-informations.md)和[提交文件](0675-submittal-file.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/file/upload/transaction`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| file\_size | Integer | 是 | 15 | 文件大小，单位byte。分块最小需大于100KB，最大不超过8M |
| agent\_id | String | 是 | 868810166 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| chunk\_numbers | Integer | 是 | 3 | 文件总块数。 |
| upload\_id | String | 是 | 99F0Bxxxxxx | 上传事务ID。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| media\_id | String | #iAEHAqRxxxxx | 文件的唯一标识media\_id。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/file/upload/transaction?access_token=ACCESS_TOKEN&agent_id=AGENT_ID&file_size=FILE_SIZE&chunk_numbers=CHUNK_NUMBERS
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/file/upload/transaction");
OapiFileUploadTransactionRequest request = new OapiFileUploadTransactionRequest();
request.setAgentId("13xxxxx01");
request.setFileSize(1000L);
request.setChunkNumbers(1L);
request.setUploadId("99F0F6DBB55A4C82822268192Bxxxxxx_0#iAEAAqRmxxxxxxxxxxxxxxxxxx");
request.setHttpMethod("GET");
OapiFileUploadTransactionResponse response = client.execute(request,accessToken);
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "media_id": "#iAEHAqRmaWxlA6h5dW5kaXNrMATOCxdnqwXNBsYGzQVPB85fV3gDCM0BlA"
}
```
