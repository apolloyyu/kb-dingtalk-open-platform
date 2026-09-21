# 更新企业账号工作状态

doc_id: VQHer10J10
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/contact/orgAccounts/owness
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Contact.OrgAccountOwnness.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- userId (String, required): 员工id。

## Body
- ownnessId (Long, required): 业务标识ID，同增加时候录入的ownnessId。
- text (String, required): 文案。
- ownenssType (Long, required): 状态类型，仅支持： - **1**：请假中 - **3**：出差中 - **4**：会议中 - **7**：外出中
- startTime (Long, required): 开始时间戳。
- endTime (Long, required): 结束时间戳。

## Returns
- optional: result(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-modifyorgaccuserownness
updated_at: 2026-09-21 17:06:39
