# 获取报表假期数据

doc_id: 94WUTZWXFz
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getleavetimebynames
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userid (String, required): 用户的userId。
- leave_names (String, required): 假期名称，多个用英文逗号分隔，最大长度20。
- from_date (Date, required): 开始时间，不支持获取 225 天之前的数据。
- to_date (Date, required): 结束时间，结束时间减去开始时间必须在31天以内。

## Returns
- optional: result(ColumnValListForTopVo), columns(ColumnValForTopVo[]), columnvo(ColumnForTopVo), name(String), sub_type(Number), status(Number), alias(String), type(Number), columnvals(ColumnDayAndVal[]), value(String), date(Date), errcode(Number), request_id(String)

## Limits
- 假期名称，多个用英文逗号分隔，最大长度20。
- 开始时间，不支持获取 225 天之前的数据。
- 结束时间，结束时间减去开始时间必须在31天以内。

source_url: https://open.dingtalk.com/document/development/obtains-the-holiday-data-from-the-smart-attendance-report
updated_at: 2026-05-27 17:06:17
