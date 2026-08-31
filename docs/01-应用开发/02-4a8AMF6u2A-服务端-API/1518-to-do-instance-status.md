---
title: "更新实例状态"
source_url: "https://open.dingtalk.com/document/development/to-do-instance-status"
namespace: "development"
slug: "to-do-instance-status"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 更新实例状态"
doc_id: "sml9gsxb6m"
updated_at: "2026-08-25 09:37:56"
---

> Source: https://open.dingtalk.com/document/development/to-do-instance-status
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 更新实例状态
> Updated: 2026-08-25 09:37:56

# 更新实例状态

调用本接口，更新实例状态。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新实例状态](0514-update-instance-status.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | UpdateProcessInstanceRequest | 否 |  | 请求对象。 |
| agentid | Number | 否 | 111 | 应用的agentid。   - 企业内部应用可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。 - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| process\_instance\_id | String | 是 | proc | 审批实例ID，由[创建实例](1517-initiate-an-approval-process-without-a-process.md)接口返回。 |
| status | String | 是 | COMPLETED | 实例状态：   - **COMPLETED**：结束审批流 - **TERMINATED**：终止审批流 |
| result | String | 是 | agree | 实例结果：   - 实例状态是**COMPLETED**，必须设置代表以下含义。    - **agree**：同意   - **refuse**：拒绝 - 实例状态为**TERMINATED，**必须设置代表含义，result取值**agree**和**refuse**均代表撤销审批流。 |
| cancel\_running\_task | Boolean | 否 | true | 取消任务。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 65v5c56q2wv9 | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request":{
    "result":"agree",
    "agentid":"111",
    "process_instance_id":"proc",
    "cancel_running_task":true,
    "status":"COMPLETED"
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/update");
OapiProcessWorkrecordUpdateRequest req = new OapiProcessWorkrecordUpdateRequest();
UpdateProcessInstanceRequest obj1 = new UpdateProcessInstanceRequest();
obj1.setAgentid(111L);
obj1.setProcessInstanceId("proc");
obj1.setStatus("COMPLETED");
obj1.setResult("agree");
obj1.setCancelRunningTask(true);
req.setRequest(obj1);
OapiProcessWorkrecordUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "request_id": "65v5c56q2wv9"
}
```

## 错误码

| **错误码（errorcode）** | **错误码描述（errmsg）** | **错误原因** | **解决方案** |
| --- | --- | --- | --- |
| 43007 | 需要授权 | access\_token不正确 | 请确认access\_token是否正确 |
| 40056 | 无效的微应用ID | 微应用ID参数错误 | 请确认微应用ID是否正确 |
| 40083 | 无效的suiteKey | 应用suiteKey参数错误 | 请确认应用suiteKey是否正确 |
| -1 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400001 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 8100017 | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 实例ID（process\_instance\_id）参数不正确 | 实例ID（process\_instance\_id）必须是[创建实例](1517-initiate-an-approval-process-without-a-process.md)接口返回的process\_instance\_id值，不能使用官方审批流的实例值 |
| 810003 | 审批流的表单格式错误 | 审批流的表单格式错误 | 请参照[创建实例](1517-initiate-an-approval-process-without-a-process.md)中「支持的表单参数」部分进行传值 |
| 820008 | 审批系统错误，原因为【审批表单已被管理员修改】 | 没有传result参数 | 更新审批单实例时，请传入result值后，再尝试 |
