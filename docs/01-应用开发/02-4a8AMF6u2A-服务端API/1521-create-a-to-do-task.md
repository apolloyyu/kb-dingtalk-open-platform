---
title: "创建待办事项"
source_url: "https://open.dingtalk.com/document/development/create-a-to-do-task"
namespace: "development"
slug: "create-a-to-do-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 创建待办事项"
doc_id: "tzZP7zAP7H"
updated_at: "2026-08-25 09:37:58"
---

> Source: https://open.dingtalk.com/document/development/create-a-to-do-task
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 创建待办事项
> Updated: 2026-08-25 09:37:58

# 创建待办事项

调用本接口把待办事项的审批节点信息同步到钉钉待办。一个待办实例下最多创建100个待办事项。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/process/workrecord/task/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | SaveTaskRequest | 是 |  | 请求对象。 |
| agentid | Number | 否 | 1234 | 应用标识。可在[开发者后台](https://open-dev.dingtalk.com/)的应用详情页获取。  image |
| process\_instance\_id | String | 是 | proc-zzz | 审批实例ID，由[创建实例](1515-initiate-an-approval-process-without-a-process.md)接口获取。 |
| activity\_id | String | 否 | activity-zzz | 节点ID。 |
| tasks | TaskTopVo[] | 是 |  | 待办事项列表。 |
| userid | String | 是 | manager | 待办事项执行人的userid。 |
| url | String | 是 | https://www.dingtalk.com | 待办事项跳转URL。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 3q4cc4wndken | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 成功 | 返回码描述。 |
| tasks | TaskTopVo[] |  | 待办事项i列表。 |
| task\_id | Number | 111 | 待办事项ID。 |
| userid | String | user123 | 待办事项执行人的userid。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/process/workrecord/task/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "request": {
    "agentid": "11",
    "process_instance_id": "proc-zzz",
    "activity_id": "activity-zzz",
    "tasks": [
      {
        "userid": "manager",
        "url": "https://www.dingtalk.com"
      }
    ]
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/process/workrecord/task/create");
OapiProcessWorkrecordTaskCreateRequest req = new OapiProcessWorkrecordTaskCreateRequest();
SaveTaskRequest obj1 = new SaveTaskRequest();
obj1.setAgentid(11L);
obj1.setProcessInstanceId("proc-zzz");
obj1.setActivityId("activity-zzz");
List<TaskTopVo> list3 = new ArrayList<TaskTopVo>();
TaskTopVo obj4 = new TaskTopVo();
list3.add(obj4);
obj4.setUserid("manager");
obj4.setUrl("https://www.dingtalk.com");
obj1.setTasks(list3);
req.setRequest(obj1);
OapiProcessWorkrecordTaskCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "request_id": "3q4cc4wndken"
  "errcode":"0",
  "errmsg":"成功",
  "tasks":{
    "task_id":"",
    "userid":""
  }
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
| 820010 | 流程任务的数量到达上限 | 实例下的待办任务超过限制。 | 一个实例下，最多只能创建100个待办，请删除不需要的待办任务重试或新建实例。 |
| 820012 | 流程实例已完结，不能继续创建任务。 | 流程实例已完结，不能继续创建任务。 | 请确认审批实例ID是否正确。 |
| 820011 | 假流程并发创建任务和实例 | 创建待办事项并发错误 | 请控制接口调用频率，稍后重试。 |
| 820004 | 审批实例不存在 | 审批实例ID参数错误 | 请确认审批实例ID是否正确。 |
| 8100017 | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 审批实例ID参数错误 | 实例ID（process\_instance\_id）必须是[创建实例](1515-initiate-an-approval-process-without-a-process.md)接口返回的process\_instance\_id值，不能使用官方审批流的实例值。 |
| 820008 | 系统繁忙，请稍后再试 | 参数URL过长 | 缩短URL参数的长度。 |

## 常见问题

**Q：调用这个接口后，会有什么效果**？

调用该接口后，会在对应待办执行人的钉钉审批应用“我审批的”页面，产生一条审批单记录。同时，在钉钉待办页面，也是出现对应的待办卡片。

**Q：这里又传了一个url，和创建审批实例接口中的url有什么区别？**

创建审批实例接口里的url，实现的是钉钉审批应用里的审批单跳转。这个接口里的url，实现的是钉钉待办页面，对应的待办卡片的跳转。两种跳转场景不同。需要注意的是，钉钉的待办页面，也同时支持移动端和PC端，所以这个接口里传的url参数，它所对应的页面也要适配好移动端和PC端。

**Q：同一个页面，前端怎么样可以判断请求来自PC端还是移动端？**

钉钉的jsapi可以判断，如下图：

![JSAPI](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2834199951/p162125.png)
