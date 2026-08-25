---
title: "批量取消待办"
source_url: "https://open.dingtalk.com/document/development/cancel-multiple-tasks"
namespace: "development"
slug: "cancel-multiple-tasks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 批量取消待办"
doc_id: "ImKC7bJg2g"
updated_at: "2026-08-25 09:37:59"
---

> Source: https://open.dingtalk.com/document/development/cancel-multiple-tasks
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 批量取消待办
> Updated: 2026-08-25 09:37:59

# 批量取消待办

调用本接口实现在或签等场景下，批量将正在运行中的待办事项设置为CANCELED。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/taskgroup/cancel`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | UpdateTaskRequest | 是 |  | 请求对象。 |
| agentid | Number | 是 | 111 | 应用标识。可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。  image |
| process\_instance\_id | String | 是 | EF6YJL35 | 实例ID，由[创建实例](1515-initiate-an-approval-process-without-a-process.md)接口获取。 |
| activity\_id | String | 是 | 1111 | 待办组ID，需要在调用[查询待办列表](1522-query-a-user-s-to-do-items.md)接口时，主动设置该值。 |
| activity\_id\_list | String[] | 否 | ["1111","2222"] | 待办组ID列表，用于批量取消。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| request\_id | String | 146262d9p0xmi | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/taskgroup/cancel?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "agentid": 111,
    "process_instance_id": "proc-zzz",
    "activity_id": "1111",
    "activity_id_list": [
      "1111",
      "2222"
    ]
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/taskgroup/cancel");
OapiProcessWorkrecordTaskgroupCancelRequest req = new OapiProcessWorkrecordTaskgroupCancelRequest();
UpdateTaskRequest obj1 = new UpdateTaskRequest();
obj1.setAgentid(111L);
obj1.setProcessInstanceId("proc-zzz");
obj1.setActivityId("1111");
ArrayList<String> activityIdList = new ArrayList<>();
activityIdList.add("1111");
activityIdList.add("2222");
obj1.setActivityIdList(activityIdList);
req.setRequest(obj1);
OapiProcessWorkrecordTaskgroupCancelResponse rsp = client.execute(req, "access_token");
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "request_id": "146262d9p0xmi"
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
| 820004 | 流程实例不存在 | 流程实例参数错误 | 请确认流程实例参数是否正确 |
| 8100017 | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，审批实例或者模板参数错误 | 实例ID（process\_instance\_id）必须是[创建实例](1515-initiate-an-approval-process-without-a-process.md)接口返回的process\_instance\_id值，不能使用官方审批流的实例值。 |

## 常见问题

**Q：什么场景下调用此接口？**

在或签等场景下，开发者需要批量把正在运行中的待办事项设置为CANCELED，可以调用此接口。

**Q：从哪里获取activity\_id？**

在调用创建待办事项接口时，开发者需要主动设置此activity\_id，当做任务组id。通常来说，可以使用流程节点的id当做此activity\_id。
