---
title: "获取审批钉盘空间信息"
source_url: "https://open.dingtalk.com/document/development/query-the-space-of-an-approval-nail"
namespace: "development"
slug: "query-the-space-of-an-approval-nail"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取审批钉盘空间信息"
doc_id: "1EDhejZaWH"
updated_at: "2026-08-25 09:37:47"
---

> Source: https://open.dingtalk.com/document/development/query-the-space-of-an-approval-nail
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 获取审批钉盘空间信息
> Updated: 2026-08-25 09:37:47

# 获取审批钉盘空间信息

调用本接口获取审批钉盘空间的ID并授予当前用户上传附件的权限。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，已接入用户不受影响。

建议开发者通过以下方式实现带附件的审批流程：

1. 调用**本接口**，获取钉盘空间的上传权限，并获取space\_id。
2. 使用参数space\_id，调用H5微应用[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0816-upload-attachment-to-nail-plate-select-file-from-nail-plate-h5.md)或者小程序[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0737-upload-attachment-to-nail-plate-select-file-from-nail-plate.md)后获取钉盘附件的信息。

   space\_id的使用说明：

   > **[!NOTE]**
   >
   > - 一个企业内审批附件钉盘spaceid是唯一的。
   > - 此接口有授权上传权限的作用，每次调用上传附件API接口前，建议使用上传操作人userid再调用一次本接口。
   > - 审批附件钉盘，属于企业钉盘的一部分，占用的是企业钉盘空间，但是审批附件钉盘空间和其中的文件在客户端内是不可见的。
3. 调用[发起审批实例](1519-oa-approval-initiates-approval-instances.md)传递附件信息。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/cspace/info`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| user\_id | String | 是 | abcdef | 用户的userid。 |
| agent\_id | String | 否 | 8345000 | 应用的agentid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | AppSpaceResponse |  | 返回结果。 |
| space\_id | Number | 3996960664 | 钉盘空间ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回描述。 |
| request\_id | String | 7jdciddady4z | 请求ID。 |
| success | Boolean | true | 调用是否成功。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/cspace/info?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "user_id":"manager4220",
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/cspace/info");
OapiProcessinstanceCspaceInfoRequest req = new OapiProcessinstanceCspaceInfoRequest();
req.setUserId("manager4220");
OapiProcessinstanceCspaceInfoResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "result": {
    "space_id": 3996960664
  },
  "success": true,
  "errmsg":"ok",
  "request_id": "7jdciddady4z"
}
```
