# 获取用户可查看的公告

doc_id: b8xRUSq3t7
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/blackboard/listtopten
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_blackboard_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- userid (String, required): 员工的userId。

## Returns
- optional: errcode(Number), request_id(String), blackboard_list(OapiBlackboardVo[]), gmt_create(Date), title(String), url(String), categoryId(String), id(Sting)

## Limits
- 调用本接口，可获取指定人员的公告信息，在企业自定义工作首页进行公告轮播展示。列出用户当前有权限看到的10条公告。

source_url: https://open.dingtalk.com/document/development/list-the-user-s-announcement-list
updated_at: 2026-05-29 09:13:34
