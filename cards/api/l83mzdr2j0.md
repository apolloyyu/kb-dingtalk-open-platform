# 分页获取补卡规则列表

doc_id: l83mzdr2j0
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/attendance/adjustments
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_attendance_group_read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- pageNumber (Long, required): 分页起始页。 **[!NOTE]** 该参数值从1开始。
- pageSize (Long, required): 分页大小。 **[!NOTE]** 该参数最大不能超过50。

## Body
- none

## Returns
- optional: result(Object), pageNumber(Long), totalPage(Long), items(Array), id(Long), name(String), settingId(Long)

## Limits
- 分页大小。 **[!NOTE]** 该参数最大不能超过50。

source_url: https://open.dingtalk.com/document/development/retrieve-a-list-of-replenishment-rules-by-page
updated_at: 2026-06-01 16:47:20
