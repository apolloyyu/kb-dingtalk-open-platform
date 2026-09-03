# 获取用户忙闲信息

doc_id: 1HTjIv98oc
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/calendar/users/{userId}/querySchedule
api_version: v2-new
app_types: 第三方个人应用
permissions: Calendar.EventSchedule.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。 - 第三方个人应用，调用获取用户token接口获取。

## Path params
- userId (String, required): 本次请求的资源所归属的用户unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。

## Query params
- none

## Body
- userIds (Array of String, required): 查询目标用户的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。 用户列表最大长度 20。
- startTime (String, required): 查询的开始时间。
- endTime (String, required): 查询的结束时间。

## Returns
- optional: scheduleInformation(Array), userId(String), error(String), scheduleItems(Array), status(String), start(Object), date(String), dateTime(String), timeZone(String), end(Object)

## Limits
- 查询目标用户的unionId。 - 企业内部应用和第三方企业应用，调用查询用户详情接口获取unionid参数值。 - 第三方个人应用，调用获取用户通讯录个人信息接口获取unionId参数值。 用户列表最大长度 20。

source_url: https://open.dingtalk.com/document/development/free-schedule
updated_at: 2026-06-02 09:25:06
