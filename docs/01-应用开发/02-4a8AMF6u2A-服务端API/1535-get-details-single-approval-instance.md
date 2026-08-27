---
title: "获取单个审批实例详情"
source_url: "https://open.dingtalk.com/document/development/get-details-single-approval-instance"
namespace: "development"
slug: "get-details-single-approval-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > OA审批 > 获取单个审批实例详情"
doc_id: "s8boCwon1a"
updated_at: "2026-08-25 09:37:41"
---

> Source: https://open.dingtalk.com/document/development/get-details-single-approval-instance
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > OA审批 > 获取单个审批实例详情
> Updated: 2026-08-25 09:37:41

# 获取单个审批实例详情

调用本接口根据审批实例ID，获取审批实例详情。详情包括审批表单信息、操作记录列表、操作人、抄送人、审批任务列表。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/processinstance/get`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| process\_instance\_id | String | 是 | 1a2b-3e4dxxxx | 审批实例ID   - 企业内部应用可通过[获取审批实例ID列表](1533-operation-to-retrieve-a-list-of.md)接口获取。 - 钉钉三方企业应用可以通过推送的审批事件中获取，参考[biz\_type=22](../04-LFcRvVD08N-事件订阅/0360-approval-events-3.md)。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 14bi2dzcz92s | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| process\_instance | ProcessInstanceTopVo |  | 审批实例详情。 |
| title | String | xx提交的请假申请 | 审批实例标题。 |
| create\_time | Date | 2020-09-05 16:48:30 | 开始时间。 |
| finish\_time | Date | 2020-09-05 16:48:30 | 结束时间。 |
| originator\_userid | String | manager1 | 发起人的userid。 |
| originator\_dept\_id | String | -1 | 发起人的部门。-1表示根部门。 |
| status | String | NEW | 审批状态：   - **NEW**：新创建 - **RUNNING**：审批中 - **TERMINATED**：被终止 - **COMPLETED**：完成 - **CANCELED**：取消 |
| approver\_userids | String[] | manager1 | 审批人userid。  **[!NOTE]**  在OA审批应用手动发起的审批单该参数才返回，使用接口发起的审批单该参数不返回。 |
| cc\_userids | String[] | ["manager1"] | 抄送人userid。 |
| result | String | agree | 审批结果：   - **agree**：同意 - **refuse**：拒绝   **[!NOTE]**  status为**COMPLETED**且result为**同意**时，表示审批单完结并审批通过。 |
| business\_id | String | 2017111111 | 审批实例业务编号。 |
| operation\_records | OperationRecordsVo[] |  | 操作记录列表。 |
| userid | String | manager1 | 操作人userid。 |
| date | Date | 2020-09-05 16:48:30 | 操作时间。 |
| operation\_type | String | EXECUTE\_TASK\_NORMAL | 操作类型：   - **EXECUTE\_TASK\_NORMAL**：正常执行任务 - **EXECUTE\_TASK\_AGENT**：代理人执行任务 - **APPEND\_TASK\_BEFORE**：前加签任务 - **APPEND\_TASK\_AFTER**：后加签任务 - **REDIRECT\_TASK**：转交任务 - **START\_PROCESS\_INSTANCE**：发起流程实例 - **TERMINATE\_PROCESS\_INSTANCE**：终止(撤销)流程实例 - **FINISH\_PROCESS\_INSTANCE**：结束流程实例 - **ADD\_REMARK**：添加评论 - **REDIRECT\_PROCESS：**审批退回 - **PROCESS\_CC**：抄送 |
| operation\_result | String | AGREE | 操作结果：   - **AGREE**：同意 - **REFUSE**：拒绝 - **NONE** |
| remark | String | 评论 | 评论内容。  审批操作附带评论时才返回该字段。 |
| attachments | Attachment[] |  | 评论附件。 |
| file\_name | String | 学历证明 | 附件名称。 |
| file\_size | String | 11890851 | 附件大小。 |
| file\_id | String | 22581233705 | 附件ID。 |
| file\_type | String | pdf | 附件类型 |
| tasks | TaskTopVo[] |  | 任务列表。 |
| userid | String | manager1 | 任务处理人。 |
| task\_status | String | NEW | 任务状态：   - **NEW**：未启动 - **RUNNING**：处理中 - **PAUSED**：暂停 - **CANCELED**：取消 - **COMPLETED**：完成 - **TERMINATED**：终止 |
| task\_result | String | REDIRECTED | 结果：   - **AGREE**：同意 - **REFUSE**：拒绝 - **REDIRECTED**：转交 |
| create\_time | Date | 1497249913000 | 开始时间。 |
| finish\_time | Date | 1497249913000 | 结束时间。 |
| taskid | String | 1497249 | 任务节点ID。 |
| url | String | https://www.xxxx.com | 任务URL。 |
| originator\_dept\_name | String | 测试 | 发起部门。 |
| biz\_action | String | MODIFY | 审批实例业务动作：   - **MODIFY**：表示该审批实例是基于原来的实例修改而来 - **REVOKE**：表示该审批实例是由原来的实例撤销后重新发起的 - **NONE**表示正常发起 |
| attached\_process\_instance\_ids | String[] | ["instance1","instance2"] | 审批附属实例列表，当已经通过的审批实例被修改或撤销，会生成一个新的实例，作为原有审批实例的附属。  如果想知道当前已经通过的审批实例的状态，可以依次遍历它的附属列表，查询里面每个实例的biz\_action。 |
| form\_component\_values | FormComponentValueVo[] |  | 表单详情列表。 |
| name | String | 名称 | 标签名。 |
| value | String | 示例值 | 标签值。 |
| ext\_value | String | 示例值 | 标签扩展值。 |
| id | String | DDHolidayField-J2Bxxxx | 组件ID。 |
| component\_type | String | DDSelectField | 组件类型。 |
| main\_process\_instance\_id | String | instance | 主流程实例标识。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/processinstance/get?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "process_instance_id":"1a2b-3e4dxxxx"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/processinstance/get");
OapiProcessinstanceGetRequest req = new OapiProcessinstanceGetRequest();
req.setProcessInstanceId("1a2b-3e4dxxxx");
OapiProcessinstanceGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
    "errmsg":"ok",
    "process_instance":{
    "form_component_values":[
      {
        "component_type":"TextField",
        "name":"请假天数",
        "id":"TextField_23QXWOU7G4JK0",
        "value":"1"
      }
    ],
      "create_time":"2020-12-21 15:30:26",
      "attached_process_instance_ids":[],
      "cc_userids":[
      "user456"
    ],
      "originator_dept_name":"测试2",
      "originator_userid":"user456",
      "title":"测试用户提交的请假",
      "finish_time":"2020-12-21 15:30:27",
      "result":"agree",
      "originator_dept_id":"433xxx",
      "business_id":"20201",
      "tasks":[
      {
        "task_status":"COMPLETED",
        "activity_id":"0dxxx",
        "task_result":"AGREE",
        "userid":"user456",
        "finish_time":"2020-12-21 15:30:27",
        "taskid":"66738",
        "url":"https://www.xxxx.com"
      },
      {
        "task_status":"COMPLETED",
        "activity_id":"e2xxx",
        "task_result":"AGREE",
        "userid":"user456",
        "finish_time":"2020-12-21 15:30:27",
        "taskid":"66738",
        "url":"https://www.xxxx.com"
      }
    ],
      "biz_action":"NONE",
      "operation_records":[
      {
        "date":"2020-12-21 15:30:26",
        "operation_type":"START_PROCESS_INSTANCE",
        "operation_result":"NONE",
        "userid":"user456"
      },
      {
        "date":"2020-12-21 15:30:26",
        "operation_type":"EXECUTE_TASK_AUTO",
        "operation_result":"AGREE",
        "userid":"user456"
      },
      {
        "date":"2020-12-21 15:30:26",
        "operation_type":"EXECUTE_TASK_AUTO",
        "operation_result":"AGREE",
        "userid":"user456"
      },
      {
        "date":"2020-12-21 15:30:26",
        "operation_type":"PROCESS_CC",
        "operation_result":"NONE",
        "remark":"",
        "userid":"user456"
      }
    ],
      "status":"COMPLETED"
  },
  "request_id":"10c0pggajcsu7"
}
```
