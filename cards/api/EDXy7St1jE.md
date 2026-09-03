# 创建实例

doc_id: EDXy7St1jE
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/workrecord/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过服务商获取第三方应用授权企业的access_token接口获取。

## Body
- request (SaveFakeProcessInstanceRequest, required): 请求对象。
- agentid (Number, required): 应用标识。可在开发者后台的应用详情页获取。应用的agentid。 - 企业内部应用可在开发者后台的应用详情页获取。 image - 第三方企业应用可调用获取企业授权信息接口获取 **[!IMPORTANT]** 如果是第三方企业应用必须指定该参数。
- process_code (String, required): 审批模板唯一码，调用创建或更新审批模板接口获取process_code参数值。
- originator_user_id (String, required): 审批实例接收人的userid。
- form_component_values (FormComponentValueVo[], required): 表单参数列表。
- name (String, required): 表单名称。表单每一栏的名称，对应表单组件的label字段。
- value (String, required): 表单值。
- url (String, required): 实例在审批应用里的跳转url，需要同时适配移动端和pc端。
- optional: title(String)

## Returns
- optional: request_id(String), success(Boolean), errcode(Number), errmsg(String), result(SaveFaceProcessInstanceResponse), process_instance_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/initiate-an-approval-process-without-a-process
updated_at: 2026-08-25 09:37:55
