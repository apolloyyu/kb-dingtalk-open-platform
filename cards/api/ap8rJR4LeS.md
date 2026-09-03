# 保存文件到自定义或审批钉盘空间

doc_id: ap8rJR4LeS
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/cspace/add
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- code (String, required): code值为应用免登授权码： - 免登授权码 - 获取微应用免登授权码
- media_id (String, required): 调用单步文件上传接口得到的media_id。
- space_id (String, required): 钉盘空间ID。
- name (String, required): 上传文件的名称，不能包含非法字符，需要utf-8 urlEncode。 **[!NOTE]** 必须带文件扩展名。
- optional: agent_id(String), folder_id(String), overwrite(Boolean)

## Body
- none

## Returns
- optional: dentry(String), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/add-file-to-user-s-dingtalk-disk
updated_at: 2026-08-25 09:38:14
