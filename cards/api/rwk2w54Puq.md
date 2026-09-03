# 获取跳转到企业实名的地址

doc_id: rwk2w54Puq
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/corps/realnames
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
- userId (String, required): 当前用户userid。 必须是管理员。
- optional: redirectUrl(String)

## Returns
- optional: taskId(String), pcUrl(String), mobileUrl(String)

## Limits
- 企业实名操作成功后的重定向地址。 **[!NOTE]** 地址有效期为2小时。
- 企业在e签宝进行实名认证时，只能由企业的管理员或子管理员操作，因此实名入口的展示建议做权限判断，只展示给企业管理员。因e签宝应用首页也有实名入口，此企业实名入口展示非必须，ISV可实际需求处理。

source_url: https://open.dingtalk.com/document/development/obtain-the-address-that-is-redirected-to-the-enterprise-s-real
updated_at: 2026-06-04 19:11:10
