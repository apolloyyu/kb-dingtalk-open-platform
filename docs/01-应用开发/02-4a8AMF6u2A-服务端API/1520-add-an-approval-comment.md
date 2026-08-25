---
title: "添加审批评论"
source_url: "https://open.dingtalk.com/document/development/add-an-approval-comment"
namespace: "development"
slug: "add-an-approval-comment"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 添加审批评论"
doc_id: "ccTcPAeZLJ"
updated_at: "2026-08-25 09:37:43"
---

> Source: https://open.dingtalk.com/document/development/add-an-approval-comment
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 添加审批评论
> Updated: 2026-08-25 09:37:43

# 添加审批评论

调用本接口对审批实例添加评论。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[添加审批评论](0500-official-approval-adds-approval-comments.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/instance/comment/add`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

## Body参数

> **[!NOTE]**
>
> 添加审批评论附件需将文件上传至审批钉盘空间，可以获取到接口参数file\_type，file\_name，file\_id，file\_size。获取方式如下：
>
> 1. 调用[获取审批钉盘空间信息](1534-query-the-space-of-an-approval-nail.md)，获取钉盘空间的上传权限，并获取space\_id。
> 2. 使用参数space\_id，调用H5微应用[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端JSAPI/0821-upload-attachment-to-nail-plate-select-file-from-nail-plate-h5.md)或者小程序[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端JSAPI/0742-upload-attachment-to-nail-plate-select-file-from-nail-plate.md)后获取钉盘附件file的信息。

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | AddCommentRequest | 是 |  | 请求对象。 |
| process\_instance\_id | String | 是 | 88c2f806-xxxx | 审批实例ID，调用[获取审批实例ID列表](1531-operation-to-retrieve-a-list-of.md)接口获取。 |
| file | File | 否 |  | 文件。 |
| attachments | Attachment[] | 否 |  | 附件列表。 |
| space\_id | String | 否 | 232323 | 钉盘空间ID，调用[获取审批钉盘空间信息](1534-query-the-space-of-an-approval-nail.md)接口获取。 |
| file\_type | String | 否 | file | 文件类型。 |
| file\_name | String | 否 | 打卡证明 | 文件名称。 |
| file\_id | String | 否 | B1oQixxxx | 文件ID。 |
| file\_size | String | 否 | 1024 | 文件大小。 |
| photos | String[] | 否 | ["https://url1":"https://url1"] | 图片URL列表。 |
| text | String | 是 | 测试 | 评论的内容。 |
| comment\_userid | String | 是 | user123 | 评论人的userid。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 返回结果。 |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | ocnl8hjqmu3y | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/instance/comment/add?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "comment_userid": "user123",
    "process_instance_id": "88c2f806-316d-4683-ba30-xxxxx",
    "text": "测试",
    "file": {
      "attachments": [
        {
          "space_id": "22331",
          "file_size": "1024",
          "file_id": "B1oQixxxx",
          "file_name": "打卡证明",
          "file_type": "file"
        }
      ],
      "photos": ["https://url1"]
    }
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/instance/comment/add");
OapiProcessInstanceCommentAddRequest req = new OapiProcessInstanceCommentAddRequest();
AddCommentRequest commentRequest = new AddCommentRequest();
commentRequest.setProcessInstanceId("88c2f806-316d-4683-ba30-xxxx");
commentRequest.setCommentUserid("user456");
commentRequest.setText("测试");
req.setRequest(commentRequest);
OapiProcessInstanceCommentAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": true,
  "success": true,
  "request_id": "ocnl8hjqmu3y"
}
```
