# 创建或更新审批模板

doc_id: VVsKKZHtS8
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/save
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
- saveProcessRequest (SaveProcessRequest, required): 审批模板信息。
- agentid (Number, required): 应用标识。可在开发者后台的应用详情页获取。
- name (String, required): 审批模板名称。
- description (String, required): 审批模板描述。
- form_component_list (FormComponentVo[], required): 表单列表。
- component_name (String, required): 表单名称。每种表单组件的component_name是固定的。表单组件的props里的id，必须在模板里唯一，可以有两段字符串组成，第一段为表单的component_name；第二段为8位随机字符串。 **[!NOTE]** 只支持下表中的表单，不支持其他值。
- props (FormComponentPropVo, required): 表单属性。
- id (String, required): 表单ID，最大不能超过22个字符。
- label (String, required): 表单名称。
- optional: process_code(String), required(Boolean), fake_mode(Boolean)

## Returns
- optional: request_id(String), errmsg(String), errcode(Number), result(ProcessTopVo), process_code(String)

## Limits
- 表单ID，最大不能超过22个字符。
- - 每个企业最多创建200个自有审批模板，超过最大数量后调用接口会报错。
- > 选项最多200项，每项最多50个字。
- 4. **调用接口返回错误码810002，错误信息是复制的审批流已超过最大数量**
- 目前一个企业最多可创建200个自有审批模板，超过最大数量后调用接口会报错。

source_url: https://open.dingtalk.com/document/development/save-approval-template
updated_at: 2026-08-25 09:37:52
