# 删除企业内部应用

doc_id: UCcY4sty4M
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/microApp/apps/{agentId}
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用的agentId，请参考基础概念-AgentId。

## Query params
- opUnionId (String, required): 操作人的unionId，可调用查询用户详情接口获取。 操作删除的员工必须满足是以下两种身份之一，才可以成功删除应用，否则接口会报错**不合法的agentId**。 - 该应用所在企业的创建者。 - 该应用的创建人。

## Body
- none

## Returns
- optional: result(Boolean)

## Limits
- 通过本接口，管理员可安全地删除企业内部应用，删除后应用会进入24小时的待删除状态，期间可撤销删除操作，确保应用管理的安全性和可控性。
- - 如果24小时内没有撤销删除操作，该应用会从企业内部应用列表中彻底删除。
- - 如果24小时内单击**撤销删除**按钮，应用会恢复正常状态。

source_url: https://open.dingtalk.com/document/development/delete-an-internal-h5-application
updated_at: 2026-06-04 19:10:03
