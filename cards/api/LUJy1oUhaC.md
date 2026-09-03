# 创建高校账号用户

doc_id: LUJy1oUhaC
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/exclusiveAccounts/users
api_version: v2-new
app_types: 企业内部应用
permissions: Edu.College.Contact.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- name (String, required): 员工名称，长度最大80个字符。
- empType (String, required): 员工的成员类型： - college_teacher：教职工 - college_student：学生
- deptIdList (Array of Long, required): 部门id。
- mainDeptId (Long, required): 主部门ID。
- exclusiveAccount (Boolean, required): 必须填true，表示要创建高校账号。
- exclusiveAccountType (String, required): 高校账号类型（dingtalk、sso），默认dingtalk，表示钉钉自建高校账号。sso表示SSO高校账号
- optional: userid(String), mobile(String), telephone(String), jobNumber(String), title(String), email(String), orgEmail(String), orgEmailType(String), workPlace(String), remark(String), deptOrderList(Array), deptId(Long), order(Integer), deptTitleList(Array), extension(Map<String, String>), seniorMode(Boolean), hiredDate(Long), managerUserid(String), sendActiveSms(Boolean), initPassword(String), loginIdType(String), avatarMediaId(String), nickname(String), deptPositionSet(Array), managerUserId(String)

## Returns
- optional: success(Boolean), result(Object), userid(String), unionId(String), createResult(Integer)

## Limits
- 员工唯一标识ID（不可修改），企业内必须唯一。 长度为1~64个字符，如果不传，将自动生成一个userid。
- 员工名称，长度最大80个字符。
- 分机号，长度最大50个字符。
- 教职工工号/学生学号，长度最长为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。
- 员工的企业邮箱，长度最大100个字符。
- 办公地点，长度最大100个字符。

source_url: https://open.dingtalk.com/document/development/api-addcollegecontactexclusive
updated_at: 2026-06-04 19:11:30
