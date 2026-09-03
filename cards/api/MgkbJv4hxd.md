# 创建客户群组

doc_id: MgkbJv4hxd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/groupSets
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 群组名。
- ownerUserId (String, required): 群主userId。 裂变出的新群会自动设置该userId为群主。
- creatorUserId (String, required): 创建人userId。
- relationType (String, required): 关系类型。 - **crm_customer**：企业客户 - **crm_customer_personal**：个人客户
- optional: templateId(String), memberQuota(Integer), managerUserIds(String), notice(String), noticeToped(Integer), welcome(String)

## Returns
- optional: name(String), openGroupSetId(String), relationType(String), memberQuota(Long), memberCount(Long), templateId(String), ownerUserId(String), managerUserIds(String), notice(String), noticeToped(Integer), owner(Object), userId(String), manager(Array), lastOpenConversationId(String), gmtCreate(String), gmtModified(String), inviteLink(String)

## Limits
- 单个群的人数上限，最大值900。
- 单个群的人数上限。
- - 客户群组可以设置群成员数的最大值，当每个客户群成员数超过最大值，会自动创建一个新的客户群。
- - 每次创建新群时，会自动设置群主、群管理员、群公告等信息。

source_url: https://open.dingtalk.com/document/development/crm-create-group
updated_at: 2026-06-04 19:12:19
