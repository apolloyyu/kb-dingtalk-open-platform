# 更新用户信息

doc_id: zP8p6VMbMO
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/update
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
- userid (String, required): 员工userid，不可修改，长度为1~64个字符，可通过根据手机号查询用户接口获取。
- optional: name(String), managerUserid(String), workPlace(String), remark(String), isSenior(Boolean), orgEmail(String), tel(String), orderInDepts(JSONObject), department(List[]), email(String), position(String), positionInDepts(JSONObject), extattr(String), jobnumber(String), isHide(Boolean), lang(String), hiredDate(Number)

## Returns
- optional: errcode(Number), errmsg(String)

## Limits
- 员工userid，不可修改，长度为1~64个字符，可通过根据手机号查询用户接口获取。
- 员工姓名，长度为1~64个字符。
- 办公地点，长度为0~50个字符。
- 备注，长度为0~1000个字符。
- 分机号，长度为0~50个字符。
- 员工邮箱。 长度为0~64个字符。企业内必须唯一，不可重复。
- 职位信息。 长度为0~64个字符。
- 扩展属性。 **[!IMPORTANT]** - 手机上最多只能显示10个扩展属性，可登录**OA管理后台****>设置>通讯录信息**进行设置。 - 如果给员工设置有10个扩展属性字段，更新时即使扩展属性字段值没变，也必须要将10个扩展属性字段都传进去。如果只传其中1个，那么剩下9个字段都会被清空。 **查看扩展属性：** - 链接类型扩展属性，只支持在“移动端钉钉-点击该用户头像-个人资料页”查看，点击链接可以跳转。 **[!NOTE]** 链接类型支持变量通配符自动替换

source_url: https://open.dingtalk.com/document/development/update-user-details
updated_at: 2026-08-25 09:36:49
