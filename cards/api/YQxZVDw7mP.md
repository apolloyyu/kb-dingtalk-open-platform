# 导入简历创建候选人

doc_id: YQxZVDw7mP
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/ats/candidates/importCandidateByResume
api_version: v2-new
app_types: 企业内部应用, 第三方企业应用
permissions: qyapi_recruitment_plugin

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- optional: opUserId(String)

## Body
- fileSourceType (Integer, required): 简历文件来源： - **2**：链接url方式传入 - **3**：钉盘方式传入
- fileName (String, required): 简历文件名称。
- fileType (String, required): 简历文件类型，支持pdf、doc、docx、png、jpg、jpeg等类型。
- fileSize (Long, required): 文件字节大小。
- optional: url(String), spaceId(Long), fileId(String), channelCode(String)

## Returns
- optional: candidateId(String), corpId(String), name(String)

## Limits
- - 单个组织限制每分钟调用限制30次，请调用方控制调用频率。

source_url: https://open.dingtalk.com/document/development/api-importcandidatebyresume
updated_at: 2026-07-10 10:05:49
