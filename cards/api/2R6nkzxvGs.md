# 发起审批实例

doc_id: 2R6nkzxvGs
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/workflow/processInstances
api_version: v2-new
app_types: 第三方企业应用
permissions: Workflow.Instance.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- originatorUserId (String, required): 审批发起人的userId，可通过获取部门用户userid列表接口获取。
- processCode (String, required): 审批流的唯一码。process_code在审批模板编辑页面的URL中获取。
- formComponentValues (Array, required): 表单控件列表，详情请参考FormComponentValues 参数说明，最大列表长度：150。
- name (String, required): 控件名称，与创建或更新审批表单模板接口中组件`label`字段值保持一致。
- value (String, required): 控件值，最大长度65535字符。
- optional: bizDetailPageUrl(String), deptId(Long), microappAgentId(Long), approvers(Array), actionType(String), userIds(Array of String), ccList(Array of String), ccPosition(String), targetSelectActioners(Array), actionerKey(String), actionerUserIds(Array of String), id(String), bizAlias(String), extValue(String), componentType(String), details(Array)

## Returns
- optional: instanceId(String)

## Limits
- 第三方审批系统中审批单详情页地址，用于满足三方业务自研页面 + OA审批官方工作流集成的复杂业务场景诉求。最大长度1024字符。 - 指定bizDetailPageUrl功能为OA高级版专享功能，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。查看全部专享OpenAPI - 若指定了bizDetailPageUrl，在钉钉OA审批、钉钉待办、消息卡片等入口点击跳转时，将会直接跳转对应业务系统详情页地址。
- 不使用审批流模板时，直接指定的审批人列表，最大列表长度：20。 指定审批单的执行流程，会覆盖审批单在OA后台设置的默认流程。
- 抄送人 userId。 最大列表长度为50。
- 使用审批流模板时，流程预测结果中节点规则上必填的自选操作人列表，最大列表长度：20。 使用OA后台设置的默认流程，并且流程中有审批人自选节点，该参数必填。
- 表单控件列表，详情请参考FormComponentValues 参数说明，最大列表长度：150。
- 控件值，最大长度65535字符。
- 控件扩展值，最大长度65535字符。
- 子控件列表，最大元素个数：150。明细控件最大总长度65535字符。

source_url: https://open.dingtalk.com/document/development/create-an-approval-instance
updated_at: 2026-06-03 10:12:25
