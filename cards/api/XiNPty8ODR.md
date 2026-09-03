# 更新企业内部应用的可使用范围

doc_id: XiNPty8ODR
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/microApp/apps/{agentId}/scopes
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_microapp_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- agentId (Long, required): 应用agentId，参考AgentId。

## Query params
- none

## Body
- optional: addUserIds(Array of String), delUserIds(Array of String), addDeptIds(Array of Long), delDeptIds(Array of Long), addRoleIds(Array of Long), delRoleIds(Array of Long), onlyAdminVisible(Boolean)

## Returns
- optional: result(Boolean)

## Limits
- 待添加的用户userId列表，最大长度100。 添加后总用户数不得超过2000，否则将返回错误。
- 删除的可使用用户userId列表，最大长度100。
- 待添加的部门ID列表，最大长度100。 添加后总部门数不得超过2000，否则将返回错误。
- 待删除的部门ID列表，最大长度100。
- 待添加的角色ID列表，最大长度100。可通过获取角色列表接口获取具体ID值。 添加后总角色数不得超过2000，否则接口会报错。
- 删除的可使用角色列表，最大长度100。可通过获取角色列表接口获取id参数值。

source_url: https://open.dingtalk.com/document/development/update-the-visible-range-of-micro-applications
updated_at: 2026-07-14 09:22:23
