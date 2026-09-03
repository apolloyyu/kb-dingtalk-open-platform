# 配置企业钉工牌

doc_id: qOHVmFesnU
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/badge/codes/corpInstances
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
- codeIdentity (String, required): 码标识，取值： - **DT_VISITOR**：访客码 - **DT_CONFERENCE**：会展码 - **DT_IDENTITY**：身份码
- corpId (String, required): 开通的企业corpId。
- status (String, required): 状态，传入关闭状态需要用户手动开启后才会渲染二维码。 - **OPEN**：开启 - **CLOSED**：关闭 - **INVALID**：失效
- optional: extInfo(Map<String, String>)

## Returns
- optional: codeIdentity(String), corpId(String), status(String), extInfo(Map<String, String>)

## Limits
- 扩展参数，是否关联支付宝。 - **true**: 关联支付宝：可以应用到当面付等支付场景，支付时可以使用用户支付宝的钱。 - **false**: 不关联支付宝：用户生成的码只能用作身份码，不能应用到支付场景。 参数示例： ``` "extInfo": { "supportRelateAlipay": "false" } ```

source_url: https://open.dingtalk.com/document/development/save-dingtalk-enterprise-instance
updated_at: 2026-06-04 19:11:51
