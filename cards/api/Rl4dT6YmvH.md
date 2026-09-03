# 同步钉工牌码验证结果

doc_id: Rl4dT6YmvH
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/badge/codes/verifyResults
api_version: v2-new
app_types: 第三方企业应用
permissions: Badge.Common.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- payCode (String, required): 码值，接入方硬件设备扫描钉工牌二维码获取的码值。
- corpId (String, required): 企业corpId。可在钉钉开发者后台首页查看。
- userCorpRelationType (String, required): 用户和企业的关系类型，用于区分内部员工，外部联系人，无关系普通用户。 - **INTERNAL_STAFF**：企业内部员工 - **EXTERNAL_CONTACT**：外部联系人 - **NO_RELATION**：普通用户与组织无关
- userIdentity (String, required): 用户身份标识。取值和userCorpRelationType参数值有关。 - 如果是企业内部用户，通过获取部门用户详情接口传用户的userId。 - 如果是外部联系人通过获取外部联系人列表接口传外部联系人的userid。 - 如果是无关系用户需传入用户手机号，手机号需带有国家码，例如86-xxxxxxxxxxx。
- verifyTime (String, required): 验证时间。
- verifyResult (Boolean, required): 验证结果。
- optional: verifyLocation(String), verifyNo(String), verifyEvent(String), remark(String)

## Returns
- optional: result(String)

## Limits
- 验证事件。8个汉字以内，如门禁验证、班车登记、餐盘绑定等。

source_url: https://open.dingtalk.com/document/development/notification-dingtalk-badge-verification-result
updated_at: 2026-06-04 19:11:55
