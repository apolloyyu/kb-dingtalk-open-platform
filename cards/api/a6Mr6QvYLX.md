# 根据设备ID获取员工信息

doc_id: a6Mr6QvYLX
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/attendance/machines/getUser/{devId}
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- devId (Long, required): 考勤机设备ID，可调用查询设备列表接口获取device_id参数值。

## Query params
- nextToken (String, required): 分页游标。
- maxResults (Integer, required): 分页大小。

## Body
- none

## Returns
- optional: result(Object), userList(Array), userId(String), name(String), hasFace(Boolean), hasMore(Boolean), nextToken(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-information-about-employees-based-on-device-ids
updated_at: 2026-06-02 09:24:50
