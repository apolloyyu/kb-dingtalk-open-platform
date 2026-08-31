---
title: "流程实例"
source_url: "https://open.dingtalk.com/document/development/yida-process-instance"
namespace: "development"
slug: "yida-process-instance"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 流程实例"
doc_id: "jvnKkZDQP2"
updated_at: "2026-08-27 12:32:06"
---

> Source: https://open.dingtalk.com/document/development/yida-process-instance
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 宜搭 > 旧版宜搭API参考 > 流程实例
> Updated: 2026-08-27 12:32:06

# 流程实例

> **[!IMPORTANT]**
>
> 此旧版宜搭API接口文档已不在维护，已经接入的用户可继续使用，正在准备接入宜搭的用户请查看[宜搭应用开发](0304-overview-yida.md)。

## 发起流程

- 接口：[/yida\_vpc/process/startInstance.json](https://s-api.alibaba-inc.com/yida_vpc/process/startInstance.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxSLVP |  |
  | systemToken | 应用密钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | processCode | 流程code | 是 | TPROC--EFxxxx400RCJ4 | 单独发起页链接上可查 |
  | formUuid | 表单ID | 是 | FORM-EF6xxxx0RCJ3 | 单独发起页链接上可查 |
  | formDataJson | 表单数据 | 是 |  | 参考：附录1保存/更新 表单数据格式说明 |
  | deptId | 发起人所在部门号 | 否 | 18295 | 不填，默认发起人主职部门 |
- 返回值

  - result：实例ID；
  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；
- 返回示例

  ```
  {
     "result":"f3023xxxx530",
     "success":true
  }
  ```

## 根据条件搜索流程实例ID

- 接口：[/yida\_vpc/process/getInstanceIds.json](https://s-api.alibaba-inc.com/yida_vpc/process/getInstanceIds.json)

  > **[!NOTE]**
  >
  > 只有应用管理员才能使用这个接口
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_xxxxSLVP |  |
  | systemToken | 应用密钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US  默认：zh\_CN |
  | formUuid | 表单ID | 是 | FORM-EF6xxxxCJ3 |  |
  | searchFieldJson | 根据表单内组件值查询 | 否 |  | 格式见附录2：根据组件值进行条件搜索，组件值格式说明 |
  | taskId | 任务ID | 否 | 2199132092 | 一般用不到。 |
  | instanceStatus | 实例状态 | 否 | RUNNING | 可选值为：  - **RUNNING**：运行中 - **TERMINATED**：已终止 - **COMPLETED**：已完成 - **ERROR**：异常 |
  | approvedResult | 流程审批结果 | 否 | agree | 可选值为：  - **agree**：同意 - **disagree**：拒绝 |
  | currentPage | 当前页 | 否 | 1 | 必须大于0，默认1 |
  | pageSize | 每页记录数 | 否 | 10 | 必须大于0，默认10，不能大于100 |
  | originatorId | 根据流程发起人工号查询 | 否 |  |  |
  | createFrom | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式yyyy-MM-DD |
  | createTo | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。和createFrom一起，相当于查询在2018-01-01到2018-01-31之间(包含01和31号)创建的数据。 |
  | modifiedFrom | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式 |
  | modifiedTo | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。 和modifiedFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)被修改的数据。 |
- 返回值

  - result：实例ID；
  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；
- 返回示例

  ```
  {
     "result":{
        "data":[
           "f30233xxxxee530",
           "bc095xxxx8523ab",
           "f540cxxxx8a2802"
        ],
        "totalCount":3,
        "currentPage":1
     },
     "success":true
  }
  ```

## 根据搜索条件获取实例详情列表

- 接口：[/yida\_vpc/process/getInstances.json](https://s-api.alibaba-inc.com/yida_vpc/process/getInstances.json)

  > **[!NOTE]**
  >
  > 只有应用管理员才能使用这个接口
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxxSLVP |  |
  | systemToken | 应用密钥 | 是 | helxxxy | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US  默认：zh\_CN |
  | formUuid | 表单ID | 是 | FORM-EF6xxxx00RCJ3 |  |
  | searchFieldJson | 根据表单内组件值查询 | 否 |  | 格式见附录2：根据组件值进行条件搜索，组件值格式说明 |
  | taskId | 任务ID | 否 | 2199132092 | 一般用不到。 |
  | instanceStatus | 实例状态 | 否 | RUNNING | 可选值为：  - **RUNNING**：运行中 - **TERMINATED**：已终止 - **COMPLETED**：已完成 - **ERROR**：异常 |
  | approvedResult | 流程审批结果 | 否 | agree | 可选值为：  - **agree**：同意 - **disagree**：拒绝 |
  | currentPage | 当前页 | 否 | 1 | 必须大于0，默认1 |
  | pageSize | 每页记录数 | 否 | 10 | 必须大于0，默认10，不能大于100 |
  | originatorId | 根据流程发起人工号查询 | 否 |  |  |
  | createFrom | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式 |
  | createTo | createFrom和createTo两个时间构造一个时间段。查询在该时间段创建的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。和createFrom一起，相当于查询在2018-01-01到2018-01-31之间(包含01和31号)创建的数据。 |
  | modifiedFrom | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表 | 否 | 2018-01-01 | 字符串格式，且为yyyy-MM-DD格式 |
  | modifiedTo | modifiedFrom和modifiedTo构成一个时间段，查询在该时间段有修改的数据列表。 | 否 | 2018-02-01 | 字符串格式，且为yyyy-MM-DD格式。 和modifiedFrom一起，相当于查询在 2018-01-01到2018-01-31之间(包含01和31号)被修改的数据。 |
- 返回值

  - result：

    - currentPage：当前页
    - totalCount：符合条件的实例总数
    - data：实例详情列表
  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 根据实例ID获取流程实例详情

- 接口：[/yida\_vpc/process/getInstanceById.json](https://s-api.alibaba-inc.com/yida_vpc/process/getInstanceById.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxxSLVP |  |
  | systemToken | 应用密钥 | 是 | hexxyy | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US  默认：zh\_CN |
  | processInstanceId | 流程实例ID | 是 | f3023xxxxee530 |  |
- 返回值

  - result：实例详情
  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 删除流程实例

- 接口：[/yida\_vpc/process/deleteInstance.json](https://s-api.alibaba-inc.com/yida_vpc/process/deleteInstance.json)

  > **[!NOTE]**
  >
  > 只有应用管理员才能使用这个接口
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxxSLVP |  |
  | systemToken | 应用密钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US  默认：zh\_CN |
  | processInstanceId | 流程实例ID | 是 | f3023xxxxe530 |  |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 终止流程实例

- 接口：[/yida\_vpc/process/terminateInstance.json](https://s-api.alibaba-inc.com/yida_vpc/process/terminateInstance.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxxVP |  |
  | systemToken | 应用密钥 | 是 | hexxxx | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US  默认：zh\_CN |
  | processInstanceId | 流程实例ID | 是 | f302xxxxee530 |  |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 根据实例ID批量获取流程实例详情

- 接口：[/yida\_vpc/process/getInstancesByIds.json](https://s-api.alibaba-inc.com/yida_vpc/process/getInstancesByIds.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxxLVP |  |
  | systemToken | 应用密钥 | 是 | hexxyy | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | processInstanceIds | 流程实例ID列表，多个用，分割 | 是 | f3023xxxx9ee530 |  |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；
  - result：实例详情列表；

## 执行单个任务接口

- 接口：[/yida\_vpc/task/executeTask.json](https://s-api.alibaba-inc.com/yida_vpc/task/executeTask.json)
- 参数：

  | 参数 | 描述 | 是否必填 | 示例值 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_PxxxxSLVP |  |
  | systemToken | 应用密钥 | 是 | hexxyy | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | taskId | 任务ID | 是 | 12002575 |  |
  | procInstId | 实例ID | 是 | f30xxxx9ee530 |  |
  | outResult | 审批结果 | 是 | AGREE | **AGREE**：同意  **DISAGREE**：不同意 |
  | remark | 审批意见 | 是 | 确认同意 |  |
  | formDataJson | 更新的表单值 | 否 |  | 参考：附录1保存/更新 表单数据格式说明。参数有的组件更新，没有的组件保持不变。明细的值只能统一更新，无法只更新明细下某个组件的值 |
  | noExecuteExpressions | 是否不执行校验&关联操作 | 否 | y | 本任务节点有绑定校验规则或者关联操作时，y -> 不执行校验规则&关联操作n -> 执行校验规则&关联操作不传默认为n，即会执行校验规则&关联操作 |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 获取审批记录

- 接口：/yida\_vpc/process/getOperationRecords.json
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_Pxxxx7SLVP |  |
  | systemToken | 应用密钥 | 是 | hexxyy | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  |  |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US默认：zh\_CN |
  | processInstanceId | 流程实例ID | 是 | f302xxxxe530 |  |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；
- 返回示例

  ```
  {
    "success": true,
    "content": [
      {
        "operateTime": "2018-06-22 14:35:40",
        "remark": "",
        "taskHoldTime": 0,
        "type": "HISTORY",
        "operatorName": "王XX",
        "operator": "WB260752",
        "activityId": "sid-restartevent",
        "action": "提交申请",
        "actionExt": "submit",
        "id": 2846866118,
        "operatorPhotoUrl": "//work.alibaba-inc.com/photo/WB260752.128x128.jpg",
        "processInstanceId": "8c124xxxx310837",
        "showName": "提交申请",
        "operateType": "NEW_PROCESS",
        "domains": [],
        "operatorStatus": "A",
        "operatorAgentIds": [],
        "size": 1,
        "operatorDisplayName": "王XX",
        "taskId": "null"
      },
      {
        "taskHoldTime": 531398377,
        "type": "TODO",
        "operatorName": "王XX",
        "operator": "WB260752",
        "activityId": "sidJIOBxxxxDOS28",
        "taskType": "COMMON_ALL_AT_ONCE",
        "actionExt": "doing",
        "operatorPhotoUrl": "//work.alibaba-inc.com/photo/WB260752.128x128.jpg",
        "processInstanceId": "8c12xxxx10837",
        "showName": "执行人",
        "activeTime": "2018-06-22 14:35:41",
        "domains": [],
        "operatorStatus": "A",
        "operatorAgentIds": [],
        "size": 1,
        "operatorDisplayName": "王XX",
        "taskId": "2846866145"
      }
    ]
  }
  ```

## 执行虚拟节点任务

- 接口：/yida\_vpc/process/executePlatformTask.json
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_xxxx7SLVP |  |
  | systemToken | 应用密钥 | 是 | hexxyyddd | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 | yida\_pub\_account | 写死 yida\_pub\_account |
  | language | 语言 | 否 | zh\_CN | 可选值：zh\_CN/en\_US  默认：zh\_CN |
  | procInstId | 流程实例ID | 是 | f302xxxxee530 |  |
  | outResult | 审批结果 | 是 | agree | - **agree**：同意 - **disagree**：拒绝 |
  | formDataJson | 更新的表单数据 | 否 |  | 参考：附录1保存/更新 表单数据格式说明。参数有的组件更新，没有的组件保持不变。明细的值只能统一更新，无法只更新明细下某个组件的值 |
  | remark | 审批意见 | 是 | 确认同意 |  |
  | noExecuteExpressions | 是否不执行校验&关联操作 | 否 | y | 本任务节点有绑定校验规则或者关联操作时，y -> 不执行校验规则&关联操作n -> 执行校验规则&关联操作不传默认为n，即会执行校验规则&关联操作 |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 流程实例更新

- 接口：/yida\_vpc/process/updateInstance.json
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_xxxx7SLVP |  |
  | systemToken | 应用密钥 | 是 | hello1234 | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  | 会校验userId是否有流程发起权限 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | processInstanceId | 实例ID | 是 |  |  |
  | updateFormDataJson | 更新的表单数据 | 是 |  | 参考：附录1保存/更新 表单数据格式说明 |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；

## 获取流程设计节点上的按钮列表

- 接口：/yida\_vpc/process/getActivityButtonVOs.json
- 参数：

  | 参数 | 描述 | 是否必填 | 示例 | 备注 |
  | --- | --- | --- | --- | --- |
  | appType | 应用ID | 是 | APP\_xxxx7SLVP |  |
  | systemToken | 应用密钥 | 是 | hello1234 | 在应用数据中获取。 |
  | userId | 钉钉的userId | 是 |  | 会校验userId是否有流程发起权限 |
  | language | 语言环境 | 否 | zh\_CN | 可选值：zh\_CN/en\_US |
  | processCode | 流程编码 | 是 | TPRxxxxxYELIWJ1 |  |
  | activityId | 节点ID | 是 |  |  |
- 返回值

  - success：请求是否成功；
  - errorMsg：错误信息；
  - errorCode：错误码；
- 返回示例

  ```
  {
    "result": [
      {
        "aliasEn": "Forward",
        "alias": "转交",
      },
      {
        "aliasEn": "Append",
        "alias": "加签",
      },
      {
        "aliasEn": "Return",
        "alias": "退回",
      }
    ],
    "success": true,
    "errorCode": null,
    "content": null,
    "errorMsg": null
  }
  ```
