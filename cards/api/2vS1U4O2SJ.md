# 更新客户群组

doc_id: 2vS1U4O2SJ
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/crm/groupSets/set
api_version: v2-new
app_types: 第三方企业应用
permissions: Crm.CustomerGroup.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证： 企业内部应用，可通过获取企业内部应用的accessToken接口获取。 第三方企业应用，可通过获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- openGroupSetId (String, required): 群组openGroupSetId，调用查询客户群组列表接口获取openGroupSetId参数值。
- optional: name(String), memberQuota(Integer), ownerUserId(String), managerUserIds(String), notice(String), noticeToped(Integer), templateId(String), welcome(String)

## Returns
- none

## Limits
- 单个群的人数上限。

source_url: https://open.dingtalk.com/document/development/crm-update-group
updated_at: 2026-06-04 19:12:20
