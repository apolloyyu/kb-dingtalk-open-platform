# 获取发起签署任务的地址

doc_id: 2XcoVETuRo
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/processes/startUrls
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- initiatorUserId (String, required): 任务发起方的userid。
- files (Array, required): 文件列表。
- fileId (String, required): 文件ID。
- fileName (String, required): 文件名称。
- accountType (String, required): 用户类型，取值： - **DING_USER**：钉钉用户 - **OUTER_USER**：外部用户
- optional: taskName(String), redirectUrl(String), participants(Array), signRequirements(String), userId(String), account(String), accountName(String), orgName(String), ccs(Array), sourceInfo(Object), showText(String), pcUrl(String), mobileUrl(String), autoStart(String), thirdBizId(String)

## Returns
- optional: taskId(String), pcUrl(String), mobileUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-address-used-to-initiate-a-signed-task
updated_at: 2026-06-04 19:11:12
