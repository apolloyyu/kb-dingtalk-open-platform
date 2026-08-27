---
title: "上传文件块"
source_url: "https://open.dingtalk.com/document/development/upload-file-blocks"
namespace: "development"
slug: "upload-file-blocks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 上传文件块"
doc_id: "UWRf3DcLuL"
updated_at: "2026-08-25 09:38:40"
---

> Source: https://open.dingtalk.com/document/development/upload-file-blocks
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件上传 > 上传文件块
> Updated: 2026-08-25 09:38:40

# 上传文件块

本接口为文件分块上传中间环节，传输文件块，除最后一块外每块的大小不得小于100KB，最大不超过超过8M。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 请保证自己的机器有足够的出口带宽，否则可能导致上传异常缓慢。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件上传信息](0674-obtain-file-upload-informations.md)和[提交文件](0675-submittal-file.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/file/upload/chunk`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| upload\_id | String | 是 | lAzPDgCwxxxx | 上传事务ID。 |
| agent\_id | String | 是 | 868810166 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| chunk\_sequence | Long | 是 | 1 | 文件块号，从1开始计数。  **[!NOTE]**  开启分块上传事务接口中，将文件分为几块，就循环调用本接口几次，直到最后一块文件上传成功后，再调用提交文件上传事务接口，获取media\_id。 |

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
POST /file/upload/chunk?access_token=ACCESSTOKEN&agent_id=AGENTID&upload_id=UPLOADID&chunk_sequence=1 HTTP/1.1
Host:oapi.dingtalk.com
Content-Type: multipart/form-data;
```

**请求示例（JAVA SDK）**

```
OapiFileUploadChunkRequest request = new OapiFileUploadChunkRequest();
request.setAgentId("13xxxxx01");
request.setChunkSequence(1L);
request.setUploadId("99F0F6DBB55A4Cxxxx63FCM4AAXTG");
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/file/upload/chunk?"+WebUtils.buildQuery(request.getTextParams(),"utf-8"));
request = new OapiFileUploadChunkRequest();
request.setFile(new FileItem("/Users/mxh/Downloads/test.png"));
OapiFileUploadChunkResponse response = client.execute(request,accessToken);
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok"
}
```
