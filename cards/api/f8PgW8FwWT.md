# 批量查询员工假期余额变更记录

doc_id: f8PgW8FwWT
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/attendance/vacations/records/query
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_holiday_readonly

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- opUserId (String, required): 当前企业内拥有OA审批应用权限的管理员的userId，建议传入企业主管理员userId，可调用获取管理员列表接口，获取返回参数主管理员`userId`字段。
- leaveCode (String, required): 假期类型唯一标识，调用查询假期规则列表接口获取`leave_code`参数值。
- userIds (Array of String, required): 待查询员工userId列表，每次调用最多传50个userId。
- pageNumber (Long, required): 分页游标： - 首次查询，该参数传0。 - 非首次查询，根据上一次的偏移量的累积值进行传参。
- pageSize (Integer, required): 分页偏移量，最大200。

## Returns
- optional: result(Object), hasMore(Boolean), leaveRecords(Array), userId(String), leaveCode(String), recordId(String), quotaId(String), calType(String), startTime(Long), endTime(Long), leaveViewUnit(String), leaveReason(String), leaveRecordType(String), leaveStatus(String), recordNumPerDay(Long), recordNumPerHour(Long), gmtCreate(Long), gmtModified(Long), opUserId(String), success(Boolean)

## Limits
- 待查询员工userId列表，每次调用最多传50个userId。
- 分页偏移量，最大200。
- 额度有效期开始时间或请假开始时间，毫秒级时间戳。
- 额度有效期结束时间或请假结束时间，毫秒级时间戳。
- 以天计算的消费额度。 - **说明** 假期类型按天计算时，该值不为空且按百分之一天折算。 例如：1000=10天。
- 以小时计算的消费额度。 - **说明** 假期类型按小时，计算该值不为空且按百分之一小时折算。例如：1000=10小时。

source_url: https://open.dingtalk.com/document/development/batch-query-employee-leave-balance-change-record
updated_at: 2026-06-02 09:24:54
