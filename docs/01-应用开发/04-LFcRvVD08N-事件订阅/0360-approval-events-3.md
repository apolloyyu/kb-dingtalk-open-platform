---
title: "审批事件"
source_url: "https://open.dingtalk.com/document/development/approval-events-3"
namespace: "development"
slug: "approval-events-3"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 审批事件"
doc_id: "E64RYzjHip"
updated_at: "2025-10-16 15:06:35"
---

> Source: https://open.dingtalk.com/document/development/approval-events-3
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 审批事件
> Updated: 2025-10-16 15:06:35

# 审批事件

本文介绍了审批的RDS和SyncHTTP推送的数据格式。

> **[!IMPORTANT]**
>
> 为提升事件的使用体验，钉钉针对OA审批相关事件进行了升级。本接口文档将于2023年5月15日迁移至**历史文档（不推荐）**目录下，事件不会下线。
>
> - 已接入的用户建议您根据自身实际情况评估是否切换至新事件。
> - 新接入的用户请直接使用新事件[OA审批事件](https://open.dingtalk.com/document/isvapp/oa-approval-event)。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 审批数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 22 | xxxxx\_0 | corpxxxx | ef-sss-sv | 22 | ISV自定义审批 |

## **审批回调事件业务场景**

审批推送给三方ISV的回调事件有两类场景：

- 审批定向事件场景，ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，此类场景下该审批模板是归属于ISV的，因此用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。
- 审批广播事件场景，归属于某个ISV或官方OA审批应用的审批单模板，有可能也需要授权给另外的ISV做系统集成，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。

### **审批定向事件场景**

ISV通过开放接口创建的官方OA审批，或用户在OA管理后台创建的“ISV套件”模板，给对应归属的ISV应用定向推送回调。

![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3810961761/p537684.png)

### **审批广播事件场景**

归属于某个ISV或官方OA审批应用的审批单模板，在通过[授权获取审批实例数据](https://open.dingtalk.com/document/isvapp/obtain-approval-instance-data)jsapi获取企业授权后，会给所有已授权的ISV推送回调。

![](https://alidocs.oss-cn-zhangjiakou.aliyuncs.com/res/W4j6OJwNK7d7l3p8/img/da6ba6da-742b-4ec2-8453-64d99cb9e8df.png)

## biz\_type=22

当biz\_type=22时，数据为由ISV通过接口发起的审批实例数据。

该数据为在授权的第三方企业应用中，当由ISV通过接口发起的审批出现变更的时刻产生数据推送，插入表open\_sync\_biz\_data\_medium中。

> **[!NOTE]**
>
> 当表单内容大于64KB时，为防止推送失败，推送数据中会省略掉formValueVOS字段，并同时添加formValuesOmitted为true的标识字段。若需要获取表单完整数据，可调用服务端API-[获取单个审批实例详情](https://open.dingtalk.com/document/isvapp/obtains-the-details-of-a-single-approval-instance-pop)接口。

| **字段** | **说明** |
| --- | --- |
| subscribe\_id | 第三方企业应用的suiteid加下划线0。 |
| corp\_id | 开通第三方企业应用的企业corpid。 |
| biz\_id | 审批实例ID。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下。

其中"syncAction" 字段取值含义如下：

- isv\_bpms：一条审批记录的创建或者流程更新。
- isv\_bpms\_cancel：一条审批记录撤销（字段保留待开发）

```
{
  "processInstanceId": "bbdf6db4-8786-4cd7-afce-xxx955094716",
  "attachedProcessInstanceIds": [],
  "syncAction": "isv_bpms",
  "businessId": "201808201943000524542",
  "title": "1356766****的test_1534743715441",
  "originatorDeptId": "-1",
  "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding6e51bbd3049d542f35c2f4657eb6378f&dd_share=false&showmenu=true&dd_progress=false&back=native&procInstId=bbdf6db4-8786-4cd7-afce-1ee955094716c&taskId=&dinghash=approval&dd_from=isv#approval",
  "operationRecords": [{
    "date": 1534765433000,
    "result": "NONE",
    "type": "START_PROCESS_INSTANCE",
    "userId": "0805174458-2101290130"
  }],
  "result": "",
  "bizAction": "NONE",
  "ccUserids": ["0805174458-xxxx290130"],
  "createTime": 1534765433000,
  "originatorUserid": "0805174458-210129xxxx",
  "processCode": "PROC-0D214F00-1817-490F-xxxx-541FEF589574",
  "formValueVOS": [{
    "name": "文本1",
    "id": "TextField-JL1PLEE3",
    "value": "测试"
  }],
  "tasks": [{
    "result": "NONE",
    "createTime": 1534765434000,
    "userId": "0805174458-2101290130",
    "taskId": 39260212292,
    "status": "RUNNING"
  }],
  "approverUserids": ["0805174458-2101290130"],
  "originatorDeptName": "XX的体验组织",
  "status": "RUNNING"
}
```

字段说明，请参考[获取单个审批实例详情](https://open.dingtalk.com/document/isvapp/obtains-the-details-of-a-single-approval-instance-pop)。
