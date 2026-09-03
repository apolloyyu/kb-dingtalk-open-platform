# 获取宜搭附件临时免登地址

doc_id: TmkVPbKktY
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/yida/apps/temporaryUrls/{appType}
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Attachment.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- appType (String, required): 应用编码，可在宜搭的应用设置中获取，如下图所示： image

## Query params
- systemToken (String, required): 应用密钥，可在宜搭的应用设置中获取，如下图所示： image
- userId (String, required): 用户的userid，可调用获取部门用户userid列表接口获取。
- fileUrl (String, required): 宜搭附件地址。
- optional: language(String), timeout(Long)

## Body
- none

## Returns
- optional: result(String)

## Limits
- 临时地址失效时间，单位毫秒。 例如：60000表示有效期一分钟。 - 最大值: 86400000 , 即24小时。 - 不填则默认60000，即1分钟 - 填0或者负数无效。

source_url: https://open.dingtalk.com/document/development/obtain-the-temporary-free-access-address-of-yixian-accessories
updated_at: 2026-06-02 11:32:15
