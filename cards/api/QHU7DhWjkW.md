# 获取授权的页面地址

doc_id: QHU7DhWjkW
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/auths/urls
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: Esign.Common.ReadWrite

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。
- optional: serviceGroup(String)

## Path params
- none

## Query params
- none

## Body
- optional: redirectUrl(String)

## Returns
- optional: taskId(String), pcUrl(String), mobileUrl(String)

## Limits
- 完成后的重定向地址。授权成功后，在URL中会携带授权结果，其中： - **status**：授权状态，取值 - SUCCESS：成功 - FAIL：失败 - **taskid**：任务ID **[!NOTE]** 地址有效期为2小时。

source_url: https://open.dingtalk.com/document/development/obtain-the-address-of-the-authorized-page
updated_at: 2026-06-04 19:11:03
