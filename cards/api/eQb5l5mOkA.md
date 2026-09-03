# 更新个人账号用户信息

doc_id: eQb5l5mOkA
completeness: full
archived: false
method: PUT
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
- userid (String, required): 员工唯一标识ID（不可修改），企业内必须唯一。
- optional: name(String), empType(String), hideMobile(Boolean), telephone(String), jobNumber(String), title(String), email(String), orgEmail(String), workPlace(String), remark(String), deptIdList(Array of Long), mainDeptId(Long), deptOrderList(Array), deptId(Long), order(Integer), deptTitleList(Array), extension(Map<String, String>), seniorMode(Boolean), hiredDate(Long), managerUserid(String), deptPositionSet(Array), managerUserId(String), language(String), forceUpdateFields(String)

## Returns
- optional: success(Boolean)

## Limits
- 员工名称，长度最大80个字符。
- 分机号，长度最大50个字符。
- 教职工工号/学生学号，长度最长为50个字符。
- 职位，长度最大为200个字符。
- 员工个人邮箱，长度最大50个字符。
- 员工的企业邮箱，长度最大100个字符。
- 办公地点，长度最大100个字符。
- 备注，长度最大2000个字符。

source_url: https://open.dingtalk.com/document/development/api-updatecollegecontactuser
updated_at: 2026-06-04 14:18:32
