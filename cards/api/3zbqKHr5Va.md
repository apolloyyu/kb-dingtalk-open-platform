# 获取用户发出的日志列表

doc_id: 3zbqKHr5Va
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/report/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_report_query

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- start_time (Number, required): 查询的日志创建的开始时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- end_time (Number, required): 查询的日志创建的结束时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- cursor (Number, required): 查询游标，初始传入0，后续从上一次的返回值中获取。
- size (Number, required): 每页数据量，最大值为20。
- optional: template_name(String), userid(String), modified_start_time(Number), modified_end_time(Number)

## Returns
- optional: result(PageVo), data_list(ReportOapiVo[]), contents(JsonObject[]), sort(String), type(String), value(String), key(String), remark(String), template_name(String), dept_name(String), creator_name(String), creator_id(String), create_time(Number), report_id(String), modified_time(Number), size(Number), next_cursor(Number), has_more(Boolean), errcode(Number), errmsg(String)

## Limits
- 查询的日志创建的开始时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- 查询的日志创建的结束时间，Unix时间戳，单位毫秒。 **[!NOTE]** start_time参数和end_time参数最多相隔180天。
- 每页数据量，最大值为20。

source_url: https://open.dingtalk.com/document/development/query-logs-sent-by-an-employee
updated_at: 2026-05-27 13:10:15
