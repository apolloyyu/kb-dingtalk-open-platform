# 获取群活跃明细列表

doc_id: IBfZki7Bzv
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/data/activeGroups
api_version: v2-new
app_types: 第三方企业应用
permissions: Custom.Common.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- statDate (String, required): 统计日期，例如：20220101。
- pageNumber (Long, required): 分页起始页，该参数值从1开始。
- pageSize (Long, required): 分页大小，参数值建议不超过200。
- optional: dingGroupId(String), groupType(Long)

## Body
- none

## Returns
- optional: data(Array), statDate(String), dingGroupId(String), groupCreateTime(String), groupCreateUserId(String), groupCreateUserName(String), groupName(String), groupType(Long), groupUserCnt1d(Integer), sendMessageUserCnt1d(Long), sendMessageCnt1d(Long), openConvUv1d(Integer), totalCount(Long)

## Limits
- 分页大小，参数值建议不超过200。
- 最近1天群人数。
- 最近1天发消息人数。
- 最近1天发消息次数。
- 最近1天打开群人数。

source_url: https://open.dingtalk.com/document/development/obtains-the-group-activity-details-list
updated_at: 2026-06-04 19:10:00
