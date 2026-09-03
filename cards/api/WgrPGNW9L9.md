# 查询项目中文件操作日志

doc_id: WgrPGNW9L9
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/workspace/auditlog/list
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_project

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Body
- start_date (Number, required): 操作日志起始时间，Unix时间戳，单位毫秒。
- end_date (Number, required): 操作日志截止时间，Unix时间戳，单位毫秒。
- page_size (Number, required): 操作列表长度，最大500。
- optional: load_more_gmt_create(Number), load_more_bizId(Number)

## Returns
- optional: errcode(Number), errmsg(String), result(OpenAuditLogDto), log_list(EventAuditLogDto[]), receiver_name(String), gmt_create(String), org_name(String), project_name(String), task_name(String), resource_extension(String), resource_size(String), resource(String), action(String), browser(String), ip_address(String), platform(String), operator_name(String), ding_talk_id(String), emp_id(String), biz_id(String), request_id(String)

## Limits
- 操作列表长度，最大500。

source_url: https://open.dingtalk.com/document/development/query-file-operation-logs-of-a-project
updated_at: 2026-07-20 09:21:55
