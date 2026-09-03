# 更新家长

doc_id: 1tSZjzvp26
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/edu/guardians/infos
api_version: v2-new
app_types: 第三方企业应用
permissions: qyapi_edu_safe

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- stuId (String, required): 学生ID，可调用获取人员列表接口获取userid参数值。
- userId (String, required): 家长userId。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。
- relation (String, required): 家长与学生的关系： - F：爸爸 - M：妈妈 - GF：爷爷 - GM：奶奶 - GFA：外公 - GMA：外婆 - U：叔叔 - A：阿姨 - B：哥哥 - S：姐姐 - O：其他
- classId (Long, required): 班级ID，可调用获取部门列表接口获取dept_type为class时的dept_id参数值。
- bizId (String, required): 业务ID，自定义值，每次调用该参数保持唯一。

## Returns
- optional: success(Boolean), result(Object), bizId(String), userId(String)

## Limits
- 业务ID，自定义值，每次调用该参数保持唯一。

source_url: https://open.dingtalk.com/document/development/api-updateguardian
updated_at: 2026-06-03 09:13:45
