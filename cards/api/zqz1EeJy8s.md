# 添加课程参与方

doc_id: zqz1EeJy8s
completeness: full
archived: false
method: POST
endpoint: https://oapi.dingtalk.com/topapi/edu/course/participant/add
api_version: v1-oapi
app_types: 第三方企业应用
permissions: qyapi_edu_course_write

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用该接口的应用凭证，通过获取第三方企业的access_token接口获取。

## Body
- op_userid (String, required): 当前操作者的userId。
- participant_corpid (String, required): 参与方的组织cropId。CorpId **[!IMPORTANT]** **必须和当前组织相同或者存在关联关系。** 第三方企业应用请参考关联关系。
- course_code (String, required): 课程唯一编码，调用创建课程接口获取course_code参数值。
- participant_type (Number, required): 参与方类型。 - **1**：用户，可添加的人数上限为1000。 - **2**：部门，可添加的部门数上限为100，对应家校通讯录中的班级、年级。 - **3**：组织，可添加的组织数上限为5。
- participant_id (String, required): 参与方ID。 - participant_type=1时，participant_id为用户的userid - participant_type=2时，participant_id为部门ID - participant_type=3时，participant_id为组织的corpid
- role (String, required): 参与方角色。 - **student**：学生 - **guardian**: 监护人 - **teacher**：老师 **[!IMPORTANT]** 授课老师只支持通过创建课程和修改课程接口进行添加和修改。

## Returns
- optional: request_id(String), result(Boolean), success(Boolean), errcode(Number), errmsg(String)

## Limits
- 参与方类型。 - **1**：用户，可添加的人数上限为1000。 - **2**：部门，可添加的部门数上限为100，对应家校通讯录中的班级、年级。 - **3**：组织，可添加的组织数上限为5。

source_url: https://open.dingtalk.com/document/development/add-course-participants
updated_at: 2026-06-08 09:47:44
