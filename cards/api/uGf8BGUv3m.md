# 初始化家校架构

doc_id: uGf8BGUv3m
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/school/init
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
- campus (OpenCampus, required): 校区信息。
- name (String, required): 校区名称。
- periods (OpenPeriod[], required): 学段列表。
- step (String, required): 学段名称： - 幼儿园 - 小学 - 初中 - 高中
- grades (OpenGrade[], required): 年级列表，最大列表长度为999。
- grade (String, required): 年级级数，一年级为1，二年级为2。
- start_year (String, required): 入学年份。 **[!NOTE]** 请注意start_year、name、grade三者之间的关联关系。
- classes (Number, required): 每个年级下班级级数，1班为1，2班为2。0表示无限。 **[!NOTE]** 尽量不要超过100个，否则页面性能有问题。
- period_code (String, required): 学段编码。 - **kindergarten** ：幼儿园 - **primary_school**：小学 - **middle_school**： 初中 - **high_school**： 高中
- name_mode (String, required): 学段名称类型。 - **text**：文本型，如初中为七年级，八年级，九年级。 - **number**：数字型，如初中一年级1班，二年级1班等。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。

## Returns
- optional: result(OpenEduSchoolInitResponse), campus_list(Number[]), effected(String), success(Boolean), errcode(Number), errmsg(String), request_id(String)

## Limits
- 年级列表，最大列表长度为999。
- 每个年级下班级级数，1班为1，2班为2。0表示无限。 **[!NOTE]** 尽量不要超过100个，否则页面性能有问题。

source_url: https://open.dingtalk.com/document/development/initialize-the-home-school-architecture
updated_at: 2026-06-08 09:48:09
