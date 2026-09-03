# 炼丹炉专属模型服务

doc_id: HHkcQSu1d8
completeness: full
archived: false
method: POST
endpoint: https://api.dingtalk.com/v1.0/aiPaaS/ai/generate
api_version: v2-new
app_types: 第三方企业应用
permissions: AIPaaS.Model.Read

## Request headers
- x-acs-dingtalk-access-token (String, required): 调用该接口的访问凭证，通过以下获取： - 企业内部应用，调用获取企业内部应用的accessToken接口获取。 - 第三方企业应用，调用获取第三方应用授权企业的accessToken接口获取。

## Path params
- none

## Query params
- none

## Body
- module (String, required): 功能模块标识，主要是记录使用大模型使用场景，用户自己定义该参数值，纯英文格式。
- modelId (String, required): 模型ID，炼丹炉平台内模型上线部署后，点击查看，可获取模型ID。
- prompt (String, required): 输入的问题。
- userId (String, required): 当前用户的userId。

## Returns
- optional: requestId(String), result(Map)

## Limits
- none stated

source_url: https://open.dingtalk.com/document/development/api-liandanluexclusivemodel
updated_at: 2026-06-04 19:11:32
