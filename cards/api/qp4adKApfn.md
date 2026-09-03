# 查询用户信息详情

doc_id: qp4adKApfn
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/users
api_version: v2-new
app_types: 企业内部应用
permissions: Edu.College.Contact.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: userid(String), jobNumber(String), language(String)

## Body
- none

## Returns
- optional: success(Boolean), result(Object), userid(String), unionId(String), name(String), avatar(String), empType(String), stateCode(String), mobile(String), managerUserid(String), hideMobile(Boolean), telephone(String), jobNumber(String), title(String), email(String), workPlace(String), remark(String), exclusiveAccount(Boolean), orgEmail(String), deptIdList(Array of Long), mainDeptId(Long), deptOrderList(Array), deptId(Long), order(Integer), deptTypeSet(Array), deptName(String), deptType(String), deptStructType(String), structDeptId(Long), extension(String), hiredDate(Long), active(Boolean), realAuthed(Boolean), senior(Boolean), admin(Boolean), boss(Boolean), orgEmailType(String), leaderInDept(Array), leader(Boolean), roleList(Array), id(Long), groupName(String), loginId(String), loginType(String), exclusiveAccountType(String), exclusiveAccountCorpName(String), exclusiveAccountCorpId(String), unionEmpExt(Object), corpId(String), unionEmpMapList(Array), deptPositionSet(Array), isMain(Boolean), managerUserId(String)

## Limits
- 扩展属性，最大长度2000个字符。 具体支持的字段可见成员信息管理 `身份证号在该字段内不返回`

source_url: https://open.dingtalk.com/document/development/api-querycollegecontactuserdetail
updated_at: 2026-06-04 14:18:35
