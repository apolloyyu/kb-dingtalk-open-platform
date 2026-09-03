# 创建用户

doc_id: nQNBzcvPNZ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/create
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API授权凭证，通过获取企业内部应用的access_token接口获取。

## Body
- mobile (String, required): 手机号码，企业内必须唯一，不可重复。
- department (String, required): 成员所属部门ID列表，多个ID之间使用英文逗号分隔。
- name (String, required): 成员名称。 长度为1~64个字符。
- optional: userid(String), isSenior(Boolean), isHide(Boolean), jobnumber(String), email(String), managerUserid(String), remark(String), workPlace(String), tel(String), position(String), positionInDepts(JSONObject), extattr(String), orgEmail(String), orderInDepts(JSONObject), hiredDate(Number)

## Returns
- optional: errcode(Number), errmsg(String), userid(String), unionId(String)

## Limits
- 员工唯一标识ID（不可修改），企业内必须唯一。 长度为1~64个字符，如果不传，将自动生成一个userid。
- 员工工号，对应显示到OA后台和客户端个人资料的工号栏目。 长度为0~64个字符。
- 员工邮箱。 长度为0~64个字符。企业内必须唯一，不可重复。
- 备注。 长度为0~1000个字符。
- 办公地点。 长度为0~50个字符。
- 分机号。 长度为0~50个字符，企业内必须唯一，不可重复。
- 职位信息。 长度为0~64个字符。
- 成员名称。 长度为1~64个字符。

source_url: https://open.dingtalk.com/document/development/create-user
updated_at: 2026-08-25 09:36:47
