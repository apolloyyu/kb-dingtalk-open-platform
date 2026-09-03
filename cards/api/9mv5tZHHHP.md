# 查询离职记录列表

doc_id: 9mv5tZHHHP
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/contact/empLeaveRecords
api_version: v2-new
app_types: 企业内部应用
permissions: Contact.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- startTime (String, required): 开始时间。 格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601/RFC 3339）。
- maxResults (Integer, required): 每页最大条目数，最大值50。
- optional: endTime(String), nextToken(String)

## Body
- none

## Returns
- optional: nextToken(String), records(Array), userId(String), name(String), stateCode(String), mobile(String), leaveTime(String), leaveReason(String)

## Limits
- 结束时间。 格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601/RFC 3339）。 **[!NOTE]** - 如果该参数不传，开始时间距离当前时间不能超过365天。 - 如果该参数传参，开始时间和结束时间跨度不能超过365天。
- 每页最大条目数，最大值50。

source_url: https://open.dingtalk.com/document/development/query-the-details-of-employees-who-have-left-office
updated_at: 2026-06-01 15:20:41
