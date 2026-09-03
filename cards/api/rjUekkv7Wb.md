# 获取模板详情

doc_id: rjUekkv7Wb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/template/getbyname
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_report_statistics, qyapi_report_query

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 操作该接口的员工userId。
- template_name (String, required): 模板名称。

## Returns
- optional: result(ReportTemplateResponseVo), default_receivers(DefaultReceivers[]), user_name(String), userid(String), name(String), id(String), fields(Fields[]), field_name(String), type(Number), sort(Number), default_received_convs(BaseConversationVo[]), conversation_id(String), title(String), errcode(Number), errmsg(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/query-template-details
updated_at: 2026-05-27 13:10:14
