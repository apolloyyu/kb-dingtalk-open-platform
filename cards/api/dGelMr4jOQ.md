# 上传媒体文件

doc_id: dGelMr4jOQ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/media/upload
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_base

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- type (String, required): 媒体文件类型： - **image**：图片，图片最大20MB。支持上传jpg、gif、png、bmp格式。 - **voice**：语音，语音文件最大2MB。支持上传amr、mp3、wav格式。 - **video**：视频，视频最大20MB。支持上传mp4格式。 - **file**：普通文件，最大20MB。支持上传doc、docx、xls、xlsx、ppt、pptx、zip、pdf、rar格式。 **[!IMPORTANT]** 如果使用C#调用该接口出现**40004**（不合法的媒体文件类型）错误，需将参
- media (FileItem, required): 要上传的媒体文件。 form-data中媒体文件标识，有filename、filelength、content-type等信息。

## Returns
- optional: errcode(Number), errmsg(String), type(String), media_id(String), created_at(Number)

## Limits
- 媒体文件类型： - **image**：图片，图片最大20MB。支持上传jpg、gif、png、bmp格式。 - **voice**：语音，语音文件最大2MB。支持上传amr、mp3、wav格式。 - **video**：视频，视频最大20MB。支持上传mp4格式。 - **file**：普通文件，最大20MB。支持上传doc、docx、xls、xlsx、ppt、pptx、zip、pdf、rar格式。 **[!IMPORTANT]** 如果使用C#调用该接口出现**40004

source_url: https://open.dingtalk.com/document/development/upload-media-files
updated_at: 2026-06-01 09:15:23
