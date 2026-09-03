# 获取行业角色下的用户列表

doc_id: 5hUYgHoy0a
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/resident/industryRoles/users
api_version: v2-new
app_types: 第三方企业应用
permissions: Village.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- tagCode (String, required): 行业角色编码，有以下取值： - **通用管理角色** - **super-admin**：创建者 - **main-admin**：主管理员 - **sub-admin**：子管理员 - **乡村行业** - **Villager**：村民 - **Leaseholder**：租客 - **GroupManager**：组长 - **HeadOfHouseHold**：户主 - **HouseAdmin**：家庭管理员 - **Party**：党员 - **Probationary**：预备党员 - **FlowP

## Body
- none

## Returns
- optional: userIdList(Array of String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-a-list-of-users-under-an-industry-role
updated_at: 2026-06-04 19:11:31
