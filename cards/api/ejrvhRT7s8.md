# 删除模板

doc_id: ejrvhRT7s8
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/topapi/process/delete
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
- request (DeleteProcessRequest, required): 请求对象。
- agentid (Number, required): 应用标识。可在开发者后台的应用详情页获取。应用的agentid。 - 企业内部应用可在开发者后台的应用详情页获取。 image - 第三方企业应用可调用获取企业授权信息接口获取。 **[!IMPORTANT]** 如果是第三方企业应用必须指定该参数。
- process_code (String, required): 审批模板唯一码，调用创建或更新审批模板接口获取process_code参数值。
- optional: clean_running_task(Boolean)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-a-template
updated_at: 2026-08-25 09:37:54
