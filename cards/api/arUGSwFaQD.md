# 获取课堂明细数据

doc_id: arUGSwFaQD
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/detaildata/list
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_course_read

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- cursor (Number, required): 分页游标，从0开始。
- size (Number, required): 分页大小，取值0~100。
- course_code (String, required): 课程唯一编码，调用创建课程接口获取course_code参数值。
- category_code (String, required): 数据类别编码，可参考数据类别介绍。
- op_userid (String, required): 当前操作人的userId。
- optional: factor_codes(String[]), user_ids(String[]), user_cropid(String)

## Returns
- optional: result(PageQueryResponse), next_cursor(Number), has_more(Boolean), list(CourseDetailDataDTO[]), user_cropid(String), userid(String), category_code(String), category_biz_key(String), value(String), course_code(String), factor_code(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 数据因子编码数组。 不填则自动填充类别下全部的明细因子。 **[!NOTE]** 一次最多可传入100个数据因子。
- 需要获取的用户userId。 **[!NOTE]** 一次最多可传入100个userId。

source_url: https://open.dingtalk.com/document/development/obtain-course-detail-data
updated_at: 2026-07-20 09:21:46
