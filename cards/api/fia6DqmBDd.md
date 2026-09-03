# 创建个人或企业客户数据

doc_id: fia6DqmBDd
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/crm/personalCustomers
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_crm_maindata_write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- creatorUserId (String, required): 记录创建人的用户userId。
- data (Map, required): 客户数据内容，JSON格式字符串，格式请参见新增和更新客户字段格式说明V1。
- optional: creatorNick(String), extendData(Map), permission(Object), ownerStaffIds(Array of String), participantStaffIds(Array of String), relationType(String), skipDuplicateCheck(Boolean), action(String)

## Returns
- optional: instanceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-crm-personal-customers
updated_at: 2026-06-04 19:12:05
