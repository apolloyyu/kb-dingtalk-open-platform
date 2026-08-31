---
title: "发送钉盘文件给指定用户"
source_url: "https://open.dingtalk.com/document/development/sends-a-file-to-a-specified-user"
namespace: "development"
slug: "sends-a-file-to-a-specified-user"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 发送钉盘文件给指定用户"
doc_id: "uE3OPEwzXz"
updated_at: "2026-08-25 09:38:13"
---

> Source: https://open.dingtalk.com/document/development/sends-a-file-to-a-specified-user
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 发送钉盘文件给指定用户
> Updated: 2026-08-25 09:38:13

# 发送钉盘文件给指定用户

调用本接口将文件发送给指定用户，用户将收到以应用名义发送的一条文件消息。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[以应用身份发送文件给指定用户](0641-sends-a-storage-file-to-a-specified-user.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/cspace/add_to_single_chat`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| file\_name | String | 是 | 文件.pdf | 文件名包含扩展名，需要utf-8 urlEncode。 |
| media\_id | String | 是 | @123456 | 文件media\_id，调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口或者[提交文件](0675-submittal-file.md)接口获取。  **[!NOTE]**  参数需要utf-8 urlEncode处理。 |
| userid | String | 是 | 123456 | 文件接收人的userid。 |
| agent\_id | String | 是 | 123 | 文件发送者应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/cspace/add_to_single_chat?access_token=ACCESS_TOKEN&agent_id=AGENT_ID&userid=USERID&media_id=MEDIA_ID&file_name=FILE_NAME
```

请求正文

```
{
  "agent_id":"868810166",
  "file_name":"test",
  "media_id":"@lAzPxxxxs5xiBws",
  "userid":"manager4220"
}
```

**请求示例（JAVA SDK）**

```
OapiCspaceAddToSingleChatRequest request = new OapiCspaceAddToSingleChatRequest();
request.setAgentId("135xxx601");
request.setUserid("01376xxxxxx479");
request.setMediaId("#iAEAAqRmaWxxxxx863FCM4AAXTG");
request.setFileName("文件.pdf");
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/cspace/add_to_single_chat?"+WebUtils.buildQuery(request.getTextParams(),"utf-8"));
OapiCspaceAddToSingleChatResponse response = client.execute(request, accessToken);
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```
