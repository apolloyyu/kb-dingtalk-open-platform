# 获取公告详情

doc_id: IN8RnUASa6
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/blackboard/get_blackboard
api_version: v2-new
app_types: 企业内部应用
permissions: qyapi_blackboard_manage

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，企业内部应用通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- optional: operationUserId(String), blackboardId(String)

## Body
- none

## Returns
- optional: id(String), senderStaffId(String), title(String), content(String), categoryId(String), categoryName(String), coverPicUrl(String), privateLevel(Long), isPushTop(Long), depNameList(Array of String), userNameList(Array of String), gmtCreate(String), gmtModified(String), readCount(Long), unReadCount(Long), userList(Array), corpId(String), staffId(String), name(String), deptList(Array), deptId(String), attachments(Array), fileName(String), fileType(String), dentryId(String), spaceId(String)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/obtains-the-details-get-blackboard
updated_at: 2026-06-02 09:18:06
