# 获取考勤报表列值

doc_id: 9qdK9MIwfy
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getcolumnval
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
- column_id_list (String, required): 报表列ID，可通过获取考勤报表列定义接口获取id参数值。多值用英文逗号分隔，最大长度20。
- from_date (Date, required): 开始时间。
- to_date (Date, required): 结束时间，结束时间减去开始时间必须在31天以内。

## Returns
- optional: request_id(String), errcode(Number), result(ColumnValListForTopVo), column_vals(ColumnValForTopVo[]), date(Date), value(String), column_vo(ColumnForTopVo), id(Number), fixed_value(String)

## Limits
- 报表列ID，可通过获取考勤报表列定义接口获取id参数值。多值用英文逗号分隔，最大长度20。
- 结束时间，结束时间减去开始时间必须在31天以内。
- - 本接口获取应出勤天数字段值，只支持获取距今15天内的应出勤天数value值，超过15天后的应出勤天数value值为0。

source_url: https://open.dingtalk.com/document/development/queries-the-column-value-of-the-attendance-report
updated_at: 2026-05-27 18:39:10
