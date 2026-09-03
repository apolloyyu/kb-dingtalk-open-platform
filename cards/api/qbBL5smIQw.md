# 删除流程实例

doc_id: qbBL5smIQw
completeness: full
archived: false
method: DELETE
endpoint: https://api.dingtalk.com/v1.0/yida/processes/instances
api_version: v2-new
app_types: 第三方企业应用
permissions: Yida.Process.Write

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- appType (String, required): 应用编码，获取方式可参考下图所示：
- systemToken (String, required): 应用密钥，获取方式可参考下图所示：
- userId (String, required): 用户的userId，可通过获取部门用户userid列表接口获取。
- processInstanceId (String, required): 流程实例ID，可通过调用发起宜搭审批流程接口获取。
- optional: language(String)

## Body
- none

## Returns
- none

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/delete-the-process-instance
updated_at: 2026-06-02 09:07:42
