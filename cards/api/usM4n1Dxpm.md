# 创建企业内部应用H5微应用

doc_id: usM4n1Dxpm
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/microapp/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端接口的授权凭证，可通过获取企业内部应用的access_token接口获取。

## Body
- appIcon (String, required): H5微应用的图标。 需要调用上传媒体文件将图标上传到钉钉服务器后获取到的mediaId。
- appDesc (String, required): H5微应用的描述。
- homepageUrl (String, required): H5微应用的移动端主页，必须以http开头或https开头。
- appName (String, required): H5微应用的名称。长度限制为1~10个字符。
- optional: pcHomepageUrl(String), ompLink(String)

## Returns
- optional: errcode(Number), errmsg(String), agentid(Number)

## Limits
- H5微应用的名称。长度限制为1~10个字符。

source_url: https://open.dingtalk.com/document/development/create-an-h5-microapplication
updated_at: 2026-08-25 09:39:04
