# 获取文件操作记录

doc_id: nsckkWsAxA
completeness: full
archived: false
method: GET
endpoint: https://api.dingtalk.com/v1.0/exclusive/fileAuditLogs
api_version: v2-new
app_types: 企业内部应用
permissions: Custom.OpFileAudit.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过调用获取企业内部应用的accessToken接口获取。

## Path params
- none

## Query params
- startDate (Long, required): 操作日志起始时间，UNIX时间戳，单位毫秒。
- endDate (Long, required): 操作日志截止时间，UNIX时间戳，单位毫秒。
- pageSize (Integer, required): 每页最大条目数，最大值500。
- optional: nextGmtCreate(Long), nextBizId(Long)

## Body
- none

## Returns
- optional: list(Array), operatorName(String), platform(Integer), platformView(String), status(Integer), action(Integer), actionView(String), resource(String), gmtCreate(Long), userId(String), ipAddress(String), orgName(String), receiverName(String), receiverTypeView(String), receiverType(Integer), resourceExtension(String), resourceSize(Long), targetSpaceId(Long), realName(String), bizId(String), operateModuleView(String), operateModule(Long), gmtModified(Long), docMemberList(Array), memberName(String), memberType(Integer), memberTypeView(String), permissionRole(Long), permissionRoleView(String), docReceiverList(Array), workSpaceName(String), workSpacePcUrl(String), workSpaceMobileUrl(String), docPcUrl(String), docMobileUrl(String), workSpaceId(Long), prevWorkSpaceId(Long), prevWorkSpaceName(String), prevWorkSpacePcUrl(String), prevWorkSpaceMobileUrl(String)

## Limits
- 每页最大条目数，最大值500。

source_url: https://open.dingtalk.com/document/development/obtain-file-operation-records
updated_at: 2026-06-04 19:09:58
