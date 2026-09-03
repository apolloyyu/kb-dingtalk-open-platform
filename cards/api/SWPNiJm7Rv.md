# 新增服务号

doc_id: SWPNiJm7Rv
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/serviceaccount/add
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_service_account_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- name (String, required): 服务号名称。
- avatar_media_id (String, required): 头像图片mediaId，可以通过上传媒体文件接口上传图片获取mediaId。
- desc (String, required): 机器人主页中的服务号功能简介，最多200个字符。
- preview_media_id (String, required): 机器人主页中，消息预览图片的mediaId，可以通过上传媒体文件接口上传图片获取mediaId。
- optional: brief(String)

## Returns
- optional: errmsg(String), errcode(Number), unionid(String), request_id(String)

## Limits
- 机器人主页中的服务号功能简介，最多200个字符。

source_url: https://open.dingtalk.com/document/development/added-service-number
updated_at: 2026-06-01 09:15:34
