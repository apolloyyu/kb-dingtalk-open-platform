# 获取部门用户签到记录

doc_id: mYtLzfrL2y
completeness: full
archived: false
method: GET
endpoint: https://oapi.dingtalk.com/checkin/record
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_checkin_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。
- department_id (String, required): 部门ID，1表示根部门，可通过获取部门列表接口获取dept_id参数值。
- end_time (Number, required): 结束时间，Unix时间戳，单位毫秒。
- start_time (Number, required): 开始时间，开始时间，Unix时间戳，单位毫秒。 **[!NOTE]** 开始时间和结束时间的间隔不能大于45天。
- optional: offset(Number), size(Number), order(String)

## Body
- none

## Returns
- optional: data(Data[]), name(String), userId(String), avatar(String), timestamp(Number), place(String), detailPlace(String), remark(String), imageList(String[]), latitude(String), longitude(String), errmsg(String), errcode(Number)

## Limits
- 开始时间，开始时间，Unix时间戳，单位毫秒。 **[!NOTE]** 开始时间和结束时间的间隔不能大于45天。
- 支持分页查询，与offset 参数同时设置时才生效，此参数代表分页大小，最大100。
- > 目前最多获取1000人以内的签到数据，如果所传部门ID及其子部门下的user超过1000，会报错。

source_url: https://open.dingtalk.com/document/development/get-check-in-data
updated_at: 2026-05-27 17:06:34
