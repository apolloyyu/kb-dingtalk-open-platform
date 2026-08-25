---
title: "OA审批事件"
source_url: "https://open.dingtalk.com/document/development/oa-approval-event"
namespace: "development"
slug: "oa-approval-event"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > OA审批事件"
doc_id: "KUgdTCNlNn"
updated_at: "2025-10-16 15:06:36"
---

> Source: https://open.dingtalk.com/document/development/oa-approval-event
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > OA审批事件
> Updated: 2025-10-16 15:06:36

# OA审批事件

本文介绍了OA审批回调的RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 245 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=245的数据格式解释。 | 245 | 审批实例状态变更事件（广播）。  **[!NOTE]**  需先通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权。 |
| 246 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=246的数据格式解释。 | 246 | 审批任务状态变更事件（广播）。  **[!NOTE]**  需先通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权。 |
| 247 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=247的数据格式解释。 | 247 | 审批实例状态变更事件（定向）。  **[!NOTE]**  定向推送给该审批模板所归属的业务来源方。 |
| 248 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=248的数据格式解释。 | 248 | 审批任务状态变更事件（定向）。  **[!NOTE]**  定向推送给该审批模板所归属的业务来源方。 |

## 审批回调事件业务场景

审批推送给三方ISV的回调事件有两类场景：

- 审批定向事件场景，ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，此类场景下该审批模板是归属于ISV的，因此用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。
- 审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### 审批定向事件场景

ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，给对应归属的ISV应用定向推送回调。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3810961761/p537684.png)

### **审批广播事件场景**

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，会给所有已授权的ISV推送回调。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2661366761/p554629.png)

## biz\_type=245

当biz\_type=245时，数据为审批实例状态变更（广播）相关数据。

该数据为审批实例状态变更（广播）相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值245，表示审批实例状态变更（广播）相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "eventId": "53eee5d611c14089b0a432f68cexxx",
    "corpId": "dingbe60690a7ed2d34624f2f5cc6abecxxx",
    "syncAction": "workflow_instance_change_broadcast",
    "businessId": "202212141011000137xxx",
    "title": "xx提交的审批模版测试",
    "type": "start",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=xxx&dd_share=false&showmenu=false&dd_progress=false&back=native&procInstId=adlB-HLWSEGKe_m-xxx&taskId=&swfrom=isv&dinghash=approval&dtaction=os&dd_from=#approval",
    "createTime": 1670983873000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "staffId": "managerxxx"
}
```

字段说明：

| **参数** | **数据类型** | **说明** |
| --- | --- | --- |
| syncAction | String | 事件类型：   - **workflow\_instance\_change\_broadcast**：表示审批实例状态变更事件（广播） |
| processInstanceId | String | 审批实例id。 |
| corpId | String | 审批实例对应的企业corpId。 |
| createTime | Long | 创建审批实例时间，时间戳，单位毫秒。 |
| finishTime | Long | 结束审批实例时间，时间戳，单位毫秒。 |
| title | String | 实例标题。 |
| type | String | 实例状态变更类型：   - **start：**审批实例开始 - **finish：**审批正常结束（同意或拒绝） - **terminate：**审批终止（发起人撤销审批单） |
| staffId | String | 发起审批实例的员工userId。 |
| url | String | 审批实例url，可在钉钉内跳转到审批页面。 |
| result | String | 审批结果：   - **agree**：同意 - **refuse**：拒绝   **[!NOTE]**  审批终止时无此参数 |
| processCode | String | 审批模板的唯一码。 |

## biz\_type=246

当biz\_type=246时，数据为审批任务状态变更（广播）相关数据。

该数据为审批任务状态变更（广播）相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值246，表示审批任务状态变更（广播）相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "processInstanceId": "pLSJ6XEAStOhfATIP_Q_xxx",
    "eventId": "e52cff3268b24ceaaa7efba26a00fxxx",
    "corpId": "dingbe60690a7ed2d34624f2f5cc6abecxxx",
    "syncAction": "workflow_task_change_broadcast",
    "businessId": "202212132022000437xxx",
    "title": "xx提交的审批模版测试",
    "type": "start",
    "createTime": 1670934164000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "staffId": "managerxxx",
    "taskId": 77537611
}
```

字段说明：

| **参数** | **数据类型** | **说明** |
| --- | --- | --- |
| syncAction | String | 事件类型：   - **workflow\_task\_change\_broadcast：**表示审批任务状态变更事件（广播） |
| taskId | Long | 任务id。 |
| processInstanceId | String | 审批实例id。 |
| corpId | String | 发生审批任务变更的企业corpId。 |
| createTime | Long | 当前任务创建的时间，时间戳，单位毫秒。 |
| finishTime | Long | 当前任务结束，或转交动作发生的时间戳，单位毫秒。 |
| title | String | 实例标题。 |
| type | String | 任务状态变更类型：   - **start：**审批任务开始 - **finish：**审批任务正常结束（完成或转交） - **cancel：**说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件。   **[!NOTE]**  type为**finish**表示审批任务转交。 |
| staffId | String | 用户userId：   - 当前任务的审批人userId - 操作转交动作的用户userId |
| result | String | 审批结果：   - **agree：**同意 - **refuse：**拒绝 - **redirect：**表示审批任务转交 |
| remark | String | 操作时写的评论内容。 |
| processCode | String | 审批模板的唯一码。 |

## biz\_type=247

当biz\_type=247时，数据为审批实例状态变更（定向）相关数据。

该数据为审批实例状态变更（定向）相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值247，表示审批实例状态变更（定向）相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "processInstanceId": "adlB-HLWSEGKe_m-xxx",
    "eventId": "53eee5d611c14089b0a432f68cexxx",
    "corpId": "dingbe60690a7ed2d34624f2f5cc6abecxxx",
    "syncAction": "workflow_instance_change_directed",
    "businessId": "202212141011000137xxx",
    "title": "xx提交的审批模版测试",
    "type": "start",
    "version": "2",
    "url": "https://pre-aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=xxx&dd_share=false&showmenu=false&dd_progress=false&back=native&procInstId=adlB-HLWSEGKe_m-xxx&taskId=&swfrom=isv&dinghash=approval&dtaction=os&dd_from=#approval",
    "createTime": 1670983873000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "staffId": "managerxxx"
}
```

字段说明：

| **参数** | **数据类型** | **说明** |
| --- | --- | --- |
| syncAction | String | 事件类型：   - **workflow\_instance\_change\_directed：**表示审批实例状态变更事件（定向） |
| processInstanceId | String | 审批实例id。 |
| corpId | String | 审批实例对应的企业corpId。 |
| createTime | Long | 创建审批实例时间，时间戳，单位毫秒。 |
| finishTime | Long | 结束审批实例时间，时间戳，单位毫秒。 |
| title | String | 实例标题。 |
| type | String | 实例状态变更类型：   - **start：**审批实例开始 - **finish：**审批正常结束（同意或拒绝） - **terminate：**审批终止（发起人撤销审批单） |
| staffId | String | 发起审批实例的员工userId。 |
| url | String | 审批实例url，可在钉钉内跳转到审批页面。 |
| result | String | 审批结果：   - **agree**：同意 - **refuse**：拒绝   **[!NOTE]**  审批终止时无此参数 |
| processCode | String | 审批模板的唯一码。 |

## biz\_type=248

当biz\_type=248时，数据为审批任务状态变更（定向）相关数据。

该数据为审批任务状态变更（定向）相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值248，表示审批任务状态变更（定向）相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "processInstanceId": "pLSJ6XEAStOhfATIP_Q_xxx",
    "eventId": "e52cff3268b24ceaaa7efba26a00fxxx",
    "corpId": "dingbe60690a7ed2d34624f2f5cc6abecxxx",
    "syncAction": "workflow_task_change_directed",
    "businessId": "202212132022000437xxx",
    "title": "xx提交的审批模版测试",
    "type": "start",
    "createTime": 1670934164000,
    "processCode": "PROC-27BBC5E6-DFFA-4EC3-A1F1-xxx",
    "staffId": "managerxxx",
    "taskId": 77537611
}
```

字段说明：

| **参数** | **数据类型** | **说明** |
| --- | --- | --- |
| syncAction | String | 事件类型：   - **workflow\_task\_change\_directed：**表示审批任务状态变更事件（定向） |
| taskId | Long | 任务id。 |
| processInstanceId | String | 审批实例id。 |
| corpId | String | 发生审批任务变更的企业corpId。 |
| createTime | Long | 当前任务创建的时间，时间戳，单位毫秒。 |
| finishTime | Long | 当前任务结束，或转交动作发生的时间戳，单位毫秒。 |
| title | String | 实例标题。 |
| type | String | 任务状态变更类型：   - **start：**审批任务开始 - **finish：**审批任务正常结束（完成或转交） - **cancel：**说明当前节点有多个审批人并且是或签，其中一个人执行了审批，其他审批人会推送cancel类型事件。   **[!NOTE]**  type为**finish**表示审批任务转交。 |
| staffId | String | 用户userId：   - 当前任务的审批人userId - 操作转交动作的用户userId |
| result | String | 审批结果：   - **agree：**同意 - **refuse：**拒绝 - **redirect：**表示审批任务转交 |
| remark | String | 操作时写的评论内容。 |
| processCode | String | 审批模板的唯一码。 |
