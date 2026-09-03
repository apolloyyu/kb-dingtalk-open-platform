# 审核词条

doc_id: Bc5lV9Gs8j
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/pedia/words/approve
api_version: v2-new
app_types: 第三方企业应用
permissions: Pedia.Words.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- uuid (Long, required): 当前审核的词条的主键编号，可调用分页获取企业词条信息接口获取未审核的词条。
- userId (String, required): 操作人的组织员工userId。
- approveStatus (String, required): 审核的结果： - 1：通过 - 0：拒绝
- imHighLight (Boolean, required): 当前内部群是否高亮： - true：高亮 - false：不高亮
- simHighLight (Boolean, required): 服务群是否高亮： - true：高亮 - false：不高亮
- optional: approveReason(String)

## Returns
- optional: success(Boolean)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/review-entries
updated_at: 2026-06-02 19:45:01
