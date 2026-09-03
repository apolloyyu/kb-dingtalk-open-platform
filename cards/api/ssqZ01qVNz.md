# 查询用户详情

doc_id: ssqZ01qVNz
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/get
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- userid (String, required): 员工唯一标识userid。 - 企业内部应用可通过根据手机号查询用户接口获取。 - 第三方企业应用可通过获取部门用户userid列表接口获取。
- optional: lang(String)

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String), userid(String), unionid(String), managerUserid(String), hiredDate(Date), tel(String), remark(String), workPlace(String), name(String), position(String), mobile(String), stateCode(String), email(String), orgEmail(String), isSenior(Boolean), jobnumber(String), active(Boolean), avatar(String), extattr(String), roles(Roles[]), id(Number), type(Number), groupName(String), department(String), orderInDepts(JSONObject), isAdmin(Boolean), isLeaderInDepts(String), isHide(Boolean), isBoss(Boolean), realAuthed(Boolean)

## Limits
- 员工工号，对应显示到OA后台和客户端个人资料的工号栏目。 长度为0~64个字符。
- 扩展属性，可以设置多种属性。 **[!NOTE]** 第三方企业应用不返回该参数。 手机上最多只能显示10个扩展属性，可登录**OA管理后台** **> 设置 > 通讯录信息**进行设置。 **查看扩展属性：** - 链接类型扩展属性，只支持在“移动端钉钉-点击该用户头像-个人资料页”查看，点击链接可以跳转。 **[!NOTE]** 链接类型支持变量通配符自动替换，目前支持通配符有：userid，corpid。示例： `工位地址`。 - 非链接类型扩展属性，支持在“移动端钉钉

source_url: https://open.dingtalk.com/document/development/queries-user-details
updated_at: 2026-08-25 09:36:51
