# 设置高管模式

doc_id: i51DcKjLJ4
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/seniorSettings
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_manage_addresslist

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- seniorStaffId (String, required): 需要设置的员工userid。
- open (Boolean, required): 是否开启高管模式，取值： - **true**：开启高管模式 - **false**：关闭高管模式
- optional: permitStaffIds(Array of String), permitDeptIds(Array of Long), permitTagIds(Array of Long), protectScenes(Array of String)

## Returns
- none

## Limits
- 高管白名单员工userid列表。 参数**permitStaffIds**、**permitDeptIds**、**permitTagIds**列表内元素之和最大为200。
- 高管白名单部门列表。 参数**permitStaffIds**、**permitDeptIds**、**permitTagIds**列表内元素之和最大为200。
- 高管白名单角色列表。 参数**permitStaffIds**、**permitDeptIds**、**permitTagIds**列表内元素之和最大为200。

source_url: https://open.dingtalk.com/document/development/update-executive-settings
updated_at: 2026-06-02 09:18:09
