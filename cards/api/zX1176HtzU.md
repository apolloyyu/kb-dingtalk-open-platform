# 获取用户签到记录

doc_id: zX1176HtzU
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/checkin/record/get
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
- userid_list (String, required): 需要查询的用户列表，最大列表长度为10。
- start_time (Number, required): 开始时间，Unix时间戳，单位毫秒。
- end_time (Number, required): 截止时间，单位毫秒。 - 如果是取1个人的数据，时间范围最大10天。 - 如果是取多个人的数据，时间范围最大1天。
- cursor (Number, required): 分页查询的游标，最开始可以传0。
- size (Number, required): 分页查询的每页大小，最大100。

## Returns
- optional: result(PageResult), next_cursor(Number), page_list(CheckinRecordVo[]), checkin_time(Number), image_list(String[]), detail_place(String), remark(String), userid(String), place(String), longitude(String), latitude(String), visit_user(String), errcode(Number), request_id(String)

## Limits
- 需要查询的用户列表，最大列表长度为10。
- 截止时间，单位毫秒。 - 如果是取1个人的数据，时间范围最大10天。 - 如果是取多个人的数据，时间范围最大1天。
- 分页查询的每页大小，最大100。

source_url: https://open.dingtalk.com/document/development/obtain-the-check-in-records-of-multiple-users
updated_at: 2026-05-27 17:06:33
