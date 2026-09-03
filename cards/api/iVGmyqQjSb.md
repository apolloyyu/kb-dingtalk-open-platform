# 获取打卡详情

doc_id: iVGmyqQjSb
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/attendance/listRecord
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_get_attendance_data

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- userIds (List, required): 企业内的员工ID列表，最大值50。 **[!IMPORTANT]** 务必确保userId参数的正确性，否则本接口获取信息为空。
- checkDateFrom (String, required): 查询考勤打卡记录的起始工作日。格式为：yyyy-MM-dd hh:mm:ss。 例如，参数传"2021-12-01 10:00:00"，员工在09:00的打卡信息获取不到。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）
- checkDateTo (String, required): 查询考勤打卡记录的结束工作日。格式为：yyyy-MM-dd hh:mm:ss。 例如，参数传"2021-12-01 18:00:00"，员工在19:00的打卡信息获取不到。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）
- optional: isI18n(Boolean)

## Returns
- optional: errmsg(String), errcode(String), recordresult(Array of Object), userAccuracy(String), classId(Long), userLatitude(String), userLongitude(String), userAddress(String), deviceId(String), locationMethod(String), isLegal(String), userCheckTime(String), procInstId(String), baseCheckTime(String), approveId(String), timeResult(String), locationResult(String), checkType(String), sourceType(String), userId(String), workDate(String), corpId(String), planId(String), groupId(String), id(String), invalidRecordType(String), userSsid(String), userMacAddr(String), planCheckTime(String), baseAddress(String), baseLongitude(String), baseLatitude(String), baseAccuracy(String), baseSsid(String), baseMacAddr(String), gmtCreate(String), invalidRecordMsg(String), gmtModified(String), outsideRemark(String), deviceSN(String), bizId(String), photoUrl(String)

## Limits
- 企业内的员工ID列表，最大值50。 **[!IMPORTANT]** 务必确保userId参数的正确性，否则本接口获取信息为空。
- 查询考勤打卡记录的起始工作日。格式为：yyyy-MM-dd hh:mm:ss。 例如，参数传"2021-12-01 10:00:00"，员工在09:00的打卡信息获取不到。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）
- 查询考勤打卡记录的结束工作日。格式为：yyyy-MM-dd hh:mm:ss。 例如，参数传"2021-12-01 18:00:00"，员工在19:00的打卡信息获取不到。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）
- - 本接口不支持查询180天之前的数据。

source_url: https://open.dingtalk.com/document/development/attendance-clock-in-record-is-open
updated_at: 2026-05-27 17:05:52
