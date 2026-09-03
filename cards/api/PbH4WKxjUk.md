# 创建个人账号用户

doc_id: PbH4WKxjUk
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/edu/collegeContact/personalAccounts/users
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
- mobile (String, required): 手机号码，企业内必须唯一，不可重复。 目前仅限国内手机号码，国外手机号不可使用
- empType (String, required): 员工的成员类型： - college_teacher：教职工 - college_student：学生
- deptIdList (Array of Long, required): 部门ID。
- mainDeptId (Long, required): 主部门ID。
- optional: userid(String), hideMobile(Boolean), telephone(String), jobNumber(String), title(String), email(String), orgEmail(String), orgEmailType(String), workPlace(String), remark(String), deptOrderList(Array), deptId(Long), order(Integer), deptTitleList(Array), extension(Map<String, String>), seniorMode(Boolean), hiredDate(Long), managerUserid(String), loginEmail(String), sendActiveSms(Boolean), deptPositionSet(Array), managerUserId(String)

## Returns
- optional: success(Boolean), result(Object), userid(String), unionId(String), createResult(Integer)

## Limits
- 员工唯一标识ID（不可修改），企业内必须唯一。 长度为1~64个字符，如果不传，将自动生成一个userid。
- 员工名称，长度最大80个字符。
- 手机号码，企业内必须唯一，不可重复。 目前仅限国内手机号码，国外手机号不可使用
- 分机号，长度最大50个字符。
- 教职工工号/学生学号，长度最长为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。
- 员工的企业邮箱，长度最大100个字符。

source_url: https://open.dingtalk.com/document/development/api-addcollegecontactuser
updated_at: 2026-06-04 14:15:56
