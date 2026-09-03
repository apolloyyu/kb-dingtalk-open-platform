# 创建签署流程

doc_id: e1pu2hEE5y
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/process/startAtOnce
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证。 - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- initiatorUserId (String, required): 发起人的userid。
- taskName (String, required): 任务名称，不支持特殊字符。
- fileId (String, required): 文件ID。
- fileType (Integer, required): 文件类型，取值： - **1**：合同文件 - **2**：附件
- fileName (String, required): 文件名称。
- signRequirements (String, required): 签署印章类型，取值： - **1**：企业章 - **2**：个人章 - **1,2**：个人和企业章
- accountType (String, required): 用户类型，取值： - **DING_USER**：钉钉用户 - **OUTER_USER**：外部用户
- optional: signEndTime(Long), redirectUrl(String), files(Array), participants(Array), signOrder(Integer), account(String), userId(String), accountName(String), orgName(String), signPosList(Array), isCrossPage(Boolean), needSignDate(Boolean), page(String), signDate(Object), format(String), signRequirement(String), x(double), y(double), ccs(Array), sourceInfo(Object), showText(String), pcUrl(String), mobileUrl(String), thirdBizId(String)

## Returns
- optional: taskId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/use-the-api-to-initiate-a-signature-process
updated_at: 2026-06-04 19:11:13
