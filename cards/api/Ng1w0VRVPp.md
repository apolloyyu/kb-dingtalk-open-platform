# 启用群模板

doc_id: Ng1w0VRVPp
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/im/chat/scenegroup/template/apply
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_chat_manage

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- owner_user_id (String, required): 群主的userid。
- template_id (String, required): 群模板id，登录开发者后台 > 开放能力 > 场景群 > 群模板查看id：群开放-场景群-群模板-启用群模板-获取群模板ID **[!NOTE]** 调用本接口前，需要在钉钉开发者后台为群模板设置灰度企业。企业灰度
- open_conversation_id (String, required): 群ID，调用创建场景群接口获取`open_conversation_id`参数值。

## Returns
- optional: success(Boolean), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/enable-a-group-template
updated_at: 2026-07-14 09:22:06
