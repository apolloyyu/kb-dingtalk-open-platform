---
title: "授权预览审批附件"
source_url: "https://open.dingtalk.com/document/development/preview-authorization-attachment"
namespace: "development"
slug: "preview-authorization-attachment"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 授权预览审批附件"
doc_id: "OZO8mhzxQZ"
updated_at: "2026-08-25 09:37:48"
---

> Source: https://open.dingtalk.com/document/development/preview-authorization-attachment
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 授权预览审批附件
> Updated: 2026-08-25 09:37:48

# 授权预览审批附件

调用本接口授权预览审批附件。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[授权预览审批附件](0503-official-authorized-preview-approval-attachment.md)接口，已接入用户不受影响。

> **[!IMPORTANT]**
>
> 此接口需配合钉盘JSAPI使用，调用本接口只支持授予审批附件组件中文件的预览权限，不支持授予审批评论附件的预览权限。
>
> 使用方法如下：
>
> 1. 调用[获取审批钉盘空间信息](1536-query-the-space-of-an-approval-nail.md)接口，获取审批钉盘空间space\_id。
> 2. 根据space\_id，调用H5微应用[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0784-upload-attachment-to-nail-plate-select-file-from-nail-plate-h5.md)或者小程序[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0705-upload-attachment-to-nail-plate-select-file-from-nail-plate.md)接口，获取上传附件的信息。
> 3. 调用[发起审批实例](1519-oa-approval-initiates-approval-instances.md)接口，获取审批实例process\_instance\_id。
> 4. 根据上述获取信息，调用本文接口，授权用户审批附件预览权限。每一次预览审批附件前，都需要调用该接口进行授权。
> 5. 调用H5微应用[预览钉盘文件](../03-Ogu5SlPY4t-客户端-JSAPI/0785-preview-nail-plate-file.md)或者小程序[钉盘文件预览](../03-Ogu5SlPY4t-客户端-JSAPI/0704-nail-plate-file-preview.md)接口，进行预览。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/cspace/preview`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | GrantCspaceRequest | 是 |  | 请求信息。 |
| agentid | Number | 否 | 868810166 | 应用标识。可在开发者后台的应用详情页获取。 |
| process\_instance\_id | String | 是 | a17444d1-075b-4a4d-xxxx | 实例ID：   - 企业内部应用，通过[获取审批实例ID列表](1533-operation-to-retrieve-a-list-of.md)接口获取。 - 第三方企业应用，通过推送的审批事件中获取，参考[biz\_type=22](../04-LFcRvVD08N-事件订阅/0363-approval-events-3.md)。 |
| file\_id | String | 是 | 11 | 审批附件ID。  **[!NOTE]**  file\_id必须与发起审批实例中附件组件中的文件fileId保持一致，否则出现无权限错误信息。 |
| userid | String | 是 | user123 | 授权允许预览附件的用户userid。 |
| fileid\_list | String[] | 否 | 123 | 附件ID列表，支持批量授权，最大列表长度：20。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | OK | 返回码描述。 |
| result | AppSpaceResponse |  | 授权结果。 |
| space\_id | Number | 1 | 审批所在的钉盘空间ID。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 3vp6ui8jeroa | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/cspace/preview?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request":{
    "agentid":868810166,
    "file_id":"11",
    "process_instance_id":"a17444d1-075b-4a4d-xxxx",
    "userid":"manager4220"
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/cspace/preview");
OapiProcessinstanceCspacePreviewRequest req = new OapiProcessinstanceCspacePreviewRequest();
GrantCspaceRequest grantCspaceRequest = new GrantCspaceRequest();
grantCspaceRequest.setAgentid(868810166L);
grantCspaceRequest.setProcessInstanceId("a17444d1-075b-4a4d-xxxx");
grantCspaceRequest.setFileId("11");
grantCspaceRequest.setUserid("manager4220");
req.setRequest(grantCspaceRequest);
OapiProcessinstanceCspacePreviewResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "result":{
    "space_id":"1"
  },
  "errcode":0,
  "request_id": "3vp6ui8jeroa"
}
```
