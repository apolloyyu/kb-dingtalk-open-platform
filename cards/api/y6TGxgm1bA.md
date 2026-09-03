# 获取班级圈话题列表

doc_id: y6TGxgm1bA
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/circle/topiclist
api_version: v1-oapi
app_types: 企业内部应用
permissions: qyapi_edu_task

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取企业内部应用的access_token接口获取。

## Body
- class_id (Number, required): 班级ID，调用获取部门列表接口获取dept_id参数值。
- biz_type (Number, required): 业务类型，固定值为**4**，表示班级圈。
- userid (String, required): 用户userId，建议传当前班级内老师的userId。

## Returns
- optional: result(OpenCircleTopicResponse[]), topic_id(Number), init_topic(Boolean), name(String), post_count(Number), album_media_id(String), desc(String), success(Boolean), errmsg(String), errcode(Number)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtain-a-topic-list-of-class-circles
updated_at: 2026-06-08 09:48:21
