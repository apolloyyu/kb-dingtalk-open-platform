# 异步转译通讯录ID

doc_id: Tb2VE3RKXf
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/contact/files/translate
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_get_member

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- medias (Map<String, String>, required): 需要转译的文件信息。 - Map类型，key为钉盘文件media_id，调用获取文件上传信息接口获取。 - value为文件名，需要包含文件扩展名，与调用获取文件上传信息接口时传入的文件名称保持一致。 - 只支持xlsx，xls，csv，txt类型文件。 - 最大数量20个文件。
- unionId (String, required): 当前操作导出文档的用户的unionId，可以调用通过免登码获取用户信息接口获取。
- optional: outputFileName(String)

## Returns
- optional: jobId(String)

## Limits
- 需要转译的文件信息。 - Map类型，key为钉盘文件media_id，调用获取文件上传信息接口获取。 - value为文件名，需要包含文件扩展名，与调用获取文件上传信息接口时传入的文件名称保持一致。 - 只支持xlsx，xls，csv，txt类型文件。 - 最大数量20个文件。
- 异步转译任务ID，最大长度为64字符。 **jobId**用于接口获取异步转译任务结果传递。

source_url: https://open.dingtalk.com/document/development/asynchronous-address-book-file-content-translation
updated_at: 2026-07-02 10:35:53
