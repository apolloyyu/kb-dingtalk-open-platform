---
title: "删除模板"
source_url: "https://open.dingtalk.com/document/development/delete-a-template"
namespace: "development"
slug: "delete-a-template"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > OA审批 > 删除模板"
doc_id: "ejrvhRT7s8"
updated_at: "2026-08-25 09:37:54"
---

> Source: https://open.dingtalk.com/document/development/delete-a-template
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > OA审批 > 删除模板
> Updated: 2026-08-25 09:37:54

# 删除模板

调用本接口删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[删除模板](0512-self-owned-approval-deletion-template.md)接口，已接入用户不受影响。

> **[!NOTE]**
>
> - 企业内部应用，只删除模板，不删除通过模板创建的实例和待办任务。
> - 第三方企业应用，删除模板，同时删除使用该模板创建的实例和待办任务。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/delete`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | DeleteProcessRequest | 是 |  | 请求对象。 |
| agentid | Number | 是 | 123456 | 应用标识。可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。应用的agentid。   - 企业内部应用可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。  image - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。   **[!IMPORTANT]**  如果是第三方企业应用必须指定该参数。 |
| process\_code | String | 是 | PROC-7C8BB7AE-E758-4Axxxx | 审批模板唯一码，调用[创建或更新审批模板](1532-save-approval-template.md)接口获取process\_code参数值。 |
| clean\_running\_task | Boolean | 否 | true | 是否清理运行中的任务：   - **true**：清理 - **false**（默认）：不清理 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 成功标识。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码信息。 |
| request\_id | String | 6f9h396s8c | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/delete?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "agentid": 123456,
    "process_code": "PROC-7C8BB7AE-E758-4A96-9375-27CFD376B19C",
    "clean_running_task": true
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/delete");
OapiProcessDeleteRequest req = new OapiProcessDeleteRequest();
DeleteProcessRequest obj1 = new DeleteProcessRequest();
obj1.setAgentid(123456L);
obj1.setProcessCode("PROC-7C8BB7AE-E758-4A96-9375-27CFD376B19C");
obj1.setCleanRunningTask(true);
req.setRequest(obj1);
OapiProcessDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "request_id": "pqclbhtxdqde"
}
```

## 错误码

| **错误码（errorcode）** | **错误码描述（errmsg）** | **错误原因** | **解决方案** |
| --- | --- | --- | --- |
| 43007 | 需要授权 | access\_token不正确 | 请确认access\_token是否正确 |
| 8100017 | 没有访问权限 | 没有访问审批表单的权限 | 请确认表单code参数是否正确 |
| 40056 | 无效的微应用ID | 微应用ID参数错误 | 请确认微应用ID是否正确 |
| 40083 | 无效的suiteKey | 应用suiteKey参数错误 | 请确认应用suiteKey是否正确 |
| -1 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 400001 | 系统繁忙 | 系统繁忙 | 请稍后重试 |
| 820004 | 模板不存在 | 模板code参数错误 | 请确认表单code参数是否正确 |
