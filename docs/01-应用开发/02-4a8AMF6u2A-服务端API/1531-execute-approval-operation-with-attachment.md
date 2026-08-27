---
title: "同意或拒绝审批任务"
source_url: "https://open.dingtalk.com/document/development/execute-approval-operation-with-attachment"
namespace: "development"
slug: "execute-approval-operation-with-attachment"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 同意或拒绝审批任务"
doc_id: "uC2iCBdMvY"
updated_at: "2026-08-25 09:37:51"
---

> Source: https://open.dingtalk.com/document/development/execute-approval-operation-with-attachment
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 同意或拒绝审批任务
> Updated: 2026-08-25 09:37:51

# 同意或拒绝审批任务

调用本接口根据指定模板ID、实例ID、审批节点ID和审批人，对单个审批任务进行处理。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[同意或拒绝审批任务](0506-approve-or-reject-the-approval-task.md)接口，已接入用户不受影响。

## 使用说明

审批流程可以包含多个审批节点，单个审批节点可能包含一个或多个审批任务。操作单个审批任务，不代表审批流程结束。

- 审批流程只有一个审批人，对单个审批任务操作同意或拒绝，审批流程结束。

  ![一个审批人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1064156361/p349526.png)
- 审批流程有多个审批人，整个审批流程受多个任务影响。

  - 对单个审批任务操作拒绝，审批流程结束。
  - 对单个审批任务操作同意，审批流程转到下一个审批人。

    ![会签或签](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1064156361/p349521.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/instance/execute`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | ExecuteTaskRequest | 否 |  | 请求参数。 |
| process\_instance\_id | String | 是 | 88c2fxxxxx | 审批实例id，调用[获取审批实例ID列表](1533-operation-to-retrieve-a-list-of.md)接口获取。 |
| remark | String | 否 | 同意 | 审批意见，可为空。 |
| result | String | 是 | agree | 审批操作，取值。   - **agree**：同意 - **refuse**：拒绝 |
| file | File | 否 |  | 文件。 |
| attachments | Attachment[] | 否 |  | 附件列表。 |
| space\_id | String | 否 | 22331 | 钉盘空间ID。 |
| file\_size | String | 否 | 1024 | 文件大小。 |
| file\_id | String | 否 | B1oQixxxx | 文件ID。 |
| file\_name | String | 否 | 打卡证明 | 文件名称。 |
| file\_type | String | 否 | file | 文件类型。 |
| photos | String[] | 否 | ["https://url1","https://url1"] | 图片URL地址。 |
| actioner\_userid | String | 是 | user123 | 操作人userid，调用[获取单个审批实例详情](1535-get-details-single-approval-instance.md)接口获取。 |
| task\_id | Number | 是 | 67583405630 | 任务节点id，调用[获取单个审批实例详情](1535-get-details-single-approval-instance.md)接口获取。 |

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
POST https://oapi.dingtalk.com/topapi/process/instance/execute?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "actioner_userid": "manager4220",
    "process_instance_id": "88c2f806-316d-4683-ba30-xxxxx",
    "remark": "同意",
    "result": "agree",
    "task_id": 67583405630,
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
      "photos": ["https://url1","https://url1"]
    }
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/instance/execute");
OapiProcessinstanceExecuteV2Request req = new OapiProcessinstanceExecuteV2Request();
ExecuteTaskRequest executeTaskRequest = new ExecuteTaskRequest();
executeTaskRequest.setProcessInstanceId("88c2f806-316d-4683-ba30-xxxx");
executeTaskRequest.setActionerUserid("manager");
executeTaskRequest.setTaskId(67583405630L);
executeTaskRequest.setRemark("同意");
executeTaskRequest.setResult("agree");
req.setRequest(executeTaskRequest);
OapiProcessinstanceExecuteV2Response rsp = client.execute(req, orgToken);
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
