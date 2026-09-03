# 查询请假状态

doc_id: 1DFxFzoUPK
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/getleavestatus
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_attendance_data

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid_list (String, required): 待查询用户的ID列表，每次最多100个。
- start_time (Number, required): 开始时间 ，Unix时间戳，支持最多180天的查询。
- end_time (Number, required): 结束时间，Unix时间戳，支持最多180天的查询。
- offset (Number, required): 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。
- size (Number, required): 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大20。

## Returns
- optional: errcode(Number), result(LeaveStatusListVO), has_more(Boolean), leave_status(LeaveStatusVO[]), duration_unit(String), duration_percent(Number), end_time(Number), start_time(Number), userid(String), success(Boolean), request_id(String)

## Limits
- 待查询用户的ID列表，每次最多100个。
- 开始时间 ，Unix时间戳，支持最多180天的查询。
- 结束时间，Unix时间戳，支持最多180天的查询。
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大20。
- 假期时长\*100，例如用户请假时长为1天，该值就等于100。

source_url: https://open.dingtalk.com/document/development/query-status
updated_at: 2026-05-27 17:06:25
