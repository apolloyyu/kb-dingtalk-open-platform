# 更新班级

doc_id: 2c61mMGD6A
completeness: full
archived: false
method: PUT
endpoint: https://api.dingtalk.com/v1.0/edu/classes/infos
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
- deptId (Long, required): 班级ID。
- gradeLevel (Integer, required): 年级Level。
- operator (String, required): 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。
- openClass (Object, required): 班级信息。
- nick (String, required): 班级昵称。
- onlyUseNick (String, required): 是否只展现nick。
- classLevel (Integer, required): 每个年级下班级级数，1班为1，2班为2。
- superId (Long, required): 年级ID。

## Returns
- optional: success(Boolean), result(Object), deptId(Long)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-updateclass
updated_at: 2026-06-03 09:13:44
