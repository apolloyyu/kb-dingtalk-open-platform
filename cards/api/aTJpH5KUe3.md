# 获取班级圈动态列表

doc_id: aTJpH5KUe3
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/circle/post/list
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
- optional: open_feed_query_param(OpenFeedQueryParam), cursor(Number), student_id(String), class_id(Number), topic_id(Number), biz_type(Number), feed_type(Number), count(Number), user_role(String), userid(String)

## Returns
- optional: result(OpenCircleTopicResponse), has_more(Boolean), posts(Posts[]), comments(Comments[]), comment_id(Number), content(String), origin_user(OrgUserDto), show_name(String), staff_id(String), author(Author), owner(Boolean), icon_media_id(String), title(String), type(String), avatar_media_id(String), nick(String), is_owner(Boolean), tag(Number), user_role(String), feed_type(Number), biz_id(String), post_id(Number), create_at(Number), geo_content(String), text(String), content_type(Number), tags(String), status(Number), success(Boolean), errmsg(String), errcode(Number)

## Limits
- 分页游标，第一页传入系统时间，毫秒。 **[!NOTE]** 返回的数据的时间戳不超过该数值
- 分页大小，最大值20。

source_url: https://open.dingtalk.com/document/development/dynamic-list-opening-of-class-circle
updated_at: 2026-06-08 09:48:23
