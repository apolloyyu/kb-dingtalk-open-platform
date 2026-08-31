---
title: "创建企业内部应用H5微应用"
source_url: "https://open.dingtalk.com/document/development/create-an-h5-microapplication"
namespace: "development"
slug: "create-an-h5-microapplication"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 应用管理 > 创建企业内部应用H5微应用"
doc_id: "usM4n1Dxpm"
updated_at: "2026-08-25 09:39:04"
---

> Source: https://open.dingtalk.com/document/development/create-an-h5-microapplication
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 应用管理 > 创建企业内部应用H5微应用
> Updated: 2026-08-25 09:39:04

# 创建企业内部应用H5微应用

调用本接口创建H5微应用。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取企业所有应用列表](0864-obtains-a-list-of-all-enterprise-applications.md)接口，已接入用户不受影响。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**应用管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月24日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[创建企业内部应用](0861-create-an-h5-application-for-your-enterprise.md)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/microapp/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| appIcon | String | 是 | @lADPDfmVQafoVxxxx | H5微应用的图标。  需要调用[上传媒体文件](0646-upload-media-files.md)将图标上传到钉钉服务器后获取到的mediaId。 |
| appDesc | String | 是 | 钉钉H5微应用 | H5微应用的描述。 |
| homepageUrl | String | 是 | https://www.dingtalk.com | H5微应用的移动端主页，必须以http开头或https开头。 |
| pcHomepageUrl | String | 否 | https://www.dingtalk.com | H5微应用的PC端主页，必须以http开头或https开头，如果不为空则必须与homepageUrl的域名一致。 |
| ompLink | String | 否 | https://www.dingtalk.com | H5微应用的OA后台管理主页，必须以http开头或https开头。 |
| appName | String | 是 | H5微应用 | H5微应用的名称。长度限制为1~10个字符。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| agentid | Number | 1073399584 | H5微应用ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/microapp/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "appIcon":"@lADPDfmVQafoVxxxx",
  "homepageUrl":"https://www.dingtalk.com",
  "appName":"H5微应用",
  "appDesc":"钉钉H5微应用",
  "pcHomepageUrl":"https://www.dingtalk.com",
  "ompLink":"https://www.dingtalk.com"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/microapp/create");
OapiMicroappCreateRequest req = new OapiMicroappCreateRequest();
req.setAppIcon("@lADPDfmVQafoVxxxx");
req.setAppDesc("钉钉H5微应用");
req.setHomepageUrl("https://www.dingtalk.com");
req.setPcHomepageUrl("https://www.dingtalk.com");
req.setOmpLink("https://www.dingtalk.com");
req.setAppName("H5微应用");
OapiMicroappCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "agentid": "1073399584"
}
```
