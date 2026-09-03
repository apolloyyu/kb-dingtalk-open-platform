# 获取用户发送日志的概要信息

doc_id: gN5jHZYcc7
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/simplelist
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_report_statistics, qyapi_report_query

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- start_time (Number, required): 查询起始时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- end_time (Number, required): 查询截止时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- cursor (Number, required): 查询游标，初始传入0，后续从上一次的返回值中获取。
- size (Number, required): 每页数据量，最大为20。
- optional: template_name(String), userid(String)

## Returns
- optional: result(PageVo), data_list(ReportOapiVo[]), remark(String), template_name(String), dept_name(String), creator_name(String), creator_id(String), create_time(Number), report_id(String), size(Number), next_cursor(Number), has_more(Boolean), errcode(Number), request_id(String)

## Limits
- 查询起始时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- 查询截止时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- 每页数据量，最大为20。

source_url: https://open.dingtalk.com/document/development/view-log-summary-data
updated_at: 2026-05-27 13:10:16
