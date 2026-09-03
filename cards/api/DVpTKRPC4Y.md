# 获取签署人签署地址

doc_id: DVpTKRPC4Y
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v2.0/esign/process/executeUrls
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
- taskId (String, required): 任务ID。
- optional: signContainer(Integer), account(String)

## Returns
- optional: mobileUrl(String), pcUrl(String), longUrl(String), shortUrl(String)

## Limits
- 流程地址，用于在浏览器内打开，短链地址30天有效, 不区分移动端或PC端，UI会自适应。 **signContainer**为**2**时，返回该地址。

source_url: https://open.dingtalk.com/document/development/get-signatory-address
updated_at: 2026-06-04 19:11:13
