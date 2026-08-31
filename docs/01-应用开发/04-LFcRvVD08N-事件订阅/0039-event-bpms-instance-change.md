---
title: "审批实例开始、结束、终止、删除"
source_url: "https://open.dingtalk.com/document/development/event-bpms-instance-change"
namespace: "development"
slug: "event-bpms-instance-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "办公 > OA审批 > 审批实例开始、结束、终止、删除"
doc_id: "Fy4Neg0dZn"
updated_at: "2026-07-22 16:25:35"
---

> Source: https://open.dingtalk.com/document/development/event-bpms-instance-change
> Path: 应用开发 / 事件订阅 / 办公 > OA审批 > 审批实例开始、结束、终止、删除
> Updated: 2026-07-22 16:25:35

# 审批实例开始、结束、终止、删除

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 审批实例开始、结束、终止、删除 |
| 英文名称 | bpms\_instance\_change |

## 功能描述

当审批实例开始、结束、终止或删除时，钉钉服务器给开发者回调地址推送审批实例事件。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## **订阅规则**

你可以在目标应用的事件订阅中进行审批事件的订阅设置，规则如下：

| 规则 | 描述 | 示例 | 说明 |
| --- | --- | --- | --- |
| `/v1.0/event/bpms_instance_change/bizCategoryId/{bizCategoryId}/processCode/{processCode}/type/{type}` | 针对某个业务分类下特定审批模板的实例开始、结束或终止事件进行订阅。 | `/v1.0/event/bpms_instance_change/bizCategoryId/{bizCategoryId}/processCode/{PROC-EA*F-885E-47AA-AEB9-8F59CB10E309}/type/start` | - bizCategoryId：审批表单所属的业务分类标识 - processCode：审批表单的唯一编码   详情参考[审批 ID 说明](../02-4a8AMF6u2A-服务端-API/0473-workflow-overview.md)。 |
| `/v1.0/event/bpms_instance_change/processCode/{processCode}/type/{type}` | 针对某个审批模板下的实例开始、结束或终止事件进行订阅。 | `/v1.0/event/bpms_instance_change/processCode/{PROC-EA*F-885E-47AA-AEB9-8F59CB10E309}/type/start` | - processCode：审批表单的唯一编码   详情参考[审批 ID 说明](../02-4a8AMF6u2A-服务端-API/0473-workflow-overview.md)。 |

### **OA审批****套件业务分类标识**

> 下方为常用业务分类 bizCategoryId，具体企业请根据实际分类标识进行区分。

| **业务分类标识****bizCategoryId** | **套件名称** | **业务名称** |
| --- | --- | --- |
| open.com.dd.at.approveCheck | 打卡审批 | 考勤 |
| attendance.batchovertime | 加班 | 考勤 |
| attendance.supply | 补卡 | 考勤 |
| attendance.goout | 外出 | 考勤 |
| attendance.relieve | 换班 | 考勤 |
| alitrip.business | 出差 | 考勤 |
| hrm.termination | 离职 | 智能人事 |
| hrm.transfer | 转岗 | 智能人事 |
| hrm.regular | 转正 | 智能人事 |
| hrm.hire | 入职 | 智能人事 |
| hrm.terminationAndHandover | 离职&离职交接 | 智能人事 |
| hrm.handOver | 离职交接 | 智能人事 |
| hrm.hireTrial | 试岗入职 | 智能人事 |
| hrm.promotion | 晋升 | 智能人事 |
| hrm.transferAndSalary | 调岗调薪 | 智能人事 |
| hrm.hireAndSalary | 入职定薪 | 智能人事 |
| hrm.regularAndSalary | 转正调薪 | 智能人事 |
| hrm.promotionAndSalary | 晋升调薪 | 智能人事 |
| dingtalk.hrm.offer | offer审批 | 智能人事 |
| dingtalk.hrm.integratedSuite | 人事综合套件 | 智能人事 |
| dingtalk.businessFinance.reimbursement | 报销套件 | 智能财务 |
| dingtalk.businessFinance.payment | 付款套件 | 智能财务 |
| dingtalk.businessFinance.collection | 收款套件 | 智能财务 |
| dingtalk.businessFinance.receivable | 应收套件 | 智能财务 |
| dingtalk.businessFinance.returned | 应收回款 | 智能财务 |
| dingtalk.businessFinance.badDebt | 应收坏账 | 智能财务 |
| dingtalk.businessFinance.payable | 应付套件 | 智能财务 |
| dingtalk.businessFinance.payablePayment | 应付实付 | 智能财务 |
| dingtalk.businessFinance.noPayment | 应付免付 | 智能财务 |
| dingtalk.businessFinance.reserve | 备用金 | 智能财务 |
| dingtalk.businessFinance.reserveVerification | 备用金核销 | 智能财务 |
| dingtalk.businessFinance.reserveReturned | 备用金还款 | 智能财务 |
| dingtalk.businessFinance.transfer | 转账 | 智能财务 |
| dingtalk.businessFinance.invoiceApplication | 开票申请 | 智能财务 |
| dingtalk.businessFinance.costApplication | 费用申请 | 智能财务 |
| open.com.dd.suite.seal | 用印申请 | 智能合同 |
| open.com.dd.suite.icontract | 合同审批 | 智能合同 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.processInstanceId`（string）：审批实例id。
- `data.finishTime`（long）：结束审批实例时间。时间戳，单位毫秒。
- `data.createTime`（long）：创建审批实例时间。时间戳，单位毫秒。
- `data.processCode`（string）：审批模板的唯一码。
- `data.bizCategoryId`（string）：业务分类标识。
- `data.businessId`（string）：流程实例业务标识。
- `data.type`（string）：实例状态变更类型：  
  - start：审批实例开始  
  - finish：审批正常结束（同意或拒绝）  
  - terminate：审批终止（发起人撤销审批单）  
  - delete：审批实例删除
- `data.title`（string）：审批实例标题。
- `data.businessType`（string）：业务身份。
- `data.url`（string）：审批实例url，可在钉钉内跳转到审批页面。
- `data.staffId`（string）：发起审批实例的员工userId。
- `data.result`（string）：审批结果(审批终止时无此参数)：  
  - agree： 同意  
  - refuse：拒绝

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "bpms_instance_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "result": "agree",
    "processInstanceId": "9Qgx5QqjR7axMwxxxx",
    "finishTime": 1495592272000,
    "createTime": 1495592305000,
    "processCode": "Pro-xxx",
    "bizCategoryId": "20230xxx",
    "businessId": "yewu1",
    "type": "finish",
    "title": "自测-1016",
    "businessType": "yewu1",
    "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid\\u003dding2c015874d817xxxx\\u0026dd_share\\u003d",
    "staffId": "manager75"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `processInstanceId`（string）：审批实例id。
- `finishTime`（long）：结束审批实例时间。时间戳，单位毫秒。
- `createTime`（long）：创建审批实例时间。时间戳，单位毫秒。
- `processCode`（string）：审批模板的唯一码。
- `bizCategoryId`（string）：业务分类标识。
- `businessId`（string）：流程实例业务标识。
- `type`（string）：实例状态变更类型：  
  - start：审批实例开始  
  - finish：审批正常结束（同意或拒绝）  
  - terminate：审批终止（发起人撤销审批单）  
  - delete：审批实例删除
- `title`（string）：审批实例标题。
- `businessType`（string）：业务身份。
- `url`（string）：审批实例url，可在钉钉内跳转到审批页面。
- `staffId`（string）：发起审批实例的员工userId。
- `result`（string，必填）：审批结果(审批终止时无此参数)：  
  - agree： 同意  
  - refuse：拒绝

### **事件体示例**

```
{
  "EventType": "bpms_instance_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "result": "agree",
  "processInstanceId": "9Qgx5QqjR7axMwxxxx",
  "finishTime": 1495592272000,
  "createTime": 1495592305000,
  "processCode": "Pro-xxx",
  "bizCategoryId": "20230xxx",
  "businessId": "yewu1",
  "type": "finish",
  "title": "自测-1016",
  "businessType": "yewu1",
  "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid\\u003dding2c015874d817xxxx\\u0026dd_share\\u003d",
  "staffId": "manager75"
}
```
