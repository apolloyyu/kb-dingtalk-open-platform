# 获取文件上传地址

doc_id: mbjaqGtHPp
completeness: full
archived: true
method: POST
endpoint: https://api.dingtalk.com/v1.0/esign/files/getUploadUrl
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
- contentType (String, required): 目标文件的MIME类型。支持如下格式： - application/octet-stream - application/pdf 文件流上传的Content-Type参数要和这里一致，否则会出现错误码为403的错误。
- contentMd5 (String, required): 先计算文件md5值，在对该md5值进行base64编码。 - 可使用E签宝官网工具进行计算。 MD5计算
- convert2Pdf (Boolean, required): 是否转换成pdf文档，取值： - true：转换 - false：不转换（默认值） 如果需要转换为pdf文档，那么需要先调用查询文件详情接口查询文件状态，待转换完成后才可使用。 如果本身就是pdf文件，该参数必须传false。
- fileName (String, required): 文件名称。 此文件名必须包含文件扩展名，且必须与真实的文件扩展名保持一致。例如：需要上传的文件为xxx.docx，那么此参数必须为xxx.docx，而不能是xxx.pdf。
- fileSize (Long, required): 文件大小，单位byte。 上传的文件大小不能超过50M。

## Returns
- optional: code(Integer), message(String), data(Object), fileId(String), uploadUrl(String)

## Limits
- 文件直传地址。在获取到文件上传地址后，可以直接使用此地址进行文件上传，详情请参考上传文件。 可以重复使用，但是只能传一样的文件，有效期一小时。

source_url: https://open.dingtalk.com/document/development/obtain-the-file-upload-address-1
updated_at: 2026-08-25 09:37:34
