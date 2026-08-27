---
title: "授权下载审批钉盘文件"
source_url: "https://open.dingtalk.com/document/development/approve-nail-disk-file-authorization"
namespace: "development"
slug: "approve-nail-disk-file-authorization"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 授权下载审批钉盘文件"
doc_id: "yakmBajb86"
updated_at: "2026-08-25 09:37:49"
---

> Source: https://open.dingtalk.com/document/development/approve-nail-disk-file-authorization
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 授权下载审批钉盘文件
> Updated: 2026-08-25 09:37:49

# 授权下载审批钉盘文件

调用本接口，根据钉盘空间spaceId和文件fileId对钉盘文件进行授权审批钉盘空间下载权限。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[授权下载审批钉盘文件](0504-download-the-approval-nail-file.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/dentry/auth`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | GrantCspaceRequestV2 | 否 |  | 请求对象。 |
| file\_infos | FileInfo[] | 是 |  | 授权的钉盘文件信息列表。 |
| space\_id | Number | 是 | 22331 | 钉盘空间spaceId。 |
| file\_id | String | 是 | B1oQixxxx | 文件ID。  **[!NOTE]**  只支持授予审批附件组件中文件的下载权限。 |
| userid | String | 是 | user123 | 授权的用户userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 返回结果。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | ocnl8hjqmu3y | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/dentry/auth?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "file_infos": [
      {
        "file_id": "B1oQixxxx",
        "space_id": 22331
      }
    ],
    "userid": "user123"
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/dentry/auth");
OapiProcessDentryAuthRequest req = new OapiProcessDentryAuthRequest();
GrantCspaceRequestV2 grantCspaceRequestV2 = new GrantCspaceRequestV2();
grantCspaceRequestV2.setUserid("user123");
FileInfo fileInfo = new FileInfo();
fileInfo.setFileId("B1oQixxxx");
fileInfo.setSpaceId(22331L);
grantCspaceRequestV2.setFileInfos(Arrays.asList(fileInfo));
req.setRequest(grantCspaceRequestV2);
OapiProcessDentryAuthResponse rsp = client.execute(req, orgToken);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": true,
  "request_id": "ocnl8hjqmu3y"
}
```
