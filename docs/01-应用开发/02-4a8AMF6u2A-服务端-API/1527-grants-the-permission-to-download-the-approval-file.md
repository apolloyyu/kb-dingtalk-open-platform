---
title: "下载审批附件"
source_url: "https://open.dingtalk.com/document/development/grants-the-permission-to-download-the-approval-file"
namespace: "development"
slug: "grants-the-permission-to-download-the-approval-file"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 下载审批附件"
doc_id: "ByjxOh0JoV"
updated_at: "2026-08-25 09:37:50"
---

> Source: https://open.dingtalk.com/document/development/grants-the-permission-to-download-the-approval-file
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 下载审批附件
> Updated: 2026-08-25 09:37:50

# 下载审批附件

调用本接口获取审批文件下载授权，并且生成下载链接。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[下载审批附件](0505-download-an-approval-attachment.md)接口，已接入用户不受影响。

## **接口说明**

- 如果审批单是手动在钉钉客户端发起的，手动选择本地文件作为附件，调用该接口获取的附件下载地址是这样的格式为`#zifgs49xxxxx.file`。

  需要与[获取单个审批实例详情](1535-get-details-single-approval-instance.md)接口结合使用，获取实例详情接口得到附件的fileName和fileType，按照本接口返回的`#zifgs49xxxxx.file`进行名称和后缀替换，该附件就可以正常打开了。
- 附件文件大小不能为0，比如txt文件等，不支持获取下载链接。
- 该接口只能下载审批附件钉盘空间的文件，无法下载到审批评论的附件。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/file/url/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | GrantCspaceRequest | 是 |  | 请求信息。 |
| process\_instance\_id | String | 是 | 123a-234bxx | 审批单实例id，调用[获取单个审批实例详情](1535-get-details-single-approval-instance.md)接口获取。 |
| file\_id | String | 是 | 123456 | 文件id，调用[获取单个审批实例详情](1535-get-details-single-approval-instance.md)接口获取。  **[!IMPORTANT]**  文件id是审批组件中上传的fileid（如下图所示），评论中上传的附件fileid暂不支持获取下载链接。  文件组件 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | AppSpaceResponse |  | 返回结果。 |
| file\_id | String | 26748422566 | 文件id。 |
| space\_id | Number | 3996960664 | 文件spaceId。 |
| download\_uri | String | http://lippi-space-zjk.oss-cn-zhangjiakou.aliyuncs.com/xxxxx | 文件下载地址。  **[!NOTE]**  文件下载地址有效期15分钟。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码的描述。 |
| success | Boolean | true | 调用是否成功。 |
| request\_id | String | v1lkp9inb6f4 | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/file/url/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request":{
    "process_instance_id":"PROC-XXX-XXX",
    "file_id":"26748422566"
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/file/url/get");
OapiProcessinstanceFileUrlGetRequest req = new OapiProcessinstanceFileUrlGetRequest();
GrantCspaceRequest obj1 = new GrantCspaceRequest();
obj1.setProcessInstanceId("PROC-XXX-XXX");
obj1.setFileId("123456");
req.setRequest(obj1);
OapiProcessinstanceFileUrlGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "download_uri": "http://lippi-space-zjk.oss-cn-zhangjiakou.aliyuncs.com/xxxxx",
    "file_id": "26748422566",
    "space_id": 3996960664
  },
  "success": true,
  "request_id": "41zxbpy0rmbq"
}
```
