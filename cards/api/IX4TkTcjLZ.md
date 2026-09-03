# 创建年级

doc_id: IX4TkTcjLZ
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/grade/create
api_version: v1-oapi
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_edu_safe

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该API的应用凭证。 - 企业内部应用，通过获取企业内部应用的access_token接口获取。 - 第三方企业应用，通过获取第三方企业的access_token接口获取。

## Body
- open_grade (OpenGrade, required): 年级信息。
- grade (String, required): 年级级数，一年级为1，二年级为2。
- classes (Number, required): 每个年级下班级级数，1班为1，2班为2。0表示无限。 **[!NOTE]** 尽量不要超过100个，否则页面性能有问题。
- name (String, required): 年级名称，需要与grade和start_year对应。
- start_year (String, required): 入学年份。 **[!NOTE]** 请注意start_year、name、grade三者之间的关联关系。
- super_id (Number, required): 学段ID，可调用获取部门列表接口获取dept_type为period时的dept_id参数值。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。

## Returns
- optional: result(OpenGradeCreateResponse), dept_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 每个年级下班级级数，1班为1，2班为2。0表示无限。 **[!NOTE]** 尽量不要超过100个，否则页面性能有问题。

source_url: https://open.dingtalk.com/document/development/create-grade
updated_at: 2026-06-08 09:48:12
