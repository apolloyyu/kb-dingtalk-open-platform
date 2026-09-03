# 给员工颁发荣誉

doc_id: ADB0QZGDS0
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/orgCulture/honors/{honorId}/grant
api_version: v2-new
app_types: 第三方企业应用
permissions: OrgCulture.Honor.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- honorId (String, required): 荣誉Id，可调用查询当前企业下可颁发的荣誉列表接口获取honorId参数值。

## Query params
- none

## Body
- senderUserId (String, required): 发送人userId。 如果是同一个发送人给多个员工颁发荣誉，请分别按照顺序执行，不允许并发执行，防止颁发顺序出错。
- grantReason (String, required): 颁奖词，最多100个字符。
- granterName (String, required): 颁奖人名字，最多50个字符。
- receiverUserIds (Array of String, required): 接受人userId列表，最大值10。
- optional: expirationTime(Long), noticeSingle(Boolean), noticeAnnouncer(Boolean), openConversationIds(Array of String)

## Returns
- optional: success(Boolean), result(Object), successUserIds(Array of String), failedUserIds(Array of String)

## Limits
- 颁奖词，最多100个字符。
- 颁奖人名字，最多50个字符。
- 荣誉有效期到期时间戳，单位毫秒。 - 该参数值可不传，代表永久有效。 - 该参数值不允许传当天的时间戳。 有效期时间范围要求1~366天后，例如调用本接口的时间为2022-01-01 12:00:00，有效期时间范围是2022-01-01 12:00:00——2023-01-02 12:00:00。
- 接受人userId列表，最大值10。
- 接收荣誉消息的群openConversationId列表，最大值。 - 企业内部应用，可调用创建群会话接口获取openConversationId。 - 第三方企业应用，可调用创建场景群接口获取openConversationId。 荣誉发送人senderUserId，必须是群成员。

source_url: https://open.dingtalk.com/document/development/award-of-honor
updated_at: 2026-07-20 09:21:33
