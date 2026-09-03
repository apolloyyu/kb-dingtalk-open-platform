# 获取部门用户详情

doc_id: 3STk4T7IgZ
completeness: partial
partial_reason: missing_basic_table,missing_method,missing_request_section,missing_response_section
archived: true
method: —
endpoint: https://oapi.dingtalk.com/user/listbypage
api_version: v1-oapi
app_types: not_stated
permissions: not_stated

## Request headers
- none

## Path params
- none

## Query params
- access_token (String, required): 调用服务端API的应用凭证。 - 企业内部应用可通过获取企业内部应用的access_token接口获取。 - 第三方企业应用可通过服务商获取第三方应用授权企业的access_token接口获取。
- department_id (Number, required): 获取的部门ID。1表示根部门，可调用获取部门列表。 **[!NOTE]** 只获取当前部门下的员工信息，不包含子部门内的员工。
- offset (Number, required): 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。
- size (Number, required): 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。
- optional: lang(String), order(String)

## Body
- none

## Returns
- optional: errcode(Number), errmsg(String), hasMore(Boolean), userlist(Userlist[]), userid(String), order(Number), unionid(String), mobile(String), tel(String), workPlace(String), remark(String), isAdmin(Boolean), isBoss(Boolean), isHide(Boolean), isLeader(Boolean), name(String), active(Boolean), department(Number[]), position(String), email(String), orgEmail(String), avatar(String), jobnumber(String), hiredDate(Date), extattr(String)

## Limits
- 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。

source_url: https://open.dingtalk.com/document/development/obtain-department-members-details
updated_at: 2026-08-25 09:36:53
