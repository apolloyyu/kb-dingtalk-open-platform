# 上传打卡记录

doc_id: R9Zrzl0rDO
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/attendance/record/upload
api_version: v1-oapi
app_types: 企业内部应用
permissions: Pro.AttendanceRecord.Write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 需要上传打卡记录的员工userId。
- device_name (String, required): 考勤机名称，该参数值是自定义的，比如123456。
- device_id (String, required): 考勤机ID，该参数值是自定义的，比如abcde。
- user_check_time (Number, required): 员工打卡的时间，单位毫秒。 **[!NOTE]** - 该参数单位必须是毫秒。 - 需要传 180 天以内的日期。
- optional: photo_url(String)

## Returns
- optional: success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 员工打卡的时间，单位毫秒。 **[!NOTE]** - 该参数单位必须是毫秒。 - 需要传 180 天以内的日期。

source_url: https://open.dingtalk.com/document/development/upload-punch-records
updated_at: 2026-05-27 18:39:33
