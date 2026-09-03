# 发起审批实例

doc_id: Ux5oJcLPwl
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/processinstance/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取 - 第三方企业应用可通获取第三方应用授权企业的access_token

## Body
- process_code (String, required): 审批流的唯一码。 process_code在审批模板编辑页面的URL中获取。
- originator_user_id (String, required): 审批实例发起人的userid。
- dept_id (Number, required): 发起人所在的部门，如果发起人属于根部门，传-1。
- form_component_values (FormComponentValueVo[], required): 审批流表单参数，最大列表长度200。 仅支持下表列举的表单控件。 **[!NOTE]** - 明细内组件个数上限是200个。 - 明细内使用的联系人组件上限是50个，过多使用联系人组件会导致超时。
- name (String, required): 表单每一栏的名称。
- value (String, required): 表单每一栏的值。 - 单行输入框内的值，使用建议不超过1000个字符。 - 多行输入框内的值，使用建议不超过8000个字符。
- optional: agent_id(Number), approvers(String), approvers_v2(ProcessInstanceApproverVo[]), task_action_type(String), user_ids(String[]), cc_list(String), cc_position(String), ext_value(String)

## Returns
- optional: errcode(Number), errmsg(String), request_id(String), process_instance_id(String)

## Limits
- 审批人userid列表，最大列表长度20。 多个审批人用逗号分隔，按传入的顺序依次审批。
- 审批人列表，最大列表长度20。 支持会签/或签，优先级高于approvers变量。
- 审批人userid列表： - 会签/或签列表长度必须大于1 - 非会签/或签列表长度只能为1 最大列表长度20。
- 抄送人userid列表，最大列表长度20。 **[!NOTE]** 该参数需要与approvers或approvers_v2参数一起传，抄送人才会生效。
- 审批流表单参数，最大列表长度200。 仅支持下表列举的表单控件。 **[!NOTE]** - 明细内组件个数上限是200个。 - 明细内使用的联系人组件上限是50个，过多使用联系人组件会导致超时。
- 表单每一栏的值。 - 单行输入框内的值，使用建议不超过1000个字符。 - 多行输入框内的值，使用建议不超过8000个字符。

source_url: https://open.dingtalk.com/document/development/oa-approval-initiates-approval-instances
updated_at: 2025-12-05 19:25:32
