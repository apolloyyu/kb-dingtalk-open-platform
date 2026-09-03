# 添加智能招聘文件到钉盘

doc_id: lFe1W2Hkbc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/ats/files
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: bizCode(String), opUserId(String)

## Body
- mediaId (String, required): 文件mediaId，调用获取智能招聘文件上传信息接口获取。 调用获取智能招聘文件上传信息接口获取的mediaId，必须使用OSS上传后才能使用，上传流程请参考本文档介绍的接口调用流程示例。否则本接口会出现报错**钉盘空间不可用**。
- fileName (String, required): 文件名称。 需要包含扩展名。

## Returns
- optional: spaceId(Long), fileId(String), fileName(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-nail-disk-file
updated_at: 2026-07-14 09:22:33
