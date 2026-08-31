---
title: "保存文件到自定义或审批钉盘空间"
source_url: "https://open.dingtalk.com/document/development/add-file-to-user-s-dingtalk-disk"
namespace: "development"
slug: "add-file-to-user-s-dingtalk-disk"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 保存文件到自定义或审批钉盘空间"
doc_id: "ap8rJR4LeS"
updated_at: "2026-08-25 09:38:14"
---

> Source: https://open.dingtalk.com/document/development/add-file-to-user-s-dingtalk-disk
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 保存文件到自定义或审批钉盘空间
> Updated: 2026-08-25 09:38:14

# 保存文件到自定义或审批钉盘空间

调用本接口，将文件保存到自定义钉盘空间或审批附件钉盘空间。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件上传信息](0674-obtain-file-upload-informations.md)和[提交文件](0675-submittal-file.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> - 调用该接口之前，不同的上传空间需要授权不同的上传权限：
>
>   - 自定义企业钉盘空间，需通过[添加权限](0681-add-permissions-file.md)接口进行授权。
>   - 企业审批附件钉盘空间，需通过[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口进行授权。
> - 文件不是保存到钉钉客户端的钉盘中，而是保存到自定义钉盘和审批附件钉盘。自定义钉盘和审批附件钉盘在钉钉客户端内不可见。
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：GET

**请求地址**：`https://oapi.dingtalk.com/cspace/add`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |
| agent\_id | String | 否 | 123 | 应用的AgentId。   - 企业内部应用可以在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可以调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| code | String | 是 | a6981a1df0c03297b70aa23a6db2ce65 | code值为应用免登授权码：   - [免登授权码](../03-Ogu5SlPY4t-客户端-JSAPI/0510-mini-program-free-login.md) - [获取微应用免登授权码](../03-Ogu5SlPY4t-客户端-JSAPI/0748-obtain-the-micro-application-exemption-authorization-code.md) |
| media\_id | String | 是 | @123 | 调用[单步文件上传](1582-single-step-file-upload.md)接口得到的media\_id。 |
| space\_id | String | 是 | 234 | 钉盘空间ID。 |
| folder\_id | String | 否 | 0 | 钉盘文件夹ID。  **[!IMPORTANT]**   - 如果**space\_id**是审批附件钉盘，**folder\_id**参数传0。 - 如果**space\_id**是自定义钉盘，该参数不传。 |
| name | String | 是 | test.pdf | 上传文件的名称，不能包含非法字符，需要utf-8 urlEncode。  **[!NOTE]**  必须带文件扩展名。 |
| overwrite | Boolean | 否 | true | 遇到同名文件是否覆盖。  若不覆盖，则会自动重命名本次新增的文件，默认为**false**不覆盖。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| dentry | String | {\"account\":\"X\",\"site\":0} | 文件的详细信息。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码详情。 |

## 示例

**请求示例（HTTP）**

```
GET https://oapi.dingtalk.com/cspace/add?access_token=ACCESS_TOKEN&agent_id=123&code=asdfwd&media_id=@123&folder_id=123&space_id=234&name=test&overwrite=true
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/cspace/add");
OapiCspaceAddRequest req = new OapiCspaceAddRequest();
req.setAgentId("923680251");
req.setCode("d56d81e69xxxxx");
req.setMediaId("$iAEKAqNxxxx");
req.setSpaceId("4226670592");
req.setName("iAEKAqNxxxx.jpg");
req.setOverwrite(true);
req.setHttpMethod("GET");
OapiCspaceAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":"0",
  "dentry":"{\"contentType\":\"document\",\"createTime\":1451560026000,\"creator\":{\"account\":\"X\",\"site\":0},\"extension\":\"txt\",\"id\":\"54301\",\"modifiedTime\":1451560026000,\"modifier\":{\"account\":\"X\",\"site\":0},\"name\":\"1.txt\",\"parentId\":0,\"path\":\"\/1.txt\",\"size\":9,\"type\":\"file\",\"version\":\"0\"}",
  "errmsg":"ok"
}
```
