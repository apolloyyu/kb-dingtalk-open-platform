# 获取单个客户群组详情

doc_id: 6cCH06hVLB
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/crm/groupSets
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- openGroupSetId (String, required): 群组openGroupSetId，调用查询客户群组列表接口获取openGroupSetId参数值。

## Body
- none

## Returns
- optional: name(String), openGroupSetId(String), relationType(String), memberQuota(Integer), memberCount(Integer), templateId(String), ownerUserId(String), managerUserIds(String), notice(String), noticeToped(Integer), owner(Object), userId(String), manager(Array), lastOpenConversationId(String), gmtCreate(String), gmtModified(String), groupChatCount(Integer), inviteLink(String)

## Limits
- 群组内客户群上限人数。
- 调用本接口，获取单个客户群组详情，包括群组内已自动创建的群数量、群组设置的群主、群组设置的管理员和群组设置的上限成员数等。

source_url: https://open.dingtalk.com/document/development/queries-the-details-of-a-single-customer-group
updated_at: 2026-06-04 19:12:19
