# 获取打卡结果

doc_id: Ai0FqxfGGB
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/attendance/list
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_attendance_isv_query_result, qyapi_get_attendance_data

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- workDateFrom (String, required): 查询考勤打卡记录的起始工作日。格式为yyyy-MM-dd HH:mm:ss，HH:mm:ss可以使用00:00:00，将返回此日期从0点到24点的结果。 例如，参数传"2021-12-01 10:00"，获取的是12月1日一整天的考勤结果。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）。
- workDateTo (String, required): 查询考勤打卡记录的结束工作日。格式为“yyyy-MM-dd HH:mm:ss”，HH:mm:ss可以使用00:00:00，将返回此日期从0点到24点的结果。 例如，参数传"2021-12-01 19:00"，获取的是12月1日一整天的考勤结果。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）。
- userIdList (String[], required): 员工在企业内的userId列表，最大值50。 **[!IMPORTANT]** 务必确保userId参数的正确性，否则本接口获取信息为空。
- offset (Number, required): 表示获取考勤数据的起始点。第一次传0，如果还有多余数据，下次获取传的offset值为之前的offset+limit，0、1、2...依次递增。
- limit (Number, required): 表示获取考勤数据的条数，最大值50。
- optional: isI18n(Boolean)

## Returns
- optional: recordresult(Recordresult[]), sourceType(String), baseCheckTime(Date), userCheckTime(Date), procInstId(String), approveId(Number), locationResult(String), timeResult(String), checkType(String), userId(String), workDate(Date), recordId(Number), planId(Number), groupId(Number), id(Number), hasMore(Boolean), errmsg(String), errcode(Number)

## Limits
- 查询考勤打卡记录的起始工作日。格式为yyyy-MM-dd HH:mm:ss，HH:mm:ss可以使用00:00:00，将返回此日期从0点到24点的结果。 例如，参数传"2021-12-01 10:00"，获取的是12月1日一整天的考勤结果。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）。
- 查询考勤打卡记录的结束工作日。格式为“yyyy-MM-dd HH:mm:ss”，HH:mm:ss可以使用00:00:00，将返回此日期从0点到24点的结果。 例如，参数传"2021-12-01 19:00"，获取的是12月1日一整天的考勤结果。 **[!IMPORTANT]** workDateFrom和workDateTo参数 相隔最多7天（包含7天）。
- 员工在企业内的userId列表，最大值50。 **[!IMPORTANT]** 务必确保userId参数的正确性，否则本接口获取信息为空。
- 表示获取考勤数据的条数，最大值50。

source_url: https://open.dingtalk.com/document/development/open-attendance-clock-in-data
updated_at: 2026-05-27 17:05:51
