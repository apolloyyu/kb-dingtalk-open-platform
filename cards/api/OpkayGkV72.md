# 创建学段

doc_id: OpkayGkV72
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/period/create
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
- super_id (Number, required): 校区ID，可调用获取部门列表接口获取dept_type为campus时的dept_id参数值。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。
- open_period (OpenPeriod, required): 学段信息。
- step (String, required): 学段名称。 - 幼儿园 - 小学 - 初中 - 高中
- grades (Grades[], required): 年级列表，最大列表长度为999。
- grade (String, required): 年级级数，一年级为1，二年级为2。
- classes (Number, required): 每个年级下班级级数，1班为1，2班为2。0表示无限。 **[!NOTE]** 尽量不要超过100个，否则页面性能有问题。
- name (String, required): 年级名称，需要与grade和start_year对应。
- start_year (String, required): 入学年份。 **[!NOTE]** 请注意start_year、name、grade三者之间的关联关系。
- period_code (String, required): 学段编码。 - **kindergarten** ：幼儿园 - **primary_school**：小学 - **middle_school**： 初中 - **high_school**： 高中
- name_mode (String, required): 学段名称类型。 - **text**：文本型，如初中为七年级，八年级，九年级。 - **number**：数字型，如初中一年级1班，二年级1班等。

## Returns
- optional: result(OpenPeriodCreateResponse), deptId(Number), grades(EduGradeDo[]), campus_id(Number), dept_id(Number), grade(Number), name(String), super_id(Number), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 年级列表，最大列表长度为999。
- 每个年级下班级级数，1班为1，2班为2。0表示无限。 **[!NOTE]** 尽量不要超过100个，否则页面性能有问题。

source_url: https://open.dingtalk.com/document/development/create-a-learning-segment
updated_at: 2026-07-20 09:21:49
