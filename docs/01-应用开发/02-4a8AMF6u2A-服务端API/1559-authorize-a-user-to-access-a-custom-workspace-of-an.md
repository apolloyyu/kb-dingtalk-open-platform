---
title: "授权用户访问企业的自定义空间"
source_url: "https://open.dingtalk.com/document/development/authorize-a-user-to-access-a-custom-workspace-of-an"
namespace: "development"
slug: "authorize-a-user-to-access-a-custom-workspace-of-an"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 授权用户访问企业的自定义空间"
doc_id: "sGCnOjhdFi"
updated_at: "2026-08-25 09:38:16"
---

> Source: https://open.dingtalk.com/document/development/authorize-a-user-to-access-a-custom-workspace-of-an
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 授权用户访问企业的自定义空间
> Updated: 2026-08-25 09:38:16

# 授权用户访问企业的自定义空间

调用本接口授权企业下指定人员访问其使用的自定义空间。授权类型包括上传和下载， 预览权限等同于下载权限。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[添加权限](0681-add-permissions-file.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/cspace/grant_custom_space`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| agent\_id | String | 否 | 123 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| domain | String | 是 | aa | 企业内部调用时传入，授权访问该domain的自定义空间，该值来自[添加空间](0652-add-space.md)接口参数。 |
| type | String | 是 | add | 权限类型：   - **add**：上传 - **download**：下载 - **delete**：删除 |
| userid | String | 是 | user123 | 授权的企业用户userid。 |
| path | String | 否 | /test | 授权访问的路径，如授权访问所有文件传“/”。  例如授权访问/doc文件夹传“/doc/” ，需要使用utf-8 urlEncode。  **[!NOTE]**  type为add时必须传递。 |
| fileids | String | 否 | 123 | 授权访问的文件ID列表，多个文件之间用英文逗号隔开，如“fileId1,fileId2”。  **[!NOTE]**  type为download时必须传递。 |
| duration | Number | 是 | 30 | 权限有效时间，有效范围为0~3600秒，超出此范围或不传默认为30秒。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/cspace/grant_custom_space?access_token=ACCESS_TOKEN&agent_id=123&domain=aa&type=add&userid=1234&path=/test&fileids=123&duration=30
```

- 授权上传，传入需要上传的路径。如在根目录下上传一个文件：

  ```
  https://oapi.dingtalk.com/cspace/grant_custom_space?access_token=ACCESS_TOKEN&domain=preview&type=add&userid=USERID&path=/
  ```
- 授权下载，传入需要下载的文件id列表。如授权下载xxx和yyy两个文件：

  ```
  https://oapi.dingtalk.com/cspace/grant_custom_space?access_token=ACCESS_TOKEN&domain=preview&type=download&userid=USERID&fileids=xxx,yyy
  ```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/cspace/grant_custom_space");
OapiCspaceGrantCustomSpaceRequest req = new OapiCspaceGrantCustomSpaceRequest();
req.setAgentId("123");
req.setDomain("aa");
req.setType("add");
req.setUserid("1234");
req.setPath("/test");
req.setFileids("123");
req.setDuration(30L);
req.setHttpMethod("GET");
OapiCspaceGrantCustomSpaceResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok"
}
```
