# 获取发起签署任务地址

doc_id: Q4UdwwCXPq
completeness: full
archived: true
method: POST
endpoint: https://api.dingtalk.com/v1.0/esign/process/start
api_version: v2-new
app_types: 第三方企业应用
permissions: not_stated

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- optional: files(Array), fileId(String), fileName(String), initiatorUserId(String), participants(Array), accountType(String), signRequirements(String), userId(String), account(String), accountName(String), orgName(String), redirectUrl(String), sourceInfo(Object), mobileUrl(String), pcUrl(String), showText(String), taskName(String), ccs(Array)

## Returns
- optional: message(String), code(Integer), data(Object), taskId(String), pcUrl(String), mobileUrl(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-the-address-of-the-initiating-signing-task
updated_at: 2026-08-25 09:37:35
